#!/usr/bin/env python3
"""Round 6: test candidate figure cells the way the gate will read them."""
import sys, re
sys.path.insert(0, 'scripts')
import citation_hub_dossier as c

SOURCES = {
    "irs8938": "https://www.irs.gov/businesses/corporations/do-i-need-to-file-form-8938-statement-of-specified-foreign-financial-assets",
    "fbar": "https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar",
    "6038D": "https://www.law.cornell.edu/uscode/text/26/6038D",
    "6038": "https://www.law.cornell.edu/uscode/text/26/6038",
    "5321": "https://www.law.cornell.edu/uscode/text/31/5321",
    "821": "https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-G/section-1010.821",
}

texts = {}
for k, u in SOURCES.items():
    r = c.fetch_source(u)
    texts[k] = r.get('text') or ''
    print(f"{k}: {r.get('status')} {r.get('http')} len={len(texts[k])}")

print("\n### 1010.821 — find the FBAR row (31 U.S.C. 5321(a)(5))")
t = texts['821']
for m in re.finditer(r"5321\(a\)\(5\)", t):
    print("   ", t[max(0, m.start()-120): m.start()+400].replace("\n", " "))
print("\n### 6038(c) foreign tax credit reduction")
t = texts['6038']
for m in list(re.finditer(r"Penalty of reducing foreign tax credit", t))[:2]:
    print("   ", t[m.start(): m.start()+700].replace("\n", " "))

print("\n### candidate cells -> evidence window (gate semantics)")
CASES = [
    ("irs8938", "$200,000 — a US taxpayer living abroad files Form 8938 when the total value of specified foreign financial assets is more than $200,000 on the last day of the tax year, or more than $300,000 at any time during the year (joint filers: $400,000 / $600,000)"),
    ("irs8938", "$50,000 — the baseline Form 8938 threshold in the statute's own terms, which the IRS raises for taxpayers who live abroad and for joint filers"),
    ("fbar", "$10,000 — the FBAR is required when the aggregate value of foreign financial accounts exceeded $10,000 at any time during the calendar year reported"),
    ("fbar", "October 15 — the FBAR is due April 15 with an automatic extension to October 15 that you do not have to request"),
    ("6038D", "$10,000 — a failure to furnish the required information under § 6038D carries a penalty of $10,000, and where the failure continues more than 90 days after notice, a further $10,000 for each 30-day period, capped at $50,000"),
    ("6038", "$10,000 — a failure to report a foreign business entity carries a penalty of $10,000 for each annual accounting period, plus additional amounts capped at $50,000"),
    ("5321", "$10,000 — a non-willful FBAR violation carries a civil penalty of not more than $10,000"),
    ("5321", "50 percent — a willful FBAR violation raises the maximum penalty to the greater of $100,000 or 50 percent of the account balance"),
]

for key, cell in CASES:
    ev = c.figure_evidence(cell, texts[key])
    print(f"\n[{key}] {cell[:70]}…")
    print(f"   -> {'…' + ev[:260].replace(chr(10), ' ') + '…' if ev else 'ABSENT'}")
