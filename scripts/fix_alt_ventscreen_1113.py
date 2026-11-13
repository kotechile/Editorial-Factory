import json, base64, urllib.request
from pathlib import Path

ROOT = Path('/root/editorial-factory')
SLUG = 'your-1-8-inch-screen-leaks-embers'
MEDIA = 412
ARTICLE_ID = '6e62c756-d59e-43bd-82ea-eebbaf75554b'
NEW_ALT = "A rusted steel vent screen glows orange from fire behind it as a tuft of fine insulation catches embers."
NEW_CAPTION = "The 1/8-inch vent screen the discount list accepts, with burning embers still passing through."

env = {}
for line in (ROOT / '.env').read_text().splitlines():
    if '=' in line and not line.strip().startswith('#'):
        k, v = line.split('=', 1)
        env[k.strip()] = v.strip().strip('"').strip("'")

side_path = ROOT / 'context/assets/illustrations' / SLUG / 'featured.json'
side = json.loads(side_path.read_text())
side['alt_text'] = NEW_ALT
side['caption'] = NEW_CAPTION
side_path.write_text(json.dumps(side, indent=2, ensure_ascii=False) + "\n")
print('sidecar alt len ->', len(NEW_ALT), '|', len(NEW_CAPTION))

for path in [ROOT / 'published' / f'2026-11-13_{SLUG}.md',
             ROOT / 'context/drafts' / f'2026-11-13_{SLUG}_final.md']:
    lines = path.read_text().splitlines(keepends=True)
    for i, line in enumerate(lines):
        if line.startswith('image_alt:'):
            lines[i] = f'image_alt: "{NEW_ALT}"\n'
        elif line.startswith('image_caption:'):
            lines[i] = f'image_caption: "{NEW_CAPTION}"\n'
    path.write_text(''.join(lines))
    print('patched', path.name, NEW_ALT in path.read_text())

auth = base64.b64encode(f"{env['WP_WELLROOST_USER']}:{env['WP_WELLROOST_APP_PASSWORD']}".encode()).decode()
req = urllib.request.Request(
    f"https://cms.wellroost.com/wp-json/wp/v2/media/{MEDIA}",
    data=json.dumps({"alt_text": NEW_ALT, "caption": NEW_CAPTION}).encode(),
    headers={"Authorization": f"Basic {auth}", "Content-Type": "application/json"},
    method="POST",
)
resp = json.load(urllib.request.urlopen(req, timeout=60))
print('media alt now ->', resp.get('alt_text'))
print('media caption now ->', (resp.get('caption') or {}).get('rendered'))

url = env['SUPABASE_URL'].rstrip('/'); key = env['SUPABASE_SERVICE_ROLE_KEY']
req = urllib.request.Request(
    f"{url}/rest/v1/articles?id=eq.{ARTICLE_ID}&select=metadata",
    headers={"apikey": key, "Authorization": f"Bearer {key}"},
)
row = json.load(urllib.request.urlopen(req, timeout=45))[0]
meta = row['metadata'] or {}
meta.setdefault('illustration', {})['alt_text'] = NEW_ALT
meta.setdefault('illustration', {})['caption'] = NEW_CAPTION
meta.setdefault('wordpress', {})['media_alt'] = NEW_ALT
req = urllib.request.Request(
    f"{url}/rest/v1/articles?id=eq.{ARTICLE_ID}",
    data=json.dumps({"metadata": meta}).encode(),
    headers={"apikey": key, "Authorization": f"Bearer {key}", "Content-Type": "application/json",
             "Prefer": "return=minimal"},
    method="PATCH",
)
urllib.request.urlopen(req, timeout=45)
print('supabase row patched')
