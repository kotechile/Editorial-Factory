import urllib.request, re, sys

UAS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/126 Safari/537.36"}
def get(url):
    req = urllib.request.Request(url, headers=UAS)
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.read().decode("utf-8", "replace")

def strip(h):
    h = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", h)
    h = re.sub(r"(?s)<[^>]+>", " ", h)
    h = h.replace("&nbsp;"," ").replace("&amp;","&").replace("&lt;","<").replace("&gt;",">")
    return re.sub(r"[ \t]+", " ", re.sub(r"\n\s*\n+", "\n", h))

for aid in sys.argv[1:]:
    try:
        t = strip(get(f"https://arxiv.org/html/{aid}v1"))
    except Exception as e:
        print(f"### {aid} FAIL {e}"); continue
    open(f"/tmp/{aid}.txt","w").write(t)
    print(f"\n######## {aid}  ({len(t)} chars) -> /tmp/{aid}.txt")
    print(t[:1200])
