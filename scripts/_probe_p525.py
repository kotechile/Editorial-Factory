import sys, re
sys.path.insert(0, 'scripts')
import citation_hub_dossier as c

t = c.fetch_source("https://www.irs.gov/publications/p525")['text']
print("LEN", len(t))
idxs = [m.start() for m in re.finditer(r"[Ee]mployee stock purchase", t)]
print("occurrences:", len(idxs))
for i in idxs[:6]:
    print("-" * 60)
    print(t[max(0, i - 300):i + 1800])
