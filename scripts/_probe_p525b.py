import sys, re
sys.path.insert(0, 'scripts')
import citation_hub_dossier as c

# 1) Pub 525 ISO section
t = c.fetch_source("https://www.irs.gov/publications/p525")['text']
for m in list(re.finditer(r"[Ii]ncentive [Ss]tock [Oo]ptions", t))[:4]:
    print("=" * 60, "Pub525 ISO at", m.start())
    print(t[m.start():m.start() + 2500].replace("\n", " "))

# 2) Form 3921 instructions
for u in ["https://www.irs.gov/instructions/i3921", "https://www.irs.gov/forms-pubs/about-form-3921"]:
    r = c.fetch_source(u)
    tt = r.get('text') or ''
    print("=" * 60, u, r.get('status'), len(tt))
    for f in ["$100,000", "January 31", "exercise price"]:
        ev = c.figure_evidence(f, tt)
        print("   FIG", f, "->", (ev[:300].replace("\n", " ") if ev else None))
