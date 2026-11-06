import sys, re
sys.path.insert(0, 'scripts')
import citation_hub_dossier as c

t422 = c.fetch_source("https://www.law.cornell.edu/uscode/text/26/422")['text']
treg = c.fetch_source("https://www.ecfr.gov/current/title-26/section-1.422-4")['text']

i = t422.find("Economic Recovery")
print("--- Economic Recovery note ---")
print(t422[max(0, i - 500):i + 400].replace("\n", " "))

print("\n--- 1981 mentions ---")
for m in list(re.finditer("1981", t422))[:6]:
    print(" *", t422[max(0, m.start() - 200):m.start() + 120].replace("\n", " "))

print("\n--- cell probes on eCFR ---")
for cell in ["2014 — ten annually granted immediately exercisable options worth $100,000 each are all exercised in one later year and every one is treated as an incentive stock option",
             "$150,000 — an immediately exercisable option worth $150,000 at grant is bifurcated into an incentive stock option on $100,000 of stock and a nonstatutory option on the rest",
             "2004 — three options with $150,000 of grant-date value, of which the last granted is treated as a nonstatutory option in its entirety once a change in control accelerates it"]:
    ev = c.figure_evidence(cell, treg)
    print("\n>>", cell[:80])
    print("  ", (ev[:400].replace("\n", " ") if ev else None))
