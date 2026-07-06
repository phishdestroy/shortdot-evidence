# ShortDot SA — Principals & Structural Conflicts

ShortDot SA was co-founded in 2017 and launched its first zone (.icu) in 2018.
Four named principals have held governance roles across ShortDot SA and related entities.
Each maintains simultaneous positions that create structural conflicts of interest with the registry's
stated obligations under its ICANN registry agreement.

---

## Lars Jensen — Co-Founder & CEO

| Field | Detail |
|---|---|
| Current roles | CEO, ShortDot SA (2017–present) |
| IANA contact | Named administrative contact for .icu and .bond in IANA delegation records |
| Financial stake | Investor in NameBlock (ShortDot zones enrolled as partners) |
| Prior — Ascio / Speednames | COO & VP, March 2000 – February 2006 (wholesale registrar, acquired by Tucows) |
| Prior — Toweb GmbH | Co-Founder, August 2007 – April 2011 (Germany) |
| Prior — Telnic (.tel registry) | Global Sales Director, July 2008 – October 2009 |
| Prior — Toweb Brasil LTDA EPP | CEO & Owner, September 2008 – August 2018 (CNPJ 10.424.053/0001-93) |
| Education | Aarhus University / IBA Kolding (Denmark) |

### The IANA Contact Issue

Lars Jensen is the individual named in IANA's official delegation records as ShortDot's administrative
contact for .icu (last updated 2024-06-19) and .bond (last updated 2024-04-18). In standard practice
this role is held by a named officer of the registry — but IANA's administrative contact function
carries no independent regulatory oversight. The CEO of the registry is simultaneously its own
IANA-facing representative, with no separation between operator and named contact.

### Toweb Brasil — Registrar Background

Toweb Brasil LTDA EPP (CNPJ 10.424.053/0001-93) was a Brazilian domain registrar/trustee,
with Jensen as CEO & Owner from September 2008 through August 2018. As of 2024-2025:
- Toweb Brasil remains operationally active (active .com.br registrations, active IP blocks)
- 500+ abuse reports attributed to Toweb Brasil IP range (201.47.123.254)
- WIPO arbitration respondent in May 2024 (betanobr.com.br dispute, lost)
- WordPress.com uses Toweb Brasil as trustee for .com.br registrations

Jensen formally divested from Toweb Brasil in August 2018 per his LinkedIn profile.
No evidence found of Toweb Brasil domains registered in ShortDot gTLD zones.

---

## Kevin Kopas — Co-Founder & COO

| Field | Detail |
|---|---|
| Current roles | COO, ShortDot SA (October 2017–present) |
| Simultaneous role | SVP of Business Development + **Board Member, NameBlock** (November 2022–present) |
| Other | Member, usTLD Stakeholder Council (self-reported) |
| Prior — Radix FZC | Channel Manager, Americas |
| Prior — PIR (.org operator) | Channel Manager, APAC |
| Prior — Web.com / Moniker | Brokerage & Acquisitions |

### The Kopas Conflict — Dual Board Membership

Kevin Kopas has served simultaneously as COO of ShortDot SA and SVP/Board Member at NameBlock
since November 2022. NameBlock is incorporated as **NameBlock AS** (Norwegian aksjeselskap),
affiliated with iQ Global AS, and is not a ShortDot SA subsidiary.

NameBlock's business model:
- Brands pay NameBlock to block their name across participating zones before abusers register it
- NameBlock alerts brands when impersonation domains appear in enrolled zones
- Brands pay defensive registration fees across the enrolled zones

All seven ShortDot zones are enrolled in NameBlock's blocking marketplace.

When ShortDot's zones generate brand-impersonating domains (as documented in this repository),
those events directly drive demand for NameBlock's service — a service on whose board the COO
of ShortDot sits. No organizational separation exists at the individual level.

**NameBlock principals (separate from ShortDot):**
- Rolf Larsen — Co-Founder / Chairman (Norwegian domain industry veteran, previously co-founded .global TLD)
- Pinkard "Pinky" Brand — CEO

**ShortDot principals with NameBlock stakes:**
- Lars Jensen — investor in NameBlock
- Kevin Kopas — SVP + Board Member (while COO of ShortDot)

---

## Michael Riedl — Co-Founder & Chairman

| Field | Detail |
|---|---|
| Current roles | Chairman, ShortDot SA (2017–present) |
| Simultaneous role | **CEO, Team Internet Group plc** (LSE: TIG; formerly CentralNic Group Plc) |
| Simultaneous role | Chairman, Team Internet AG (German operating subsidiary) |
| Simultaneous role | Director, Open Registry SA |
| Simultaneous role | Director, ESGAI Technologies, Inc. |
| Prior — KeyDrive SA | CFO, 2011–2019 (Luxembourg domain company, acquired by CentralNic) |
| Prior — CentralNic Group Plc | CFO February 2019; CEO December 2022 |

### The Riedl Conflict — Registry Chairman = Backend Vendor CEO

This is the most significant structural conflict in the ShortDot principal network.

**CentralNic / Team Internet** provides the technical registry services backend for ShortDot SA:
- DNS resolution for all 6.2M domains across 7 zones
- EPP (Extensible Provisioning Protocol) — registrar-to-registry communication layer
- Zone file management and CZDS submissions
- SLA monitoring and uptime obligations

Michael Riedl is simultaneously the **Chairman of ShortDot SA** and the **CEO of Team Internet Group**
— the company providing all of the above services under contract to ShortDot.

The commercial relationship between ShortDot (as registry client) and Team Internet (as backend
vendor) is governed by a contract. The terms of that contract — pricing, SLAs, liability, audit rights,
abuse enforcement thresholds — are negotiated between entities that share a chairman/CEO. No
independent representation exists at the board level on either side of this contract.

Team Internet Group plc is listed on the London Stock Exchange (LSE: TIG) and is a public company
subject to UK disclosure obligations. Michael Riedl's simultaneous role as Chairman of ShortDot SA
represents a related-party transaction that its board is obligated to manage under UK corporate
governance standards.

**Timeline:**
- 2011: KeyDrive SA (Luxembourg) founded; Riedl becomes CFO
- 2019: CentralNic acquires KeyDrive; Riedl becomes CentralNic CFO
- 2022: Riedl appointed CentralNic Group CEO (December)
- 2022: CentralNic rebrands to Team Internet Group
- 2017–present: Riedl serves as ShortDot SA Chairman throughout the CentralNic/Team Internet period

---

## Christian Tecar — Co-Founder & Board Member

| Field | Detail |
|---|---|
| Current roles | Board Member, ShortDot SA (2017–present) |
| Other role | CEO, GlobeHosting / GlobeSSL (Romania-based SSL and hosting) |
| ICANN | Attended 6+ ICANN meetings as registrar-side stakeholder (ICANN 49 Singapore, Mexico, Sydney, Paris, Seoul) |

GlobeHosting/GlobeSSL operates hosting and SSL certificate services. As a board member of a
gTLD registry whose zones host phishing infrastructure, Tecar brings registrar-side operational
perspective but has no publicly documented active abuse enforcement role within ShortDot.

---

## Structural Summary

```
ShortDot SA (Luxembourg)
├── Lars Jensen (CEO) — IANA admin contact for own zones + NameBlock investor
├── Kevin Kopas (COO) — NameBlock board member while operating zone compliance
├── Michael Riedl (Chairman) — CEO of ShortDot's own backend vendor (Team Internet/CentralNic)
└── Christian Tecar (Board) — Romania-based hosting operator

Team Internet Group plc (CentralNic)  ← ShortDot's backend
└── Michael Riedl (CEO)                ← same person

NameBlock AS (Norway)                  ← brand protection on ShortDot zones
├── Rolf Larsen (Chairman)
├── Pinkard Brand (CEO)
├── Kevin Kopas (SVP + Board)          ← same person as ShortDot COO
└── Lars Jensen (investor)             ← same person as ShortDot CEO
```

No layer of governance in this structure operates at arm's length from ShortDot's own principals.
The registry, its backend vendor, and its co-located brand protection service are all connected
at the individual level through the same four people who co-founded ShortDot SA in 2017.

---

## Team Internet Annual Report Disclosures — Verified

ShortDot SA is mentioned in Team Internet Group plc's related-party transactions notes
across all three available annual reports. The relationship is acknowledged and numerically
quantified. However, Riedl's role at ShortDot is consistently described as **"Director and
Shareholder"** — not as Chairman.

| Year | Filing | Disclosed amount | Riedl role as stated | Riedl bio mentions ShortDot |
|------|--------|-----------------|---------------------|----------------------------|
| 2022 | Note 26, p.99 | USD 1,306,000 (services provided) | "Director and Shareholder" | No |
| 2023 | Note 25, p.117 | USD 3,215,000 → restated to USD 308,000 | "Director and Shareholder" | No |
| 2024 | Note 26, p.117 | USD 573,000 (net revenue) | "Director and Shareholder" | No |

### Exact language (2024 annual report, Note 26):

> *"In line with third party registry operator arrangements, the Group serves as an agent for
> Shortdot S.A. ('ShortDot'), a company where Michael Riedl holds the positions of
> **Director and Shareholder**, in the monetisation of the top-level domains it operates."*

### The "Chairman" omission

Riedl's personal website (mr.ceo) states he "chairs technology businesses… including a leading
new top-level domain registry." Third-party business intelligence sources (RocketReach, MarketScreener)
consistently list his ShortDot title as "Co-Founder and Chairman of the Board."

All three annual reports use "Director" — not "Chairman." Under UK AIM Rule 13, related-party
transaction disclosures must describe the **nature of the relationship**. Chairman of a counterparty
company constitutes a materially different governance relationship than a passive directorship.
The board biography sections for Riedl in all three annual reports contain no mention of ShortDot SA.

### The 2023 Restatement

The 2023 annual report initially disclosed USD 3,215,000 as the ShortDot-related figure.
The 2024 annual report restated this to USD 308,000, with the explanation:

> *"The disclosure now reflects the revenue recorded by the Group of USD 308,000 rather than
> the amount remitted to ShortDot of USD 3,215,000."*

The gross flow to ShortDot in 2023 was therefore ~$3.2M — approximately 10× the disclosed
net figure after restatement. Both figures are technically correct (gross vs. net); the choice
to restate to the smaller number reduces the visible magnitude of the related-party relationship.

### Sources (primary documents)
- Annual Report 2022: `teaminternet.com/wp-content/uploads/2023/08/Annual-Report-2022.pdf`
- Annual Report 2023: `teaminternet.com/wp-content/uploads/2024/03/Annual-Report-2023.pdf`
- Annual Report 2024: `teaminternet.com/wp-content/uploads/2025/04/Annual-Report-2024.pdf`
- Companies House (no. 08576358): `find-and-update.company-information.service.gov.uk/company/08576358`

---

## Questions for Disclosure

1. Team Internet Group plc annual reports describe Riedl's ShortDot role as "Director and
   Shareholder." His personal site and third-party sources call it "Chairman." Under AIM Rule 13,
   does the omission of the Chairman title constitute an incomplete description of the
   nature of the related-party relationship?

2. Does Kevin Kopas's NameBlock board seat constitute a reportable conflict under ShortDot SA's
   Luxembourg SA governance obligations? Has it been disclosed to ShortDot's shareholders?

3. Lars Jensen is the named IANA administrative contact for .icu and .bond.
   What process governs his removal if ShortDot fails to meet ICANN compliance requirements?
   Does the CEO of the registry have unchecked authority over the zones under his own name?

4. Does Team Internet Group plc earn additional revenue when ShortDot zone registration volumes
   increase? If so, what is Riedl's incentive to advocate for reduced phantom registration volumes?

---

*Sources: IANA delegation records, DN Journal, Newswire NameBlock launch announcement,
LinkedIn (Kopas, Jensen; indexed 2025-2026), MarketScreener (Riedl), Team Internet annual
reports 2022–2024 (primary documents), Companies House filing 08576358, WebUnited joint
venture press release (Newsfilecorp), WIPO arbitration record (Toweb Brasil, 2024), AbuseIPDB.*
