import sys, re
sys.path.insert(0, 'scripts')
import citation_hub_dossier as c

CANDS = [
    ("https://www.backblaze.com/blog/how-long-do-disk-drives-last",
     ["65%", "2% to 2.5%", "2.5% a year", "six years", "80%"]),
    ("https://www.backblaze.com/blog/backblaze-drive-stats-for-q2-2026",
     ["1.73", "354,415", "1.41", "6.95%"]),
    ("https://diskprices.com/",
     ["$23.57", "$/TB", "per TB"]),
    ("https://www.eia.gov/energyexplained/electricity/prices-and-factors-affecting-prices.php",
     ["17.30", "13.63", "35.72"]),
    ("https://www.backblaze.com/cloud-storage/pricing",
     ["$6", "per TB", "$6.00"]),
]

for url, figs in CANDS:
    r = c.fetch_source(url)
    text = r.get('text', '') or ''
    print("=" * 100)
    print(url)
    print("status:", r.get('status'), "http:", r.get('http'), "len:", len(text))
    if r.get('status') != 'fetched':
        print("reason:", r.get('reason'))
        continue
    for f in figs:
        ev = c.figure_evidence(f, text)
        print(f"  fig {f!r}: {'FOUND' if ev else 'absent'} :: {(ev or '')[:200]}")
