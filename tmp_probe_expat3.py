#!/usr/bin/env python3
"""Round 3: FBAR / foreign-account-and-entity reporting candidates."""
import sys
sys.path.insert(0, 'scripts')
import citation_hub_dossier as c

CASES = [
    ("https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-C/section-1010.350", "$10,000"),
    ("https://www.law.cornell.edu/uscode/text/31/5321", "$100,000"),
    ("https://www.law.cornell.edu/uscode/text/26/6038D", "$10,000"),
    ("https://www.law.cornell.edu/uscode/text/26/6038", "$10,000"),
    ("https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar", "$10,000"),
    ("https://www.irs.gov/businesses/corporations/comparison-of-form-8938-and-fbar-requirements", "$50,000"),
]

for u, fig in CASES:
    try:
        r = c.fetch_source(u)
        t = r.get('text') or ''
        print(f"{r.get('status'):<12} http={r.get('http','')!s:<5} len={len(t):<7} {u}")
        if r.get('status') == 'fetched' and t:
            ev = c.figure_evidence(fig, t)
            print(f"      figure {fig!r} -> {('FOUND: …' + ev[:200].replace(chr(10),' ') + '…') if ev else 'ABSENT'}")
            for kw in ['aggregate', 'October 15', 'per violation', 'continuation']:
                if kw.lower() in t.lower():
                    i = t.lower().index(kw.lower())
                    print(f"      [{kw}] …{t[max(0,i-130):i+170].replace(chr(10),' ')}…")
    except Exception as e:
        print(f"ERROR {type(e).__name__}: {e} {u}")
