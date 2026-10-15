#!/usr/bin/env python3
"""Probe candidate primary sources for the expat evergreen brief via the gate's own fetcher."""
import sys, re
sys.path.insert(0, 'scripts')
import citation_hub_dossier as c

URLS = [
    "https://www.irs.gov/individuals/international-taxpayers/permanent-establishment",
    "https://www.irs.gov/individuals/international-taxpayers/substantial-presence-test",
    "https://www.irs.gov/individuals/international-taxpayers/claiming-tax-treaty-benefits",
    "https://www.law.cornell.edu/uscode/text/26/864",
    "https://www.law.cornell.edu/uscode/text/26/877A",
    "https://www.gov.uk/hmrc-internal-manuals/international-manual/intm260000",
    "https://www.oecd.org/en/topics/sub-issues/permanent-establishment.html",
    "https://www.ssa.gov/international/agreements_overview.html",
    "https://www.tax.ny.gov/pit/file/telecommuters.htm",
    "https://www.irs.gov/publications/p519",
    "https://www.ato.gov.au/businesses-and-organisations/international-tax-for-business/permanent-establishment",
]

for u in URLS:
    try:
        r = c.fetch_source(u)
        t = r.get('text') or ''
        print(f"{r.get('status'):<12} http={r.get('http','')!s:<5} len={len(t):<7} {u}")
        if r.get('status') == 'fetched' and t:
            low = t.lower()
            for kw in ['183', '90 day', 'permanent establishment', 'fixed place', 'substantial presence', 'withhold']:
                if kw in low:
                    i = low.index(kw)
                    print(f"      [{kw}] …{t[max(0,i-100):i+140].replace(chr(10),' ')}…")
    except Exception as e:
        print(f"ERROR {type(e).__name__}: {e} {u}")
