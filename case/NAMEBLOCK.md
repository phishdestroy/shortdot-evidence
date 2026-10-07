# The NameBlock Protection Racket

> "Advanced brand protection tools... shaping how digital identity, ownership, and trust evolve online."
> — ShortDot SA website

> **"ShortDot's NameBlock tool offers advanced brand and trademark protection, securing domains
> and shielding them from revenue and reputation risks."**
> — ShortDot SA website (direct quote, emphasis added)

> "We partner with NameBlock, Nicky and WebUnited to provide a comprehensive and effective
> domain experience."
> — ShortDot SA website

ShortDot's own marketing describes NameBlock as *"ShortDot's NameBlock tool"* — their tool,
not an independent partner. The legal separation (NameBlock AS is a Norwegian entity) does not
prevent ShortDot from publicly claiming ownership of the product in marketing materials.

---

## What NameBlock Says It Is

NameBlock is described as a brand protection service. Specifically, it offers:
- Blocking a brand name across TLD zones before anyone registers it
- Monitoring for brand-impersonating domains after they're registered
- Dispute resolution support for cybersquatting cases
- "Defensive" registration of brand-name domains across multiple TLD zones

Standard services. Many companies offer this legitimately.

---

## What NameBlock Actually Is

NameBlock is a **subsidiary venture of ShortDot SA** — the same entity that operates the TLD zones in which the brand threat exists.

This is the structural problem. Broken down step by step:

### Step 1 — ShortDot creates the attack surface

ShortDot registers .icu, .sbs, .bond, .cyou, .cfd, .buzz, .qpon with ICANN.  
These zones have near-zero organic legitimate adoption.  
They are, by the data, predominantly used for phishing, crypto draining, carding, and spam.

### Step 2 — Abuse actors register impersonation domains

```
binance.icu     → Binance phishing
chase.bond      → JPMorgan Chase phishing
metamask.sbs    → MetaMask wallet drain
kraken.cyou     → Kraken exchange phishing
paypal.buzz     → PayPal credential harvester
```

These registrations generate wholesale revenue for ShortDot.

### Step 3 — The threat exists. NameBlock sells the insurance.

NameBlock approaches the same brands being impersonated:
- "Someone has already registered [brand].icu"
- "For $X/year, we'll block all variants of your name across our zones"
- "Without blocking, anyone can register [brand].sbs tomorrow"

The threat is real. The brand IS being impersonated. NameBlock's offer addresses a genuine problem.  
The problem was created by the seller of the solution.

### Step 4 — Revenue extracted twice from the same zone

| Event | Beneficiary | Amount |
|---|---|---|
| Phisher registers `chase.bond` | ShortDot (wholesale) + ICANN | ~$6.68 |
| Chase buys NameBlock protection for `.bond` | NameBlock service fee + ShortDot wholesale | $100–$500+/year |
| Chase registers defensive `chase.bond` variations | ShortDot (wholesale) | ~$6.50/domain |

Every impersonation domain creates:
1. Immediate wholesale revenue from the abuser
2. Downstream demand for NameBlock's "protection" product
3. Wholesale revenue from defensive registrations the brand is now compelled to make

---

## Is This Illegal?

Not necessarily. Defensive domain registration services are legal. Brand monitoring is legal.  
ShortDot operating both a TLD registry and a brand protection service is legal.

What is documented here is not a crime — it is a **structural incentive alignment** that makes abuse profitable at every stage:

| If abuse INCREASES | ShortDot benefits because... |
|---|---|
| More phishing domains registered | More wholesale revenue |
| More brands impersonated | More NameBlock demand |
| More defensive registrations purchased | More wholesale + NameBlock fees |

There is no stage in this chain where ShortDot has a *financial incentive* to reduce abuse.

| If abuse DECREASES | ShortDot loses... |
|---|---|
| Fewer phishing domains | Lost wholesale revenue |
| Fewer impersonation incidents | Reduced NameBlock demand |
| Fewer defensive registrations | Lost wholesale revenue |

The company that has the technical power to implement zone-level abuse controls (ShortDot as registry operator) is the same company that profits most from the absence of those controls.

---

## ShortDot's Own Language

From the ShortDot website:

> *"From blockchain-integrated domain mirroring and crypto wallet connectivity to advanced brand protection tools, we're shaping how digital identity, ownership, and trust evolve online."*

Parsed:

| ShortDot claim | Observable reality |
|---|---|
| "blockchain-integrated domain mirroring" | Domains in ShortDot zones mirror legitimate crypto brands (MetaMask.sbs, Uniswap.bond) — this is phishing infrastructure |
| "crypto wallet connectivity" | ShortDot zones disproportionately host crypto wallet drain panels |
| "advanced brand protection tools" | NameBlock — sold to the same brands being impersonated in ShortDot zones |
| "digital identity, ownership, and trust" | These words describe what phishing destroys |

The marketing language describes the attack surface, not the protection.

---

## The NameBlock Sales Cycle

Based on observable patterns:

1. Brand registers with NameBlock → pays for monitoring across ShortDot zones
2. NameBlock detects `brand.icu`, `brand.sbs`, `brand.bond` registrations (which it's monitoring)
3. NameBlock alerts brand → brand submits abuse report / UDRP
4. Domain suspended → brief disruption to phisher → phisher re-registers `brand2.icu`
5. Cycle repeats → NameBlock subscription renewed

This is not "brand protection." It is a reactive abuse notification loop that generates:
- Recurring revenue for NameBlock (subscription)
- Wholesale revenue for ShortDot on every new phisher registration
- No structural reduction in the abuse rate

A genuine brand protection solution would work at the registry level: ShortDot could implement sunrise periods, TMCH integration, and proactive blocking of exact-match brand registrations. This would eliminate the problem — and eliminate NameBlock's revenue model.

---

## Questions for NameBlock

1. What percentage of NameBlock clients are clients specifically because of abuse in ShortDot zones?
2. Has NameBlock quantified the correlation between ShortDot zone abuse events and NameBlock subscription conversion rates?
3. Does NameBlock proactively contact companies after impersonation domains are registered in ShortDot zones?
4. What would happen to NameBlock's revenue model if ShortDot implemented proactive TMCH-level brand blocking across all 7 zones?
5. Who owns NameBlock? What is the corporate relationship to ShortDot SA?

---

## Comparison: Legitimate Brand Protection vs. NameBlock Model

| Feature | Legitimate brand protection (e.g., Markmonitor) | NameBlock |
|---|---|---|
| Registry independence | Yes — monitors zones they don't control | No — monitors zones their parent company controls |
| Financial incentive to reduce abuse | Yes | No — abuse drives demand |
| Proactive registry-level controls | Advocates for them | Parent company (ShortDot) implements none |
| Client conflict of interest | None | Parent company profits from the threats |

---

## The Broader Ecosystem: Third-Party Vendors Monetizing the Same Surface

NameBlock is not the only vendor whose business model depends on abuse in ShortDot zones.
A cluster of brand protection services specifically markets against the exact threat ShortDot's zones create:

### BrandShelter

BrandShelter offers domain monitoring and defensive registration across new gTLD zones.
Its client pitch is substantially identical to NameBlock's: monitor for impersonation registrations,
file disputes, acquire defensive domains. The difference is that BrandShelter operates independently of the registry.

From a revenue-flow perspective:
- Every new phishing domain registered in a ShortDot zone is a potential BrandShelter lead
- BrandShelter's monitoring alerts drive defensive registrations → ShortDot collects wholesale
- BrandShelter collects its service fee; ShortDot collects wholesale on the defensive domain
- The abuse event that triggered the alert is never structurally prevented

### BrandSight

BrandSight focuses on brand intelligence and domain risk scoring. It indexes new gTLD zones
(including all 7 ShortDot zones) and sells the resulting intelligence to brand owners.
Its value proposition: "know before your brand is targeted."

From a structural standpoint: BrandSight's intelligence product has value precisely because
ShortDot zones are high-abuse environments. In a zone with genuine legitimate use,
brand monitoring generates few alerts. In .bond, .icu, .sbs — monitoring generates continuous alerts,
continuous subscription value, continuous revenue.

### Brandma

Brandma markets proactive brand blocking: reserve your brand name across new gTLD zones
*before* abusers do. Its pitch explicitly acknowledges that new gTLD zones are abuse vectors
requiring defensive registration at cost.

Brandma customers pay to register defensive domains across ShortDot zones.
Each defensive registration generates:
- ShortDot wholesale revenue
- Brandma service fee
- ICANN transaction fee

The customer is paying to defend against a threat the registry permits to exist.

### The Market Structure in Summary

```
┌─────────────────────────────────────────────────────────────────────┐
│             ShortDot creates high-abuse zone environment            │
└────────────────────────────────┬────────────────────────────────────┘
                                 │
          ┌──────────────────────┼──────────────────────┐
          │                      │                      │
          ▼                      ▼                      ▼
     NameBlock               BrandShelter         BrandSight / Brandma
   (ShortDot venture)     (independent vendor)   (independent vendor)
          │                      │                      │
          └──────────────────────┼──────────────────────┘
                                 │
                     All three charge brands
                     to monitor/block/defend
                     against threats in zones
                     ShortDot controls
                                 │
                                 ▼
                    ShortDot collects wholesale
                    on every defensive domain
                    registered by any of them
```

The market for brand protection in ShortDot zones is not incidental to the zones' abuse profile.
It is a *consequence* of it. Every vendor in this market has a financial incentive for
ShortDot's zones to remain high-abuse environments. NameBlock has the additional conflict
of being owned by the registry that creates the environment.

---

## ShortDot's "Leading Distribution Channels" — The Admission

ShortDot's official website lists the following companies under the heading **"Leading Distribution Channels"**:

- [BrandShelter](https://www.brandshelter.com/)
- [BrandMa](https://www.brandma.com/)
- [BrandSight](https://www.brandsight.com/)
- [LexSynergy](https://www.lexsynergy.com/)

None of these are domain registrars. All four are brand protection / trademark monitoring services
whose business model depends on threat levels in domain zones.

ShortDot calls them **distribution channels** — because they distribute demand for defensive
domain registrations in ShortDot zones. A brand protection company that monitors `.bond`
and alerts clients to impersonation generates defensive registration orders. Those orders go
through registrars. ShortDot collects wholesale on every one.

In a legitimate registry ecosystem, brand protection companies are independent monitors.
In ShortDot's framing, they are distribution partners — part of the revenue chain, not watchdogs.

The architecture, stated publicly on ShortDot's own website:

```
ShortDot zones generate phishing threat
        │
        ├── BrandShelter alerts brand → brand registers defensive domains → ShortDot collects
        ├── BrandMa alerts brand → brand registers defensive domains → ShortDot collects
        ├── BrandSight alerts brand → brand registers defensive domains → ShortDot collects
        ├── LexSynergy files UDRP → brand pays + new defensive domains → ShortDot collects
        └── NameBlock ("ShortDot's tool") → brand pays subscription + defensive domains → ShortDot collects
```

ShortDot has 400+ registrar partners. Among the named "Leading Distribution Channels" publicly
featured on their website are not banks, e-commerce platforms, or technology companies with
legitimate domain needs — but brand protection vendors whose entire value proposition is the
threat environment ShortDot's zones create.

---

## Corporate Structure — Corrected Record

NameBlock AS (Norwegian org 991 279 466) is legally separate from ShortDot SA (Luxembourg).
However the separation is nominal at the principal level:

| Name | ShortDot role | NameBlock role | Source |
|---|---|---|---|
| Lars Jensen | Co-Founder & CEO | **Chairman (Styrets leder)** | Norwegian brreg, updated 2025-06-28 |
| Kevin Kopas | Co-Founder & COO | SVP Biz Dev (publicly stated) | LinkedIn, press releases |

Lars Jensen is the sole person with signing authority over NameBlock AS ("Styrets leder alene").
The CEO of the registry that creates the abuse threat is simultaneously the Chairman with
sole signing authority over the company that sells protection from it.

The "legally separate entity" defense does not survive contact with the brreg filing.

---

*This document presents structural analysis of publicly documented corporate relationships and observed domain abuse patterns. It does not allege specific criminal conduct.*
