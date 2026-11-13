#!/usr/bin/env python3
"""Repair pass for 2026-11-13 12-structures-froze-50000-policies (resilient_home_assets).

1. Recover the truncated alt text from the sidecar's own history[0] and reconcile it
   across the sidecar, the artifact, media 407 and the Supabase row.
2. Curate the generated Related-reading block (rule 12): the generator justified
   /your-condensers-repair-bill-2090-vs-700/ on category alone, which is not evidence.
3. Write the enriched body back to the row and the live post as HTML, then toggle
   status draft->publish so the reader front rebuilds.
"""
import base64
import json
import re
import sys
import urllib.request

sys.path.insert(0, "scripts")
import wp_draft as W

SLUG = "12-structures-froze-50000-policies"
ARTIFACT = f"published/2026-11-13_{SLUG}.md"
FINAL = f"context/drafts/2026-11-13_{SLUG}_final.md"
SIDE = f"context/assets/illustrations/{SLUG}/featured.json"
POST_ID = 408
MEDIA = 407

ALT = ("A California ranch house at blue hour with a blank wall clock above its garage, "
       "burnt ground and a charred perimeter line stopping at the driveway.")

BLOCK = """<!-- internal-links:start -->
## Related reading

- [Your Nonrenewal Isn't Final: Count 120 Days](/your-nonrenewal-isnt-final-count-120-days/) — more on Home Cost Decisions
- [Energy & Efficiency](/categories/energy-efficiency/) — more on Energy & Efficiency
<!-- internal-links:end -->"""

W.load_env()

# --- 1. alt text, sidecar + artifacts -------------------------------------
side = json.loads(open(SIDE, encoding="utf-8").read())
side["alt_text"] = ALT
open(SIDE, "w", encoding="utf-8").write(json.dumps(side, indent=2, ensure_ascii=False) + "\n")
print("sidecar alt ->", len(ALT), "chars")

for path in (ARTIFACT, FINAL):
    lines = open(path, encoding="utf-8").read().splitlines(keepends=True)
    for i, line in enumerate(lines):
        if line.startswith("image_alt:"):
            lines[i] = f'image_alt: "{ALT}"\n'
    open(path, "w", encoding="utf-8").write("".join(lines))
    print("artifact patched:", path)

# --- 2. curated related-reading block -----------------------------------
text = open(ARTIFACT, encoding="utf-8").read()
new_text, n = re.subn(r"<!-- internal-links:start[^\n]*-->.*?<!-- internal-links:end -->",
                      BLOCK, text, flags=re.S)
print("link block replaced:", n)
open(ARTIFACT, "w", encoding="utf-8").write(new_text)

# --- 3. media alt --------------------------------------------------------
user, password = W.credentials_for("wellroost.com")
auth = base64.b64encode(f"{user}:{password}".encode()).decode()
req = urllib.request.Request(
    f"https://cms.wellroost.com/wp-json/wp/v2/media/{MEDIA}",
    data=json.dumps({"alt_text": ALT}).encode(),
    method="POST",
    headers={"Authorization": f"Basic {auth}", "Content-Type": "application/json"},
)
resp = json.load(urllib.request.urlopen(req, timeout=60))
print("media alt now ->", resp.get("alt_text"))

# --- 4. Supabase row: body + metadata ------------------------------------
url, key = W.supabase_config()
sb = W.Supabase(url, key)
row = sb.articles(slug=SLUG)[0]
meta = row.get("metadata") or {}
meta.setdefault("illustration", {})["alt_text"] = ALT
meta.setdefault("wordpress", {})["media_alt"] = ALT
meta["internal_links"] = [
    {"title": "Your Nonrenewal Isn't Final: Count 120 Days",
     "url": "/your-nonrenewal-isnt-final-count-120-days/"},
    {"title": "Energy & Efficiency", "url": "/categories/energy-efficiency/"},
]
html = W.md_to_html(new_text)
sb.update_body(row["id"], html, meta)
print("supabase body updated:", len(html), "chars html")

# --- 5. live post: HTML body, then status toggle -------------------------
def post(payload):
    req = urllib.request.Request(
        f"https://cms.wellroost.com/wp-json/wp/v2/posts/{POST_ID}",
        data=json.dumps(payload).encode(),
        method="POST",
        headers={"Authorization": f"Basic {auth}", "Content-Type": "application/json"},
    )
    return json.load(urllib.request.urlopen(req, timeout=90))

out = post({"content": html})
print("post content updated; modified", out.get("modified"))
post({"status": "draft"})
back = post({"status": "publish"})
print("status toggled ->", back.get("status"))

req = urllib.request.Request(
    f"https://cms.wellroost.com/wp-json/wp/v2/posts/{POST_ID}?context=view",
    headers={"Authorization": f"Basic {auth}"},
)
p = json.load(urllib.request.urlopen(req, timeout=60))
rendered = (p.get("content") or {}).get("rendered", "")
print("readback len", len(rendered),
      "| Related reading:", "Related reading" in rendered,
      "| condenser link gone:", "condensers-repair-bill" not in rendered,
      "| nonrenewal link:", "your-nonrenewal-isnt-final-count-120-days" in rendered)
