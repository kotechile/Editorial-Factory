import urllib.request, urllib.parse, json, time, datetime

UAS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/126 Safari/537.36"}
EPOCH = int(datetime.datetime(2026,10,19).timestamp())

def get(url):
    req = urllib.request.Request(url, headers=UAS)
    with urllib.request.urlopen(req, timeout=45) as r:
        return json.loads(r.read().decode("utf-8","replace"))

queries = ["agent orchestration","MCP","multi-agent","saga pattern","compensating transaction",
           "agent gateway","A2A protocol","tool calling","agent identity","workflow engine",
           "temporal durable execution","agent permissions","SAP agent","LLM agent enterprise"]

seen = {}
for q in queries:
    url = ("https://hn.algolia.com/api/v1/search_by_date?query=" + urllib.parse.quote(q)
           + f"&tags=story&numericFilters=created_at_i%3E{EPOCH},points%3E8&hitsPerPage=40")
    try:
        d = get(url)
    except Exception as e:
        print(f"[{q}] FAIL {e}"); continue
    n=0
    for h in d.get("hits", []):
        oid = h.get("objectID")
        if oid in seen: continue
        seen[oid]=1
        t = h.get("title") or ""
        pts = h.get("points") or 0
        dt = (h.get("created_at") or "")[:10]
        print(f"{dt} {pts:>4} {t[:105]}  <{h.get('url') or 'https://news.ycombinator.com/item?id='+str(oid)}>")
        n+=1
    print(f"--- {q}: {n} new")
    time.sleep(1)
print("TOTAL", len(seen))
