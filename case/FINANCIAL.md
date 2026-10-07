# Follow the Money: ShortDot SA Financial Analysis

> **Aggregate snapshot — 2026-07-04 (ICANN CZDS zone data)**
>
> | Metric | Value |
> |---|---|
> | Total active domains across 7 zones | **6,231,825** |
> | Domains with no IP (phantom/dead) | **4,387,385 (70.4%)** |
> | Est. ShortDot wholesale revenue | **$12,559,037** |
> | ICANN fees collected | **$1,121,729** |
> | Combined extracted from these zones | **$13,680,765** |
> | Verified legitimate use cases | **0** |
>
> The IP concentration adds another dimension: just two IP addresses (188.114.97.3, 188.114.96.3) host
> **368,223 domains** — all pointing to Cloudflare parking infrastructure. The top 20 shared IPs
> account for over 788,000 domains, or 12.6% of all deployed zones.

---

## Revenue Chain Overview

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                         SHORTDOT ZONE REVENUE FLOW                              │
└─────────────────────────────────────────────────────────────────────────────────┘

 Abuse actor / phantom buyer
        │
        │  Pays retail price at registrar
        │  .icu: $0.99 · .sbs: $0.99 · .cfd: $0.99 · .cyou: $0.99
        │  .bond: $9.99 · .buzz: $4.99 · .qpon: $3.99
        │
        ▼
 Registrar (NameSilo, GoDaddy, Namecheap, etc.)
        │
        │  Pays ICANN transaction fee: $0.18/domain/year  →  ICANN
        │  Pays ShortDot wholesale fee: $0.50–$6.50/domain/year  →  ShortDot SA
        │  Keeps remainder as margin
        │
        ▼
 Domain registered. Revenue collected. No legitimacy check required.
 Domain may: serve phishing · remain parked · inflate metrics · never activate.
 Revenue flows to ShortDot and ICANN in all cases.
```

---

## Per-Domain Economics

| TLD | Retail price | ShortDot wholesale (est.) | ICANN fee | ShortDot margin | ICANN take |
|---|---|---|---|---|---|
| `.icu` | $0.99 | $0.65 | $0.25 | **$0.65** | **$0.25** |
| `.sbs` | $0.99 | $0.65 | $0.25 | **$0.65** | **$0.25** |
| `.cfd` | $0.99 | $0.65 | $0.25 | **$0.65** | **$0.25** |
| `.cyou` | $0.99 | $0.65 | $0.25 | **$0.65** | **$0.25** |
| `.bond` | $9.99 | $6.50 | $0.25 | **$6.50** | **$0.25** |
| `.buzz` | $4.99 | $3.25 | $0.25 | **$3.25** | **$0.25** |
| `.qpon` | $3.99 | $2.50 | $0.25 | **$2.50** | **$0.25** |

*Wholesale prices are estimates based on industry norms for new gTLDs. ShortDot does not publish wholesale pricing publicly.*

---

## The NameSilo Phantom Registration Scenario

NameSilo reported approximately 585,000 dead (no-IP, never-activated) domain registrations in 2025.
ShortDot TLDs represent ~11% of NameSilo's portfolio (.sbs ~7%, .cfd ~4%).

**Conservative estimate — ShortDot phantom revenue via NameSilo alone (2025):**

| TLD | Estimated phantom domains | ShortDot wholesale | Annual ShortDot revenue |
|---|---|---|---|
| `.sbs` (7% of 585K) | 40,950 | $0.65 | **$26,618** |
| `.cfd` (4% of 585K) | 23,400 | $0.65 | **$15,210** |
| Other ShortDot TLDs | 15,000 (est.) | $0.65–$6.50 | **$9,750–$97,500** |
| **Total (ShortDot)** | ~79,350 | | **~$51,578–$139,328** |

**ICANN fees on these same phantom domains:**

| Domains | ICANN fee | Annual ICANN revenue |
|---|---|---|
| 79,350 | $0.18 | **$14,283** |

**Total extracted from NameSilo phantom registrations alone:** ~$65,000–$153,000/year between ShortDot and ICANN.

*These domains serve no verifiable legitimate purpose. They generate revenue for the registry and ICANN while contributing to metric inflation at the registrar level.*

---

## The Price of Admission: This Is Not an Accident, It's a Business Model

ShortDot SA and its predecessors want regulators to believe that zone abuse is an unfortunate
side effect they're "actively combating." The ICANN fee schedule proves otherwise.

**Getting into this business costs:**

| Fee | Amount | Source |
|---|---|---|
| Application fee per TLD | **$227,000** | ICANN New gTLD Program |
| Annual registry fee | **$25,800/year** per TLD | ICANN Registry Agreement |
| Volume transaction cut (zones >50k registrations) | **$0.25/domain/year** | ICANN transaction fee schedule |
| Backend operator (CentralNic/Team Internet contract) | $100,000–$500,000/year est. | Industry norm |

**ShortDot's total ICANN entry cost for 7 TLDs:**

| Item | Calculation | Total |
|---|---|---|
| Application fees (7 TLDs, original applicants) | 7 × $227,000 | **$1,589,000** |
| Annual ICANN fees (7 zones) | 7 × $25,800/year | **$180,600/year** |
| ICANN volume cuts at current 6.2M domains | 6,231,825 × $0.25 | **$1,557,956/year** |
| `.sbs` + `.cfd` secondary market acquisition (April 2024) | est. $500K–$2M | **~$1M+ additional** |

**Total ICANN revenue from ShortDot zone operations: ~$1.74M/year ongoing**, not counting the
one-time application fees.

### The Mathematics of Cynicism

No investor pays $227,000 per zone application — non-refundable if rejected — planning to sell
domains to university students at $0.99 each. The breakeven math at legitimate-use pricing
($0.99 retail → $0.65 wholesale) with organic legitimate demand (measured in thousands, not
millions) never closes.

The ROI only works with one specific model:

```
Step 1: Flood zones with phantom registrations via bulk registrars
        → $12.6M/year wholesale revenue at scale
        → Inflated metric → looks like "market adoption" to outside observers

Step 2: Zone becomes toxically abused → brands are being impersonated at scale
        → NameBlock, BrandShelter, BrandSight, Brandma all need to sell "protection"
        → Brands pay $100–$500/year per brand per zone, across 7 zones

Step 3: ICANN continues collecting $0.25/domain/year + $25,800/zone/year
        → Silent financial beneficiary; regulatory authority to act; financial incentive not to
```

ShortDot spent millions acquiring access to ICANN's permission structure specifically to operate
this model. The "accidental abuse" narrative cannot survive contact with the fee schedule they
agreed to.

---

## Registry Acquisition Costs (Detail)

| Fee | Amount | Notes |
|---|---|---|
| Application fee per TLD | **$227,000** | Non-refundable |
| Annual registry fee | **$25,800/year** | Per zone |
| Volume fee >50k domains | **$0.25/domain/year** | All 7 ShortDot zones exceed 50k |
| `.sbs` + `.cfd` 2024 acquisition | est. $500K–$2M | Secondary market transfer |

---

## The Breakeven Calculation

At ShortDot's actual weighted wholesale average (~$2.02/domain across 7 zones):

| Volume needed to break even on application fees alone | Breakeven point |
|---|---|
| At $2.02/domain wholesale | **~787,000 domains** |
| Current zone total | **6,231,825** |
| Application fee recovery multiple | **~7.9×** |

At current volumes, ShortDot has recovered all application fees approximately 8 times over.
Every phantom domain, every abuse registration, every defensive domain registered by a brand
victim — all contribute to this figure.

**At current registration volumes:**
- Average wholesale across all 7 zones: ~$2.02/domain (weighted by volume)
- Annual gross wholesale revenue: **$12,559,037**
- ICANN volume fee at $0.25/domain: **$1,557,956** (ICANN collects this)
- Annual ICANN zone fees: **$180,600** (ICANN collects this)
- Application cost recovery: complete — approximately **8× over**

---

## ICANN's Structural Conflict

ICANN functions simultaneously as:
1. **The regulator** that enforces anti-abuse policies on registrars and registries
2. **The beneficiary** that collects $0.18 per domain registered, including abuse domains

At 500,000 phantom/abuse domain registrations across ShortDot zones annually:
- ICANN collects: **$90,000/year**
- From domains that serve no legitimate purpose

This is not an accusation of corruption. It is a structural observation: the organization with the mandate and authority to reduce domain abuse also has a financial incentive for high registration volumes. Enforcement that reduces volume reduces ICANN revenue.

---

## The ShortDot / NameBlock Double Extraction

NameBlock (a ShortDot venture) sells "brand protection" — defensive registration services that block brand names across ShortDot's own TLD zones.

**Extraction model:**

```
Round 1: Phisher registers chase.icu, chase.sbs, chase.bond for $0.99–$9.99 each
         → ShortDot collects wholesale on each
         → ICANN collects $0.18 on each

Round 2: JPMorgan Chase's security team discovers the phishing domains
         → Chase contacts NameBlock for "brand protection"
         → NameBlock charges Chase to register/block all variants of "chase" across all 7 zones
         → ShortDot collects wholesale on each defensive registration
         → NameBlock collects service fee

Both rounds collect revenue for the ShortDot ecosystem.
The phisher registration funds Round 1. Chase's self-defense funds Round 2.
```

**Questions for ShortDot and NameBlock:**
1. What percentage of NameBlock's brand protection clients are in ShortDot's own zones?
2. Has ShortDot quantified the revenue from defensive registrations driven by abuse in its own zones?
3. Does NameBlock proactively approach companies after abuse is detected in ShortDot zones?
4. Is there any Chinese wall between ShortDot zone operations and NameBlock sales targeting?

---

## Questions That Require Answers

1. **Who** is purchasing hundreds of thousands of .sbs and .cfd domains through NameSilo and not activating them? Registrar records exist. Registrant emails and payment methods are on file.

2. **Where** does the payment originate? Are these bulk purchases from single accounts, or distributed across thousands of registrant profiles?

3. **Did ShortDot's April 2024 acquisition** of .sbs and .cfd involve any coordination with NameSilo regarding volume pricing, reseller agreements, or promotional registrations?

4. **Does ShortDot apply anti-abuse screening** to high-volume registrars, or does wholesale revenue take priority?

5. **What is ShortDot's abuse mitigation cost** as a percentage of zone revenue? If zero, why?

6. **Does NameBlock's revenue model** explicitly or implicitly depend on abuse in ShortDot zones to generate demand for brand protection services?

---

*Sources: ShortDot SA website, IANA TLD delegation records, PhishDestroy 130M domain analysis, ICANN fee schedules, public registrar reporting.*
