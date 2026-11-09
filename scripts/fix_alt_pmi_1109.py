import json, base64, urllib.request
from pathlib import Path

ROOT = Path('/root/editorial-factory')
SLUG = 'your-pmi-ends-at-78-not-todays-value'
MEDIA = 381
NEW_ALT = ("An open grey closing folder on a kitchen table with a blank schedule page, a red pencil, "
           "brass clips and a house key.")

env = {}
for line in (ROOT / '.env').read_text().splitlines():
    if '=' in line and not line.strip().startswith('#'):
        k, v = line.split('=', 1)
        env[k.strip()] = v.strip().strip('"').strip("'")

side_path = ROOT / 'context/assets/illustrations' / SLUG / 'featured.json'
side = json.loads(side_path.read_text())
side['alt_text'] = NEW_ALT
side_path.write_text(json.dumps(side, indent=2, ensure_ascii=False) + "\n")

auth = base64.b64encode(f"{env['WP_WELLROOST_USER']}:{env['WP_WELLROOST_APP_PASSWORD']}".encode()).decode()
req = urllib.request.Request(
    f"https://cms.wellroost.com/wp-json/wp/v2/media/{MEDIA}",
    data=json.dumps({"alt_text": NEW_ALT}).encode(),
    headers={"Authorization": f"Basic {auth}", "Content-Type": "application/json"},
    method="POST",
)
with urllib.request.urlopen(req, timeout=60) as r:
    body = json.loads(r.read())
print("media", body.get("id"), "alt ->", body.get("alt_text"))

# read back
req2 = urllib.request.Request(
    f"https://cms.wellroost.com/wp-json/wp/v2/media/{MEDIA}?context=edit",
    headers={"Authorization": f"Basic {auth}"},
)
with urllib.request.urlopen(req2, timeout=60) as r:
    body = json.loads(r.read())
print("read-back alt:", body.get("alt_text"))
