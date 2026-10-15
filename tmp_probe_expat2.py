#!/usr/bin/env python3
"""Round 2: find fetchable authority pages carrying PE / nexus figures."""
import sys, re
sys.path.insert(0, 'scripts')
import citation_hub_dossier as c

URLS = [
    "https://www.gov.uk/hmrc-internal-manuals/international-manual/intm260000",
    "https://www.gov.uk/hmrc-internal-manuals/international-manual/intm261000",
    "https://www.gov.uk/hmrc-internal-manuals/international-manual/intm264000",
    "https://www.gov.uk/hmrc-internal-manuals/international-manual/intm266000",
    "https://www.gov.uk/hmrc-internal-manuals/international-manual/intm267000",
    "https://www.law.cornell.edu/uscode/text/26/7701",
    "https://www.law.cornell.edu/uscode/text/26/884",
    "https://www.law.cornell.edu/uscode/text/26/1442",
    "https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010",
    "https://www.irs.gov/individuals/international-taxpayers/foreign-employers-withholding-requirements",
    "https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/permanent-establishment.html",
]

for u in URLS:
    try:
        r = c.fetch_source(u)
        t = r.get('text') or ''
        print(f"{r.get('status'):<12} http={r.get('http','')!s:<5} len={len(t):<7} {u}")
        if r.get('status') == 'fetched' and t:
            low = t.lower()
            for kw in ['183', '90 day', 'dependent agent', 'fixed place', 'effectively connected', 'branch profits']:
                if kw in low:
                    i = low.index(kw)
                    print(f"      [{kw}] …{t[max(0,i-120):i+180].replace(chr(10),' ')}…")
    except Exception as e:
        print(f"ERROR {type(e).__name__}: {e} {u}")
