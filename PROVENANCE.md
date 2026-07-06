# Data Provenance

## Zone Data

**Source:** NetAPI (`https://netapi.com/`) — `download-whois` method, `filter_type=new`, queried per TLD  
**Coverage:** All seven ShortDot-operated zones: .icu, .bond, .cyou, .sbs, .cfd, .buzz, .qpon  
**Update frequency:** Daily (GitHub Actions, 06:00 UTC)  
**Data format:** CSV (domain, registration date, expiration date, registrar, email, phone, IP, IP country, Majestic rank)

The NetAPI license permits use for security research and threat intelligence. WHOIS data for generic TLDs is publicly accessible per ICANN policy.

## Threat Intelligence Sources

| Source | Type | Usage |
|---|---|---|
| Spamhaus DBL | DNS-based | Zone phishing/malware classification |
| SURBL | DNS-based | URI reputation |
| URLhaus (abuse.ch) | REST API | Active malware distribution |
| ThreatFox (abuse.ch) | REST API | IOC database |
| PhishDestroy Destroylist | HTTP | Correlation with main blocklist |

All TI sources are used under their respective public / research-use terms.

## HTTP Scan Data

HTTP fingerprinting and browser rendering data was collected by making standard HTTP GET requests to publicly accessible URLs. No authentication was used. No scraping of paywalled or restricted content occurred. Rate limiting was applied.

## Screenshots

Screenshots of phishing pages were captured using headless Chromium (Playwright). Screenshots are stored in `evidence/` and SHA-256 hashed for integrity verification.

## STIX 2.1 Bundle

STIX bundle (`data/ioc/stix-bundle.json`) is generated from the above sources and structured per the STIX 2.1 specification. It is suitable for import into MISP, OpenCTI, and other compatible threat intelligence platforms.

## ICANN / IANA References

Registry delegation records referenced from the IANA TLD database (publicly available).  
ShortDot ICANN registry agreement data from ICANN public records.

## Financial Estimates

Revenue estimates are derived from:
- Published retail pricing (publicly observable at registrar websites)
- Industry norms for new gTLD wholesale pricing
- ICANN published fee schedules

Wholesale pricing is estimated, not disclosed by ShortDot. Estimates are conservative.
