#!/usr/bin/env python3
"""Repair pass for 2026-11-18 your-fleets-8-3-year-bill (warehouse_automation_robotics_capex).

The art director's alt arrived as the overlay headline glued to a clipped phrase with a broken
capital ("Your Fleet'S …") and two sentences. Reconcile one sentence across the sidecar, both
artifacts, media 1784 and the Supabase row. Body untouched, so no status toggle.
"""
import base64
import json
import sys
import urllib.request

sys.path.insert(0, "scripts")
import wp_draft as W

SLUG = "your-fleets-8-3-year-bill"
ARTIFACT = f"published/2026-11-18_{SLUG}.md"
FINAL = f"context/drafts/2026-11-18_{SLUG}_final.md"
SIDE = f"context/assets/illustrations/{SLUG}/featured.json"
MEDIA = 1784
SITE = "aichieve.net"
CMS = "cms.giniloh.com"

ALT = ("A fleet of identical autonomous mobile robots stands in a warehouse aisle beside a blank "
       "invoice held by a steel rack.")

print("alt length:", len(ALT))

side = json.loads(open(SIDE, encoding="utf-8").read())
side["alt_text"] = ALT
side["revision"] = int(side.get("revision", 1)) + 1
open(SIDE, "w", encoding="utf-8").write(json.dumps(side, indent=2, ensure_ascii=False) + "\n")
print("sidecar alt ->", side["alt_text"][:60], "revision", side["revision"])

for path in (ARTIFACT, FINAL):
    lines = open(path, encoding="utf-8").read().splitlines(keepends=True)
    for i, line in enumerate(lines):
        if line.startswith("image_alt:"):
            lines[i] = f'image_alt: "{ALT}"\n'
    open(path, "w", encoding="utf-8").write("".join(lines))
    print("artifact patched:", path)

W.load_env()
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

url, key = W.supabase_config()
sb = W.Supabase(url, key)
row = sb.articles(slug=SLUG)[0]
meta = row.get("metadata") or {}
meta.setdefault("illustration", {})["alt_text"] = ALT
meta.setdefault("wordpress", {})["media_alt"] = ALT
ill = dict(meta.get("illustration") or {})
ill["alt_text"] = ALT
sb.record_illustration(row["id"], meta, ill)
print("supabase illustration alt ->", ill["alt_text"])
