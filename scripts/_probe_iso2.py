import sys, re
sys.path.insert(0, 'scripts')
import citation_hub_dossier as c

ecfr = c.fetch_source("https://www.ecfr.gov/current/title-26/section-1.422-4")['text']
p525 = c.fetch_source("https://www.irs.gov/publications/p525")['text']
us422 = c.fetch_source("https://www.law.cornell.edu/uscode/text/26/422")['text']

print("--- eCFR Example 4 block ---")
i = ecfr.find("Example 4")
print(ecfr[i - 200:i + 3000].replace("\n", " "))

print("\n--- candidate cell probes (eCFR) ---")
for cell in ["120,000", "$60,000", "$150,000", "110 percent", "5 years"]:
    ev = c.figure_evidence(cell, ecfr)
    print(repr(cell), "->", (ev[:260].replace("\n", " ") if ev else None))

print("\n--- candidate cell probes (USC 422) ---")
for cell in ["110 percent", "$100,000", "5 years", "10 percent"]:
    ev = c.figure_evidence(cell, us422)
    print(repr(cell), "->", (ev[:260].replace("\n", " ") if ev else None))

print("\n--- Pub 525 ISO section ---")
for m in list(re.finditer(r"Incentive [Ss]tock [Oo]ption", p525))[:3]:
    print("###", m.start())
    print(p525[m.start():m.start() + 3000].replace("\n", " "))
    print()
