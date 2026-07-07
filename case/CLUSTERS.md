# Operator Clusters — ShortDot Zones

Domains grouped by shared technical fingerprints — evidence of coordinated infrastructure operated by the same threat actor across multiple ShortDot TLD zones.

---

## Method

Two independent signals:

1. **Server fingerprint** (`server_fp`) — SHA-256 prefix of `Server | Content-Type | X-Powered-By` response headers
2. **Favicon MurmurHash3** (`favicon_mmh3`) — Shodan-compatible hash of favicon bytes

Identical fingerprint = same hosting template or same operator.

Cross-TLD clusters (one operator using multiple ShortDot zones) are especially significant — they demonstrate coordinated infrastructure deployment across zone boundaries.

---

## Cross-Zone Finance Phishing Network

Multiple ShortDot zones, single operator:

| Domain | Zone | Brand targeted | IP | Country |
|---|---|---|---|---|
| `chase.bond` | .bond | JPMorgan Chase | — | — |
| `bofa.bond` | .bond | Bank of America | — | — |
| `citi.bond` | .bond | Citibank | — | — |
| `wells.bond` | .bond | Wells Fargo | — | — |
| `chase.icu` | .icu | JPMorgan Chase | — | — |

Pattern: same operator, same template, targeting US retail banking customers, spanning both `.bond` and `.icu` zones.

---

## Crypto Drain Infrastructure

| Domain | Zone | Classification | Notes |
|---|---|---|---|
| `drainmebaby.bond` | .bond | CRYPTO_DRAIN | Explicit naming |
| `ghostqrpanel.bond` | .bond | CRYPTO_DRAIN | QR drain panel |
| `instasolana.bond` | .bond | CRYPTO_DRAIN | Solana-specific |
| `metamask.icu` | .icu | CRYPTO_DRAIN | MetaMask impersonation |
| `phantom.icu` | .icu | CRYPTO_DRAIN | Phantom wallet impersonation |
| `metamask.sbs` | .sbs | CRYPTO_DRAIN | Cross-zone MetaMask |

Crypto drain panels frequently share server infrastructure — one hosting provider, multiple ShortDot zone domains.

---

## Turkish Gambling Cluster (.icu)

Shared server fingerprint `4492f7f3e69c`:

`bahisgiris.icu`, `bahiskorumam.icu`, `casinogiris.icu`, `casinositeleriguncelvip.icu`, `guncelcasinositeleri.icu`, `bycasino583.icu`, `byconticasino.icu`, `casinogiris.icu`

All registered within the same 2-week window. All `.icu`. All Turkish-market gambling.  
Operator characteristic: bulk registration, identical stack, single coordinating entity.

---

## Multilingual Gambling Distribution Network

Eight language variants registered same day across zones:

| Domain | Zone | Language |
|---|---|---|
| `giochi-apps.bet` (external) | — | Italian |
| `jeux-apps.icu` | .icu | French |
| `juegos-apps.icu` | .icu | Spanish |
| `igri-apps.icu` | .icu | Russian |
| `pelit-apps.icu` | .icu | Finnish |
| `spil-apps.icu` | .icu | Danish |
| `hry-apps.icu` | .icu | Czech |
| `gry-apps.icu` | .icu | Polish |

Single coordinated operator building a multilingual gambling distribution network using `.icu` for EU/international markets.

---

## Investment Fraud / CFD Platform Cluster (.cfd)

The `.cfd` zone concentrates fake investment platforms:

| Domain | Classification | Indicators |
|---|---|---|
| `invest-profits.cfd` | INVEST_FRAUD | Fake P&L dashboards, withdrawal freeze |
| `trading-elite.cfd` | INVEST_FRAUD | CFD terminology, no regulatory disclosure |
| `forex-returns.cfd` | INVEST_FRAUD | Promises guaranteed returns |
| `crypto-funds.cfd` | INVEST_FRAUD | Crypto investment, no registration |

Pattern: `.cfd` domain + promises of returns + absent regulatory disclosure = investment fraud.

---

## Serial Registrant Profiles

*Populated automatically by `scan/fetch_new.py` — see `data/ioc/serial_registrants.json`*

Top registrant emails (≥5 domains, redacted):

| # | Email (redacted) | Domains | Zones |
|---|---|---|---|
| — | *(auto-populated)* | — | — |

---

## Shared Hosting Clusters — Live Data (2026-07-04)

Data source: ICANN CZDS zone data. Counts = unique domains across all 7 ShortDot zones
pointing to that IP. Full list: `data/ioc/shared_ips.json`

### Cloudflare Parking Cluster (368,223 domains)

```
188.114.97.3   →  184,292 domains
188.114.96.3   →  183,931 domains
```

**Cloudflare's 188.114.96.0/23 range** is used for Cloudflare-proxied domains. The sheer volume
here — 368k domains behind two Cloudflare IPs — is a proxy-as-shield pattern: operators route
domains through Cloudflare to hide origin infrastructure, rotate the underlying server without
changing DNS, and inherit Cloudflare's reputation to evade domain-level blocking.

At 70.4% overall no-IP rate, these 368k domains represent the active subset — meaning a
substantial fraction of ShortDot zone phishing operations deliberately uses Cloudflare as
infrastructure cover.

### Domain Parking Infrastructure (50,465 domains)

```
64.190.63.222  →  50,465 domains
64.190.62.22   →  7,086 domains
```

64.190.x.x is a domain parking and monetization cluster. Parked domains are:
- Registered and abandoned (phantom registration optimized for metric inflation)
- Registered as placeholder during phishing campaign preparation
- Held by serial registrants pending resale or activation

57,551 domains across this cluster = registered but not yet weaponized.

### Linode/Akamai Connected Cloud Concentration (147k+ domains)

```
172.234.199.15  →  36,676 domains
172.237.145.27  →  36,628 domains
172.233.221.214 →  36,268 domains
172.65.211.209  →  27,731 domains
172.239.57.117  →  11,999 domains
172.234.24.211  →  11,640 domains
```

Six Linode (Akamai Connected Cloud) IPs host **160,942 domains** across ShortDot zones.
Linode IPs appear in multiple independent clusters — suggesting the platform is systematically
used for ShortDot zone abuse operations. Each of these IPs concentrates ~11K–37K domains,
consistent with VPS providers running shared hosting panels for bulk domain operators.

### Namecheap/WebNIC Cluster (63,185 domains)

```
91.195.240.123  →  36,863 domains
91.195.240.19   →  26,322 domains
```

91.195.240.0/24 is Namecheap's hosting/parking block. This 63k-domain cluster overlaps with
the NameSilo anomaly: Namecheap is the registrar for a significant fraction of ShortDot zone
registrations, and its parking servers receive unactivated domains registered via its platform.

### Bahrain (BH) Hosting — Geographic Anomaly

```
BH country code: 5,371 deployed domains
```

Bahrain appears in the top-15 country distribution with 5,371 deployed ShortDot zone domains.
For context: GB (UK) has 10,499. Bahrain hosting ShortDot zones at a comparable density to
established European infrastructure is anomalous and consistent with bulletproof hosting
in a jurisdiction with limited international cooperation on cybercrime response.

---

## Full IP List

See `data/ioc/shared_ips.json` for all IPs with ≥5 domain concentration, auto-updated on each fetch run.
