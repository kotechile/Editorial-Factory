import sys
sys.path.insert(0, 'scripts')
import citation_hub_dossier as c

CANDS = [
    ("https://www.seagate.com/products/nas-drives/ironwolf-hard-drive/", ["5-year", "5 year", "warranty"]),
    ("https://www.westerndigital.com/products/internal-drives/wd-red-plus-sata-3-5-hdd", ["5-year", "warranty"]),
    ("https://serverpartdeals.com/collections/manufacturer-recertified-drives", ["$", "TB"]),
    ("https://www.provantage.com/seagate-st8000vn004~7SEA90GC.htm", ["$"]),
    ("https://www.bhphotovideo.com/c/product/1402001-REG/seagate_st8000vn004_ironwolf_8tb_7200.html", ["$"]),
    ("https://www.wasabi.com/pricing", ["$6.99", "per TB"]),
    ("https://www.backblaze.com/blog/hard-drive-failure-rates-backup-advice/", ["failure"]),
    ("https://www.servethehome.com/", ["$"]),
]

for url, figs in CANDS:
    try:
        r = c.fetch_source(url)
    except Exception as e:
        print("=" * 90); print(url); print("EXC", e); continue
    text = r.get('text', '') or ''
    print("=" * 90)
    print(url)
    print("status:", r.get('status'), "http:", r.get('http'), "len:", len(text))
    if r.get('status') != 'fetched':
        print("reason:", r.get('reason'))
        continue
    print("head:", " ".join(text[:300].split()))
    for f in figs:
        ev = c.figure_evidence(f, text)
        print(f"  fig {f!r}: {'FOUND' if ev else 'absent'} :: {(ev or '')[:160]}")
