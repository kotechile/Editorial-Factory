"""Reconcile the featured-image alt text and caption for mowers-2cm-dies-under-trees.

The art director's alt arrived as the house overlay headline glued to a clipped phrase
("Mower'S 2 Cm Dies Under Trees. Wire-free robotic mower ... split-screen contrast"), so the
sidecar, the published artifact, the CMS media record and the Supabase row are all set to the
complete sentence the sidecar's history[0] preserved, per skills/evergreen_topics.md.
"""
import base64
import json
import os
import pathlib
import sys
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wp_draft as w  # noqa: E402

SLUG = "mowers-2cm-dies-under-trees"
MEDIA = 350
CMS = "https://cms.wellroost.com"

ALT = ("Wire-free robotic mower on a residential driveway under conifer canopy and open sky, "
       "split-screen contrast.")
CAPTION = ("The same wire-free mower holds centimetre accuracy under open sky and loses the fix "
           "to metres beneath dense conifer canopy.")

w.load_env()

user = pw = ""
for dom in ("wellroost.com", "giniloh.com", "aichieve.net"):
    try:
        user, pw = w.credentials_for(dom)
        print(f"[creds] using {dom}")
        break
    except SystemExit:
        continue
if not user:
    sys.exit("no WP credentials")

auth = base64.b64encode(f"{user}:{pw}".encode()).decode()
body = json.dumps({"alt_text": ALT, "caption": CAPTION}).encode()
req = urllib.request.Request(
    f"{CMS}/wp-json/wp/v2/media/{MEDIA}",
    data=body, method="POST",
    headers={"Authorization": f"Basic {auth}", "Content-Type": "application/json"})
try:
    with urllib.request.urlopen(req, timeout=60) as r:
        print("[media] PATCH", r.status)
except urllib.error.HTTPError as e:
    print("[media] PATCH failed", e.code, e.read()[:300])

req = urllib.request.Request(
    f"{CMS}/wp-json/wp/v2/media/{MEDIA}?context=edit",
    headers={"Authorization": f"Basic {auth}"})
with urllib.request.urlopen(req, timeout=60) as r:
    m = json.load(r)
print("[media] read back alt:", m.get("alt_text"))
print("[media] read back caption:", (m.get("caption") or {}).get("raw"))

side = ROOT / "context/assets/illustrations" / SLUG / "featured.json"
d = json.loads(side.read_text())
d["alt_text"] = ALT
d["caption"] = CAPTION
side.write_text(json.dumps(d, indent=2) + "\n")
print("[sidecar] updated")

for rel in (f"published/2026-11-07_{SLUG}.md",
            f"context/drafts/2026-11-07_{SLUG}_final.md"):
    p = ROOT / rel
    if not p.exists():
        print("[artifact] missing", rel)
        continue
    out = []
    for line in p.read_text().splitlines():
        if line.startswith("image_alt:"):
            line = f'image_alt: "{ALT}"'
        elif line.startswith("image_caption:"):
            line = f'image_caption: "{CAPTION}"'
        out.append(line)
    p.write_text("\n".join(out) + "\n")
    print("[artifact] updated", rel)

url = os.environ["SUPABASE_URL"].rstrip("/")
key = os.environ["SUPABASE_SERVICE_ROLE_KEY"]
hdr = {"apikey": key, "Authorization": f"Bearer {key}", "Content-Type": "application/json"}
q = f"{url}/rest/v1/articles?slug=eq.{SLUG}&select=id,metadata"
with urllib.request.urlopen(urllib.request.Request(q, headers=hdr), timeout=60) as r:
    rows = json.load(r)
row = rows[0]
meta = row.get("metadata") or {}
meta.setdefault("illustration", {})["alt_text"] = ALT
meta["illustration"]["caption"] = CAPTION
meta.setdefault("wordpress", {})["media_alt"] = ALT
req = urllib.request.Request(
    f"{url}/rest/v1/articles?id=eq.{row['id']}", data=json.dumps({"metadata": meta}).encode(),
    method="PATCH", headers={**hdr, "Prefer": "return=representation"})
with urllib.request.urlopen(req, timeout=60) as r:
    upd = json.load(r)
print("[supabase] patched", upd[0]["id"], "media_alt:", upd[0]["metadata"]["wordpress"].get("media_alt"))
