#!/usr/bin/env python3
"""Round 8: justify the runner-up candidates + confirm the ownership trigger text."""
import sys, re
sys.path.insert(0, 'scripts')
import citation_hub_dossier as c

for u in [
    "https://www.who.int/news-room/fact-sheets/detail/universal-health-coverage-(uhc)",
    "https://www.oecd.org/en/topics/sub-issues/health-expenditure.html",
    "https://www.expathealthbarometer.com/",
]:
    r = c.fetch_source(u)
    print(f"{r.get('status'):<12} http={r.get('http','')!s:<5} len={len(r.get('text') or ''):<7} {u}")

r = c.fetch_source("https://www.law.cornell.edu/uscode/text/26/6038")
t = r.get('text') or ''
print("\n### 6038(a)(1) ownership trigger")
m = re.search(r"\(a\) Information with respect", t) or re.search(r"10 percent or more", t)
print("   ", t[max(0, m.start()-80): m.start()+900].replace("\n", " ") if m else "not found")

r = c.fetch_source("https://www.irs.gov/publications/p519")
t = r.get('text') or ''
print("\n### P519 90-day / $3,000 window")
for m in list(re.finditer(r"90 days", t))[:3]:
    print("   ", t[max(0, m.start()-320): m.start()+320].replace("\n", " "))
print("\n### P519 permanent establishment sentence")
m = re.search(r"not borne by a U\.S\. permanent establishment", t)
print("   ", t[max(0, m.start()-500): m.start()+400].replace("\n", " ") if m else "not found")
