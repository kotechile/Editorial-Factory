import sys, re
sys.path.insert(0, 'scripts')
import citation_hub_dossier as c

for u in ["https://www.irs.gov/publications/p575",
          "https://www.law.cornell.edu/uscode/text/26/402",
          "https://www.irs.gov/taxtopics/tc412",
          "https://www.irs.gov/retirement-plans/plan-participant-employee/rollovers-of-retirement-plan-and-ira-distributions"]:
    r = c.fetch_source(u)
    t = r.get('text') or ''
    print("=" * 70)
    print(u, "->", r.get('status'), len(t))
    for f in ["net unrealized appreciation", "unrealized appreciation", "lump-sum", "5 years", "10-year", "Nua"]:
        n = len(re.findall(f, t, flags=re.I))
        print("   count", repr(f), n)
