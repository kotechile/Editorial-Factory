import json, base64, os, urllib.request, urllib.error
from pathlib import Path

ROOT = Path('/root/editorial-factory')
SLUG = 'your-fill-rate-is-a-pallet-price'
MEDIA = 1570
ARTICLE_ID = '7d37233c-f0bc-4f2b-9be1-ffe93fdfb6c5'
NEW_ALT = "A single wooden pallet on a concrete warehouse floor, with one slate tag and one amber tag tied to opposite corners."

env = {}
for line in (ROOT / '.env').read_text().splitlines():
    if '=' in line and not line.strip().startswith('#'):
        k, v = line.split('=', 1)
        env[k.strip()] = v.strip().strip('"').strip("'")

# 1. sidecar
side_path = ROOT / 'context/assets/illustrations' / SLUG / 'featured.json'
side = json.loads(side_path.read_text())
side['alt_text'] = NEW_ALT
side_path.write_text(json.dumps(side, indent=2, ensure_ascii=False) + "\n")
print('sidecar alt ->', side['alt_text'][:60])

# 2. artifact frontmatter
art = ROOT / 'published/2026-11-09_your-fill-rate-is-a-pallet-price.md'
text = art.read_text()
lines = text.splitlines(keepends=True)
for i, line in enumerate(lines):
    if line.startswith('image_alt:'):
        lines[i] = f'image_alt: "{NEW_ALT}"\n'
art.write_text(''.join(lines))
print('artifact patched:', 'image_alt: "' + NEW_ALT[:30] in art.read_text())

# 3. CMS media
auth = base64.b64encode(f"{env['WP_GINILOH_USER']}:{env['WP_GINILOH_APP_PASSWORD']}".encode()).decode()
req = urllib.request.Request(
    f"https://cms.giniloh.com/wp-json/wp/v2/media/{MEDIA}",
    data=json.dumps({"alt_text": NEW_ALT}).encode(),
    headers={"Authorization": f"Basic {auth}", "Content-Type": "application/json"},
    method="POST",
)
resp = json.load(urllib.request.urlopen(req, timeout=60))
print('media alt now ->', resp['alt_text'][:60])

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
