# Data Directory

All domain data across ShortDot zones (.icu, .bond, .cyou, .sbs, .cfd, .buzz, .qpon).

| Path | Description |
|---|---|
| `all.txt` | All tracked domains — one per line |
| `index.json` | Full analytics snapshot (updated daily) |
| `by_tld/` | Per-TLD domain lists |
| `ioc/` | IOC exports: STIX 2.1, serial registrants, shared IPs, brand domains |
| `snapshots/` | Monthly analytics snapshots |
| `new/YYYY/MM/` | Daily domain additions (TXT + enriched JSON) |

Updated daily at 06:00 UTC via GitHub Actions.
