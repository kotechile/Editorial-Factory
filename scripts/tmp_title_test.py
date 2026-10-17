import sys, pathlib
sys.path.insert(0, 'scripts')
import headline_score as hs

body = pathlib.Path('context/drafts/2026-10-17_old-compute-new-disks-65-percent_draft.md').read_text()
for t in ["Your Disks Die Before Your Board",
          "Old Compute, New Disks: The 65% Rule",
          "Your NAS Disks: 65% Alive at Six Years",
          "Disks Die by Year Six: Your Board Won't",
          "Your Disk Is the Only Part That Wears"]:
    r = hs.score(t, body=body)
    print(t, "->", r.get('score'), r.get('verdict'), "lead_ok:", r.get('lead_ok'))
    fails = r.get('fails') or r.get('failures') or []
    print("   ", fails)
