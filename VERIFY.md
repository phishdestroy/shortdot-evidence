# Verification

## Verify Screenshot Integrity

```bash
sha256sum -c evidence/HASHES.txt
```

## Verify Domain List Integrity

```bash
sha256sum data/all.txt
cat SHA256SUMS.txt | grep data/all.txt
```

## Verify STIX Bundle

Import `data/ioc/stix-bundle.json` into MISP or OpenCTI and validate against STIX 2.1 schema.

## Reproduce Domain Counts

```python
with open('data/all.txt') as f:
    domains = [l.strip() for l in f if l.strip()]
print(len(domains))  # matches total in README
```

## Verify TLD Attribution

```python
from collections import Counter
with open('data/all.txt') as f:
    tlds = Counter(l.strip().rsplit('.', 1)[-1] for l in f if l.strip())
print(tlds.most_common())
```
