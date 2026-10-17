import sys, re
sys.path.insert(0, 'scripts')
import citation_hub_dossier as c

t = c.fetch_source("https://www.backblaze.com/blog/backblaze-drive-stats-for-q2-2026").get('text', '')
print("### Q2 2026 outliers context")
for m in re.finditer(r'(7\.63|9\.33|8\.26|years old|six years|seven years)', t):
    s = max(0, m.start()-260); e = min(len(t), m.end()+260)
    print(">>", " ".join(t[s:e].split()))
    print("-")
print()
t2 = c.fetch_source("https://www.backblaze.com/cloud-storage/pricing").get('text', '')
print("### B2 pricing context")
for m in re.finditer(r'6\.95', t2):
    s = max(0, m.start()-400); e = min(len(t2), m.end()+300)
    print(">>", " ".join(t2[s:e].split()))
    print("-")
