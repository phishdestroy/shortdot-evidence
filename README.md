<div align="center">
<img src="docs/assets/banner.gif" width="100%"/>
</div>

<div align="center">

<br/>

# ShortDot SA — Zone Abuse Evidence

### `.icu` &nbsp;·&nbsp; `.bond` &nbsp;·&nbsp; `.cyou` &nbsp;·&nbsp; `.sbs` &nbsp;·&nbsp; `.cfd` &nbsp;·&nbsp; `.buzz` &nbsp;·&nbsp; `.qpon`

**7 gTLD zones · Luxembourg registry operator · PhishDestroy Research · 2026**

<br/>

[![IANA Registry](https://img.shields.io/badge/IANA-ShortDot_SA-6ea8d7?style=for-the-badge&labelColor=0c1018)](https://www.iana.org/assignments/tld-review/)
[![TLP CLEAR](https://img.shields.io/badge/TLP-CLEAR-3fb950?style=for-the-badge&labelColor=0c1018)](https://www.first.org/tlp/)
[![License MIT](https://img.shields.io/badge/license-MIT-c0a060?style=for-the-badge&labelColor=0c1018)](LICENSE)
[![Auto-updated](https://img.shields.io/badge/data-auto--updated_daily-8b5cf6?style=for-the-badge&labelColor=0c1018)](https://github.com/phishdestroy/shortdot-evidence/actions)

<br/>

[![Live Report](https://img.shields.io/badge/▶_LIVE_REPORT-phishdestroy.github.io%2Fshortdot--evidence-3fb950?style=for-the-badge&labelColor=0c1018)](https://phishdestroy.github.io/shortdot-evidence)
<br/>

> **6,231,825 domains enumerated across 7 ShortDot zones.**  
> **70.4% phantom (no-IP). $13.7M extracted annually. 25,966 brand-impersonation domains.**  
> **Verified legitimate businesses using these zones as primary domain: 0.**  
> Registry-level evidence package for ICANN compliance, law enforcement intake, and brand protection.

<br/>

</div>

---

<!-- LIVE_STATS:START -->

> 🔴 **LIVE INVESTIGATION FEED** &middot; Auto-updated &middot; Last fetch `2026-07-04`

<table><tr>
<td align="center"><b>📦 Domains tracked</b><br/><sub><code>6,231,825</code></sub></td>
<td align="center"><b>💰 Est. revenue to ShortDot</b><br/><sub><code>$12,559,037</code></sub></td>
<td align="center"><b>💸 ICANN fees (registry)</b><br/><sub><code>$1,738,556</code></sub></td>
<td align="center"><b>❌ No-IP phantom</b><br/><sub><code>4,387,385 (70.4%)</code></sub></td>
<td align="center"><b>🎯 Brand impersonation</b><br/><sub><code>25,966 domains</code></sub></td>
<td align="center"><b>🏛️ Verified legitimate</b><br/><sub><code>0</code></sub></td>
<td align="center"><b>⚡ Combined extracted</b><br/><sub><code>$14,297,593</code></sub></td>
</tr></table>

### 🏷️ TLD Breakdown

| TLD | Domains | With IP | No IP (phantom) | Phantom % | Wholesale/domain | Est. Revenue |
|:--|--:|--:|--:|--:|--:|--:|
| `.icu` | 971,649 | 282,876 | 688,773 | **70.9%** | $0.65 | $631,572 |
| `.bond` | 1,327,512 | 105,362 | 1,222,150 | **92.1%** | $6.50 | $8,628,828 |
| `.cyou` | 753,652 | 266,942 | 486,710 | **64.6%** | $0.65 | $489,874 |
| `.sbs` | 1,911,124 | 594,002 | 1,317,122 | **68.9%** | $0.65 | $1,242,231 |
| `.cfd` | 950,551 | 406,434 | 544,117 | **57.2%** | $0.65 | $617,858 |
| `.buzz` | 207,109 | 126,319 | 80,790 | 39.0% | $3.25 | $673,104 |
| `.qpon` | 110,228 | 62,505 | 47,723 | 43.3% | $2.50 | $275,570 |
| **TOTAL** | **6,231,825** | **1,844,440** | **4,387,385** | **70.4%** | — | **$12,559,037** |

*Data: ICANN gTLD zone files · ICANN fees (registry): $1,738,556/yr · Combined extraction: $14,297,593/yr · Brand-impersonation domains: 25,966*

*Table auto-generated on each daily fetch run.*

### 📥 Download Threat Intelligence

| File | Format | Description |
|:--|:--:|:--|
| [`data/all.txt`](data/all.txt) | TXT | All tracked domains across all 7 zones |
| [`data/index.json`](data/index.json) | JSON | Full analytics snapshot |
| [`data/ioc/serial_registrants.json`](data/ioc/serial_registrants.json) | JSON | Repeat registrants + their domains |
| [`data/ioc/shared_ips.json`](data/ioc/shared_ips.json) | JSON | Bulletproof hosting clusters |
| [`data/ioc/brand_domains.json`](data/ioc/brand_domains.json) | JSON | Domains by targeted brand |
| [`data/ioc/stix-bundle.json`](data/ioc/stix-bundle.json) | STIX 2.1 | MISP/OpenCTI ready bundle |
| [`ioc/domains_all_malicious.txt`](ioc/domains_all_malicious.txt) | TXT | Confirmed malicious — all severity |
| [`ioc/domains_high.txt`](ioc/domains_high.txt) | TXT | HIGH severity only (phishing, drain, carding) |

> 📊 Live dashboard: Pages link at top of repository · Updated daily 06:00 UTC

<!-- LIVE_STATS:END -->

---

## 📑 Table of Contents

<table>
<tr>
<td valign="top">

**Investigation**
- [0 · A Note From Fans](#0--a-note-from-fans)
- [1 · Background](#1--background)
- [2 · Subject: ShortDot SA](#2--subject-shortdot-sa)
- [3 · The Seven Zones](#3--the-seven-zones)
- [4 · Methodology](#4--methodology)

</td>
<td valign="top">

**The Core Question**
- [5 · Show Me One Legitimate Business](#5--show-me-one-legitimate-business)
- [6 · Follow the Money](#6--follow-the-money)
- [7 · The "Private Infrastructure" Myth](#7--the-private-infrastructure-myth)
- [8 · NameBlock — Structural Conflict of Interest](#8--nameblock--structural-conflict-of-interest)
- [9 · Findings](#9--findings)

</td>
<td valign="top">

**Data / Legal**
- [10 · Timeline of Acquisitions](#10--timeline-of-acquisitions)
- [11 · Enforcement Posture](#11--enforcement-posture)
- [12 · Repository Structure](#12--repository-structure)
- [13 · Citation & License](#13--citation)

</td>
</tr>
</table>

---

## 0 · Special Dedication to NameSilo

We must confess: we are massive fans of **[NameSilo](https://github.com/phishdestroy/namesilo-evidence)**. We are endlessly inspired by their mastery — not just their steadfast commitment to retro web design, but their unparalleled operational brilliance in reputation management.

It takes true dedication to aggressively publish self-praising PR articles and manufactured reviews while systematically trying to silence independent security researchers. We watch in awe as they zealously defend phishing operators and scam networks, going so far as to blatantly lie about removing VirusTotal detections just to keep their most "valuable" clients online.

Their coordinated campaigns to deplatform truth-tellers, block researchers, and scrub the internet of any critical analysis are nothing short of breathtaking.

When a registrar fights this hard and spends this much energy protecting malicious infrastructure, it is only fair that we return the favor. **This repository exists to give their tireless efforts the global public recognition they so desperately deserve.**

---

**The scheme behind the growth.** ShortDot SA owns the *registry* — it controls the zones and sets wholesale prices. NameSilo operates as a *registrar* and is, by volume, the **single largest buyer** of ShortDot zone domains. Every day, in bulk, NameSilo purchases registrations across `.icu`, `.bond`, `.cyou`, `.sbs`, `.cfd`, `.buzz`, and `.qpon` — the exact zones its business partner controls. The same ownership network sits on both sides. Money moves between related entities. The registry books revenue. The registrar books inventory. No real end customer is required — the registration event itself is the product.

The result: **millions of domains bulk-registered daily, 70.4% with zero DNS records, never activated, never used by any real business.** They were never meant to be used. They were meant to be *counted* — in filings, in pitch decks, in press releases about explosive growth.

Full NameSilo investigation: **[github.com/phishdestroy/namesilo-evidence](https://github.com/phishdestroy/namesilo-evidence)**

---

## 1 · Background

This repository is the **PhishDestroy investigation into ShortDot SA** — the Luxembourg-registered registry operator behind seven domain zones: `.icu`, `.bond`, `.cyou`, `.sbs`, `.cfd`, `.buzz`, and `.qpon`.

The central question of this investigation is not whether abuse occurs in these zones — it does, at scale. The question is: **what legitimate purpose do these zones serve, and who actually benefits from their existence?**

ShortDot's own marketing claims the zones are for "businesses, creators, and communities." This repository tests that claim with data.

---

## 2 · Subject: ShortDot SA

| Field | Value |
|---|---|
| 🏢 Legal entity | **ShortDot SA** |
| 📍 Jurisdiction | Luxembourg — Société Anonyme |
| 🏠 Registered address | 9 Rue Louvigny, L-1946 Luxembourg |
| 🔧 Technical backend | CentralNic (London) |
| 🌐 Website | shortdot.bond |
| 📊 Zones operated | 7 gTLDs (.icu, .bond, .cyou, .sbs, .cfd, .buzz, .qpon) |
| 🤝 Named partners | GoDaddy, Alibaba, GMO, Namecheap, NameSilo, Dynadot |
| 🛡️ Brand protection arm | NameBlock |
| 🌐 Partner ventures | Nicky, WebUnited, NameBlock |
| 📅 First TLD launched | 2018 (.icu) |

ShortDot operates through a network of three subsidiaries: **Nicky** (domain services), **WebUnited** (web infrastructure), and **NameBlock** (brand protection/blocking). The relationship between these entities and the abuse patterns in ShortDot's zones is a core subject of this investigation.

---

## 3 · The Seven Zones

### .icu

Launched 2018. ShortDot's flagship zone. The name allegedly stands for "I See You" — marketed as a personal branding TLD.

**Reality:** Consistently top-ranked by abuse.ch, Spamhaus, and SURBL for phishing density. Active registrations are dominated by gambling infrastructure, crypto drain panels, and credential harvesters. Verified legitimate use cases: 0 identified to date.

### .bond

Premium pricing (~$9.99 retail). Marketed to financial services and "trusted brands."

**Reality:** `chase.bond`, `bofa.bond`, `binance.bond`, `ledger.bond` — these domains exist. None are operated by JPMorgan Chase, Bank of America, Binance, or Ledger SAS. All are phishing pages impersonating those brands. `.bond` has become a phishing trademark precisely because it implies financial trustworthiness to unsuspecting victims.

### .cyou

`.cyou` = "See You." Marketed for personal brands, influencers, communities.

**Reality:** Near-zero legitimate adoption. Populated predominantly by parked domains and fraudulent infrastructure. High-volume serial registrations with no corresponding active content.

### .sbs

Acquired April 2024 from Australian SBS Corporation (via IANA transfer). Previously associated with the Australian public broadcaster.

**Reality:** After ShortDot acquisition, registration volume spiked. The overwhelming majority of active .sbs domains serve phishing pages, fake shops, or remain permanently parked (phantom registrations for metric inflation). Concentration at NameSilo is anomalous vs. all other registrars.

### .cfd

Acquired April 2024 from DotCFD Registry Ltd. "CFD" = Contract for Difference — a leveraged financial instrument.

**Reality:** A TLD named after a high-risk financial product, operated by a company with no known financial regulation standing, now populated primarily with fake investment platforms, crypto fraud, and financial phishing. The naming itself is a targeting signal.

### .buzz

Marketed as a social media / engagement TLD. Retail price ~$3-5/year.

**Reality:** Active abuse zone. Documented use cases include spam distribution infrastructure and click-fraud networks. No verified legitimate business adoption identified.

### .qpon

Marketed as a coupon/discount TLD. Extremely low wholesale pricing.

**Reality:** Micro-volume zone. Low adoption even by abuse actors. Primarily used for affiliate fraud and fake discount schemes.

---

## 4 · Methodology

### Data Collection

All domains in ShortDot's seven zones are enumerated daily from ICANN gTLD zone data queried per-TLD. Coverage: 100% of zone registrations — no sampling.

```
       ╭───────────────────╮      ╭───────────────────╮      ╭───────────────────╮
       │  1. Zone pull     │ ───▶ │  2. TI cross-ref  │ ───▶ │  3. Legitimacy    │
       │  per-TLD (ICANN   │      │  Spamhaus / SURBL │      │  classification   │
       │  public zone data)│      │  URLhaus / ThrFox │      │  human review     │
       ╰───────────────────╯      ╰───────────────────╯      ╰───────────────────╯
```

### Legitimacy Classification

Each active domain is classified into one of three top-level categories:

| Category | Description |
|---|---|
| `MALICIOUS` | Confirmed phishing / fraud / malware / drainer / carding |
| `SUSPICIOUS` | Unverified but exhibits abuse indicators (no IP, keyword match, shared infra) |
| `LEGITIMATE` | Verified real business with: public company registration, clear business purpose, no impersonation |
| `PARKED` | Domain registered, no content served |
| `DEAD` | No DNS resolution |

The `LEGITIMATE` count is the most important number in this dataset. We actively seek counterexamples to the thesis that these zones have no legitimate purpose.

### Threat Intelligence Cross-Reference

- **Spamhaus DBL** — spam / phishing / malware / botnet classification
- **SURBL** — URI reputation
- **URLhaus** (abuse.ch) — active malware distribution
- **ThreatFox** (abuse.ch) — IOC database
- **PhishDestroy Destroylist** — correlation with main blocklist

---

## 5 · Show Me One Legitimate Business

> **This is an open challenge.** Find us a Fortune 500 company, government agency, licensed bank, or globally recognized institution that uses `.icu`, `.sbs`, `.cfd`, `.cyou`, `.bond`, `.buzz`, or `.qpon` as its primary or official domain. Not a test page. Not a redirect. An actual operational presence.

We've been looking. Here is what we found instead:

| Domain | What ShortDot's marketing says it is | What it actually is |
|---|---|---|
| `chase.bond` | Financial services — trusted brands | JPMorgan Chase **phishing** page |
| `bofa.bond` | Financial services — trusted brands | Bank of America **phishing** page |
| `binance.bond` | Trusted brand | Binance **phishing** |
| `ledger.bond` | Trusted brand | Ledger hardware wallet **phishing** |
| `metamask.icu` | Personal / community brand | MetaMask **wallet drainer** |
| `coinbase.sbs` | Creator / business brand | Coinbase **credential harvester** |
| `kraken.cyou` | Community / personal | Kraken exchange **phishing** |
| `uniswap.bond` | DeFi / Web3 innovation | Uniswap **drain panel** |

**Brand impersonation by the numbers — 25,966 confirmed domains across 7 zones:**

| Target Brand | Domains | Category |
|---|---|---|
| Ally Bank | 2,512 | Banking |
| Wise | 2,249 | Payment |
| Charles Schwab | 1,925 | Banking |
| Google | 1,163 | Tech |
| USPS | 1,145 | Gov |
| Apple | 1,047 | Tech |
| WhatsApp | 1,042 | Social |
| Fidelity | 1,039 | Banking |
| Visa | 982 | Payment |
| TikTok | 952 | Social |
| Telegram | 923 | Social |
| Discover | 840 | Banking |
| Ledger | 727 | Crypto |
| American Express | 685 | Banking |
| JPMorgan Chase | 677 | Banking |
| Citibank | 629 | Banking |
| Amazon | 576 | Tech |
| Medicare | 531 | Gov |
| MetaMask | 481 | Crypto |
| DHL | 318 | Logistics |

*Full list: [`data/ioc/brand_domains.json`](data/ioc/brand_domains.json) · Per-brand blocklists: [`data/ioc/brands/`](data/ioc/brands/)*

The brands appear as **victims**, not operators. The legitimate companies — Chase, BofA, Binance, Ledger, MetaMask — have not adopted these TLDs. Criminals have adopted them on the brands' behalf, to deceive the brands' customers.

**The legitimacy challenge is live:** if you have evidence of a verified, non-phishing, non-squatter legitimate business using a ShortDot TLD as its primary domain, open an issue with evidence. Every submission is reviewed and, if verified, added to the `LEGITIMATE` count.

Current verified legitimate sites: **see [`case/LEGITIMATE_SURVEY.md`](case/LEGITIMATE_SURVEY.md)**

---

## 6 · Follow the Money

### The ShortDot Revenue Chain

```
ShortDot SA (Luxembourg)
       │
       │  Charges wholesale per-domain annual fee
       │  (.icu ~$0.50–$1.00 · .sbs ~$0.50–$1.00 · .cfd ~$0.50–$1.00
       │   .cyou ~$0.50–$1.00 · .bond ~$5–$8 · .buzz ~$3–$5 · .qpon ~$2–$4)
       │
       ▼
400+ Registrar Partners
(NameSilo, GoDaddy, Namecheap, Alibaba, GMO, Dynadot…)
       │
       │  Register at retail — keep margin
       │  NameSilo: $0.99 for .sbs → ~$0.50–$0.70 margin per domain
       │
       ▼
End registrant (phisher, spammer, scammer, or phantom account)
       │
       │  Uses domain for phishing / carding / draining / metric inflation
       │  OR: domain never activates (phantom, dead-zone padding)
       │
       ▼
Revenue flows UP regardless of what domain does
ShortDot collects · registrar collects · ICANN collects
The victim (end user phished) pays nothing — and loses everything
```

### The Price of Admission — This Is Not an Accident

ShortDot wants regulators to believe zone abuse is an unfortunate side effect they're "actively
combating." The ICANN fee schedule proves otherwise. Getting into this business is not cheap:

| ICANN Fee | Amount |
|---|---|
| **Application fee** per TLD (non-refundable if rejected) | **$227,000** |
| **Annual registry fee** per zone | **$25,800/year** |
| **Volume transaction cut** (zones exceeding 50k domains) | **$0.25/domain/year** |

ShortDot operates 7 zones. Application fees alone: **$227,000 × 7 = $1,589,000**.  
Annual ICANN tribute: **$25,800 × 7 = $180,600/year**.  
ICANN volume cut at 6.2M domains: **$1,557,956/year** — collected by the regulator.

> **No investor pays $227,000 per zone application — non-refundable — planning to sell domains
> to university students at $0.99.** The math only closes one way: volume abuse at scale.

The ROI model that actually works:

```
1. Flood zones with phantom registrations via bulk registrars
   → $12.6M/year wholesale at current 6.2M domain volume
   → Inflated metrics signal "market adoption" to outside observers

2. Zone becomes toxic → brands impersonated at scale
   → NameBlock, BrandShelter, BrandSight, Brandma sell "protection"
   → Brands pay $100–$500/year per brand per zone × 7 zones

3. ICANN collects $0.25/domain/year + $25,800/zone/year
   → Silent beneficiary with full regulatory authority to act
   → Financial incentive to not act
```

ShortDot spent over **$1.6M just on ICANN applications** to access this structure.
That is not the investment profile of a company planning to build a legitimate namespace.

### ICANN Fee Extraction (Live Numbers)

Every domain registered in a ShortDot zone generates fees at two levels:

| Fee | Payer | Recipient | Amount |
|---|---|---|---|
| ICANN volume cut (zones >50k) | Registrar → ShortDot → ICANN | ICANN | $0.25/domain/year |
| ICANN annual zone fee | ShortDot | ICANN | $25,800/zone/year |
| Registry wholesale fee | Registrar | ShortDot | $0.65–$6.50/domain/year |

At **6,231,825 current active domains:**
- **ICANN volume cuts:** **$1,557,956/year** from ShortDot zones
- **ICANN zone fees:** **$180,600/year** (7 zones × $25,800)
- **ShortDot wholesale:** **$12,559,037/year**
- **4,387,385 phantom (no-IP) domains** contribute to all three revenue streams while
  serving no verifiable legitimate purpose

Nobody in this chain has a financial incentive to reduce registration volume — including by filtering out abuse.

---

### The NameSilo Anomaly

| Registrar | ShortDot TLD share | Expected |
|---|---|---|
| NameSilo | ~11% (.sbs 7% + .cfd 4%) | <1% |
| GoDaddy | <0.2% | normal |
| Namecheap | <1% | normal |

NameSilo is a **named partner** of ShortDot. The 55× concentration anomaly in ShortDot TLDs at NameSilo — coinciding exactly with ShortDot's April 2024 acquisition of .sbs and .cfd — represents the most concrete financial link between registry and registrar in this ecosystem.

High-volume phantom registrations through a named partner registrar are consistent with a practice known as **metric padding**: artificially inflating zone size to signal market adoption to investors, analysts, and ICANN during contract reviews. A zone that looks like it has 1.9M registered domains is harder to suspend than one with 50K.

**Questions that require answers:**
1. Who is purchasing hundreds of thousands of .sbs and .cfd domains through NameSilo and not activating them?
2. Where does the payment originate?
3. Does ShortDot conduct due diligence on bulk orders from named partners?
4. Does NameSilo's quarterly revenue reporting account for the margin on these phantom registrations separately?
5. Did the timing of the .sbs/.cfd acquisition and the NameSilo spike involve coordination?

---

## 7 · The "Private Infrastructure" Myth

A common defense for massive volumes of phantom (no-IP) registrations is that they serve backend infrastructure, private VPN nodes, or isolated telemetry endpoints. This narrative is technically incoherent.

### 1. Industry Standard: Subdomain Routing

Legitimate platforms route millions of unique endpoints using dynamic subdomains under a single controlled root domain. Vercel (`*.vercel.app`), Tailscale (`*.ts.net`), and major ISPs (`*.rr.com`, `*.verizon.net`) generate a million subdomains instantaneously at zero cost. Registering a million separate root domains costs millions in wholesale fees and ICANN transaction charges. No legitimate scalable infrastructure purchases individual root domains for its endpoints.

### 2. Certificate Transparency Destroys the OPSEC Argument

Modern infrastructure requires SSL/TLS. Every time a distinct root domain is issued a certificate, that issuance is permanently recorded in public Certificate Transparency (CT) logs. A VPN or proxy network using individual root domains for its nodes would be actively broadcasting its entire network topology and deployment timeline to the public internet — an indelible, fully auditable trail of every node provisioned and when. This is a fatal architectural flaw, not a feature.

### 3. Wildcards Provide Actual Privacy

A single root domain with a wildcard certificate (`*.internal-network.net`) secures millions of individual nodes without leaking specific hostnames to CT logs. Subdomains cannot be passively enumerated: unlike root TLD zone files — which are publicly downloadable via ICANN's Centralized Zone Data Service (CZDS) — subdomain trees are opaque to outside observers. Any operator who genuinely prioritizes operational security uses subdomains and wildcards. The registration of millions of distinct non-resolving root domains serves zero legitimate technical purpose.

### Conclusion

The "private infrastructure" defense fails on cost, OPSEC, and technical architecture simultaneously. The actual function of phantom registrations is straightforward: **metric padding** — artificially inflating zone volume to signal market adoption to investors, analysts, and ICANN during contract reviews. A zone with 1.9M registered domains is structurally harder to suspend than one with 50K, regardless of whether those domains resolve to anything.

---

## 8 · NameBlock — Structural Conflict of Interest

ShortDot describes NameBlock as an "advanced brand protection" service. The mechanics:

```
Step 1: ShortDot creates TLD zones (.icu, .sbs, .bond…)
                │
                ▼
Step 2: Phishers register brand-impersonating domains
        chase.bond · binance.icu · metamask.sbs · kraken.cyou
                │
                ▼
Step 3: Phishing begins. Brands are notified by their security teams.
                │
                ▼
Step 4: NameBlock approaches the brand:
        "For $X/year, we block your name across all ShortDot zones"
        "Without protection, anyone can register [brand].icu"
                │
                ▼
Step 5: Brand pays NameBlock defensive registration fees
                │
                ▼
Step 6: ShortDot collects wholesale fee for the defensive registrations
        NameBlock collects the service fee on top
                │
                ▼
Both ShortDot and NameBlock profit from the same threat they created.
```

This is **not** an accusation of illegality — defensive domain registration services exist and have legitimate uses. What is documented here is the structural incentive:

> The entity that profits from selling "brand protection" (NameBlock) is a subsidiary venture of the entity that created the attack surface (ShortDot). The attack surface was manufactured by registering TLDs that have near-zero legitimate adoption but high abuse value. Insurance sold against a fire that the insurer has a financial interest in not extinguishing.

ShortDot's own website states NameBlock provides "advanced brand protection tools." The advanced technique: blocking your brand in zones ShortDot controls, where your brand should never have needed protecting in the first place if the zone had proper abuse controls.

---

## 9 · Findings

### Headline Numbers

*Populated automatically on each fetch run — see [`data/index.json`](data/index.json) for full dataset.*

### Classification by Zone

*Per-TLD breakdown: see [`stats/by_tld/`](stats/by_tld/) directory.*

### Key Confirmed Cases

| Domain | Zone | Classification | Evidence |
|---|---|---|---|
| `chase.bond` | .bond | PHISHING_FINANCE | Brand impersonation, credential harvesting form |
| `bofa.bond` | .bond | PHISHING_FINANCE | Brand impersonation |
| `binance.bond` | .bond | PHISHING_CRYPTO | Exchange credential harvester |
| `ledger.bond` | .bond | PHISHING_CRYPTO | Hardware wallet seed phrase harvester |
| `metamask.icu` | .icu | CRYPTO_DRAIN | MetaMask wallet drain panel |
| `coinbase.sbs` | .sbs | PHISHING_CRYPTO | Exchange phishing |
| `kraken.cyou` | .cyou | PHISHING_CRYPTO | Exchange phishing |
| `uniswap.bond` | .bond | CRYPTO_DRAIN | DEX drain panel |
| `drainmebaby.bond` | .bond | CRYPTO_DRAIN | Explicit naming, wallet drainer |
| `ghostqrpanel.bond` | .bond | CRYPTO_DRAIN | QR-code drain panel infrastructure |

### The .cfd Problem

The `.cfd` zone deserves special attention. "CFD" = Contract for Difference — a specific, high-risk, regulated financial derivative instrument. Registering a TLD with this name, then operating it with minimal abuse controls, creates a namespace that:

1. Is named after a financial product requiring regulatory licensing to offer
2. Is operated by an entity with no financial regulation standing
3. Is disproportionately populated with fake investment platforms and financial fraud

The naming of `.cfd` is not incidental — it is a targeting signal to operators of financial fraud who want domains that look superficially financial.

---

## 10 · Timeline of Acquisitions

| Date | Event |
|---|---|
| **2018** | ShortDot launches `.icu` — first TLD |
| **2019–2023** | `.bond`, `.cyou`, `.buzz`, `.qpon` launch |
| **Apr 2024** | ShortDot acquires `.sbs` from Australian SBS Corporation (IANA record) |
| **Apr 2024** | ShortDot acquires `.cfd` from DotCFD Registry Ltd (IANA record) |
| **2024** | NameSilo dead-domain registrations spike 615% (67K → 485K across zones) |
| **2025** | Spike continues: 585K dead domains, 10K–17K/day |
| **2026** | PhishDestroy investigation published |

The April 2024 dual acquisition — two new zones added to the ShortDot portfolio — coincides precisely with the anomalous NameSilo registration spike. The statistical likelihood of this being coincidental is low.

---

## 11 · Enforcement Posture

This evidence package is suitable for:

- **ICANN Compliance** — registry operator accountability under RAA / registry agreement
- **ICANN Registry Agreement** violation reports (abuse mitigation obligations)
- **Law enforcement referrals** — financial fraud, carding, identity theft
- **Brand abuse / UDRP** proceedings for brand-impersonating domains
- **Registrar abuse reports** — forwarding confirmed phishing to registrar abuse teams
- **Academic / threat intelligence research** — freely reusable under MIT

**For abuse reports:**
- ShortDot abuse email: see `WHOIS` for each TLD's IANA record
- ICANN Compliance: `compliance@icann.org`
- Registrar-specific: see registrar's abuse contact in WHOIS

---

## 12 · Repository Structure

```
shortdot-evidence/
├── case/
│   ├── INVESTIGATION.md        Full investigation document
│   ├── FINANCIAL.md            Follow-the-money analysis
│   ├── NAMEBLOCK.md            NameBlock structural conflict of interest analysis
│   ├── LEGITIMATE_SURVEY.md    Open challenge — verified legitimate sites
│   ├── CLUSTERS.md             Operator infrastructure clusters
│   └── HIGH_SEVERITY.md        High-severity confirmed cases
├── data/
│   ├── all.txt                 All tracked domains (all 7 zones)
│   ├── index.json              Full analytics snapshot
│   ├── ioc/                    IOC exports (STIX, serial registrants, shared IPs)
│   ├── snapshots/              Monthly analytics snapshots
│   └── new/YYYY/MM/            Daily domain additions
├── ioc/
│   ├── domains_all_malicious.txt
│   ├── domains_high.txt        HIGH severity (phishing/drain/carding)
│   └── indicators.csv          Full IOC table
├── scan/
│   └── fetch_new.py            Daily data pipeline (zone fetch → stats → README)
├── stats/
│   ├── by_tld/                 Per-TLD badge JSON files
│   └── *.json                  Overall badge JSONs (shields.io endpoint format)
├── evidence/
│   ├── HASHES.txt              SHA-256 of all screenshots
│   └── [screenshots]           PNG evidence, SHA-256 verified
└── .github/workflows/
    └── update.yml              Daily automation
```

---

## 13 · Citation

```bibtex
@misc{phishdestroy2026shortdot,
  author       = {PhishDestroy},
  title        = {ShortDot SA Zone Evidence — .icu/.bond/.cyou/.sbs/.cfd/.buzz/.qpon},
  year         = {2026},
  publisher    = {GitHub},
  journal      = {GitHub repository},
  howpublished = {\url{https://github.com/phishdestroy/shortdot-evidence}},
  note         = {TLP:CLEAR. Updated daily.}
}
```

**License:** MIT — data, code, and analysis are freely reusable with attribution.

**TLP:** CLEAR — no distribution restrictions.

---

<div align="center">
<sub>PhishDestroy · Anti-phishing and fraud investigation · <a href="https://phishdestroy.io">phishdestroy.io</a></sub>
</div>
