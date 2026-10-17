import sys, re
sys.path.insert(0, 'scripts')
import citation_hub_dossier as c

def grab(url, pats, width=320):
    t = c.fetch_source(url).get('text','')
    print("=" * 100); print(url, len(t))
    for p in pats:
        for m in re.finditer(p, t):
            s=max(0,m.start()-60); e=min(len(t), m.end()+width)
            print(f"[{p}] ...{ ' '.join(t[s:e].split()) }")
            print("-")
            break

grab("https://www.backblaze.com/blog/how-long-do-disk-drives-last",
     [r"life expectancy of 65%", r"2% to 2\.5%", r"90% of the drives", r"increases beginning in year four"])
grab("https://www.backblaze.com/blog/backblaze-drive-stats-for-q2-2026",
     [r"lifetime AFR", r"quarterly AFR is", r"outlier as an AFR above", r"nearly seven years old", r"two drives fully retire"])
grab("https://www.eia.gov/energyexplained/electricity/prices-and-factors-affecting-prices.php",
     [r"17\.30", r"13\.63"])
grab("https://www.synology.com/en-us/products/DS223j", [r"16\.31 watts"])
grab("https://www.backblaze.com/cloud-storage/pricing", [r"byte-hour"])
