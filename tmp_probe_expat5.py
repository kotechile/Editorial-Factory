#!/usr/bin/env python3
"""Round 5: FBAR statute threshold + penalty sentences + IRS 8938 thresholds."""
import sys, re
sys.path.insert(0, 'scripts')
import citation_hub_dossier as c

def windows(text, pat, before=160, after=260, limit=4):
    out = []
    for m in list(re.finditer(pat, text, re.I))[:limit]:
        out.append(text[max(0, m.start() - before): m.end() + after].replace("\n", " "))
    return out

print("### 31 USC 5321 — all $ occurrences via windows")
r = c.fetch_source("https://www.law.cornell.edu/uscode/text/31/5321")
t = r.get('text') or ''
for pat in [r"not more than \$10,000", r"50 percent", r"willfully violat", r"account balance"]:
    for w in windows(t, pat, limit=3):
        print(f"  --/{pat}/-- {w}\n")

print("### 31 USC 5314")
r = c.fetch_source("https://www.law.cornell.edu/uscode/text/31/5314")
t = r.get('text') or ''
print(f"  status={r.get('status')} len={len(t)}")
for pat in [r"10,000", r"report"]:
    for w in windows(t, pat, limit=3):
        print(f"  --/{pat}/-- {w}\n")

for u in [
    "https://www.irs.gov/businesses/corporations/do-i-need-to-file-form-8938-statement-of-specified-foreign-financial-assets",
    "https://www.irs.gov/instructions/i8938",
    "https://www.irs.gov/individuals/international-taxpayers/foreign-housing-exclusion-or-deduction",
]:
    r = c.fetch_source(u)
    t = r.get('text') or ''
    print(f"### {u}\n  status={r.get('status')} http={r.get('http')} len={len(t)}")
    for pat in [r"\$200,000", r"\$300,000", r"\$400,000", r"\$50,000"]:
        for w in windows(t, pat, limit=1):
            print(f"  --/{pat}/-- {w}\n")
