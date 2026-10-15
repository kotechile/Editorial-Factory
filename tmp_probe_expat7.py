#!/usr/bin/env python3
"""Round 7: fix the §6038 and eCFR-1010.821 cells; sanity-probe the runner-up topics."""
import sys, re
sys.path.insert(0, 'scripts')
import citation_hub_dossier as c

def show(tag, key, cell, texts):
    ev = c.figure_evidence(cell, texts.get(key, ''))
    print(f"\n[{tag}/{key}] {cell[:90]}…")
    print(f"   -> {'…' + ev[:240].replace(chr(10), ' ') + '…' if ev else 'ABSENT'}")

urls = {
    "6038": "https://www.law.cornell.edu/uscode/text/26/6038",
    "821": "https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-G/section-1010.821",
}
texts = {}
for k, u in urls.items():
    r = c.fetch_source(u)
    texts[k] = r.get('text') or ''
    print(f"{k}: {r.get('status')} len={len(texts[k])}")

CASES = [
    ("6038", "30-day period — a continued failure to report a foreign business entity adds $10,000 for each 30-day period after a 90-day notice, and the increase may not exceed $50,000"),
    ("6038", "10 percent — failing to report a foreign business entity also cuts the foreign taxes a US person may credit, by 10 percent of the taxes paid to that country"),
    ("821", "$16,536 — the non-willful FBAR maximum for a foreign financial agency transaction is inflation-adjusted: $16,536 under the table applying to penalties assessed on or after January 17, 2025"),
    ("821", "$165,353 — the willful FBAR maximum is inflation-adjusted to $165,353 under the table applying to penalties assessed on or after January 17, 2025"),
]
for key, cell in CASES:
    show("cell", key, cell, texts)

print("\n### runner-up probes (PE/nexus and health primaries)")
for u in [
    "https://www.un.org/development/desa/financing/sites/www.un.org.development.desa.financing/files/2021-04/UN_Model_2017_0.pdf",
    "https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/permanent-establishment/index.aspx",
    "https://www.oecd.org/en/topics/health.html",
    "https://www.gov.uk/hmrc-internal-manuals/international-manual/intm264600",
    "https://www.gov.uk/hmrc-internal-manuals/international-manual/intm264500",
]:
    r = c.fetch_source(u)
    t = r.get('text') or ''
    print(f"{r.get('status'):<12} http={r.get('http','')!s:<5} len={len(t):<7} {u}")
    for kw in ['183', '90 day', 'dependent agent']:
        if kw in t.lower():
            i = t.lower().index(kw)
            print(f"    [{kw}] …{t[max(0,i-120):i+160].replace(chr(10),' ')}…")
