import sys, re
sys.path.insert(0, 'scripts')
import citation_hub_dossier as c

def show(url, pats, width=700):
    r = c.fetch_source(url)
    t = r.get('text') or ''
    print("=" * 78)
    print(url, r.get('status'), len(t))
    for p in pats:
        for m in list(re.finditer(p, t))[:3]:
            s = max(0, m.start() - 250)
            print("  ---", p, "---")
            print("  ", t[s:m.start() + width].replace("\n", " "))

show("https://www.law.cornell.edu/uscode/text/26/422",
     [r"\(d\) \$100,000 per year limitation", r"10 percent", r"2 years"])

show("https://www.ecfr.gov/current/title-26/section-1.422-4",
     [r"§ 1\.422-4", r"first exercisable", r"order in which"], width=900)

show("https://www.irs.gov/taxtopics/tc427", [r"stock option", r"incentive"], width=1200)
