#!/usr/bin/env python3
"""One-off: reconcile the featured image's alt text for the 2026-11-09 agentic_ai evergreen.

The art director returned an alt with the house overlay headline glued to the front
("Your Agent Recovers 8% Of Crashes. Disk drive bay ..."), which is readable in a
screen reader as a duplicate H1. Same repair class as 2026-11-06 and 2026-11-09 sibling
runs: sidecar, artifact, media record (read back) and the Supabase row must agree.
"""
import json
import pathlib
import sys

sys.path.insert(0, "scripts")
import wp_draft  # noqa: E402

ROOT = pathlib.Path("/root/editorial-factory")
SLUG = "your-agent-recovers-8-of-crashes"
NEW_ALT = ("A hot-swap drive bay pulled halfway out of a server rack, its status light "
           "glowing amber in a dark data hall.")
MEDIA_ID = 1573
ROW_ID = "250cc8c9-cbd4-4e05-a564-965d0654251d"

sidecar = ROOT / "context/assets/illustrations" / SLUG / "featured.json"
rec = json.loads(sidecar.read_text())
print("old alt:", rec["alt_text"])
rec["alt_text"] = NEW_ALT
sidecar.write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n")

art = ROOT / "published" / f"2026-11-09_{SLUG}.md"
t = art.read_text()
old_line = next(l for l in t.splitlines() if l.startswith("image_alt:"))
t = t.replace(old_line, f'image_alt: "{NEW_ALT}"')
art.write_text(t)
print("artifact:", [l for l in t.splitlines() if l.startswith("image_alt:")][0])

wp_draft.load_env()
user, password = wp_draft.credentials_for("aichieve.net")
wp = wp_draft.WordPress("https://cms.giniloh.com", user, password)
item = wp.update_media(MEDIA_ID, {"alt_text": NEW_ALT})
back = wp.media(MEDIA_ID)
print("media alt read back:", (back or {}).get("alt_text"))
assert (back or {}).get("alt_text") == NEW_ALT

url, key = wp_draft.supabase_config()
sb = wp_draft.Supabase(url, key)
rows = sb.get(f"articles?id=eq.{ROW_ID}&select=id,metadata") if hasattr(sb, "get") else None
status, rows = sb._call("GET", f"articles?id=eq.{ROW_ID}&select=id,metadata")
row = (rows or [{}])[0]
meta = row.get("metadata") or {}
meta.setdefault("illustration", {})["alt_text"] = NEW_ALT
meta.setdefault("wordpress", {})["media_alt"] = NEW_ALT
sb._call("PATCH", f"articles?id=eq.{ROW_ID}", {"metadata": meta})
_, check = sb._call("GET", f"articles?id=eq.{ROW_ID}&select=metadata")
m = (check or [{}])[0].get("metadata") or {}
print("row alt:", (m.get("illustration") or {}).get("alt_text"))
