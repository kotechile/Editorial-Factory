import sys, pathlib
sys.path.insert(0, 'scripts')
import headline_score as hs

b = pathlib.Path('context/drafts/2026-10-17_your-disks-die-by-year-six_draft.md').read_text()
cands = [
 "Your Disks Die at 65%: Year Six",
 "Your Disks: 35% Dead by Year Six",
 "Your Disks Die Before Year Six",
 "Your Disks Die at Year Six, 65%",
 "Your Board Survives; Your Disks Die",
 "Your Disks Hit 65% by Year Six",
 "65% of Your Disks Die by Year Six",
 "Your Disks Die Before Your Board",
 "Your Disks Die by Year Six",
]
for t in cands:
    r = hs.score(t, body=b)
    print(f"{r.get('score'):>4} {r.get('verdict'):<7} lead_ok={r.get('lead_ok')} | {t}")
    for f in (r.get('fails') or []):
        print("      -", f)
