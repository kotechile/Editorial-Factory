import sys, re
sys.path.insert(0, 'scripts')
import citation_hub_dossier as c

r = c.fetch_source("https://www.seagate.com/products/nas-drives/ironwolf-hard-drive/")
t = r.get('text', '')
print("len", len(t), r.get('status'))
for m in re.finditer(r'.{0,180}warrant.{0,180}', t, re.I):
    print("WARRANTY:", " ".join(m.group(0).split()))
    print("---")
print("DOLLARS:", re.findall(r'\$\s?\d[\d,\.]*', t)[:20])
print("YEAR TOKENS:", re.findall(r'\d+\s*[- ]?\s*year', t, re.I)[:20])
print("CAPACITY sample:", re.findall(r'\b\d+\s?TB\b', t)[:10])
