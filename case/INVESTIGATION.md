# Investigation: ShortDot SA — Zone Abuse Evidence

**Status:** Active  
**Scope:** All domains registered in ShortDot-operated TLD zones: .icu, .bond, .cyou, .sbs, .cfd, .buzz, .qpon  
**Investigation start:** 2026  
**Data source:** NetAPI — full zone delta, daily pull

---

## Registry Profile

| Field | Value |
|---|---|
| Entity | ShortDot SA |
| Jurisdiction | Luxembourg — Société Anonyme |
| Address | 9 Rue Louvigny, L-1946 Luxembourg |
| Technical backend | CentralNic (London) |
| Zones operated | .icu, .bond, .cyou, .sbs, .cfd, .buzz, .qpon |
| Zone size (combined) | See `data/index.json` |
| Named partners | GoDaddy, Alibaba, GMO, Namecheap, NameSilo, Dynadot + 400+ |
| Brand protection arm | NameBlock |
| Other ventures | Nicky, WebUnited |

---

## Methodology

### Data Collection — NetAPI Pull

**Tool:** NetAPI `download-whois` endpoint, `filter_type=new`, queried per TLD  
**Coverage:** 100% of zone additions — no sampling  
**Collected per domain:**
- Registration date, expiration date
- Registrar, registrant email, phone (where not privacy-shielded)
- IP address at registration time, IP country
- Majestic rank (zero = unranked, new, no established web presence)

### HTTP Fingerprint (Phase 2)

**Tool:** aiohttp, 80 concurrent requests  
**Collected:**
- HTTP status, redirect chain, final URL
- Server / X-Powered-By / ETag headers
- Page title, text snippet
- Favicon → MurmurHash3 (Shodan-compatible operator fingerprint)
- Body SimHash (duplicate content / template detection)

### Threat Intelligence Cross-Reference (Phase 3)

- **Spamhaus DBL** — spam / phishing / malware / botnet
- **SURBL** — URI reputation
- **URLhaus** (abuse.ch) — active malware distribution URLs
- **ThreatFox** (abuse.ch) — IOC database
- **PhishDestroy Destroylist** — correlation with main blocklist

### Legitimacy Survey (Phase 4)

Every active domain (has IP) is evaluated against the legitimacy criteria:

| Criterion | Required for LEGITIMATE classification |
|---|---|
| Business registration | Verifiable company registration in any jurisdiction |
| Business purpose | Clear, lawful commercial or organizational purpose |
| No impersonation | Domain does not impersonate another brand |
| No active abuse listing | Not listed in Spamhaus / SURBL / URLhaus / ThreatFox |
| Accessible content | Serves actual content (not parked, not redirect-only) |

All five criteria must be met. Uncertainty defaults to SUSPICIOUS, not LEGITIMATE.

---

## Classification System

| Category | Severity | Description |
|---|---|---|
| `PHISHING_FINANCE` | HIGH | Bank, payment, fintech brand impersonation |
| `PHISHING_CRYPTO` | HIGH | Exchange / wallet brand impersonation |
| `CRYPTO_DRAIN` | HIGH | Wallet drainer, seed phrase / private key harvester |
| `CARDING` | HIGH | Clone cards, dumps shops, money mule infrastructure |
| `MALWARE_DIST` | HIGH | Software trojanization, fake firmware, crackware |
| `INVEST_FRAUD` | HIGH | Fake investment platforms, CFD scams, Ponzi |
| `PHISHING_GENERIC` | HIGH | Credential harvesting (unbranded or multi-brand) |
| `BRAND_ABUSE` | MEDIUM | Corporate brand squatting without active phishing |
| `SCAM_MISC` | MEDIUM | Fee scams, advance fee fraud, misc financial scam |
| `GAMBLING` | MEDIUM | Unlicensed casino / betting (many jurisdictions) |
| `AFFILIATE_FRAUD` | MEDIUM | Click fraud, fake coupon, affiliate abuse |
| `ADULT` | LOW | Adult content |
| `ACTIVE` | LOW | Responds, no malicious pattern detected |
| `LEGITIMATE` | NONE | Verified real business — all criteria met |
| `REDIRECT` | INFO | Redirect, destination not classified |
| `PARKING` | INFO | Parked page |
| `DEAD` | INFO | No DNS / no HTTP response |

---

## Key Findings

### The .bond Impersonation Pattern

`.bond` is marketed by ShortDot as suitable for "financial services and trusted brands."  
In practice, it is disproportionately used to impersonate financial brands:

| Impersonation domain | Brand impersonated | Category |
|---|---|---|
| `chase.bond` | JPMorgan Chase | PHISHING_FINANCE |
| `bofa.bond` | Bank of America | PHISHING_FINANCE |
| `binance.bond` | Binance exchange | PHISHING_CRYPTO |
| `ledger.bond` | Ledger SAS | PHISHING_CRYPTO |
| `uniswap.bond` | Uniswap DEX | CRYPTO_DRAIN |
| `drainmebaby.bond` | — | CRYPTO_DRAIN |
| `ghostqrpanel.bond` | — | CRYPTO_DRAIN |

The pattern is consistent: the word "bond" implies financial legitimacy to unsuspecting victims. ShortDot's own marketing reinforces this framing. The result is that `.bond` has become a phishing trademark.

### The .cfd Structural Problem

`.cfd` stands for "Contract for Difference" — a regulated, high-risk leveraged financial derivative. No legitimate regulated financial institution operates under a `.cfd` TLD managed by an unregulated Luxembourg SA.

Active `.cfd` domains cluster around:
- Fake CFD trading platforms (unlicensed investment fraud)
- Crypto trading scams using CFD terminology
- Financial credential harvesters

The naming of this TLD is itself a signal: it tells abuse actors where to register for maximum apparent financial legitimacy.

### The .icu Turkish Gambling Cluster

`.icu` is the largest ShortDot zone by volume. A significant cluster consists of Turkish-market gambling and betting domains:

`bahisgiris.icu`, `casinogiris.icu`, `guncelcasinositeleri.icu`, `casinositeleriguncelvip.icu` — dozens of domains, all `.icu`, all Turkish-market, all registered in bulk with identical server fingerprints.

### The NameSilo / .sbs / .cfd Anomaly

| Registrar | .sbs share | .cfd share | Expected |
|---|---|---|---|
| NameSilo | ~7% | ~4% | <1% |
| GoDaddy | <0.2% | <0.2% | normal |
| Namecheap | <1% | <1% | normal |

NameSilo is a named ShortDot partner. Both `.sbs` and `.cfd` were acquired by ShortDot in April 2024. The NameSilo spike in phantom registrations (+615% YoY) began the same month.

See [`case/FINANCIAL.md`](FINANCIAL.md) for full financial flow analysis.

---

## Evidence Integrity

All screenshots SHA-256 hashed post-capture.  
Verification:
```bash
sha256sum -c evidence/HASHES.txt
```

Raw data: `pkg/raw_data/` — gzip-compressed JSONL from NetAPI and HTTP scan stages.

---

## Intended Use

This evidence is suitable for:
- ICANN compliance complaints against ShortDot SA registry agreement violations
- Law enforcement referrals (financial fraud, investment scams, carding)
- Brand abuse reports and UDRP proceedings
- Registrar abuse reports (direct to registrar abuse contacts)
- Academic / threat intelligence research (MIT license — free reuse with attribution)
