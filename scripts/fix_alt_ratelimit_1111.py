import json, base64, urllib.request
from pathlib import Path

ROOT = Path('/root/editorial-factory')
SLUG = 'your-rate-limit-1-39-a-second'
MEDIA = 1643
ARTICLE_ID = '8abd1612-bb47-4ca5-9476-a054fe94a413'
NEW_ALT = "Cut-paper bucket with a hole draining request dots beside a blank hundred-item page stack on a control room desk."
NEW_CAPTION = "A vendor rate limit is a leaking bucket, and page size is the stack that multiplies every draw."

env = {}
for line in (ROOT / '.env').read_text().splitlines():
    if '=' in line and not line.strip().startswith('#'):
        k, v = line.split('=', 1)
        env[k.strip()] = v.strip().strip('"').strip("'")

# 1. sidecar
side_path = ROOT / 'context/assets/illustrations' / SLUG / 'featured.json'
side = json.loads(side_path.read_text())
side['alt_text'] = NEW_ALT
side['caption'] = NEW_CAPTION
side['title'] = "Rate Limit Bucket and Page Stack"
side_path.write_text(json.dumps(side, indent=2, ensure_ascii=False) + "\n")
print('sidecar alt ->', side['alt_text'][:60], len(side['alt_text']))

# 2. published artifact frontmatter
art = ROOT / 'published/2026-11-11_your-rate-limit-1-39-a-second.md'
lines = art.read_text().splitlines(keepends=True)
for i, line in enumerate(lines):
    if line.startswith('image_alt:'):
        lines[i] = f'image_alt: "{NEW_ALT}"\n'
    elif line.startswith('image_caption:'):
        lines[i] = f'image_caption: "{NEW_CAPTION}"\n'
art.write_text(''.join(lines))
print('artifact patched:', NEW_ALT[:30] in art.read_text())

# 3. CMS media
auth = base64.b64encode(f"{env['WP_GINILOH_USER']}:{env['WP_GINILOH_APP_PASSWORD']}".encode()).decode()
req = urllib.request.Request(
    f"https://cms.giniloh.com/wp-json/wp/v2/media/{MEDIA}",
    data=json.dumps({"alt_text": NEW_ALT, "caption": NEW_CAPTION}).encode(),
    headers={"Authorization": f"Basic {auth}", "Content-Type": "application/json"},
    method="POST",
)
resp = json.load(urllib.request.urlopen(req, timeout=60))
print('media alt now ->', resp['alt_text'][:60], '| caption:', resp['caption']['rendered'][:60])

# 4. Supabase row metadata
url = env['SUPABASE_URL'].rstrip('/'); key = env['SUPABASE_SERVICE_ROLE_KEY']
req = urllib.request.Request(
    f"{url}/rest/v1/articles?id=eq.{ARTICLE_ID}&select=metadata",
    headers={"apikey": key, "Authorization": f"Bearer {key}"},
)
row = json.load(urllib.request.urlopen(req, timeout=45))[0]
meta = row['metadata']
meta.setdefault('illustration', {})['alt_text'] = NEW_ALT
meta.setdefault('wordpress', {})['media_alt'] = NEW_ALT
req = urllib.request.Request(
    f"{url}/rest/v1/articles?id=eq.{ARTICLE_ID}",
    data=json.dumps({"metadata": meta}).encode(),
    headers={"apikey": key, "Authorization": f"Bearer {key}", "Content-Type": "application/json",
             "Prefer": "return=minimal"},
    method="PATCH",
)
urllib.request.urlopen(req, timeout=45)
print('supabase metadata patched')

# 5. read back
req = urllib.request.Request(
    f"{url}/rest/v1/articles?id=eq.{ARTICLE_ID}&select=metadata",
    headers={"apikey": key, "Authorization": f"Bearer {key}"},
)
back = json.load(urllib.request.urlopen(req, timeout=45))[0]['metadata']
print('readback illustration.alt_text:', back['illustration']['alt_text'][:60])
print('readback wordpress.media_alt:', back['wordpress']['media_alt'][:60])
