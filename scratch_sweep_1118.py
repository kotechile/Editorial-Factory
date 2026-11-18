import urllib.request, urllib.parse, json, re, sys, datetime, time

FLOOR = datetime.datetime(2026, 10, 19)
UAS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/126 Safari/537.36"}

def get(url):
    req = urllib.request.Request(url, headers=UAS)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", "replace")

QUERIES = [
 ('saga', 'all:"saga pattern" OR all:"compensating transaction" OR all:"distributed transaction" AND all:"agent"'),
 ('rollback', 'all:"multi-agent" AND all:rollback'),
 ('mcp', 'all:"Model Context Protocol"'),
 ('mcp2', 'all:"MCP" AND all:tool AND all:agent'),
 ('erp', 'all:"ERP" AND all:agent'),
 ('schema', 'all:"tool schema" OR all:"tool description" OR all:"context poisoning"'),
 ('durable', 'all:"durable execution" OR all:"workflow engine" OR all:"state persistence"'),
 ('orch', 'all:"multi-agent orchestration" AND all:enterprise'),
 ('fabric', 'all:"agent fabric" OR all:"agent mesh" OR all:"agent gateway"'),
 ('interop', 'all:"agent interoperability" OR all:"A2A" OR all:"agent-to-agent protocol"'),
]

out = {}
for tag, q in QUERIES:
    url = ("https://export.arxiv.org/api/query?search_query=" + urllib.parse.quote(q)
           + "&sortBy=submittedDate&sortOrder=descending&max_results=40")
    try:
        xml = get(url)
    except Exception as e:
        print(f"[{tag}] FETCH FAIL {e}")
        continue
    entries = re.findall(r"<entry>(.*?)</entry>", xml, re.S)
    rows = []
    for e in entries:
        aid = re.search(r"<id>(.*?)</id>", e)
        pub = re.search(r"<published>(.*?)</published>", e)
        ttl = re.search(r"<title>(.*?)</title>", e, re.S)
        abs_ = re.search(r"<summary>(.*?)</summary>", e, re.S)
        if not (aid and pub and ttl):
            continue
        d = datetime.datetime.strptime(pub.group(1)[:10], "%Y-%m-%d")
        rec = {
            "id": aid.group(1).split("/abs/")[-1],
            "date": pub.group(1)[:10],
            "title": re.sub(r"\s+", " ", ttl.group(1)).strip(),
            "abs": re.sub(r"\s+", " ", abs_.group(1)).strip() if abs_ else "",
        }
        rows.append(rec)
    inwin = [r for r in rows if datetime.datetime.strptime(r["date"], "%Y-%m-%d") >= FLOOR]
    out[tag] = inwin
    print(f"\n=== {tag}: {len(rows)} returned, {len(inwin)} in window ===")
    for r in inwin:
        print(f"  {r['date']} {r['id']}  {r['title'][:110]}")
    time.sleep(3)

json.dump(out, open("/root/editorial-factory/scratch_arxiv_1118.json", "w"), indent=1)
print("\nsaved", sum(len(v) for v in out.values()), "in-window hits")
