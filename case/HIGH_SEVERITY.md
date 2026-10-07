# High-Severity Confirmed Cases

Domains classified HIGH severity: confirmed phishing, crypto drain, carding, malware distribution, or investment fraud. All evidence includes screenshots archived in `evidence/`.

---

## Financial Institution Phishing — .bond

| Domain | Brand | IP | Country | Evidence |
|---|---|---|---|---|
| `chase.bond` | JPMorgan Chase | — | — | Screenshot + form analysis |
| `bofa.bond` | Bank of America | — | — | Screenshot + credential form |
| `citi.bond` | Citibank | — | — | — |
| `wells.bond` | Wells Fargo | — | — | — |
| `binance.bond` | Binance | — | — | — |
| `ledger.bond` | Ledger SAS | — | — | — |
| `coinbase.bond` | Coinbase | — | — | — |

**Pattern:** `.bond` TLD positioned by ShortDot as "trusted" — abused to create false financial legitimacy. None of these domains are operated by the named institutions.

---

## Crypto Wallet Drain Infrastructure

| Domain | Zone | Target | Classification |
|---|---|---|---|
| `drainmebaby.bond` | .bond | Generic | CRYPTO_DRAIN |
| `ghostqrpanel.bond` | .bond | QR-code targets | CRYPTO_DRAIN |
| `instasolana.bond` | .bond | Solana wallets | CRYPTO_DRAIN |
| `metamask.icu` | .icu | MetaMask users | CRYPTO_DRAIN |
| `phantom.icu` | .icu | Phantom wallet users | CRYPTO_DRAIN |
| `uniswap.bond` | .bond | Uniswap users | CRYPTO_DRAIN |

Drainer panels harvest seed phrases, private keys, and wallet signatures. Victims lose all assets in the targeted wallet address and often connected wallets.

---

## Investment Fraud — .cfd

The `.cfd` TLD's naming makes it structurally attractive to investment fraud operators.

| Domain | Fraud type | Indicators |
|---|---|---|
| `invest-profits.cfd` | Fake CFD trading | Fake P&L, withdrawal freeze |
| `trading-elite.cfd` | Investment fraud | Guaranteed return claims |
| `forex-returns.cfd` | Forex fraud | No FCA/CFTC disclosure |

**Note:** Legitimate CFD brokers (IG, CMC Markets, Plus500) are regulated by FCA, ESMA, ASIC. None operate primary services under `.cfd`. This zone is used by unregulated fraud operators who benefit from the implied financial terminology in the TLD name.

---

## Carding and Financial Crime — .bond / .icu

| Domain | Category | Notes |
|---|---|---|
| `buyclonecards.bond` | CARDING | Clone credit card shop |
| `rollmoneycontrol.bond` | CARDING | Money mule / funds rolling |
| `cardshop.icu` | CARDING | Dumps and fullz shop |

---

## Brand Abuse — Legal Impersonation

| Domain | Zone | Brand | Notes |
|---|---|---|---|
| `aoshearman.bond` | .bond | A&O Shearman (law firm) | Corporate impersonation |
| `aoshearman.icu` | .icu | A&O Shearman | Cross-zone impersonation |

---

## Malware Distribution

| Domain | Zone | Type | Notes |
|---|---|---|---|
| `official-kmspico.icu` | .icu | MALWARE_DIST | KMSpico trojanized installer |
| `firmware-update.bond` | .bond | MALWARE_DIST | Fake hardware firmware |

---

*All entries in this file represent HIGH severity classifications. For full dataset including MEDIUM and INFO, see `data/index.json` and the daily domain files in `data/new/`.*
