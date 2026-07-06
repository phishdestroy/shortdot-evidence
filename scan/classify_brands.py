"""Brand classification across all ShortDot zone domain files."""
from pathlib import Path
from collections import defaultdict, Counter
import json, re, csv
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
    ('airdrop',         'Crypto Airdrop',       'crypto'),
    ('mintnft',         'NFT Mint',             'crypto'),
    ('claimnft',        'NFT Claim',            'crypto'),
    ('walletconnect',   'WalletConnect',        'crypto'),
    ('wallet-connect',  'WalletConnect',        'crypto'),
    ('web3',            'Web3',                 'crypto'),
    ('dydx',            'dYdX',                 'crypto'),
    ('blur',            'Blur NFT',             'crypto'),
    ('wazirx',          'WazirX',               'crypto'),
    ('coinswitch',      'CoinSwitch',           'crypto'),
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

# Write brand_domains.json
brand_out = {
    'generated': TODAY,
    'total_brand_domains': len(all_brand_domains),
    'total_raw_hits': sum(len(v) for v in brand_hits.values()),
    'total_scanned': total_scanned,
    'categories': dict(cat_counts.most_common()),
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

# Write brand_all.txt
all_sorted = sorted(all_brand_domains)
(ROOT / 'data/ioc/brand_all.txt').write_text('\n'.join(all_sorted) + '\n', encoding='utf-8')
print(f'\nWrote brand_domains.json, {len(sorted_brands)} per-brand txt files, brand_all.txt ({len(all_sorted):,} domains)')

# Update ioc/indicators.csv — replace old brand rows, add fresh ones
existing_lines = (ROOT / 'ioc/indicators.csv').read_text(encoding='utf-8').splitlines()
header = existing_lines[0]
original_rows = [l for l in existing_lines[1:] if ',BRAND_IMPERSONATION,' not in l and ',,,BRAND' not in l]

new_brand_rows = []
for brand, hits in sorted_brands:
    if brand == 'Generic Phish':
        continue
    cat_str = 'BRAND_IMPERSONATION'
    for domain, tld, cat in sorted(hits, key=lambda x: x[0])[:100]:
        row = f'{domain},{tld},{cat_str},HIGH,,,{TODAY},{brand} brand impersonation'
        new_brand_rows.append(row)

all_lines = [header] + original_rows + new_brand_rows
(ROOT / 'ioc/indicators.csv').write_text('\n'.join(all_lines) + '\n', encoding='utf-8')
print(f'indicators.csv: {len(original_rows)} original + {len(new_brand_rows)} brand rows = {len(all_lines)} total')
