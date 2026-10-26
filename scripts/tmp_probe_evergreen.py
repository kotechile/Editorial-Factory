import sys, re
sys.path.insert(0, 'scripts')
import citation_hub_dossier as chd

def grab(url, pats):
    t = chd.fetch_source(url).get("text") or ""
    print("=" * 110)
    print(url)
    for p in pats:
        for m in re.finditer(p, t):
            s = re.sub(r"\s+", " ", t[max(0, m.start()-260):m.start()+320])
            print(f"\n[{p}] ...{s}...")

grab("https://inventoros.com/blog/order-fill-rate", [r"81\.7", r"Order fill rate is the strictest", r"line fill rate counts order lines"])
grab("https://www.fcbco.com/blog/use-initial-order-fill-rate-to-measure-customer-service",
     [r"76\.5", r"88\.5", r"10-15 full percentage points", r"2\.25 lines", r"3\.0 lines"])
grab("https://www.benchmarkingsuccess.com/understanding-fill-rate-kpis-line-fill-rate",
     [r"around 82%", r"7,500 perfectly filled lines", r"slow-moving items"])
grab("https://dclcorp.com/blog/fulfillment/fill-rate", [r"92", r"Line fill rate measures"])
