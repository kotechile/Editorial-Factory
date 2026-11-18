import urllib.request, urllib.parse, json, re, time

UAS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/126 Safari/537.36"}
def get(url):
    req = urllib.request.Request(url, headers=UAS)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", "replace")

ids = ["2611.22075","2611.21577","2611.20922","2611.22262","2611.21129","2611.18887",
       "2611.15223","2611.20298","2611.19123","2611.06967","2611.06989","2610.37700",
       "2611.07050","2611.06727"]
url = ("https://export.arxiv.org/api/query?id_list=" + ",".join(ids) + "&max_results=20")
xml = get(url)
for e in re.findall(r"<entry>(.*?)</entry>", xml, re.S):
    aid = re.search(r"<id>(.*?)</id>", e).group(1).split("/abs/")[-1]
    pub = re.search(r"<published>(.*?)</published>", e).group(1)[:10]
    ttl = re.sub(r"\s+"," ",re.search(r"<title>(.*?)</title>", e, re.S).group(1)).strip()
    summ = re.sub(r"\s+"," ",re.search(r"<summary>(.*?)</summary>", e, re.S).group(1)).strip()
    auths = re.findall(r"<name>(.*?)</name>", e)[:4]
    print(f"\n### {aid} | {pub} | {ttl}\nBY: {', '.join(auths)}\n{summ}")
