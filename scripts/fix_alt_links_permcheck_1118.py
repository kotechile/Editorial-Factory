#!/usr/bin/env python3
"""Repair pass for 2026-11-18 your-agent-checks-permission-not-ownership (multi_agent_enterprise_fabric).

1. Recover the truncated alt text from the sidecar's own history[0] and reconcile it across the
   sidecar, the artifact, media 1764 and the Supabase row (the director's alt arrives as the
   overlay headline glued to a clipped phrase).
2. Curate the generated Related-reading block (rule 12): the generator justified its picks on
   incidental tokens alone ("agent", "checks", "permission").
3. Write the enriched body back to the row and the live post as HTML, then toggle
   status publish->draft->publish so the reader front rebuilds.
"""
import base64
import json
import re
import sys
import urllib.request

sys.path.insert(0, "scripts")
import wp_draft as W

SLUG = "your-agent-checks-permission-not-ownership"
ARTIFACT = f"published/2026-11-18_{SLUG}.md"
FINAL = f"context/drafts/2026-11-18_{SLUG}_final.md"
SIDE = f"context/assets/illustrations/{SLUG}/featured.json"
POST_ID = 1765
MEDIA = 1764
SITE = "giniloh.com"
CMS = "cms.giniloh.com"

ALT = ("A server module slid out from a rack of identical modules, its exposed hardware revealing a "
       "different revision.")

BLOCK = """<!-- internal-links:start -->
## Related reading

- [Your Gateway: 60.5% Injection Risk](/your-tool-surface-is-a-release-surface/) — the tool surface changes after a deploy, so it needs a release process
- [Your Agent Fabric's 52.2% Blind Spot](/stale-grants-travel-the-graph/) — what a permission check cannot see once the grant travels
- [Your Signed MCP Tool Still Leaks: 3 of 3](/your-signed-tool-still-leaks-3-of-3/) — a publisher's signature is not a statement about the call
<!-- internal-links:end -->"""

W.load_env()

# --- 1. alt text, sidecar + artifacts -------------------------------------
side = json.loads(open(SIDE, encoding="utf-8").read())
side["alt_text"] = ALT
side["revision"] = int(side.get("revision", 1)) + 1
open(SIDE, "w", encoding="utf-8").write(json.dumps(side, indent=2, ensure_ascii=False) + "\n")
print("sidecar alt ->", len(ALT), "chars, revision", side["revision"])

for path in (ARTIFACT, FINAL):
    lines = open(path, encoding="utf-8").read().splitlines(keepends=True)
    for i, line in enumerate(lines):
        if line.startswith("image_alt:"):
            lines[i] = f'image_alt: "{ALT}"\n'
    open(path, "w", encoding="utf-8").write("".join(lines))
    print("artifact patched:", path)

# --- 2. curated related-reading block ------------------------------------
text = open(ARTIFACT, encoding="utf-8").read()
new_text, n = re.subn(r"<!-- internal-links:start[^\n]*-->.*?<!-- internal-links:end -->",
                      BLOCK, text, flags=re.S)
print("link block replaced:", n)
open(ARTIFACT, "w", encoding="utf-8").write(new_text)

# --- 3. media alt --------------------------------------------------------
user, password = W.credentials_for(SITE)
auth = base64.b64encode(f"{user}:{password}".encode()).decode()

def wp(path, payload=None, method="POST", timeout=90):
    req = urllib.request.Request(
        f"https://{CMS}/wp-json/wp/v2/{path}",
        data=json.dumps(payload).encode() if payload is not None else None,
        method=method if payload is not None else "GET",
        headers={"Authorization": f"Basic {auth}", "Content-Type": "application/json"},
    )
    return json.load(urllib.request.urlopen(req, timeout=timeout))

resp = wp(f"media/{MEDIA}", {"alt_text": ALT})
print("media alt now ->", resp.get("alt_text"))

# --- 4. Supabase row: body + metadata ------------------------------------
url, key = W.supabase_config()
sb = W.Supabase(url, key)
row = sb.articles(slug=SLUG)[0]
meta = row.get("metadata") or {}
meta.setdefault("illustration", {})["alt_text"] = ALT
meta.setdefault("wordpress", {})["media_alt"] = ALT
meta["internal_links"] = [
    {"title": "Your Gateway: 60.5% Injection Risk", "url": "/your-tool-surface-is-a-release-surface/"},
    {"title": "Your Agent Fabric's 52.2% Blind Spot", "url": "/stale-grants-travel-the-graph/"},
    {"title": "Your Signed MCP Tool Still Leaks: 3 of 3", "url": "/your-signed-tool-still-leaks-3-of-3/"},
]
html = W.md_to_html(new_text)
sb.update_body(row["id"], html, meta)
print("supabase body updated:", len(html), "chars html")

# --- 5. live post: HTML body, then status toggle -------------------------
out = wp(f"posts/{POST_ID}", {"content": html})
print("post content updated; modified", out.get("modified"))
wp(f"posts/{POST_ID}", {"status": "draft"})
back = wp(f"posts/{POST_ID}", {"status": "publish"})
print("status toggled ->", back.get("status"))

p = wp(f"posts/{POST_ID}?context=view", method="GET")
rendered = (p.get("content") or {}).get("rendered", "")
print("readback len", len(rendered),
      "| Related reading:", "Related reading" in rendered,
      "| old pick gone:", "your-783-silent-cap-breach" not in rendered,
      "| three curated:",
      all(s in rendered for s in ("your-tool-surface-is-a-release-surface",
                                  "stale-grants-travel-the-graph",
                                  "your-signed-tool-still-leaks-3-of-3")),
      "| earned link:", "durable-execution-not-a-transaction" in rendered)
