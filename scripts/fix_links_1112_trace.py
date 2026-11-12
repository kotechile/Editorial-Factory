#!/usr/bin/env python3
"""Strip the generated <!-- internal-links --> block from the artifact, the Supabase
row and the live CMS post for one slug (rule 12: a link justified only by one
incidental token is not evidence, and `wp_draft --refresh-live` re-stamps it)."""
import json
import re
import sys
import urllib.request
import base64

sys.path.insert(0, "scripts")
import wp_draft as W

SLUG = "your-carrier-is-exempt-your-lot-records-arent"
ARTIFACT = f"published/2026-11-12_{SLUG}.md"
POST_ID = 1677

W.load_env()

text = open(ARTIFACT, encoding="utf-8").read()
stripped = re.sub(r"\n*<!-- internal-links -->.*?<!-- internal-links:end -->\n*", "\n", text, flags=re.S)
if stripped == text:
    print("!! no internal-links block found in the artifact")
else:
    open(ARTIFACT, "w", encoding="utf-8").write(stripped)
    print("artifact: block removed", len(text), "->", len(stripped))

url, key = W.supabase_config()
sb = W.Supabase(url, key)
rows = sb.articles(slug=SLUG)
if not rows:
    print("!! no supabase row for", SLUG)
    sys.exit(1)
row = rows[0]
html = W.md_to_html(stripped)
sb.update_body(row["id"], html, row.get("metadata") or {})
print("supabase: body rewritten", len(html), "chars html")

user, password = W.credentials_for("aichieve.net")
auth = base64.b64encode(f"{user}:{password}".encode()).decode()
body = json.dumps({"content": html}).encode()
req = urllib.request.Request(
    f"https://cms.giniloh.com/wp-json/wp/v2/posts/{POST_ID}",
    data=body,
    method="POST",
    headers={"Content-Type": "application/json", "Authorization": f"Basic {auth}"},
)
with urllib.request.urlopen(req, timeout=60) as r:
    out = json.loads(r.read().decode())
print("wp: post updated", out.get("id"), out.get("modified"))

# read back
req = urllib.request.Request(f"https://cms.giniloh.com/wp-json/wp/v2/posts/{POST_ID}?context=view", headers={"Authorization": f"Basic {auth}"})
with urllib.request.urlopen(req, timeout=60) as r:
    post = json.loads(r.read().decode())
rendered = (post.get("content") or {}).get("rendered", "")
print("readback: len", len(rendered), "| related-reading:", "Related reading" in rendered,
      "| internal hrefs:", len(re.findall(r'href="/[^"]+"', rendered)))
