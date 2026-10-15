#!/usr/bin/env python3
"""Round 4: pull the exact sentences that will carry each brief row."""
import sys, re
sys.path.insert(0, 'scripts')
import citation_hub_dossier as c

def window(text, pat, before=180, after=300):
    m = re.search(pat, text, re.I | re.S)
    if not m:
        return None
    return text[max(0, m.start() - before): m.end() + after].replace("\n", " ")

TARGETS = {
    "https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-C/section-1010.350": [
        r"exceeded \$10,000", r"United States person", r"signature or other financial",
    ],
    "https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-C/section-1010.306": [
        r"April 15", r"October 15", r"shall be filed",
    ],
    "https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-G/section-1010.821": [
        r"\$", r"adjust", r"applies to",
    ],
    "https://www.law.cornell.edu/uscode/text/31/5321": [
        r"non-willful", r"willful", r"greater of", r"not to exceed \$10,000",
    ],
    "https://www.law.cornell.edu/uscode/text/26/6038D": [
        r"penalty of \$10,000", r"continues after notification", r"exceeds \$50,000", r"90-day period",
    ],
    "https://www.law.cornell.edu/uscode/text/26/6038": [
        r"penalty of \$10,000", r"continues", r"90-day",
    ],
    "https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar": [
        r"exceeded \$10,000", r"April 15", r"October 15", r"United States person",
    ],
}

for url, pats in TARGETS.items():
    r = c.fetch_source(url)
    t = r.get('text') or ''
    print("=" * 100)
    print(f"{r.get('status')} http={r.get('http')} len={len(t)} {url}")
    for p in pats:
        w = window(t, p)
        print(f"  --/{p}/--")
        print(f"    {w if w else 'NOT FOUND'}")
