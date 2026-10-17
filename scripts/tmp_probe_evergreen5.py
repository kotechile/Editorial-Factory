import sys
sys.path.insert(0, 'scripts')
import citation_hub_dossier as c

CANDS = [
    ("https://www.vertice.one/insights/unused-saas-applications", ["65%", "62%", "$75"]),
    ("https://zylo.com/blog/unused-software-cut-costs", ["46%", "54%", "$19.8M", "19.8"]),
    ("https://licenselogic.co/blog/saas-spend-optimization", ["54%", "30%", "305"]),
    ("https://www.usecarly.com/blog/saas-statistics", ["36%", "54%"]),
    ("https://zylo.com/saas-management-index", ["54%"]),
]
for url, figs in CANDS:
    try:
        r = c.fetch_source(url)
    except Exception as e:
        print("=" * 80); print(url, "EXC", e); continue
    t = r.get('text', '') or ''
    print("=" * 80)
    print(url, "|", r.get('status'), r.get('http'), "len", len(t))
    if r.get('status') != 'fetched':
        print("reason:", r.get('reason')); continue
    for f in figs:
        ev = c.figure_evidence(f, t)
        print(f"  {f!r}: {'FOUND' if ev else 'absent'} :: {(ev or '')[:170]}")
