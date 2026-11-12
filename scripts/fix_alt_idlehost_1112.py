import json, base64, urllib.request
from pathlib import Path

ROOT = Path('/root/editorial-factory')
SLUG = 'idle-host-starved-tools-11-trap'
MEDIA = 1669
ARTICLE_ID = '4eba43a2-b478-4b29-9d2d-6a24251f9ad7'
NEW_ALT = "A host CPU rack flares amber under a tool-stage burst while adjacent racks idle in cool blue in a data hall aisle."

env = {}
for line in (ROOT / '.env').read_text().splitlines():
    if '=' in line and not line.strip().startswith('#'):
        k, v = line.split('=', 1)
        env[k.strip()] = v.strip().strip('"').strip("'")

side_path = ROOT / 'context/assets/illustrations' / SLUG / 'featured.json'
side = json.loads(side_path.read_text())
side['alt_text'] = NEW_ALT
side_path.write_text(json.dumps(side, indent=2, ensure_ascii=False) + "\n")
print('sidecar alt len ->', len(side['alt_text']))

for path in [ROOT / 'published' / f'2026-11-12_{SLUG}.md',
             ROOT / 'context/drafts' / f'2026-11-12_{SLUG}_final.md']:
    lines = path.read_text().splitlines(keepends=True)
    for i, line in enumerate(lines):
        if line.startswith('image_alt:'):
            lines[i] = f'image_alt: "{NEW_ALT}"\n'
    path.write_text(''.join(lines))
    print('patched', path.name, NEW_ALT[:25] in path.read_text())

auth = base64.b64encode(f"{env['WP_GINILOH_USER']}:{env['WP_GINILOH_APP_PASSWORD']}".encode()).decode()
req = urllib.request.Request(
    f"https://cms.giniloh.com/wp-json/wp/v2/media/{MEDIA}",
    data=json.dumps({"alt_text": NEW_ALT}).encode(),
    headers={"Authorization": f"Basic {auth}", "Content-Type": "application/json"},
    method="POST",
)
resp = json.load(urllib.request.urlopen(req, timeout=60))
print('media alt now ->', resp['alt_text'])

url = env['SUPABASE_URL'].rstrip('/'); key = env['SUPABASE_SERVICE_ROLE_KEY']
req = urllib.request.Request(
    f"{url}/rest/v1/articles?id=eq.{ARTICLE_ID}&select=metadata",
    headers={"apikey": key, "Authorization": f"Bearer {key}"},
)
row = json.load(urllib.request.urlopen(req, timeout=45))[0]
meta = row['metadata'] or {}
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
print('supabase row patched')
