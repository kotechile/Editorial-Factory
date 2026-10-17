import sys, re
sys.path.insert(0, 'scripts')
import citation_hub_dossier as c

print("### backblaze survival page: sentences with numbers")
r = c.fetch_source("https://www.backblaze.com/blog/how-long-do-disk-drives-last")
t = r.get('text', '')
for kw in ["65%", "90%", "2% to 2.5%", "year four", "four years", "life expectancy"]:
    for m in re.finditer(re.escape(kw), t):
        s = max(0, m.start()-160); e = min(len(t), m.end()+160)
        print(f"[{kw}]", " ".join(t[s:e].split()))
        print("-")
        break

print("\n### probe other hosts")
CANDS = [
    ("https://datarecovery.com/rd/raid-data-recovery-why-automatic-raid-rebuilds-fail", ["secondary drive failure", "unrecoverable read error"]),
    ("https://www.ontrack.com/en-us/blog/raid-vs-drive-rebuilds", ["second drive fails", "degraded"]),
    ("https://www.synology.com/en-us/products/DS223j", ["16.31", "4 watts", "16.31 watts"]),
]
for url, figs in CANDS:
    rr = c.fetch_source(url)
    tt = rr.get('text', '') or ''
    print("=" * 90)
    print(url, "|", rr.get('status'), rr.get('http'), "len", len(tt))
    if rr.get('status') != 'fetched':
        print("reason:", rr.get('reason')); continue
    for f in figs:
        ev = c.figure_evidence(f, tt)
        print(f"  {f!r}: {'FOUND' if ev else 'absent'} :: {(ev or '')[:190]}")
