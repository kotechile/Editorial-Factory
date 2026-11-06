import sys, re
sys.path.insert(0, 'scripts')
import citation_hub_dossier as c

urls = [
    "https://www.law.cornell.edu/uscode/text/26/423",
    "https://www.ecfr.gov/current/title-26/section-1.423-2",
    "https://www.irs.gov/publications/p525",
    "https://www.irs.gov/taxtopics/tc427",
    "https://www.law.cornell.edu/uscode/text/26/422",
    "https://www.ecfr.gov/current/title-26/section-1.422-4",
]
figs = {
    "https://www.law.cornell.edu/uscode/text/26/423": ["$25,000", "85 percent", "5 years", "2 years"],
    "https://www.ecfr.gov/current/title-26/section-1.423-2": ["$25,000", "85 percent"],
    "https://www.irs.gov/publications/p525": ["85%", "2 years", "1 year"],
    "https://www.irs.gov/taxtopics/tc427": ["85%", "15%"],
    "https://www.law.cornell.edu/uscode/text/26/422": ["$100,000", "10 percent"],
    "https://www.ecfr.gov/current/title-26/section-1.422-4": ["$100,000"],
}
for u in urls:
    r = c.fetch_source(u)
    t = r.get('text') or ''
    print("=" * 70)
    print(u, "->", r.get('status'), len(t), "chars")
    for f in figs.get(u, []):
        ev = c.figure_evidence(f, t)
        print("   FIG", repr(f), "->", (ev[:220].replace("\n", " ") if ev else None))
