# Scan Pipeline

## fetch_new.py

Daily data pipeline: ICANN CZDS zone pull → per-TLD stats → IOC exports → README update → badge JSON.

### Requirements

- Python 3.12+
- No external dependencies (stdlib only)

### Environment Variables

| Variable | Required | Description |
|---|---|---|
| `NETAPI_TOKEN` | Yes | Zone data access token |
| `TLD_LIST` | No | Comma-separated TLDs (default: `icu,bond,cyou,sbs,cfd,buzz,qpon`) |

### Run Locally

```bash
export NETAPI_TOKEN=your_token_here
python scan/fetch_new.py
```

### GitHub Actions

Runs daily at 06:00 UTC via `.github/workflows/update.yml`.  
Token stored as repository secret `NETAPI_TOKEN`.

### Output

| File | Description |
|---|---|
| `data/all.txt` | All domains across all 7 zones |
| `data/index.json` | Full analytics snapshot |
| `data/by_tld/*.txt` | Per-TLD domain lists |
| `data/new/YYYY/MM/YYYY-MM-DD.txt` | Daily additions (plain list) |
| `data/new/YYYY/MM/YYYY-MM-DD.json` | Daily additions (enriched) |
| `data/ioc/` | IOC exports (STIX, serial registrants, shared IPs) |
| `data/snapshots/YYYY-MM.json` | Monthly analytics snapshot |
| `stats/*.json` | Badge JSON files (shields.io endpoint format) |
| `stats/by_tld/*.json` | Per-TLD badge JSON |
| `README.md` | `LIVE_STATS` block auto-updated |
