import sys, pathlib
sys.path.insert(0, 'scripts')
import headline_score as hs

body = pathlib.Path('context/drafts/2026-10-17_old-compute-new-disks-65-percent_draft.md').read_text()
cands = [
 "Your Disks Die on a 65% Clock",
 "Your Disks Quit at 65%: Year Six",
 "Year Six Kills 35% of Your Disks",
 "Your Disks: 65% Alive at Year Six",
 "Your Old Disks: 65% Survive Six Years",
 "35% of Your Disks Die by Year Six",
 "Disks Die at Year Six, Boards Don't",
 "Your Disk Dies; Your Board Doesn't",
]
for t in cands:
    r = hs.score(t, body=body)
    print(f"{r.get('score'):>4} {r.get('verdict'):<7} lead_ok={r.get('lead_ok')} | {t}")
    for f in (r.get('fails') or []):
        print("      -", f)
