import json, base64, urllib.request
from pathlib import Path

ROOT = Path('/root/editorial-factory')
SLUG = 'your-hidden-461-double-counts'
MEDIA = 1745
ARTICLE_ID = 'df1b812c-be18-49d2-8d42-071413d6878f'
NEW_ALT = "A container ship at a terminal quay mirrored in still dock water, with gantry cranes and stacked containers behind."
NEW_CAP = "An unbranded ship doubled by its own reflection in the dock basin: the same call entered the average twice."

env = {}
for line in (ROOT / '.env').read_text().splitlines():
    if '=' in line and not line.strip().startswith('#'):
        k, v = line.split('=', 1)
        env[k.strip()] = v.strip().strip('"').strip("'")

side_path = ROOT / 'context/assets/illustrations' / SLUG / 'featured.json'
side = json.loads(side_path.read_text())
side['alt_text'] = NEW_ALT
side['caption'] = NEW_CAP
side['revision'] = int(side.get('revision', 1)) + 1
side_path.write_text(json.dumps(side, indent=2, ensure_ascii=False) + "\n")
print('sidecar ->', len(side['alt_text']), 'chars alt, revision', side['revision'])

for path in [ROOT / 'published' / f'2026-11-17_{SLUG}.md',
             ROOT / 'context/drafts' / f'2026-11-17_{SLUG}_final.md']:
    lines = path.read_text().splitlines(keepends=True)
    for i, line in enumerate(lines):
        if line.startswith('image_alt:'):
            lines[i] = f'image_alt: "{NEW_ALT}"\n'
        if line.startswith('image_caption:'):
            lines[i] = f'image_caption: "{NEW_CAP}"\n'
    path.write_text(''.join(lines))
    print('patched', path.name, NEW_ALT[:30] in path.read_text())

auth = base64.b64encode(f"{env['WP_GINILOH_USER']}:{env['WP_GINILOH_APP_PASSWORD']}".encode()).decode()
req = urllib.request.Request(
    f"https://cms.giniloh.com/wp-json/wp/v2/media/{MEDIA}",
    data=json.dumps({"alt_text": NEW_ALT, "caption": NEW_CAP}).encode(),
    headers={"Authorization": f"Basic {auth}", "Content-Type": "application/json"},
    method="POST",
)
resp = json.load(urllib.request.urlopen(req, timeout=60))
print('media alt now ->', resp['alt_text'])
print('media caption now ->', resp['caption']['raw'][:80])

url = env['SUPABASE_URL'].rstrip('/'); key = env['SUPABASE_SERVICE_ROLE_KEY']
req = urllib.request.Request(
    f"{url}/rest/v1/articles?id=eq.{ARTICLE_ID}&select=metadata",
    headers={"apikey": key, "Authorization": f"Bearer {key}"},
)
row = json.load(urllib.request.urlopen(req, timeout=45))[0]
meta = row['metadata'] or {}
meta.setdefault('illustration', {})['alt_text'] = NEW_ALT
meta.setdefault('illustration', {})['caption'] = NEW_CAP
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

req = urllib.request.Request(
    f"{url}/rest/v1/articles?id=eq.{ARTICLE_ID}&select=title,metadata",
    headers={"apikey": key, "Authorization": f"Bearer {key}"},
)
back = json.load(urllib.request.urlopen(req, timeout=45))[0]
print('readback alt:', back['metadata']['wordpress']['media_alt'])
print('readback kind:', back['metadata'].get('kind'), '| synthesis:', back['metadata'].get('synthesis'))
