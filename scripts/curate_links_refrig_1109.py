#!/usr/bin/env python3
"""Curate the Related-reading block and fix the header alt/caption for
your-condensers-repair-bill-2090-vs-700 (rule 12: >=2 shared subject tokens per link).

Writes the artifact, the Supabase row and the live CMS post (post 383, media 382).
"""
import json, os, re, sys, urllib.request, base64, pathlib

sys.path.insert(0, "/root/editorial-factory/scripts")
ROOT = pathlib.Path("/root/editorial-factory")
for line in (ROOT / ".env").read_text().splitlines():
    if "=" in line and not line.strip().startswith("#"):
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"'))

import wp_draft as wd

SLUG = "your-condensers-repair-bill-2090-vs-700"
ART = ROOT / f"published/2026-11-09_{SLUG}.md"

ALT = ("Two isometric cutaway views of residential air conditioner condensers on concrete pads, "
       "each showing its copper coil and expansion valves beside a refrigerant cylinder.")
CAPTION = ("The gas named on the bid, not the efficiency rating beside it, sets what the next "
           "decade of that system costs.")

BLOCK = """<!-- internal-links -->

<!-- internal-links:start — curated for this article (rule 12: at least two shared subject tokens per link) -->
## Related reading

- [20% of Your AC Never Arrives](/20-percent-of-your-ac-never-arrives/) — the factory efficiency rating measured against the ducts that deliver it
- [Your Tank's Class Costs $55](/you-are-pricing-the-fuel-not-the-tank/) — the equipment class, not the fuel, sets the running bill
- [Heat Pumps Just Got Cheaper to Run](/heat-pumps-cheaper-to-run-pricier-to-buy/) — running cost measured against equipment-price inflation
<!-- internal-links:end -->"""

text = ART.read_text()
start = text.index("<!-- internal-links -->")
end = text.index("## Sources")
text = text[:start] + BLOCK + "\n\n" + text[end:]
text = re.sub(r'^image_alt: ".*"$', 'image_alt: "%s"' % ALT, text, count=1, flags=re.M)
text = re.sub(r'^image_caption: ".*"$', 'image_caption: "%s"' % CAPTION, text, count=1, flags=re.M)
ART.write_text(text)
print("artifact written:", len(text))

# --- Supabase row: body + metadata
url = os.environ["SUPABASE_URL"].rstrip("/")
key = os.environ["SUPABASE_SERVICE_ROLE_KEY"]
H = {"apikey": key, "Authorization": f"Bearer {key}", "Content-Type": "application/json"}


def sb(path, method="GET", body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url + path, data=data, headers=H, method=method)
    with urllib.request.urlopen(req) as r:
        raw = r.read()
        return json.loads(raw) if raw else None


row = sb(f"/rest/v1/articles?slug=eq.{SLUG}&select=id,content,metadata")[0]
meta = row["metadata"]
meta["illustration"]["alt_text"] = ALT
meta["illustration"]["caption"] = CAPTION
meta["wordpress"]["media_alt"] = ALT
meta["wordpress"]["media_caption"] = CAPTION
meta["internal_links"] = {
    "urls": [
        "https://wellroost.com/20-percent-of-your-ac-never-arrives/",
        "https://wellroost.com/you-are-pricing-the-fuel-not-the-tank/",
        "https://wellroost.com/heat-pumps-cheaper-to-run-pricier-to-buy/",
    ],
    "anchors": [
        "20% of Your AC Never Arrives",
        "Your Tank's Class Costs $55",
        "Heat Pumps Just Got Cheaper to Run",
    ],
    "count": 3,
    "source": "curated:by-hand",
    "note": "generated block justified two links on a single incidental token ('bill', 'prices'); curated to pages sharing >=2 subject tokens and probed 200 on wellroost.com",
}
sb(f"/rest/v1/articles?id=eq.{row['id']}", "PATCH",
   {"content": text, "metadata": meta})
print("supabase row patched:", row["id"])

# --- WordPress: media alt/caption, then the live body
user, pw = wd.credentials_for("wellroost.com")
base = "https://cms.wellroost.com/wp-json/wp/v2"
auth = "Basic " + base64.b64encode(f"{user}:{pw}".encode()).decode()


def wp(path, method="POST", body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(base + path, data=data, method=method,
                                 headers={"Authorization": auth, "Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())


media = wp("/media/382", "POST", {"alt_text": ALT, "caption": CAPTION})
print("media alt now:", media.get("alt_text"))

html = wd.md_to_html(wd.reader_markdown(text))
post = wp("/posts/383", "POST", {"content": html})
body = post["content"]["rendered"]
print("post status:", post.get("status"), "| chars:", len(body),
      "| alt echoed:", ALT[:40] in body)
print("related links in body:",
      all(p in body for p in ("/20-percent-of-your-ac-never-arrives/",
                              "/you-are-pricing-the-fuel-not-the-tank/",
                              "/heat-pumps-cheaper-to-run-pricier-to-buy/")))
print("old bad link present:", "heat-pumps-just-got-cheaper-to-run-and-pricier-to-buy" in body)
print("featured_media:", post.get("featured_media"), "| vertical term check:", post.get("vertical"))
