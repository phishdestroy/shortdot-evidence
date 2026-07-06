# ShortDot SA Zones — Documented Criminal Use

This document records criminal prosecutions, law enforcement actions, and authoritative research
where ShortDot-operated TLD domains (.icu .bond .cyou .sbs .cfd .buzz .qpon) appear as
confirmed criminal infrastructure.

The operators of ShortDot SA (Lars Jensen, Kevin Kopas, Michael Riedl, Christian Tecar) have
combined decades of senior experience in domain registries and registrars. The patterns documented
here were not emergent — they are structurally predictable from the zone design choices made.

---

## Part 1 — Convicted Cases: ShortDot Domains Appear in FBI-Published Evidence

### LabHost PhaaS Takedown — Operation PhishOFF / Nebulae

| Field | Detail |
|---|---|
| Operation | International — Europol + Metropolitan Police (UK) + FBI + 19 countries |
| Takedown date | 18 April 2024 |
| Arrests | 37 across 19 countries, 70 premises searched |
| Key conviction | **Zak Coyne**, Manchester Crown Court — **8.5 years imprisonment**, 14 April 2025 |
| Charges | Making/supplying articles for use in fraud; encouraging/assisting fraud; transferring criminal property |
| Scale | 40,000–42,515 phishing domains; 480,000 card numbers; 64,000 PINs; 1M+ passwords; ~£100M+ losses; 1M+ victims in 91 countries |
| DOJ seizure | Four U.S. domains seized, W.D. Pennsylvania warrant |
| FBI domain list | Published 29 April 2025: https://www.ic3.gov/CSA/2025/250429.pdf |

**ShortDot domains in FBI-published LabHost domain list (42,515 total):**

| TLD | Count | Primary targets |
|-----|-------|----------------|
| `.icu` | 110 | Interac, RBC Royal Bank, CIBC, TD Bank, Scotiabank, Volksbank (DE), Santander |
| `.cfd` | 110 | RBC (~60+ variants), MetaMask, Canada Post, Spotify, German targets |
| `.sbs` | 90 | Scotiabank, Bell Canada, Canada Post, JP Morgan Chase |
| `.buzz` | 19 | Canada Post, CIBC, Interac, Netflix |
| `.cyou` | 8 | Interac, CERB (Canada Revenue), Australian services |
| `.bond` | 5 | Mixed |
| `.qpon` | 0 | — |
| **Total ShortDot** | **342** | **0.8% of total LabHost domain inventory** |

Source files: `ioc/FBI_IC3_LabHost_Domains_42515.csv` · `ioc/FBI_IC3_LabHost_ShortDot_only.csv`

Example domains from convicted LabHost infrastructure:
```
etransfer.icu          → Interac e-Transfer impersonation
interac.icu            → Interac e-Transfer impersonation
rbcroyalbank.icu       → RBC Royal Bank impersonation
volksbank.anmelden.icu → German Volksbank credential harvester
rbc-app-care.cfd       → RBC phishing (1 of ~60 RBC variants in .cfd)
rbc-portal-support.cfd → RBC phishing
metamask.rf82728.cfd   → MetaMask wallet drainer
jpmorgan.chaes.sbs     → JPMorgan Chase impersonation
scotia-app-support.sbs → Scotiabank impersonation (1 of ~40 Scotia variants in .sbs)
```

**Significance:** These domains were presented as criminal evidence in UK Crown Court proceedings
that resulted in an 8.5-year prison sentence. The domains existed in ShortDot zones. The registry
and its principals collected wholesale revenue on each registration. No abuse action was taken
on any of these domains prior to the law enforcement takedown.

---

## Part 2 — Active Civil Proceedings (RICO / CFAA)

### Google LLC v. DOES 1–25 — "Lighthouse" PhaaS

| Field | Detail |
|---|---|
| Court | U.S. District Court, S.D.N.Y. |
| Docket | 1:25-cv-09421 |
| Filed | 12 November 2025 |
| Claims | RICO, Computer Fraud and Abuse Act, Lanham Act |
| Infrastructure | Smishing Triad / Lighthouse PhaaS — ~200,000 fraudulent domains in rotation |
| Victims | 1M+ across 120 countries; $1B+ estimated losses |
| ShortDot TLDs | `.icu`, `.cfd`, `.sbs`, `.buzz` — confirmed in researcher-documented Lighthouse/Smishing Triad infrastructure (Unit 42, Resecurity, SilentPush) |
| Status | Active |

### Google LLC v. Doe 1 (Yucheng Chang) — "Darcula" / "Magic Cat" PhaaS

| Field | Detail |
|---|---|
| Court | U.S. District Court, S.D.N.Y. |
| Docket | 1:25-cv-10440, Judge Hon. Jed S. Rakoff |
| Filed | December 2025 |
| Claims | CFAA, Lanham Act, California anti-phishing statutes |
| Named defendant | Yucheng Chang, 24, Henan, China |
| Scale | 884,000–900,000 credit card numbers (40,000 Americans); ~20,000 counterfeit domains at peak |
| TLD | `.cyou` documented in Darcula/Smishing Triad infrastructure; domain `mvr-bgi[.]cyou` active June 2026 |
| Outcome | **Permanent Default Judgment and Permanent Injunction entered** |

### Bulgaria — Smishing Triad Arrests (May 2026)

Bulgarian cybercrime police (ГДБОП) arrested two individuals (ages 30 and 35, Sofia) for
operating Smishing Triad / Lighthouse kit campaigns using `.cyou` domains. Charged under
Art. 212a, Bulgarian Criminal Code (computer fraud) — up to 6 years.

---

## Part 3 — Revolver Rabbit / XLoader (.bond Megacluster)

| Field | Detail |
|---|---|
| Actor | "Revolver Rabbit" (unidentified, unindicted as of mid-2026) |
| TLD | `.bond` — 500,000+ domains registered |
| Purpose | XLoader/Formbook infostealer C2 infrastructure |
| Period | Concentrated May–July 2024 |
| Registrar | Key-Systems GmbH (IANA ID 1345) |
| Estimated cost | ~$1M+ invested in .bond domains alone at ~$2/domain |
| Pattern | Dictionary words + hyphens + 5-digit numbers |
| Status | No arrest, no indictment as of mid-2026 |

**Note:** Key-Systems alone registered 74,737 phishing `.bond` domains (Interisle 2025 data),
placing it in the global Top 5 registrars by phishing domain count — across a zone controlled
by ShortDot SA.

---

## Part 4 — Authoritative Research Record (Admissible as Expert Evidence)

### Interisle Consulting Group — Phishing Landscape 2025

Five ShortDot zones simultaneously appear in the top-20 most-abused TLD rankings in each of
the five annual Interisle studies (2021–2025). Of 24 new gTLDs that made the Top 20 over this
period, five are ShortDot-operated.

| TLD | Phishing domains (Yr to May 2025) | Maliciously registered | Phishing score | vs .com |
|-----|----------------------------------|----------------------|----------------|---------|
| `.bond` | **79,875** | **100%** (79,690/79,875) | **1,759** | **58×** |
| `.cfd` | **24,241** | **96%** | 748 | 25× |
| `.icu` | 19,392 | high | 459 | 15× |
| `.sbs` | 23,293 | high | 296 | 10× |
| `.cyou` | — | high | 347 | 12× |
| `.com` (reference) | — | — | **30** | 1× |

**100% maliciously registered (.bond):** Of 79,875 phishing domains observed in `.bond`,
79,690 (99.8%) were registered specifically to commit phishing — not compromised legitimate sites.
This is the structural signature of a zone with no legitimate adoption.

### Spamhaus Domain Reputation Update (Oct 2025 – Mar 2026)

| TLD | % of zone blacklisted | Spamhaus threshold |
|-----|----------------------|--------------------|
| `.cfd` | **17.54%** | >10% = red flag |
| `.qpon` | **12.17%** | >10% = red flag |
| `.icu` | 9.73% | — |
| `.cyou` | 4.02% | — |
| `.sbs` | 2.98% | — |
| `.bond` | 5.17% (1.15M zone, 59,271 listed) | Three consecutive periods with 98%+ domain churn |

`.bond` registered the highest new-domain-to-total-zone ratio of any gTLD tracked: 1.13M new
domains against a 1.15M zone = **98.57% annual churn**. This is the operational signature of
bulk criminal registration-and-discard cycles, not legitimate business adoption.

### MADWeb 2026 Academic Paper — "Generational Analysis of TLD Reputation"

Peer-reviewed academic analysis presented at MADWeb 2026:

> "ShortDot SA, with three TLDs, has **2.5× more malicious domains than legitimate** — the
> worst malicious-to-benign ratio of any registry operator analysed."

`.sbs` acquisition finding:
> "`.sbs` became preferred for malicious registrations **after acquisition by ShortDot SA**"

Source: https://madweb.work/papers/2026/madweb26-paper30.pdf

### ICANN Correspondence — Rose/Aaron to Sinha, 26 June 2026

Official correspondence from APWG/Interisle researchers to ICANN President Tripti Sinha,
directly naming `.icu` and `.bond` in the context of the LabHost FBI domain list and requesting
ICANN enforcement action against ShortDot SA.

Source: https://itp.cdn.icann.org/en/files/correspondence/rose-aaron-to-sinha-26-06-2026-en.pdf

---

## Part 5 — The Experience Argument

The principals of ShortDot SA have combined domain industry experience spanning the full history
of gTLD abuse documentation:

| Principal | Prior role | Abuse documentation they would have seen |
|-----------|-----------|------------------------------------------|
| Lars Jensen | Ascio/Speednames COO (2000–2006) | Foundation-era registrar abuse patterns |
| Kevin Kopas | PIR (.org operator) | .org abuse patterns; ICANN policy development |
| Kevin Kopas | Radix Registry (channel manager) | New gTLD abuse patterns pre-ShortDot |
| Michael Riedl | CentralNic CFO/CEO (2011–present) | Backend registry data for hundreds of TLDs |
| Christian Tecar | ICANN meetings, 6+ conferences | Industry abuse pattern presentations |

The Interisle Phishing Landscape reports have been presented at ICANN public meetings since 2021.
ShortDot's zones have appeared in the Top 20 abuse rankings in every annual report since 2021.
APWG quarterly reports listing ShortDot TLDs are distributed to all ICANN-accredited operators.
Spamhaus published a public open letter naming ShortDot specifically ("We hope you keep .sbs clean").

The claim that ShortDot's principals were unaware of the criminal use patterns in their own zones
is not consistent with their seniority, their attendance at ICANN meetings where this data was
presented, or the public record of direct communications addressed to ShortDot SA by name.

---

*Sources: FBI IC3 Advisory CSA/2025/250429; CPS press release (Zak Coyne sentencing);
Europol LabHost press release; CourtListener dockets 71900274, 72046384;
Interisle Consulting Phishing Landscape 2024 & 2025; Spamhaus domain reputation reports;
MADWeb 2026 academic paper; ICANN correspondence Rose/Aaron to Sinha 26-06-2026;
Krebs on Security (Google Lighthouse lawsuit); BleepingComputer (Revolver Rabbit).*
