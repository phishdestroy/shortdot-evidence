#!/usr/bin/env python3
"""Full-zone backfill for the ShortDot zones after a daily-feed outage.

The daily run uses NetAPI filter_type=new, which only covers the last 24 hours,
so domains that appear while the job is down never reach the dataset. This
script downloads the full active zones once and:

  * adds domains never observed before to data/by_tld/ and lists them in
    data/backfill/<date>.txt (+ .json). Their first-seen day is unknown, so
    they are not attributed to any day in data/index.json;
  * rebuilds data/ioc/deployed/<tld>.txt from the zones' current IPs;
  * refreshes the zone-wide totals in data/index.json that incremental runs
    carry over from the last full scan.

Run scan/fetch_new.py afterwards: it regenerates phantom lists, README and badges.
"""

import os, csv, gzip, io, json, urllib.request, urllib.parse
from pathlib import Path
from datetime import date
from collections import Counter

TOKEN    = os.environ["NETAPI_TOKEN"]
TODAY    = date.today().isoformat()
TLD_LIST = [t.strip().lstrip('.').lower()
            for t in os.environ.get("TLD_LIST", "icu,bond,cyou,sbs,cfd,buzz,qpon").split(',')]

# Keep in sync with scan/fetch_new.py
TLD_WHOLESALE = {
    'icu': 0.65, 'cyou': 0.65, 'sbs': 0.65, 'cfd': 0.65,
    'bond': 6.50, 'buzz': 3.25, 'qpon': 2.50,
}
ICANN_FEE  = 0.25
ICANN_ZONE = 25800

# A zone far smaller than the last full scan means a truncated download, not
# mass deletion — abort instead of rewriting zone totals from partial data.
MIN_ZONE_RATIO = 0.5


def download(tld):
    """Full active zone as {domain: (ip_or_hostname, country)}, parsed like fetch_new.py."""
    params = urllib.parse.urlencode({
        'method':       'download',
        'zone_tld':     tld,
        'filter_type':  'active',
        'token':        TOKEN,
        'dataset_type': 'dataset',
    })
    req = urllib.request.Request(
        'https://netapi.com/api2/?' + params,
        headers={'User-Agent': 'Mozilla/5.0 PhishDestroy/2.0'}
    )
    with urllib.request.urlopen(req, timeout=900) as resp:
        raw = gzip.decompress(resp.read()).decode('utf-8', errors='replace')

    # API CSV format: url, majestic_rank, dns1, dns2, hostname, email, phone, ip, country
    zone = {}
    reader = csv.reader(io.StringIO(raw))
    next(reader, None)  # header
    for row in reader:
        if not row:
            continue
        domain = row[0].strip().lower()
        if '.' not in domain or domain.rsplit('.', 1)[-1] != tld:
            continue
        hostname  = row[4].strip() if len(row) > 4 else ''
        server_ip = row[7].strip() if len(row) > 7 else ''
        country   = row[8].strip() if len(row) > 8 else ''
        zone[domain] = (server_ip or hostname, country)
    return zone


def read_set(path):
    if not path.exists():
        return set()
    return {l.strip() for l in path.read_text(encoding='utf-8').splitlines() if l.strip()}


def write_set(path, domains):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('\n'.join(sorted(domains)) + '\n', encoding='utf-8')


def main():
    index_path = Path('data/index.json')
    index      = json.loads(index_path.read_text(encoding='utf-8'))
    prior_tlds = index.get('tld_breakdown', {})
    tld_dir    = Path('data/by_tld')
    dep_dir    = Path('data/ioc/deployed')

    # ── Download every zone before writing anything ───────────────────────────
    results        = {}
    country_counts = Counter()
    ip_counts      = Counter()
    for tld in TLD_LIST:
        print(f"Downloading full .{tld} zone ...", flush=True)
        try:
            zone = download(tld)
        except Exception as e:
            print(f"::error::.{tld} full-zone download failed: {e}")
            raise SystemExit(1)
        prior_count = prior_tlds.get(tld, {}).get('count', 0)
        if len(zone) < prior_count * MIN_ZONE_RATIO:
            print(f"::error::.{tld}: {len(zone):,} domains vs {prior_count:,} in the last full scan — "
                  f"looks truncated, aborting")
            raise SystemExit(1)

        known    = read_set(tld_dir / f'{tld}.txt')
        gap      = set(zone) - known
        deployed = {d for d, (ip, _) in zone.items() if ip}
        country_counts.update(c for _, c in zone.values() if c)
        ip_counts.update(ip for ip, _ in zone.values() if ip)
        results[tld] = {'count': len(zone), 'known': known, 'gap': gap, 'deployed': deployed}
        print(f"  .{tld}: {len(zone):,} in zone · {len(deployed):,} with IP · "
              f"{len(gap):,} never observed before", flush=True)
        del zone

    # ── Zone files: add never-observed domains (cumulative, like fetch_new.py) ─
    all_gap = set()
    for tld, res in results.items():
        if res['gap']:
            write_set(tld_dir / f'{tld}.txt', res['known'] | res['gap'])
        all_gap |= res['gap']

    # ── Deployed lists rebuilt from the current IPs ───────────────────────────
    for tld, res in results.items():
        write_set(dep_dir / f'{tld}.txt', read_set(dep_dir / f'{tld}.txt') | res['deployed'])

    # ── Backfill record: no first-seen date, so kept out of the daily index ───
    prev_days = [d['date'] for d in index.get('days', []) if d['date'] < TODAY]
    backfill_dir = Path('data/backfill')
    write_set(backfill_dir / f'{TODAY}.txt', all_gap)
    (backfill_dir / f'{TODAY}.json').write_text(json.dumps({
        'generated':        TODAY,
        'last_feed_day':    prev_days[-1] if prev_days else None,
        'count':            len(all_gap),
        'by_tld':           {tld: len(res['gap']) for tld, res in results.items()},
        'note':             'In the full zone on the generated date but never seen by the daily '
                            'new-domain feed (e.g. during a feed outage). First-seen date unknown.',
    }, indent=2) + '\n', encoding='utf-8')

    # ── Zone-wide totals carried over by incremental runs ─────────────────────
    tld_breakdown = index.get('tld_breakdown', {})
    for tld, res in results.items():
        count, deployed = res['count'], len(res['deployed'])
        tld_breakdown.setdefault(tld, {}).update({
            'count':       count,
            'price':       TLD_WHOLESALE.get(tld, 1.00),
            'no_ip':       count - deployed,
            'deploy_rate': round(deployed / count * 100, 1) if count else 0,
            'revenue':     round(count * TLD_WHOLESALE.get(tld, 1.00), 2),
            'deployed':    deployed,
        })
    total_domains  = sum(res['count'] for res in results.values())
    deployed_count = sum(len(res['deployed']) for res in results.values())
    index.update({
        'total_domains':       total_domains,
        'tld_breakdown':       tld_breakdown,
        'total_rev_wholesale': round(sum(v['revenue'] for v in tld_breakdown.values()), 2),
        'total_icann_fees':    round(total_domains * ICANN_FEE + len(TLD_LIST) * ICANN_ZONE, 2),
        'ip_countries':        dict(country_counts.most_common(10)),
        'top_shared_ips':      dict(ip_counts.most_common(20)),
        'deployed_count':      deployed_count,
        'no_ip_count':         total_domains - deployed_count,
        'deployment_rate':     round(deployed_count / total_domains * 100, 1) if total_domains else 0,
    })
    index_path.write_text(json.dumps(index, indent=2) + '\n', encoding='utf-8')

    print(f"\nBackfill {TODAY}: {total_domains:,} domains in zone · {deployed_count:,} with IP · "
          f"{len(all_gap):,} never observed before → data/backfill/{TODAY}.txt")


if __name__ == '__main__':
    main()
