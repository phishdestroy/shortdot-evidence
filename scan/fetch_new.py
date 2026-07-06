#!/usr/bin/env python3
"""Enumerate domain registrations across all ShortDot zones from ICANN gTLD zone data and update repository data."""

import os, re, gzip, csv, io, json, urllib.request, urllib.parse
from pathlib import Path
from datetime import date, datetime
from collections import defaultdict, Counter

TOKEN    = os.environ["NETAPI_TOKEN"]
TODAY    = date.today().isoformat()
TLD_LIST = [t.strip().lstrip('.').lower()
            for t in os.environ.get("TLD_LIST", "icu,bond,cyou,sbs,cfd,buzz,qpon").split(',')]

# First-run detection: use filter_type=all if no prior daily data exists
_prior = Path('data/index.json')
_prior_data = json.loads(_prior.read_text(encoding='utf-8')) if _prior.exists() else {}
_is_first_run = not bool(_prior_data.get('days'))
FILTER_TYPE = 'active' if _is_first_run else 'new'
print(f"Filter mode: {FILTER_TYPE} ({'initial full zone download' if _is_first_run else 'incremental'})")

# Retail price estimates by TLD (USD/year)
TLD_PRICES = {
    'icu': 0.99, 'cyou': 0.99, 'sbs': 0.99, 'cfd': 0.99,
    'bond': 9.99, 'buzz': 4.99, 'qpon': 3.99,
    # wholesale to ShortDot (used for revenue estimate)
}
TLD_WHOLESALE = {
    'icu': 0.65, 'cyou': 0.65, 'sbs': 0.65, 'cfd': 0.65,
    'bond': 6.50, 'buzz': 3.25, 'qpon': 2.50,
}
ICANN_FEE   = 0.25   # ICANN registry volume fee per domain/yr (zones >50k, paid by registry to ICANN)
ICANN_ZONE  = 25800  # ICANN annual fixed registry fee per TLD

def get_price(domain):
    tld = domain.rsplit('.', 1)[-1].lower()
    return TLD_PRICES.get(tld, 1.99)

def get_wholesale(domain):
    tld = domain.rsplit('.', 1)[-1].lower()
    return TLD_WHOLESALE.get(tld, 1.00)

# ── Fetch all ShortDot TLDs ───────────────────────────────────────────────────
by_date     = defaultdict(list)
all_domains = set()
tld_domain_sets = {tld: set() for tld in TLD_LIST}

for tld in TLD_LIST:
    print(f"Fetching .{tld} ...")
    params = urllib.parse.urlencode({
        'method':       'download',
        'zone_tld':     tld,
        'filter_type':  FILTER_TYPE,
        'token':        TOKEN,
        'dataset_type': 'dataset',
    })
    req = urllib.request.Request(
        'https://netapi.com/api2/?' + params,
        headers={'User-Agent': 'Mozilla/5.0 PhishDestroy/2.0'}
    )
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            raw = gzip.decompress(resp.read()).decode('utf-8', errors='replace')
    except Exception as e:
        print(f"  .{tld} fetch failed: {e}")
        continue

    # API CSV format: url, majestic_rank, dns1, dns2, hostname
    reader = csv.reader(io.StringIO(raw))
    try:
        next(reader)  # skip header row
    except StopIteration:
        print(f"  .{tld}: empty response")
        continue

    tld_count = 0
    for row in reader:
        if len(row) < 1:
            continue
        domain   = row[0].strip().lower()
        rank     = row[1].strip() if len(row) > 1 else ''
        hostname = row[4].strip() if len(row) > 4 else ''
        email    = row[5].strip() if len(row) > 5 else ''
        phone    = row[6].strip() if len(row) > 6 else ''
        server_ip= row[7].strip() if len(row) > 7 else ''
        country  = row[8].strip() if len(row) > 8 else ''

        if not domain or '.' not in domain:
            continue
        domain_tld = domain.rsplit('.', 1)[-1].lower()
        if domain_tld != tld:
            continue

        record = {
            'd': domain,
            'e': '',
            'r': rank,
            'm': email,
            'p': phone,
            'i': server_ip or hostname,
            'c': country,
        }
        by_date[TODAY].append(record)
        all_domains.add(domain)
        tld_domain_sets[tld].add(domain)
        tld_count += 1

    print(f"  .{tld}: {tld_count:,} domains")

dates = sorted(by_date.keys())
if not dates:
    print("No data returned"); exit(0)

total_domains = len(all_domains)
print(f"\nTotal: {total_domains:,} unique domains across {len(dates)} days ({dates[0]} → {dates[-1]})")

# ── Revenue calculations ──────────────────────────────────────────────────────
def day_revenue_retail(records):
    return round(sum(get_price(r['d']) for r in records), 2)

def day_revenue_wholesale(records):
    return round(sum(get_wholesale(r['d']) for r in records), 2)

def day_icann_fees(records):
    return round(len(records) * ICANN_FEE, 2)

total_revenue_retail    = sum(day_revenue_retail(by_date[d])    for d in dates)
total_revenue_wholesale = sum(day_revenue_wholesale(by_date[d]) for d in dates)
# Registry pays ICANN: per-domain volume fee + fixed annual zone fees (7 TLDs)
total_icann_fees        = round(total_domains * ICANN_FEE + len(TLD_LIST) * ICANN_ZONE, 2)

# ── Per-TLD stats ─────────────────────────────────────────────────────────────
all_recs_flat = [r for records in by_date.values() for r in records]

tld_stats = {}
for tld in TLD_LIST:
    tld_doms  = tld_domain_sets[tld]
    tld_recs  = [r for r in all_recs_flat if r['d'].rsplit('.', 1)[-1].lower() == tld]
    deployed  = sum(1 for r in tld_recs if r.get('i'))
    no_ip     = len(tld_recs) - deployed
    dep_rate  = round(deployed / len(tld_recs) * 100, 1) if tld_recs else 0
    rev       = round(sum(get_wholesale(r['d']) for r in tld_recs), 2)
    tld_stats[tld] = {
        'count':       len(tld_doms),
        'deployed':    deployed,
        'no_ip':       no_ip,
        'deploy_rate': dep_rate,
        'revenue':     rev,
        'price':       TLD_WHOLESALE.get(tld, 1.00),
    }

# ── IP / country stats ────────────────────────────────────────────────────────
country_counts = Counter(r['c'] for r in all_recs_flat if r.get('c'))
ip_counts      = Counter(r['i'] for r in all_recs_flat if r.get('i'))

deployed_count = sum(1 for r in all_recs_flat if r.get('i'))
no_ip_count    = len(all_recs_flat) - deployed_count
deploy_rate    = round(deployed_count / len(all_recs_flat) * 100, 1) if all_recs_flat else 0

# ── Registration period ───────────────────────────────────────────────────────
durations = []
period_buckets = {'lt_1yr': 0, 'eq_1yr': 0, 'yr_2': 0, 'yr_3plus': 0}

for reg_date, records in by_date.items():
    for r in records:
        exp = r.get('e', '')
        if exp and len(exp) == 10:
            try:
                d1   = datetime.strptime(reg_date, '%Y-%m-%d')
                d2   = datetime.strptime(exp, '%Y-%m-%d')
                days = (d2 - d1).days
                durations.append(days)
                if days < 350:   period_buckets['lt_1yr']   += 1
                elif days < 500: period_buckets['eq_1yr']   += 1
                elif days < 800: period_buckets['yr_2']     += 1
                else:            period_buckets['yr_3plus'] += 1
            except Exception:
                pass

avg_lifetime       = (sum(durations) // len(durations)) if durations else 365
total_with_period  = sum(period_buckets.values())
pct_gt1 = round((period_buckets['yr_2'] + period_buckets['yr_3plus']) / total_with_period * 100, 1) if total_with_period else 0
pct_gt2 = round(period_buckets['yr_3plus'] / total_with_period * 100, 1) if total_with_period else 0

# ── Burst days ────────────────────────────────────────────────────────────────
daily_counts = {d: len(set(r['d'] for r in by_date[d])) for d in dates}
avg_daily    = sum(daily_counts.values()) / len(daily_counts) if daily_counts else 1
burst_days   = sorted(daily_counts.items(), key=lambda x: -x[1])[:10]
burst_days   = [{'date': d, 'count': c, 'x_avg': round(c / avg_daily, 1)} for d, c in burst_days]

# ── Domain freshness ──────────────────────────────────────────────────────────
catch_buckets  = {'same_day': 0, 'within_week': 0, 'within_month': 0, 'older': 0}
catch_ages_list = []
today_dt = datetime.strptime(TODAY, '%Y-%m-%d')

for reg_date, records in by_date.items():
    try:
        d1  = datetime.strptime(reg_date, '%Y-%m-%d')
        age = (today_dt - d1).days
        catch_ages_list.append(age)
        n   = len(records)
        if age == 0:    catch_buckets['same_day']     += n
        elif age <= 7:  catch_buckets['within_week']  += n
        elif age <= 30: catch_buckets['within_month'] += n
        else:           catch_buckets['older']         += n
    except Exception:
        pass

avg_catch_age = (sum(catch_ages_list) // len(catch_ages_list)) if catch_ages_list else 0
catch_total   = sum(catch_buckets.values()) or 1
fresh_pct     = round((catch_buckets['same_day'] + catch_buckets['within_week']) / catch_total * 100, 1)

# ── Majestic rank ─────────────────────────────────────────────────────────────
ranked_count   = sum(1 for r in all_recs_flat if r.get('r','').strip() not in ('', '0'))
unranked_count = total_domains - ranked_count
unranked_pct   = round(unranked_count / total_domains * 100, 1) if total_domains else 0

# ── Serial registrants ────────────────────────────────────────────────────────
email_counts = Counter()
phone_counts = Counter()
for r in all_recs_flat:
    for em in r.get('m', '').split(','):
        em = em.strip().lower()
        if em and '@' in em:
            email_counts[em] += 1
    for ph in r.get('p', '').split(','):
        ph = ph.strip()
        if ph and len(ph) >= 7:
            phone_counts[ph] += 1

serial_email_count = sum(1 for c in email_counts.values() if c >= 5)

# ── Brand keyword heatmap ─────────────────────────────────────────────────────
# Extra finance/crypto keywords relevant to ShortDot zone abuse
BRAND_KEYWORDS = [
    # Core crypto wallets
    'metamask','coinbase','binance','trustwallet','phantom','ledger','trezor',
    'uniswap','opensea','raydium','jupiter','kraken','okx','bybit','kucoin',
    'exodus','walletconnect','myetherwallet','safepal','mathwallet','bitget',
    'tokenpocket','imtoken','coinomi','electrum','rabby','rainbow','argent',
    'braavos','keplr','cosmostation','yoroi','eternl','flint','petra','martian',
    'suiet','spika','fewcha','pontem','solflare','tronlink','tronwallet','ronin',
    'metamsk','metmask','mettamask','metmsk','coinbas','coinbse','walet','wallett',
    'trustpad','truspad','upheld','dlscord','logiin','extnsion','flnance','ciaim',
    'ailocation','autth','auths',
    # Hardware wallets / multi-wallet
    'keepkey','coldcard','bitbox','ellipal','dcent','onekey','tangem','gridplus',
    'cypherock','satochip','bcvault','coolwallet','opendime','bitclip','arculus',
    'prokey','secux','keystone','coinkite','ngwallet','blade','hyperpay','hypermate',
    # DeFi — AMMs / DEXes
    'sushiswap','pancakeswap','cowswap','paraswap','kyber','traderjoe','quickswap',
    'aerodrome','velodrome','camelot','ramses','lynex','equalizer','thena',
    'curve','balancer','bancor','swapr','1inch','openocean','rango','li.fi',
    'dydx','gmx','hyperliquid','drift','aevo','vertex','mango','perpetual',
    'orca','meteora','lifinity','cetus','aldrin','crema','atrix','obyte',
    # DeFi — lending/yield
    'aave','compound','maker','yearn','convex','pendle','morpho','eigenlayer',
    'lido','marinade','jito','kamino','marginfi','solend','suilend','benqi',
    'liquity','euler','ribbon','harvest','barnbridge','truefi','clearpool',
    'maple','goldfinch','inverse','dforce','iron','dhedge','piedao','powerpool',
    'alchemix','enzyme','indexed','setprotocol','badger','pickle','vesper',
    # Layer 2 / chains
    'optimism','arbitrum','starknet','linea','zksync','polygon','base','scroll',
    'mantle','blast','taiko','manta','zircuit','berachain','monad','megaeth',
    'metis','aurora','boba','loopring','zkfair','zkevm','zkcandy','zkpad','zkswap',
    'zkswapfinance','zklend','xlayer','soneium','sonic','dymension','celestia',
    'hyperliquid','monad','berachain','mitosis','plume','megaeth',
    # Bridges / cross-chain
    'wormhole','synapse','celer','stargate','layerzero','orbiter','debridge',
    'allbridge','multichain','anyswap','connext','nomad','hop','across','socket',
    'symbiosis','renzo','renzoprotocol','kelpdao','zetachain','zircuit',
    'altlayer','manta','starknet','deBridge','orbitbridge','polynetwork',
    'boringdao','chainhop','snowbridge','lightlink',
    # NFT / gaming
    'magiceden','blur','zora','nfts','nft','opensea','foundation','rarible',
    'superrare','async','objkt','tezos','rtfkt','azuki','doodles','pudgypenguins',
    'pudgy','bayc','otherdeed','otherside','neotokyo','galxe','quest','kollab',
    'collabland','pacmoon','memecoin','meme','floki','bonk','pepe','pepecoin',
    'pepeunchained','shiba','notcoin','bitcoin','bnb','avax','tron','stellar',
    'ripple','xlm','xrp','near','sui','aptos','cardano','polkadot','cosmos',
    # Staking / liquid staking
    'staking','stake','staked','stakingreward','stakingsreward','lido','marinade',
    'rocketpool','frax','ankr','sfrxeth','cbeth','wsteth','lidofinance',
    'beefyapp','beefy','beefyhub','beefyapps','yearn','convex','aura','frax',
    # Airdrops / claims
    'airdrop','airdrops','airdropalerts','claim','claims','claimable','claiming',
    'allocation','allocations','allocate','eligible','eligibility','presale',
    'whitelist','freemint','premint','premints','giveaway','reward','rewards',
    'bonus','gift','gifts','drop','drops','earn','prize',
    # Phishing actions
    'connect','verify','login','signin','signup','secure','support','recovery',
    'restore','unlock','activate','portal','auth','register','update','official',
    'account','alert','urgent','suspended','billing','helpdesk','customer','service',
    'confirm','verification','migrate','migration','access','join','invite','invites',
    'transfer','redeem','launch','launchpad','mainnet','testnet','eligibility',
    'wallet','wallets','token','tokens','crypto','defi','web3','dapp','dapps',
    # Finance / banking
    'paypal','stripe','revolut','wise','cashapp','venmo','zelle','robinhood',
    'chase','bofa','citi','wells','amex','visa','mastercard','discover','ally',
    'schwab','fidelity','etrade','bank','banking','exchange','trading','invest',
    'investment','profit','forex','fund','capital','finance','financial',
    'advcash','payeer','paybis','paxful','paxos','transak','simplex','indacoin',
    'changenow','changelly','bestchange','moonpay','banxa','wazirx','coindcx',
    'giottus','unocoin','buyucoin','coinfident','coinfield','coingate','coinhub',
    'coinify','coinigy','coinjar','coinmama','coinone','coinpayments','coinspace',
    'coinstats','coinswitch','coinus','coinvault','coinwallet','coinweb',
    # Big tech / social
    'google','apple','microsoft','amazon','netflix','facebook','instagram',
    'tiktok','telegram','whatsapp','twitter','discord','youtube','spotify',
    'steam','roblox','zoom','linkedin','reddit','snapchat','uber',
    # Specific threat actors / infra patterns
    'drain','drainer','seed','seedphrase','privatekey','mnemonic','phrase',
    'phishing','scam','hack','exploit','honeypot','rug','fake',
    'phpmyadmin','cpanel','webmail','imap','autoconfig','smtp','mysql',
    'security','alert','helpdesk','portal','dashboard','customer','support',
    # More DeFi / newer
    'eigenlayer','ethena','pendle','morpho','symbiotic','karak','swell',
    'ondo','usual','euler','aevo','hyperliquid','dydx','drift','gmx',
    'pyth','chainlink','redstone','switchboard','dia',
    'worldcoin','worldlibertyfinancial','wlfi','trump','spacex','tesla',
    'polkadex','polkadotjs','cosmos','osmosis','keplr','leap','station',
    'karura','acala','moonbeam','moonriver','astar','shiden','khala','phala',
    'harmony','hedera','hbar','iota','velas','elrond','multiversx','elrond',
    'zilliqa','zilpay','waves','ergo','kadena','solana','near','aurora',
    'harmony','klaytn','icon','neo','ontology','vechain','tron','eos',
    'iost','steemit','steemkeychain','hive','hivekeychain','blurt',
    # Ton / telegram ecosystem
    'tonkeeper','tonhub','tonspace','tonsafe','tonwallet','tonflow',
    'tonrocket','toncrystal','tonup','tonana','mytonwallet','myton',
    # DEX aggregators / trackers
    'dappradar','defillama','debank','zerion','zapperfi','instadapp',
    'zapper','1inch','paraswap','openocean','kyber','rango','li.fi',
    # CSGO / gaming skins
    'csgo','skins','case','skin','cs2','gaming',
]
keyword_counts = Counter()
for domain in all_domains:
    label = domain.split('.')[0]
    for kw in BRAND_KEYWORDS:
        if kw in label:
            keyword_counts[kw] += 1

brand_heatmap = dict(keyword_counts.most_common(30))

# ── Legitimate use survey — load existing verified list ───────────────────────
legit_path = Path('case/LEGITIMATE_SURVEY.md')
legit_count = 0
if legit_path.exists():
    legit_text = legit_path.read_text(encoding='utf-8')
    m = re.search(r'Verified count:\s*\*\*(\d+)\*\*', legit_text)
    if m:
        legit_count = int(m.group(1))

# ── Correlation with main destroylist ─────────────────────────────────────────
correlation_count = 0
correlation_pct   = 0.0
try:
    _ml_req = urllib.request.Request(
        'https://raw.githubusercontent.com/phishdestroy/destroylist/main/list.txt',
        headers={'User-Agent': 'PhishDestroy/2.0'})
    with urllib.request.urlopen(_ml_req, timeout=30) as _ml_resp:
        _main_domains = set(_ml_resp.read().decode('utf-8', errors='replace').strip().splitlines())
    _overlap          = all_domains & _main_domains
    correlation_count = len(_overlap)
    correlation_pct   = round(correlation_count / total_domains * 100, 1) if total_domains else 0
    print(f"Correlation: {correlation_count:,} ({correlation_pct}%) in main blocklist")
except Exception as _ce:
    print(f"Correlation fetch failed: {_ce}")

# ── Monthly snapshot ──────────────────────────────────────────────────────────
_snap_dir = Path('data/snapshots')
_snap_dir.mkdir(exist_ok=True)
(_snap_dir / f'{TODAY[:7]}.json').write_text(json.dumps({
    'month':              TODAY[:7],
    'generated':          TODAY,
    'total_domains':      total_domains,
    'total_rev_retail':   round(total_revenue_retail, 2),
    'total_rev_wholesale':round(total_revenue_wholesale, 2),
    'total_icann_fees':   total_icann_fees,
    'avg_reg_days':       avg_lifetime,
    'deployment_rate':    deploy_rate,
    'fresh_pct':          fresh_pct,
    'unranked_pct':       unranked_pct,
    'correlation_pct':    correlation_pct,
    'serial_registrants': serial_email_count,
    'legit_count':        legit_count,
    'tld_stats':          tld_stats,
}, indent=2), encoding='utf-8')

# ── Write daily TXT + JSON (incremental runs only — active snapshot too large) ──
data_root = Path('data/new')
if FILTER_TYPE == 'new':
    for day_date in dates:
        yr, mo = day_date[:4], day_date[5:7]
        day_dir = data_root / yr / mo
        day_dir.mkdir(parents=True, exist_ok=True)

        records = by_date[day_date]
        domains = sorted(set(r['d'] for r in records))

        (day_dir / f'{day_date}.txt').write_text('\n'.join(domains) + '\n', encoding='utf-8')
        day_json = {
            'date':              day_date,
            'count':             len(domains),
            'revenue_wholesale': day_revenue_wholesale(records),
            'revenue_retail':    day_revenue_retail(records),
            'icann_fees':        day_icann_fees(records),
            'domains': [
                {k2: v2 for k2, v2 in {
                    'domain':      r['d'],
                    'tld':         r['d'].rsplit('.', 1)[-1].lower(),
                    'expiring_at': r.get('e', ''),
                    'ip':          r.get('i', ''),
                    'ip_country':  r.get('c', ''),
                    'email':       r.get('m', '').split(',')[0].strip().lower() if r.get('m') else '',
                    'phone':       r.get('p', '').split(',')[0].strip() if r.get('p') else '',
                }.items() if v2}
                for r in sorted(records, key=lambda x: x['d'])
            ]
        }
        (day_dir / f'{day_date}.json').write_text(json.dumps(day_json, separators=(',', ':')), encoding='utf-8')

    # ── Monthly rollup TXT per TLD ────────────────────────────────────────────────
    by_month = defaultdict(set)
    for day_date, records in by_date.items():
        by_month[day_date[:7]].update(r['d'] for r in records)

    for month_key, doms in by_month.items():
        yr = month_key[:4]
        mp = data_root / yr
        mp.mkdir(parents=True, exist_ok=True)
        (mp / f'{month_key}.txt').write_text('\n'.join(sorted(doms)) + '\n', encoding='utf-8')

# Per-TLD files
tld_dir = Path('data/by_tld')
tld_dir.mkdir(parents=True, exist_ok=True)
for tld, doms in tld_domain_sets.items():
    if doms:
        (tld_dir / f'{tld}.txt').write_text('\n'.join(sorted(doms)) + '\n', encoding='utf-8')

# all.txt
Path('data/all.txt').write_text('\n'.join(sorted(all_domains)) + '\n', encoding='utf-8')

# ── data/index.json ───────────────────────────────────────────────────────────
index_days = [
    {k: v for k, v in {
        'date':              d,
        'count':             len(set(r['d'] for r in by_date[d])),
        'revenue_wholesale': day_revenue_wholesale(by_date[d]),
        'icann_fees':        day_icann_fees(by_date[d]),
        'path':              f'data/new/{d[:4]}/{d[5:7]}/{d}.txt' if FILTER_TYPE == 'new' else None,
    }.items() if v is not None}
    for d in dates
]
Path('data/index.json').write_text(json.dumps({
    'days':                    index_days,
    'total_domains':           total_domains,
    'tld_breakdown':           tld_stats,
    'total_rev_retail':        round(total_revenue_retail, 2),
    'total_rev_wholesale':     round(total_revenue_wholesale, 2),
    'total_icann_fees':        total_icann_fees,
    'avg_registration_days':   avg_lifetime,
    'ip_countries':            dict(country_counts.most_common(10)),
    'top_shared_ips':          dict(ip_counts.most_common(20)),
    'deployed_count':          deployed_count,
    'no_ip_count':             no_ip_count,
    'deployment_rate':         deploy_rate,
    'reg_periods':             period_buckets,
    'pct_gt_1yr':              pct_gt1,
    'pct_gt_2yr':              pct_gt2,
    'catch_age_buckets':       catch_buckets,
    'avg_catch_age_days':      avg_catch_age,
    'fresh_pct':               fresh_pct,
    'burst_days':              burst_days,
    'brand_heatmap':           brand_heatmap,
    'unranked_pct':            unranked_pct,
    'ranked_count':            ranked_count,
    'correlation_count':       correlation_count,
    'correlation_pct':         correlation_pct,
    'legit_count':             legit_count,
    'serial_email_count':      serial_email_count,
    'legit_ratio_pct':         round(legit_count / total_domains * 100, 4) if total_domains else 0,
    'last_updated':            dates[-1],
}, indent=2) + '\n', encoding='utf-8')

# ── IOC exports ───────────────────────────────────────────────────────────────
ioc_dir = Path('data/ioc')
ioc_dir.mkdir(parents=True, exist_ok=True)

serial_regs = []
for em, cnt in email_counts.most_common(50):
    if cnt < 5:
        break
    domains_for_email = sorted(set(
        r['d'] for r in all_recs_flat
        if r.get('m', '').split(',')[0].strip().lower() == em
    ))[:100]
    serial_regs.append({'email': em, 'count': cnt, 'domains': domains_for_email})

(ioc_dir / 'serial_registrants.json').write_text(
    json.dumps({'generated': TODAY, 'count': len(serial_regs), 'registrants': serial_regs}, indent=2),
    encoding='utf-8')

shared_ip_export = []
for ip_addr, cnt in ip_counts.most_common(50):
    if cnt < 3:
        break
    domains_for_ip = sorted(set(r['d'] for r in all_recs_flat if r.get('i') == ip_addr))
    country        = next((r.get('c', '') for r in all_recs_flat if r.get('i') == ip_addr and r.get('c')), '')
    shared_ip_export.append({'ip': ip_addr, 'count': cnt, 'country': country, 'domains': domains_for_ip[:100]})

(ioc_dir / 'shared_ips.json').write_text(
    json.dumps({'generated': TODAY, 'count': len(shared_ip_export), 'ips': shared_ip_export}, indent=2),
    encoding='utf-8')

brand_domains_export = {}
for kw in brand_heatmap:
    brand_domains_export[kw] = sorted(d for d in all_domains if kw in d.split('.')[0])[:200]

(ioc_dir / 'brand_domains.json').write_text(
    json.dumps({'generated': TODAY, 'keywords': brand_domains_export}, indent=2),
    encoding='utf-8')

(ioc_dir / 'serial_emails.txt').write_text(
    '\n'.join(f'{x["email"]}\t{x["count"]}' for x in serial_regs) + '\n' if serial_regs else '',
    encoding='utf-8')
(ioc_dir / 'shared_ips.txt').write_text(
    '\n'.join(f'{x["ip"]}\t{x["count"]}\t{x["country"]}' for x in shared_ip_export) + '\n' if shared_ip_export else '',
    encoding='utf-8')
_brand_lines = [f'{kw}\t{d}' for kw, doms in brand_domains_export.items() for d in doms]
(ioc_dir / 'brand_domains.txt').write_text('\n'.join(_brand_lines) + '\n' if _brand_lines else '', encoding='utf-8')

# Per-TLD deployed domain files
deployed_dir = ioc_dir / 'deployed'
deployed_dir.mkdir(parents=True, exist_ok=True)
for tld in TLD_LIST:
    tld_recs = [r for r in all_recs_flat if r['d'].rsplit('.', 1)[-1].lower() == tld]
    deployed_doms = sorted(r['d'] for r in tld_recs if r.get('i'))
    if deployed_doms:
        (deployed_dir / f'{tld}.txt').write_text('\n'.join(deployed_doms) + '\n', encoding='utf-8')

# Combined deployed list
all_deployed = sorted(r['d'] for r in all_recs_flat if r.get('i'))
(ioc_dir / 'deployed_all.txt').write_text('\n'.join(all_deployed) + '\n', encoding='utf-8')

# ── STIX 2.1 bundle ───────────────────────────────────────────────────────────
import uuid

def _stix_id(prefix):
    return f'{prefix}--{uuid.uuid4()}'

_identity_id = 'identity--phishdestroy-shortdot'
_stix_objs   = [{
    'type': 'identity', 'spec_version': '2.1', 'id': _identity_id,
    'created': f'{TODAY}T00:00:00.000Z', 'modified': f'{TODAY}T00:00:00.000Z',
    'name': 'PhishDestroy — ShortDot Zone Investigation',
    'identity_class': 'organization', 'sectors': ['non-profit'],
    'contact_information': 'https://phishdestroy.io',
}]

for _d in sorted(all_domains)[:5000]:
    _tld = _d.rsplit('.', 1)[-1].lower()
    _stix_objs.append({
        'type': 'indicator', 'spec_version': '2.1', 'id': _stix_id('indicator'),
        'created': f'{TODAY}T00:00:00.000Z', 'modified': f'{TODAY}T00:00:00.000Z',
        'created_by_ref': _identity_id,
        'name': f'Phishing domain: {_d}',
        'indicator_types': ['malicious-activity'],
        'pattern': f"[domain-name:value = '{_d}']",
        'pattern_type': 'stix',
        'valid_from': f'{TODAY}T00:00:00.000Z',
        'labels': ['phishing', f'tld-{_tld}', 'shortdot-zone'],
    })

for _ip_item in shared_ip_export[:200]:
    _stix_objs.append({
        'type': 'indicator', 'spec_version': '2.1', 'id': _stix_id('indicator'),
        'created': f'{TODAY}T00:00:00.000Z', 'modified': f'{TODAY}T00:00:00.000Z',
        'created_by_ref': _identity_id,
        'name': f'Shared hosting IP: {_ip_item["ip"]} ({_ip_item["count"]} domains)',
        'indicator_types': ['malicious-activity'],
        'pattern': "[ipv4-addr:value = '" + _ip_item['ip'] + "']",
        'pattern_type': 'stix', 'valid_from': f'{TODAY}T00:00:00.000Z',
        'labels': ['shared-hosting', 'bulletproof'],
    })

(ioc_dir / 'stix-bundle.json').write_text(
    json.dumps({'type': 'bundle', 'id': _stix_id('bundle'), 'objects': _stix_objs}, indent=2),
    encoding='utf-8')

# ── Auto-generate LIVE_STATS in README.md ─────────────────────────────────────
def _fmt(n): return f'{n:,}' if isinstance(n, (int, float)) else str(n)
def _bar(n, max_n, width=18):
    if not max_n: return ''
    filled = int(n / max_n * width)
    return '█' * filled + '░' * (width - filled)
def _redact(e):
    if '@' not in e: return e[:3] + '***'
    local, dom = e.split('@', 1)
    return (local[0] if len(local) <= 3 else local[:3]) + '***@' + dom

_readme_path = Path('README.md')
if _readme_path.exists():
    _md = _readme_path.read_text(encoding='utf-8')
    _parts = ['<!-- LIVE_STATS:START -->', '']
    _parts.append(f'> 🔴 **LIVE INVESTIGATION FEED** &middot; Auto-updated &middot; Last fetch `{TODAY}`')
    _parts.append('')

    _parts.append('<table><tr>')
    _parts.append(f'<td align="center"><b>📦 Domains tracked</b><br/><sub><code>{_fmt(total_domains)}</code></sub></td>')
    _parts.append(f'<td align="center"><b>💰 Est. ShortDot revenue</b><br/><sub><code>${total_revenue_wholesale:,.0f}</code></sub></td>')
    _parts.append(f'<td align="center"><b>💸 ICANN fees (registry)</b><br/><sub><code>${total_icann_fees:,.0f}</code></sub></td>')
    _parts.append(f'<td align="center"><b>✅ Confirmed malicious</b><br/><sub><code>{correlation_pct}%</code> ({_fmt(correlation_count)})</sub></td>')
    _parts.append(f'<td align="center"><b>🏛️ Verified legitimate</b><br/><sub><code>{legit_count}</code> sites found</sub></td>')
    _parts.append(f'<td align="center"><b>⚡ Fresh (≤7d)</b><br/><sub><code>{fresh_pct}%</code></sub></td>')
    _parts.append('</tr></table>')
    _parts.append('')

    _parts.append('### 🏷️ TLD Breakdown')
    _parts.append('')
    _parts.append('| TLD | Domains | Active | No IP (dead) | Confirmed Malicious | Verified Legit | Est. Revenue |')
    _parts.append('|:--|--:|--:|--:|--:|--:|--:|')
    for _tld, _info in tld_stats.items():
        _tld_corr = sum(1 for d in tld_domain_sets[_tld] if d in _main_domains) if 'correlation_count' in dir() else 0
        _parts.append(
            f"| `.{_tld}` | {_info['count']:,} | {_info['deployed']:,} ({_info['deploy_rate']}%) "
            f"| {_info['no_ip']:,} | {_tld_corr:,} | — | ${_info['revenue']:,.0f} |"
        )
    _parts.append('')
    _parts.append('*Table auto-generated on each daily fetch run.*')
    _parts.append('')

    if country_counts:
        _parts.append('### 🌍 Top Hosting Countries')
        _parts.append('')
        _parts.append('```')
        _max_c = country_counts.most_common(1)[0][1]
        for _c, _n in country_counts.most_common(8):
            _pct = _n / sum(country_counts.values()) * 100
            _parts.append(f'{(_c or "??"):3} {_bar(_n, _max_c)} {_n:>10,} ({_pct:.1f}%)')
        _parts.append('```')
        _parts.append('')

    if burst_days:
        _parts.append('### 📈 Registration Burst Days')
        _parts.append('')
        _parts.append('| Date | Domains | × Average |')
        _parts.append('|:--|--:|--:|')
        for _b in burst_days[:5]:
            _flag = ' 🚨' if _b['x_avg'] >= 5 else (' 🔥' if _b['x_avg'] >= 2 else '')
            _parts.append(f"| `{_b['date']}` | {_b['count']:,} | **{_b['x_avg']}×**{_flag} |")
        _parts.append('')

    if brand_heatmap:
        _parts.append('### 🎯 Top Targeted Brands & Keywords')
        _parts.append('')
        _parts.append(' &middot; '.join(f'`{kw} ({n:,})`' for kw, n in list(brand_heatmap.items())[:15]))
        _parts.append('')

    _parts.append('### 📥 Download Threat Intelligence')
    _parts.append('')
    _parts.append('| File | Format | Description |')
    _parts.append('|:--|:--:|:--|')
    _parts.append('| [`data/all.txt`](data/all.txt) | TXT | All tracked domains across all 7 zones |')
    _parts.append('| [`data/index.json`](data/index.json) | JSON | Full analytics snapshot |')
    _parts.append('| [`data/ioc/serial_registrants.json`](data/ioc/serial_registrants.json) | JSON | Repeat registrants + their domains |')
    _parts.append('| [`data/ioc/shared_ips.json`](data/ioc/shared_ips.json) | JSON | Bulletproof hosting clusters |')
    _parts.append('| [`data/ioc/brand_domains.json`](data/ioc/brand_domains.json) | JSON | Domains by targeted brand |')
    _parts.append('| [`data/ioc/stix-bundle.json`](data/ioc/stix-bundle.json) | STIX 2.1 | MISP/OpenCTI ready bundle |')
    _parts.append('| [`ioc/domains_all_malicious.txt`](ioc/domains_all_malicious.txt) | TXT | Confirmed malicious — all severity |')
    _parts.append('| [`ioc/domains_high.txt`](ioc/domains_high.txt) | TXT | HIGH severity only |')
    _parts.append('')
    _parts.append('> 📊 Live dashboard: Pages link at top · Updated daily 06:00 UTC')
    _parts.append('')
    _parts.append('<!-- LIVE_STATS:END -->')

    _new_block = '\n'.join(_parts)
    if '<!-- LIVE_STATS:START -->' in _md and '<!-- LIVE_STATS:END -->' in _md:
        _md = re.sub(r'<!-- LIVE_STATS:START -->.*?<!-- LIVE_STATS:END -->', _new_block, _md, count=1, flags=re.DOTALL)
    _readme_path.write_text(_md, encoding='utf-8')
    print('README.md LIVE_STATS block regenerated')

# ── Stats badge JSON files ────────────────────────────────────────────────────
stats_dir = Path('stats')
stats_dir.mkdir(exist_ok=True)

def badge(label, message, color, label_color='0c1018'):
    return json.dumps({
        'schemaVersion': 1, 'label': label, 'message': str(message),
        'color': color, 'labelColor': label_color, 'style': 'flat-square'
    })

today_recs    = by_date.get(TODAY, [])
today_count   = len(set(r['d'] for r in today_recs))

(stats_dir / 'today.json').write_text(badge('new today', f'{today_count:,}', 'da3633'), encoding='utf-8')
(stats_dir / 'total.json').write_text(badge('domains tracked', f'{total_domains:,}', 'da3633'), encoding='utf-8')
(stats_dir / 'last_fetch.json').write_text(badge('last fetch', dates[-1], '0075ca'), encoding='utf-8')
(stats_dir / 'revenue.json').write_text(badge('ShortDot revenue', f'${total_revenue_wholesale:,.0f}', 'e3b341'), encoding='utf-8')
(stats_dir / 'icann.json').write_text(badge('ICANN fees', f'${total_icann_fees:,.0f}', 'e3b341'), encoding='utf-8')
(stats_dir / 'legit.json').write_text(badge('verified legit', f'{legit_count} sites found', '3fb950'), encoding='utf-8')
(stats_dir / 'deployed.json').write_text(badge('deployed', f'{deployed_count:,} ({deploy_rate:.0f}%)', '2ea44f'), encoding='utf-8')
(stats_dir / 'no_ip.json').write_text(badge('no DNS at reg', f'{no_ip_count:,} ({100-deploy_rate:.0f}%)', 'e3b341'), encoding='utf-8')
(stats_dir / 'freshness.json').write_text(badge('fresh catch', f'{fresh_pct}% ≤7d old', '2ea44f'), encoding='utf-8')
(stats_dir / 'unranked.json').write_text(badge('unranked domains', f'{unranked_pct}% zero Majestic', '6e40c9'), encoding='utf-8')

if country_counts:
    top3 = ' · '.join(f'{c}:{n:,}' for c, n in country_counts.most_common(3) if c)
    (stats_dir / 'hosting.json').write_text(badge('top hosting', top3 or 'n/a', '0075ca'), encoding='utf-8')
if ip_counts:
    (stats_dir / 'top_ip.json').write_text(badge('top IP domains', f'{ip_counts.most_common(1)[0][1]:,} domains', '8b5cf6'), encoding='utf-8')
if serial_email_count:
    (stats_dir / 'serial_regs.json').write_text(badge('serial registrants', f'{serial_email_count:,} emails ≥5 domains', 'da3633'), encoding='utf-8')
if brand_heatmap:
    (stats_dir / 'brands.json').write_text(badge('top targets', ' · '.join(list(brand_heatmap.keys())[:3]), '6e40c9'), encoding='utf-8')

# Per-TLD badges
tld_badge_dir = stats_dir / 'by_tld'
tld_badge_dir.mkdir(exist_ok=True)
for _tld, _info in tld_stats.items():
    _msg = f"{_info['count']:,} · {_info['deploy_rate']}% deployed"
    (tld_badge_dir / f'{_tld}.json').write_text(badge(f'.{_tld}', _msg, 'da3633'), encoding='utf-8')

print(f"\nDone: {total_domains:,} domains | ${total_revenue_wholesale:,.2f} wholesale | ${total_icann_fees:,.2f} ICANN | legit: {legit_count} | deployed: {deploy_rate:.0f}% | fresh: {fresh_pct}%")
