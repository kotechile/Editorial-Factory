import sys
sys.path.insert(0, 'scripts')
import citation_hub_dossier as c

URLS = [
    "https://www.newegg.com/p/N82E16822184785",
    "https://www.cdw.com/product/seagate-ironwolf-st8000vn004-hard-drive-8-tb-sata-6gb-s/5844199",
    "https://www.scan.co.uk/products/8tb-seagate-ironwolf-st8000vn004-sata-iii-6gb-s-7200rpm-256mb-cache-3ms-nas-hard-drive",
    "https://www.overclockers.co.uk/seagate-ironwolf-8tb-st8000vn004-nas-hard-drive-hd-006-sg.html",
    "https://geizhals.de/seagate-ironwolf-8tb-st8000vn004-a1498745.html",
    "https://www.idealo.co.uk/compare/5893300/seagate-ironwolf-8tb-st8000vn004.html",
    "https://serverpartdeals.com/products/seagate-ironwolf-st8000vn004-8tb-7200rpm-sata-6gb-s-3-5-hard-drive",
    "https://www.seagate.com/products/nas-drives/ironwolf-hard-drive/",
]

for url in URLS:
    try:
        r = c.fetch_source(url)
    except Exception as e:
        print("=" * 90); print(url, "EXC", e); continue
    text = r.get('text', '') or ''
    print("=" * 90)
    print(url, "|", r.get('status'), r.get('http'), "len", len(text))
    if r.get('status') == 'fetched':
        print("head:", " ".join(text[:220].split()))
        for f in ["$", "5-year", "warranty", "Ironwolf", "IronWolf"]:
            ev = c.figure_evidence(f, text) if f == "$" else None
            if f == "$":
                print("  $ evidence:", ("FOUND :: " + (ev or "")[:120]) if ev else "absent")
            else:
                print(f"  contains {f!r}:", f.lower() in text.lower())
