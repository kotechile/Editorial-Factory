import json, base64, time, urllib.request, sys
from pathlib import Path

ROOT = Path('/root/editorial-factory')
sys.path.insert(0, str(ROOT / 'scripts'))
import wp_draft

SLUG = 'your-1-8-inch-screen-leaks-embers'
POST = 413
ARTICLE_ID = '6e62c756-d59e-43bd-82ea-eebbaf75554b'

env = {}
for line in (ROOT / '.env').read_text().splitlines():
    if '=' in line and not line.strip().startswith('#'):
        k, v = line.split('=', 1)
        env[k.strip()] = v.strip().strip('"').strip("'")

art = ROOT / 'published' / f'2026-11-13_{SLUG}.md'
raw = art.read_text()
html = wp_draft.md_to_html(raw)
print('html chars', len(html), '| carries fix:', "Fire Safe Marin's retrofit guidance" in html)

auth = base64.b64encode(f"{env['WP_WELLROOST_USER']}:{env['WP_WELLROOST_APP_PASSWORD']}".encode()).decode()
H = {"Authorization": f"Basic {auth}", "Content-Type": "application/json"}


def post(payload):
    req = urllib.request.Request(f"https://cms.wellroost.com/wp-json/wp/v2/posts/{POST}",
                                 data=json.dumps(payload).encode(), headers=H, method="POST")
    return json.load(urllib.request.urlopen(req, timeout=90))


r = post({"content": html})
print('content patched, status', r['status'], 'len', len(r['content']['rendered']))

# same-status POST does not fire the front rebuild: toggle draft -> publish
print('-> draft', post({"status": "draft"})['status'])
time.sleep(6)
print('-> publish', post({"status": "publish"})['status'])

back = json.load(urllib.request.urlopen(
    urllib.request.Request(f"https://cms.wellroost.com/wp-json/wp/v2/posts/{POST}?context=edit",
                           headers=H), timeout=60))
body = back['content']['raw']
print('raw body carries fix:', "Fire Safe Marin's retrofit guidance" in body,
      '| hrefs:', body.count('href="/'), '| status:', back['status'], '| media:', back['featured_media'])

url = env['SUPABASE_URL'].rstrip('/'); key = env['SUPABASE_SERVICE_ROLE_KEY']
req = urllib.request.Request(f"{url}/rest/v1/articles?id=eq.{ARTICLE_ID}",
                             data=json.dumps({"content": body}).encode(),
                             headers={"apikey": key, "Authorization": f"Bearer {key}",
                                      "Content-Type": "application/json", "Prefer": "return=minimal"},
                             method="PATCH")
urllib.request.urlopen(req, timeout=45)
print('supabase content patched')
