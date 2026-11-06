import sys, re
sys.path.insert(0, 'scripts')
import citation_hub_dossier as c

u422 = "https://www.law.cornell.edu/uscode/text/26/422"
u_reg = "https://www.ecfr.gov/current/title-26/section-1.422-4"
t422 = c.fetch_source(u422)['text']
treg = c.fetch_source(u_reg)['text']

print("--- 422 (b)(3) 10 years ---")
m = re.search(r"\(3\).{0,220}", t422[t422.find("(b) Incentive stock option"):])
print(m.group(0) if m else None)

print("\n--- 422 amendment note years ---")
for y in ["1981", "1986", "Economic Recovery", "100,000"]:
    print(y, len(re.findall(y, t422)))
i = t422.find("Amendments")
print(t422[i:i + 900].replace("\n", " "))

print("\n--- eCFR currency banner ---")
for pat in [r"up to date as of [0-9/]+", r"T\.D\. 9989[^;]{0,80}"]:
    mm = re.findall(pat, treg)
    print(pat, "->", mm[:3])

print("\n--- candidate cell windows ---")
cells = {
 "exceeds $100,000 — a tranche whose grant-date value first becomes exercisable in a calendar year above $100,000 is treated as an option that is not an incentive stock option": t422,
 "110 percent — a 10-percent shareholder keeps ISO treatment only if the option price is at least 110 percent of fair market value and the option expires within 5 years": t422,
 "50,000 — the regulation's designation example splits an immediately exercisable option worth $150,000 at grant into an incentive stock option on $100,000 of stock and a nonstatutory option on the rest": treg,
 "110,000 — the regulation's acceleration example adds a $60,000 option to a $50,000 option to reach $110,000 against a $100,000 ceiling, so the later option is bifurcated": treg,
 "10 years — under the general rules an incentive stock option must not be exercisable after 10 years from the date it is granted": t422,
}
for cell, txt in cells.items():
    ev = c.figure_evidence(cell, txt)
    print("\n>>", cell[:70])
    print("  ", (ev[:420].replace("\n", " ") if ev else None))
