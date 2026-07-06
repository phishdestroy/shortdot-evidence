"""
Converts data/index.json + ioc/indicators.csv -> docs/data.json for GitHub Pages.

Usage:
  python docs/build_datajson.py
  python docs/build_datajson.py --index data/index.json --ioc ioc/indicators.csv --out docs/data.json
"""

import argparse, csv, json, re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).parent.parent


def load_index(path: Path) -> dict:
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {}


def load_indicators(path: Path) -> list[dict]:
    if not path.exists():
        return []
    csv.field_size_limit(10_000_000)
    with open(path, newline="", encoding="utf-8-sig", errors="replace") as f:
        return list(csv.DictReader(f))


def load_serial_registrants(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8")).get("registrants", [])


def load_shared_ips(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8")).get("ips", [])


def load_legit_count(path: Path) -> int:
    if not path.exists():
        return 0
    text = path.read_text(encoding="utf-8")
    m = re.search(r"Verified count:\s*\*\*(\d+)\*\*", text)
    return int(m.group(1)) if m else 0


def build_clusters(serial_regs: list[dict], shared_ips: list[dict]) -> list[dict]:
    clusters = []
    for reg in serial_regs[:20]:
        clusters.append({
            "key":      reg.get("email", "")[:6] + "***",
            "label":    "serial_registrant",
            "count":    reg.get("count", 0),
            "domains":  reg.get("domains", [])[:20],
            "category": "SERIAL_REG",
        })
    for ip in shared_ips[:20]:
        clusters.append({
            "key":      ip.get("ip", ""),
            "label":    f'shared_ip · {ip.get("country", "?")}',
            "count":    ip.get("count", 0),
            "domains":  ip.get("domains", [])[:20],
            "category": "SHARED_HOSTING",
        })
    clusters.sort(key=lambda c: -c["count"])
    return clusters[:30]


def build_stats(index: dict, domains: list[dict], legit_count: int) -> dict:
    cats = Counter(r.get("category", "") for r in domains)
    high   = sum(1 for r in domains if r.get("severity", "").upper() == "HIGH")
    medium = sum(1 for r in domains if r.get("severity", "").upper() == "MEDIUM")
    return {
        "total":            index.get("total_domains", 0),
        "high":             high,
        "medium":           medium,
        "alive":            index.get("deployed_count", 0),
        "dead":             index.get("no_ip_count", 0),
        "deploy_rate":      index.get("deployment_rate", 0),
        "fresh_pct":        index.get("fresh_pct", 0),
        "unranked_pct":     index.get("unranked_pct", 0),
        "legit_count":      legit_count,
        "legit_ratio":      index.get("legit_ratio_pct", 0),
        "icann_fees":       index.get("total_icann_fees", 0),
        "shortdot_revenue": index.get("total_rev_wholesale", 0),
        "retail_revenue":   index.get("total_rev_retail", 0),
        "avg_reg_days":     index.get("avg_registration_days", 365),
        "correlation_pct":  index.get("correlation_pct", 0),
        "correlation_count":index.get("correlation_count", 0),
        "tld_breakdown":    index.get("tld_breakdown", {}),
        "burst_days":       index.get("burst_days", []),
        "brand_heatmap":    index.get("brand_heatmap", {}),
        "ip_countries":     index.get("ip_countries", {}),
        "reg_periods":      index.get("reg_periods", {}),
        "pct_gt_1yr":       index.get("pct_gt_1yr", 0),
        "pct_gt_2yr":       index.get("pct_gt_2yr", 0),
        "catch_age_buckets":index.get("catch_age_buckets", {}),
        "avg_catch_age":    index.get("avg_catch_age_days", 0),
        "serial_regs":      index.get("serial_email_count", 0),
        "icann_volume_annual": round(index.get("total_domains", 0) * 0.25, 2),
        "icann_zone_annual":   7 * 25800,
        "categories":       dict(cats.most_common()),
        "screenshots":      0,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--index",   default=str(HERE / "data" / "index.json"))
    ap.add_argument("--ioc",     default=str(HERE / "ioc" / "indicators.csv"))
    ap.add_argument("--legit",   default=str(HERE / "case" / "LEGITIMATE_SURVEY.md"))
    ap.add_argument("--out",     default=str(Path(__file__).parent / "data.json"))
    args = ap.parse_args()

    print(f"[*] Loading index: {args.index}")
    index = load_index(Path(args.index))

    print(f"[*] Loading indicators: {args.ioc}")
    domains = load_indicators(Path(args.ioc))
    print(f"    {len(domains)} indicators")

    legit_count = load_legit_count(Path(args.legit))
    print(f"[*] Legit count: {legit_count}")

    serial_regs = load_serial_registrants(HERE / "data" / "ioc" / "serial_registrants.json")
    shared_ips  = load_shared_ips(HERE / "data" / "ioc" / "shared_ips.json")
    clusters    = build_clusters(serial_regs, shared_ips)
    print(f"[*] Clusters: {len(clusters)}")

    stats = build_stats(index, domains, legit_count)

    # Include all IOC indicators in data.json for the domain table
    domains_out = domains

    # Build brand summary from brand_domains.json (keywords:{kw:[domains]}) + heatmap counts
    brand_json_path = HERE / "data" / "ioc" / "brand_domains.json"
    _hmap = stats.get("brand_heatmap", {})
    _CATS = {
        "crypto": "crypto", "vault": "crypto", "token": "crypto", "nft": "crypto",
        "bridge": "crypto", "claim": "crypto", "drain": "crypto",
        "capital": "banking", "fund": "banking", "investment": "banking",
        "trading": "banking", "trust": "banking", "cfd": "banking",
        "account": "tech", "secure": "tech", "login": "tech", "connect": "tech",
        "support": "tech", "official": "tech", "verify": "tech", "update": "tech",
    }
    brand_summary = {}
    if brand_json_path.exists():
        bd = json.loads(brand_json_path.read_text(encoding="utf-8"))
        kw_data = bd.get("keywords", {})
        if kw_data:
            _top = sorted(
                [{"brand": kw_name,
                  "count": _hmap.get(kw_name, len(dom_list) if isinstance(dom_list, list) else 0),
                  "category": _CATS.get(kw_name, "tech"),
                  "sample": (dom_list[:5] if isinstance(dom_list, list) else [])}
                 for kw_name, dom_list in kw_data.items()],
                key=lambda x: -x["count"]
            )
            _cat_totals: dict[str, int] = {}
            for item in _top:
                _cat_totals[item["category"]] = _cat_totals.get(item["category"], 0) + item["count"]
            brand_summary = {
                "total_brand_domains": sum(_hmap.values()) or sum(
                    len(v) for v in kw_data.values() if isinstance(v, list)),
                "categories": _cat_totals,
                "top_brands": _top[:30],
            }
    if not brand_summary and _hmap:
        _top = sorted(
            [{"brand": kw, "count": cnt, "category": _CATS.get(kw, "tech"), "sample": []}
             for kw, cnt in _hmap.items()],
            key=lambda x: -x["count"]
        )
        _cat_totals = {}
        for item in _top:
            _cat_totals[item["category"]] = _cat_totals.get(item["category"], 0) + item["count"]
        brand_summary = {
            "total_brand_domains": sum(_hmap.values()),
            "categories": _cat_totals,
            "top_brands": _top[:30],
        }

    # Include recent daily feed (last 60 days) from index for dashboard
    daily_feed = sorted(index.get("days", []), key=lambda d: d.get("date",""), reverse=True)[:60]

    out = {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "stats":     stats,
        "clusters":  clusters,
        "domains":   domains_out,
        "brand":     brand_summary,
        "daily":     daily_feed,
    }

    out_path = Path(args.out)
    out_path.parent.mkdir(exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
    size = out_path.stat().st_size
    print(f"[+] data.json → {out_path}  ({size // 1024} KB,  {len(domains_out)} domains in payload)")

    print(f"\n[+] Stats:")
    print(f"    Total: {stats['total']}  HIGH: {stats['high']}  MEDIUM: {stats['medium']}")
    print(f"    Legit: {stats['legit_count']}  ICANN fees: ${stats['icann_fees']:,.2f}")
    print(f"    ShortDot revenue: ${stats['shortdot_revenue']:,.2f}")
    print(f"\n[+] Top categories:")
    for cat, cnt in list(stats["categories"].items())[:8]:
        print(f"    {cat:<28} {cnt:>5}")


if __name__ == "__main__":
    main()
