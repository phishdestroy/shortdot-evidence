"""Brand classification + phishing feed cross-reference across all ShortDot zone domain files."""
from pathlib import Path
from collections import defaultdict, Counter
import json, re, csv, urllib.request, urllib.parse
from datetime import date

ROOT = Path(__file__).parent.parent
TODAY = date.today().isoformat()

BRAND_KEYWORDS = [
    # Banking
    ('chase',           'JPMorgan Chase',       'banking'),
    ('jpmorgan',        'JPMorgan Chase',       'banking'),
    ('bankofamerica',   'Bank of America',      'banking'),
    ('bofa',            'Bank of America',      'banking'),
    ('wellsfargo',      'Wells Fargo',          'banking'),
    ('wfargo',          'Wells Fargo',          'banking'),
    ('citibank',        'Citibank',             'banking'),
    ('citi',            'Citibank',             'banking'),
    ('barclays',        'Barclays',             'banking'),
    ('barclaycard',     'Barclays',             'banking'),
    ('hsbc',            'HSBC',                 'banking'),
    ('santander',       'Santander',            'banking'),
    ('lloyds',          'Lloyds',               'banking'),
    ('natwest',         'NatWest',              'banking'),
    ('halifax',         'Halifax',              'banking'),
    ('nationwide',      'Nationwide',           'banking'),
    ('capitalone',      'Capital One',          'banking'),
    ('capital-one',     'Capital One',          'banking'),
    ('usbank',          'US Bank',              'banking'),
    ('truist',          'Truist',               'banking'),
    ('suntrust',        'SunTrust',             'banking'),
    ('pncbank',         'PNC Bank',             'banking'),
    ('regions',         'Regions Bank',         'banking'),
    ('keybank',         'KeyBank',              'banking'),
    ('tdbank',          'TD Bank',              'banking'),
    ('ally',            'Ally Bank',            'banking'),
    ('discover',        'Discover',             'banking'),
    ('amex',            'American Express',     'banking'),
    ('americanexpress', 'American Express',     'banking'),
    ('fidelity',        'Fidelity',             'banking'),
    ('schwab',          'Charles Schwab',       'banking'),
    ('robinhood',       'Robinhood',            'banking'),
    ('revolut',         'Revolut',              'payment'),
    ('wise',            'Wise',                 'payment'),
    ('transferwise',    'Wise',                 'payment'),
    ('paypal',          'PayPal',               'payment'),
    ('cashapp',         'CashApp',              'payment'),
    ('cash-app',        'CashApp',              'payment'),
    ('venmo',           'Venmo',                'payment'),
    ('zelle',           'Zelle',                'payment'),
    ('stripe',          'Stripe',               'payment'),
    ('skrill',          'Skrill',               'payment'),
    ('visa',            'Visa',                 'payment'),
    ('mastercard',      'Mastercard',           'payment'),
    # Crypto
    ('metamask',        'MetaMask',             'crypto'),
    ('phantom',         'Phantom Wallet',       'crypto'),
    ('trustwallet',     'Trust Wallet',         'crypto'),
    ('trust-wallet',    'Trust Wallet',         'crypto'),
    ('ledger',          'Ledger',               'crypto'),
    ('trezor',          'Trezor',               'crypto'),
    ('exodus',          'Exodus',               'crypto'),
    ('myetherwallet',   'MyEtherWallet',        'crypto'),
    ('binance',         'Binance',              'crypto'),
    ('coinbase',        'Coinbase',             'crypto'),
    ('kraken',          'Kraken',               'crypto'),
    ('kucoin',          'KuCoin',               'crypto'),
    ('bybit',           'Bybit',                'crypto'),
    ('huobi',           'Huobi',                'crypto'),
    ('uniswap',         'Uniswap',              'crypto'),
    ('opensea',         'OpenSea',              'crypto'),
    ('raydium',         'Raydium',              'crypto'),
    ('pancakeswap',     'PancakeSwap',          'crypto'),
    ('sushiswap',       'SushiSwap',            'crypto'),
    ('magiceden',       'Magic Eden',           'crypto'),
    ('magic-eden',      'Magic Eden',           'crypto'),
    ('drainer',         'Crypto Drainer',       'crypto'),
    ('mintnft',         'NFT Mint',             'crypto'),
    ('claimnft',        'NFT Claim',            'crypto'),
    ('walletconnect',   'WalletConnect',        'crypto'),
    ('wallet-connect',  'WalletConnect',        'crypto'),
    ('web3',            'Web3',                 'crypto'),
    ('dydx',            'dYdX',                 'crypto'),
    ('blur',            'Blur NFT',             'crypto'),
    ('wazirx',          'WazirX',               'crypto'),
    ('coinswitch',      'CoinSwitch',           'crypto'),
    ('rabby',           'Rabby Wallet',         'crypto'),
    ('rainbow',         'Rainbow Wallet',       'crypto'),
    ('argent',          'Argent',               'crypto'),
    ('braavos',         'Braavos',              'crypto'),
    ('keplr',           'Keplr',                'crypto'),
    ('petra',           'Petra Wallet',         'crypto'),
    ('eternl',          'Eternl',               'crypto'),
    ('solflare',        'Solflare',             'crypto'),
    ('tronlink',        'TronLink',             'crypto'),
    ('ronin',           'Ronin',                'crypto'),
    ('tonkeeper',       'Tonkeeper',            'crypto'),
    ('mathwallet',      'MathWallet',           'crypto'),
    ('imtoken',         'imToken',              'crypto'),
    ('safepal',         'SafePal',              'crypto'),
    ('tangem',          'Tangem',               'crypto'),
    ('zerion',          'Zerion',               'crypto'),
    ('alphawallet',     'AlphaWallet',          'crypto'),
    ('coin98',          'Coin98',               'crypto'),
    ('nabox',           'Nabox',                'crypto'),
    ('nowallet',        'NoWallet',             'crypto'),
    ('tokenpocket',     'TokenPocket',          'crypto'),
    ('airdrop',         'Crypto Airdrop',       'crypto'),
    ('claim',           'Claim Portal',         'crypto'),
    ('mint',            'NFT Mint',             'crypto'),
    ('staking',         'Staking Portal',       'crypto'),
    ('presale',         'Token Presale',        'crypto'),
    ('whitelist',       'WL Portal',            'crypto'),
    ('freemint',        'Free Mint',            'crypto'),
    ('eligible',        'Eligibility Check',    'crypto'),
    ('allocation',      'Allocation Claim',     'crypto'),
    ('eigenlayer',      'EigenLayer',           'crypto'),
    ('ethena',          'Ethena',               'crypto'),
    ('pendle',          'Pendle',               'crypto'),
    ('hyperliquid',     'Hyperliquid',          'crypto'),
    ('berachain',       'Berachain',            'crypto'),
    ('monad',           'Monad',                'crypto'),
    ('layerzero',       'LayerZero',            'crypto'),
    ('wormhole',        'Wormhole',             'crypto'),
    ('stargate',        'Stargate Finance',     'crypto'),
    ('zora',            'Zora',                 'crypto'),
    ('galxe',           'Galxe',                'crypto'),
    ('jupiter',         'Jupiter',              'crypto'),
    ('jito',            'Jito',                 'crypto'),
    ('orca',            'Orca',                 'crypto'),
    ('lido',            'Lido Finance',         'crypto'),
    ('worldcoin',       'Worldcoin',            'crypto'),
    ('zksync',          'zkSync',               'crypto'),
    ('starknet',        'StarkNet',             'crypto'),
    ('arbitrum',        'Arbitrum',             'crypto'),
    ('optimism',        'Optimism',             'crypto'),
    ('polygon',         'Polygon',              'crypto'),
    ('linea',           'Linea',                'crypto'),
    ('base',            'Base',                 'crypto'),
    ('celestia',        'Celestia',             'crypto'),
    ('notcoin',         'Notcoin',              'crypto'),
    ('bonk',            'BONK',                 'crypto'),
    ('pepe',            'Pepe',                 'crypto'),
    ('shiba',           'Shiba Inu',            'crypto'),
    ('floki',           'Floki',                'crypto'),
    ('aptos',           'Aptos',                'crypto'),
    ('sui',             'Sui',                  'crypto'),
    ('near',            'NEAR',                 'crypto'),
    ('solana',          'Solana',               'crypto'),
    ('tron',            'TRON',                 'crypto'),
    ('cosmos',          'Cosmos',               'crypto'),
    ('polkadot',        'Polkadot',             'crypto'),
    ('avalanche',       'Avalanche',            'crypto'),
    # Big Tech
    ('amazon',          'Amazon',               'tech'),
    ('microsoft',       'Microsoft',            'tech'),
    ('office365',       'Microsoft',            'tech'),
    ('outlook',         'Microsoft',            'tech'),
    ('apple',           'Apple',                'tech'),
    ('icloud',          'Apple iCloud',         'tech'),
    ('google',          'Google',               'tech'),
    ('gmail',           'Google Gmail',         'tech'),
    ('youtube',         'YouTube',              'tech'),
    ('netflix',         'Netflix',              'tech'),
    ('spotify',         'Spotify',              'tech'),
    # Social
    ('facebook',        'Facebook',             'social'),
    ('instagram',       'Instagram',            'social'),
    ('tiktok',          'TikTok',               'social'),
    ('whatsapp',        'WhatsApp',             'social'),
    ('telegram',        'Telegram',             'social'),
    ('twitter',         'Twitter/X',            'social'),
    ('discord',         'Discord',              'social'),
    ('linkedin',        'LinkedIn',             'social'),
    ('reddit',          'Reddit',               'social'),
    ('snapchat',        'Snapchat',             'social'),
    # Gov / Logistics
    ('usps',            'USPS',                 'gov'),
    ('fedex',           'FedEx',                'logistics'),
    ('dhl',             'DHL',                  'logistics'),
    ('medicare',        'Medicare',             'gov'),
    ('medicaid',        'Medicaid',             'gov'),
    ('stimulus',        'Gov Stimulus',         'gov'),
    ('eftps',           'IRS EFTPS',            'gov'),
    ('irs',             'IRS',                  'gov'),
    ('ssa',             'SSA',                  'gov'),
    ('ups',             'UPS',                  'logistics'),
    # E-commerce
    ('alibaba',         'Alibaba',              'ecommerce'),
    ('aliexpress',      'AliExpress',           'ecommerce'),
    ('shopify',         'Shopify',              'ecommerce'),
    ('ebay',            'eBay',                 'ecommerce'),
    ('walmart',         'Walmart',              'ecommerce'),
    ('bestbuy',         'Best Buy',             'ecommerce'),
    ('costco',          'Costco',               'ecommerce'),
    # Generic phishing infra
    ('securelogin',     'Generic Phish',        'phish_infra'),
    ('secure-login',    'Generic Phish',        'phish_infra'),
    ('account-verify',  'Generic Phish',        'phish_infra'),
    ('verify-account',  'Generic Phish',        'phish_infra'),
    ('account-update',  'Generic Phish',        'phish_infra'),
    ('signin-secure',   'Generic Phish',        'phish_infra'),
    ('login-secure',    'Generic Phish',        'phish_infra'),
    ('recover-wallet',  'Generic Phish',        'phish_infra'),
    ('wallet-recovery', 'Generic Phish',        'phish_infra'),
    ('wallet-restore',  'Generic Phish',        'phish_infra'),
    ('seed-phrase',     'Generic Phish',        'phish_infra'),
    ('seedphrase',      'Generic Phish',        'phish_infra'),
    ('private-key',     'Generic Phish',        'phish_infra'),
    ('connectwallet',   'Generic Phish',        'phish_infra'),
    ('connect-wallet',  'Generic Phish',        'phish_infra'),
    # ── Canadian banks (LabHost evidence: 342 ShortDot domains in FBI CSV) ────
    ('rbc',             'RBC Royal Bank',       'banking'),
    ('rbcroyalbank',    'RBC Royal Bank',       'banking'),
    ('royalbank',       'RBC Royal Bank',       'banking'),
    ('scotiabank',      'Scotiabank',           'banking'),
    ('scotiaonline',    'Scotiabank',           'banking'),
    ('cibc',            'CIBC',                 'banking'),
    ('bmo',             'BMO Bank',             'banking'),
    ('bankofmontreal',  'BMO Bank',             'banking'),
    ('interac',         'Interac',              'payment'),
    ('etransfer',       'Interac e-Transfer',   'payment'),
    ('canadapost',      'Canada Post',          'logistics'),
    ('postes-canada',   'Canada Post',          'logistics'),
    # ── Australian targets (LabHost + Smishing Triad documented) ─────────────
    ('commbank',        'CommBank',             'banking'),
    ('commonwealthbank','CommBank',             'banking'),
    ('anz',             'ANZ Bank',             'banking'),
    ('nab',             'NAB',                  'banking'),
    ('westpac',         'Westpac',              'banking'),
    ('stgeorge',        'St George Bank',       'banking'),
    ('bankwest',        'Bankwest',             'banking'),
    ('bendigo',         'Bendigo Bank',         'banking'),
    ('mygov',           'myGov',                'gov'),
    ('mygovid',         'myGovID',              'gov'),
    ('servicesaustralia','Services Australia',  'gov'),
    ('centrelink',      'Centrelink',           'gov'),
    ('auspost',         'Australia Post',       'logistics'),
    # ── German banks (LabHost/Darcula documented DE targets) ─────────────────
    ('volksbank',       'Volksbank',            'banking'),
    ('sparkasse',       'Sparkasse',            'banking'),
    ('postbank',        'Postbank',             'banking'),
    ('deutschebank',    'Deutsche Bank',        'banking'),
    ('commerzbank',     'Commerzbank',          'banking'),
    ('dkb',             'DKB',                  'banking'),
    ('comdirect',       'Comdirect',            'banking'),
    ('ingdiba',         'ING-DiBa',             'banking'),
    # ── UK gov / postal ───────────────────────────────────────────────────────
    ('hmrc',            'HMRC',                 'gov'),
    ('dvla',            'DVLA',                 'gov'),
    ('royalmail',       'Royal Mail',           'logistics'),
    ('nhsuk',           'NHS',                  'gov'),
    ('postoffice',      'Post Office UK',       'logistics'),
    # ── Telecom (carrier impersonation smishing vector) ───────────────────────
    ('att',             'AT&T',                 'telecom'),
    ('tmobile',         'T-Mobile',             'telecom'),
    ('t-mobile',        'T-Mobile',             'telecom'),
    ('verizon',         'Verizon',              'telecom'),
    ('comcast',         'Comcast',              'telecom'),
    ('xfinity',         'Xfinity',              'telecom'),
    ('bellcanada',      'Bell Canada',          'telecom'),
    ('bell-canada',     'Bell Canada',          'telecom'),
    ('rogers',          'Rogers',               'telecom'),
    ('telus',           'TELUS',                'telecom'),
    ('vodafone',        'Vodafone',             'telecom'),
    ('o2mobile',        'O2',                   'telecom'),
    # ── MetaMask / Coinbase typosquats ────────────────────────────────────────
    ('metamsk',         'MetaMask typosquat',   'crypto'),
    ('metmask',         'MetaMask typosquat',   'crypto'),
    ('mettamask',       'MetaMask typosquat',   'crypto'),
    ('meta-mask',       'MetaMask typosquat',   'crypto'),
    ('metamask-app',    'MetaMask typosquat',   'crypto'),
    ('coinbas',         'Coinbase typosquat',   'crypto'),
    ('coinbse',         'Coinbase typosquat',   'crypto'),
    ('binnance',        'Binance typosquat',    'crypto'),
    ('binannce',        'Binance typosquat',    'crypto'),
    # ── Investment / CFD fraud (.cfd zone specific) ───────────────────────────
    ('forex',           'Forex Fraud',          'invest_fraud'),
    ('tradingbot',      'Trading Bot Scam',     'invest_fraud'),
    ('cloudmining',     'Cloud Mining Scam',    'invest_fraud'),
    ('cloud-mining',    'Cloud Mining Scam',    'invest_fraud'),
    ('hashrate',        'Mining Scam',          'invest_fraud'),
    ('miningpool',      'Mining Pool Scam',     'invest_fraud'),
    ('mining-pool',     'Mining Pool Scam',     'invest_fraud'),
    ('passive-income',  'Passive Income Scam',  'invest_fraud'),
    ('pig-butchering',  'Pig Butchering',       'invest_fraud'),
    ('investbot',       'Invest Bot Scam',      'invest_fraud'),
    # ── Smishing parcel / toll (specific compound patterns only) ─────────────
    ('parcel-track',    'Parcel Smishing',      'smishing'),
    ('package-track',   'Parcel Smishing',      'smishing'),
    ('toll-pay',        'Toll Smishing',        'smishing'),
    ('etoll',           'Toll Smishing',        'smishing'),
    ('e-toll',          'Toll Smishing',        'smishing'),
    ('traffic-fine',    'Fine Smishing',        'smishing'),
    ('unpaid-toll',     'Toll Smishing',        'smishing'),
    ('parcel-delivery', 'Parcel Smishing',      'smishing'),
    ('postage-due',     'Parcel Smishing',      'smishing'),
]

# Short (<=3 chars): require word boundary; long: substring anywhere in SLD
SHORT_RE = {}
SUBSTR_KW = {}
for kw, brand, cat in BRAND_KEYWORDS:
    if len(kw) <= 3:
        SHORT_RE[kw] = (brand, cat, re.compile(r'(?:^|[\-_.])' + re.escape(kw) + r'(?:[\-_.]|$)'))
    else:
        SUBSTR_KW[kw] = (brand, cat)

brand_hits = defaultdict(list)
cat_counts = Counter()
total_scanned = 0

for tld_file in sorted((ROOT / 'data/by_tld').glob('*.txt')):
    tld = tld_file.stem
    domains = tld_file.read_text(encoding='utf-8').splitlines()
    total_scanned += len(domains)
    for domain in domains:
        if not domain:
            continue
        sld = domain.rsplit('.', 1)[0].lower()
        matched_brands = set()
        for kw, (brand, cat) in SUBSTR_KW.items():
            if kw in sld and brand not in matched_brands:
                brand_hits[brand].append((domain, tld, cat))
                matched_brands.add(brand)
        for kw, (brand, cat, pat) in SHORT_RE.items():
            if pat.search(sld) and brand not in matched_brands:
                brand_hits[brand].append((domain, tld, cat))
                matched_brands.add(brand)

# Count per category (count distinct domains, not keyword matches)
all_brand_domains = set()
for brand, hits in brand_hits.items():
    for domain, tld, cat in hits:
        cat_counts[cat] += 1
        all_brand_domains.add(domain)

# ── dnstwist-style fuzzy / homoglyph matching ────────────────────────────────
# Strategy: generate ~permutations per brand → lookup in zone SET (O(1)).
# 50 brands × ~300 variants = 15K checks, not 6M iterations.

# Homoglyph substitution map (visual + keyboard confusables)
HOMOGLYPHS = {
    'a': ['а', '@', '4', 'ä'],   # cyrillic а, at-sign, 4
    'e': ['е', '3', 'ё'],         # cyrillic е, 3
    'i': ['1', 'l', '!', 'í'],
    'o': ['0', 'о', 'ö', 'ø'],   # cyrillic о, zero
    's': ['5', '$', 'ѕ'],
    'b': ['6', 'ƅ'],
    'l': ['1', 'i', '|'],
    'g': ['9', 'q'],
    'n': ['m', 'ñ', 'и'],        # rn→m handled separately
    'c': ['с'],                   # cyrillic с
    'p': ['р'],                   # cyrillic р
    'x': ['х'],                   # cyrillic х
}

# Top brands for fuzzy matching (high-value targets only — avoid noise)
FUZZY_BRANDS = [
    ('metamask',  'MetaMask',       'crypto'),
    ('coinbase',  'Coinbase',       'crypto'),
    ('binance',   'Binance',        'crypto'),
    ('ledger',    'Ledger',         'crypto'),
    ('trezor',    'Trezor',         'crypto'),
    ('trustwallet','Trust Wallet',  'crypto'),
    ('phantom',   'Phantom Wallet', 'crypto'),
    ('uniswap',   'Uniswap',        'crypto'),
    ('opensea',   'OpenSea',        'crypto'),
    ('paypal',    'PayPal',         'payment'),
    ('netflix',   'Netflix',        'tech'),
    ('apple',     'Apple',          'tech'),
    ('google',    'Google',         'tech'),
    ('amazon',    'Amazon',         'tech'),
    ('microsoft', 'Microsoft',      'tech'),
    ('facebook',  'Facebook',       'social'),
    ('instagram', 'Instagram',      'social'),
    ('wellsfargo','Wells Fargo',    'banking'),
    ('chase',     'JPMorgan Chase', 'banking'),
    ('bankofamerica','Bank of America','banking'),
]

def _fuzzy_variants(word):
    """Generate single-character homoglyph substitutions + common dnstwist mutations."""
    variants = set()
    # Homoglyph single-char swap
    for i, ch in enumerate(word):
        for sub in HOMOGLYPHS.get(ch, []):
            variants.add(word[:i] + sub + word[i+1:])
    # rn → m confusion (visual: "rn" looks like "m")
    variants.add(word.replace('rn', 'm'))
    variants.add(word.replace('m', 'rn'))
    # Single char omission
    for i in range(len(word)):
        if len(word) > 4:
            variants.add(word[:i] + word[i+1:])
    # Single char duplication
    for i, ch in enumerate(word):
        variants.add(word[:i] + ch + word[i:])
    # Adjacent transposition
    for i in range(len(word) - 1):
        t = list(word); t[i], t[i+1] = t[i+1], t[i]
        variants.add(''.join(t))
    # Hyphenation (insert hyphen at each position)
    for i in range(1, len(word)):
        variants.add(word[:i] + '-' + word[i:])
    # Common suffix additions
    for sfx in ['-app', '-web', '-wallet', '-login', '-secure', '-official', '-verify']:
        variants.add(word + sfx)
    variants.discard(word)  # remove the original
    return variants

# Build zone domain set for fast lookup
zone_set = set()
for tld_file in sorted((ROOT / 'data/by_tld').glob('*.txt')):
    for line in tld_file.read_text(encoding='utf-8').splitlines():
        if line:
            zone_set.add(line.strip().lower())

fuzzy_hits = defaultdict(list)  # brand -> [(domain, tld, cat)]
for base_kw, brand, cat in FUZZY_BRANDS:
    variants = _fuzzy_variants(base_kw)
    for var in variants:
        if not re.match(r'^[a-zA-Z0-9\-а-яёА-ЯЁ]+$', var):
            continue  # skip variants with unusual chars that can't be domains
        for tld_name in ['icu', 'bond', 'cyou', 'sbs', 'cfd', 'buzz', 'qpon']:
            candidate = f'{var}.{tld_name}'
            if candidate in zone_set and candidate not in all_brand_domains:
                fuzzy_hits[brand].append((candidate, tld_name, cat))

fuzzy_total = sum(len(v) for v in fuzzy_hits.values())
print(f'Fuzzy/homoglyph hits: {fuzzy_total} domains across {len(fuzzy_hits)} brands')
for brand, hits in sorted(fuzzy_hits.items(), key=lambda x: -len(x[1]))[:15]:
    print(f'  {brand:<28} {len(hits):>6,}')

# Add fuzzy hits to brand_hits and all_brand_domains
for brand, hits in fuzzy_hits.items():
    brand_hits[brand].extend(hits)
    for domain, tld, cat in hits:
        all_brand_domains.add(domain)
        cat_counts[cat] += 1

sorted_brands = sorted(brand_hits.items(), key=lambda x: -len(x[1]))

print(f'Scanned: {total_scanned:,}')
print(f'Brand-hit domains: {len(all_brand_domains):,}')
print(f'(some domains match multiple brands, raw hits: {sum(len(v) for v in brand_hits.values()):,})')
print()
print(f"{'BRAND':<28} {'COUNT':>8}  CAT")
print('-' * 55)
for brand, hits in sorted_brands[:45]:
    cat = hits[0][2]
    print(f'{brand:<28} {len(hits):>8,}  {cat}')
print()
print('Category totals (raw hits):')
for cat, cnt in cat_counts.most_common():
    print(f'  {cat:<18} {cnt:>8,}')

# ── Phishing feed cross-reference ────────────────────────────────────────────
SHORTDOT_TLDS = {'icu', 'bond', 'cyou', 'sbs', 'cfd', 'buzz', 'qpon'}

PHISH_FEEDS = [
    # OpenPhish community feed — updated ~hourly, free no-auth
    ('openphish',    'https://openphish.com/feed.txt'),
    # URLhaus abuse.ch — online URLs only
    ('urlhaus',      'https://urlhaus.abuse.ch/downloads/text_online/'),
    # PhishTank verified feed (no auth for basic)
    ('phishtank',    'https://data.phishtank.com/data/online-valid.csv.gz'),
    # mitchellkrogza/Phishing.Database — 300K+ active phishing domains, daily
    ('mitchellkrogza', 'https://raw.githubusercontent.com/mitchellkrogza/Phishing.Database/master/phishing-domains-ACTIVE.txt'),
    # Spam404 main blacklist — spam/phishing domains
    ('spam404',      'https://raw.githubusercontent.com/Spam404/lists/master/main-blacklist.txt'),
    # davidonzo/Threat-Intel — Italian cert-style, latest phishing domains
    ('davidonzo',    'https://raw.githubusercontent.com/davidonzo/Threat-Intel/master/lists/latestdomains.txt'),
    # hagezi dns-blocklists pro — multi-source aggregation
    ('hagezi',       'https://raw.githubusercontent.com/hagezi/dns-blocklists/main/domains/pro.txt'),
    # GlobalAntiScam.org blocklist (hosts format)
    ('globalantiscam', 'https://raw.githubusercontent.com/elliotwutingfeng/GlobalAntiScamOrg-blocklist/main/data/hosts.txt'),
]

feed_hits = {}   # domain -> set of feed names that flagged it
_HDR = {'User-Agent': 'PhishDestroy/2.0 (anti-phishing research; contact: research@phishdestroy.io)'}

def _extract_domain(url):
    try:
        url = url.strip()
        # hosts file: "0.0.0.0 domain.com" / "127.0.0.1 domain.com"
        parts = url.split()
        if len(parts) == 2 and parts[0] in ('0.0.0.0', '127.0.0.1', '::1', '::'):
            url = parts[1]
        # AdBlock filter: "||domain.com^"
        elif url.startswith('||') and url.endswith('^'):
            url = url[2:-1]
        p = urllib.parse.urlparse(url if '://' in url else 'https://' + url)
        host = p.hostname or ''
        h = host.lower()
        return h[4:] if h.startswith('www.') else h
    except Exception:
        return ''

for feed_name, feed_url in PHISH_FEEDS:
    print(f'Fetching {feed_name} ...')
    try:
        req = urllib.request.Request(feed_url, headers=_HDR)
        with urllib.request.urlopen(req, timeout=60) as resp:
            raw = resp.read()
        # decompress gzip if needed
        if feed_url.endswith('.gz'):
            import gzip as _gz
            raw = _gz.decompress(raw)
        text = raw.decode('utf-8', errors='replace')
        matched = 0
        if feed_name == 'phishtank':
            reader = csv.DictReader(text.splitlines())
            for row in reader:
                url = row.get('url', '')
                dom = _extract_domain(url)
                tld = dom.rsplit('.', 1)[-1] if '.' in dom else ''
                if tld in SHORTDOT_TLDS:
                    feed_hits.setdefault(dom, set()).add(feed_name)
                    matched += 1
        else:
            for line in text.splitlines():
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                dom = _extract_domain(line)
                tld = dom.rsplit('.', 1)[-1] if '.' in dom else ''
                if tld in SHORTDOT_TLDS:
                    feed_hits.setdefault(dom, set()).add(feed_name)
                    matched += 1
        print(f'  {feed_name}: {matched} ShortDot domain hits')
    except Exception as e:
        print(f'  {feed_name} failed: {e}')

print(f'Feed cross-ref total: {len(feed_hits)} unique domains flagged by phishing feeds')

# ── High-confidence pattern scoring (no brand name required) ─────────────────
# Patterns that indicate phishing infrastructure regardless of brand keyword
PHISH_PATTERNS = [
    # Phishing action prefix/suffix (brand-agnostic)
    (re.compile(r'(recover|restore|unlock|suspended|verify|verif|confirm|secure|auth|login|signin|account|update|alert|helpdesk|portal|support|service|customer)-'), 'action_prefix'),
    (re.compile(r'-(login|signin|secure|verify|auth|account|update|support|recover|restore|helpdesk|portal)'), 'action_suffix'),
    # Crypto recovery / drainer infrastructure
    (re.compile(r'(wallet|seed|phrase|mnemonic|privatekey|private-key|seedphrase|secret-phrase)'), 'crypto_recovery'),
    (re.compile(r'(drain|drainer|stealer|grabber|logger|keylog)'), 'drain_infra'),
    # Smishing: parcel / toll (generic words; only flag when standalone or hyphen-bound)
    (re.compile(r'(?:^|-)tracking(?:-|$)'), 'smishing_tracking'),
    (re.compile(r'(?:^|-)parcel(?:-|$)'), 'smishing_parcel'),
    (re.compile(r'(?:^|-)delivery(?:-|$)'), 'smishing_delivery'),
    (re.compile(r'(?:^|-)(toll|etoll)(?:-|$)'), 'smishing_toll'),
    # Investment fraud / CFD (.cfd zone)
    (re.compile(r'(invest|trading|profit|forex|binary|fund-)?-(bot|signal|copy|auto|robot)'), 'invest_fraud'),
    (re.compile(r'(passive|daily|weekly|monthly)-(income|profit|return|yield|earning)'), 'invest_fraud'),
    # Revolver Rabbit C2 signature: word-word-NNNNN (500K+ .bond domains, XLoader/Formbook)
    (re.compile(r'^[a-z]{3,12}-[a-z]{3,12}-\d{4,6}$'), 'revolver_rabbit_c2'),
    # High-entropy bulk registration (random alphanumeric, no brand)
    (re.compile(r'^[a-z0-9]{16,}$'), 'high_entropy'),
    (re.compile(r'^[a-z]{3,}-[a-z0-9]{8,}$'), 'random_suffix'),
]

pattern_hits = {}   # domain -> list of pattern tags
for tld_file in sorted((ROOT / 'data/by_tld').glob('*.txt')):
    tld = tld_file.stem
    if tld not in SHORTDOT_TLDS:
        continue
    for domain in tld_file.read_text(encoding='utf-8').splitlines():
        if not domain:
            continue
        sld = domain.rsplit('.', 1)[0].lower()
        matched_patterns = []
        for pat, tag in PHISH_PATTERNS:
            if pat.search(sld):
                matched_patterns.append(tag)
        if matched_patterns:
            pattern_hits[domain] = matched_patterns

print(f'Pattern-based phishing candidates: {len(pattern_hits):,}')

# Write brand_domains.json
kw_domains = {}
for brand, hits in sorted_brands:
    kw_key = brand.lower().replace(' ', '_').replace('/', '_')
    kw_domains[kw_key] = [h[0] for h in hits[:200]]

brand_out = {
    'generated': TODAY,
    'total_brand_domains': len(all_brand_domains),
    'total_raw_hits': sum(len(v) for v in brand_hits.values()),
    'total_scanned': total_scanned,
    'feed_confirmed': len(feed_hits),
    'pattern_candidates': len(pattern_hits),
    'categories': dict(cat_counts.most_common()),
    'keywords': kw_domains,
    'brands': {
        brand: {
            'count': len(hits),
            'category': hits[0][2],
            'sample': [h[0] for h in hits[:30]],
        }
        for brand, hits in sorted_brands
    },
}
(ROOT / 'data/ioc/brand_domains.json').write_text(
    json.dumps(brand_out, indent=2), encoding='utf-8')

# Write per-brand txt files
brand_dir = ROOT / 'data/ioc/brands'
brand_dir.mkdir(exist_ok=True)
for brand, hits in brand_hits.items():
    safe = re.sub(r'[^a-z0-9]', '_', brand.lower())
    (brand_dir / f'{safe}.txt').write_text(
        '\n'.join(sorted(set(h[0] for h in hits))) + '\n', encoding='utf-8')

# Write feed_confirmed.txt
if feed_hits:
    (ROOT / 'data/ioc/feed_confirmed.txt').write_text(
        '\n'.join(sorted(feed_hits)) + '\n', encoding='utf-8')
    (ROOT / 'data/ioc/feed_confirmed.json').write_text(json.dumps({
        'generated': TODAY,
        'count': len(feed_hits),
        'domains': {d: sorted(feeds) for d, feeds in sorted(feed_hits.items())},
    }, indent=2), encoding='utf-8')

# Write brand_all.txt
all_sorted = sorted(all_brand_domains)
(ROOT / 'data/ioc/brand_all.txt').write_text('\n'.join(all_sorted) + '\n', encoding='utf-8')
print(f'Wrote brand_domains.json, {len(sorted_brands)} per-brand txt files, brand_all.txt ({len(all_sorted):,} domains)')

# ── Update ioc/indicators.csv ─────────────────────────────────────────────────
existing_lines = (ROOT / 'ioc/indicators.csv').read_text(encoding='utf-8').splitlines()
header = existing_lines[0]
# Keep manual rows (not auto-generated brand/feed/pattern rows)
original_rows = [l for l in existing_lines[1:]
                 if ',BRAND_IMPERSONATION,' not in l
                 and ',PHISHING_CONFIRMED,' not in l
                 and ',PHISH_PATTERN,' not in l
                 and ',GENERIC_PHISH,' not in l]

new_rows = []

# Brand impersonation (all brands including Generic Phish → GENERIC_PHISH at MEDIUM)
for brand, hits in sorted_brands:
    is_generic = (brand == 'Generic Phish')
    cat_str  = 'GENERIC_PHISH' if is_generic else 'BRAND_IMPERSONATION'
    severity = 'MEDIUM' if is_generic else 'HIGH'
    for domain, tld, cat in sorted(hits, key=lambda x: x[0])[:100]:
        new_rows.append(f'{domain},{tld},{cat_str},{severity},,,{TODAY},{brand} brand impersonation')

# Feed-confirmed phishing (HIGHEST confidence)
for domain, feeds in sorted(feed_hits.items()):
    tld = domain.rsplit('.', 1)[-1]
    src = '+'.join(sorted(feeds))
    new_rows.append(f'{domain},{tld},PHISHING_CONFIRMED,HIGH,,,{TODAY},Confirmed by {src}')

# Pattern-based candidates — exclude bulk-entropy tags from indicators.csv (too many rows)
# high_entropy / random_suffix = millions of hits → separate file only
BULK_TAGS = {'high_entropy', 'random_suffix'}
ioc_pattern_hits = {d: t for d, t in pattern_hits.items() if not set(t).issubset(BULK_TAGS)}

for domain, tags in sorted(ioc_pattern_hits.items()):
    if domain in all_brand_domains or domain in feed_hits:
        continue
    tld = domain.rsplit('.', 1)[-1]
    tag_str = '+'.join(tags[:3])
    new_rows.append(f'{domain},{tld},PHISH_PATTERN,MEDIUM,,,{TODAY},Pattern: {tag_str}')

# Write bulk-entropy domains to separate file (too large for indicators.csv)
bulk_entropy = sorted(d for d, t in pattern_hits.items() if set(t) & BULK_TAGS)
if bulk_entropy:
    (ROOT / 'data/ioc/bulk_entropy.txt').write_text('\n'.join(bulk_entropy) + '\n', encoding='utf-8')
    print(f'bulk_entropy.txt: {len(bulk_entropy):,} high-entropy / random-suffix domains')

all_lines = [header] + original_rows + new_rows
(ROOT / 'ioc/indicators.csv').write_text('\n'.join(all_lines) + '\n', encoding='utf-8')
print(f'indicators.csv: {len(original_rows)} manual + {len(new_rows)} auto = {len(all_lines)} total')
