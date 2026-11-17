"""Curate the generated Related-reading block for your-approval-gate-kills-20 and write it to
the artifact, the Supabase row and the live CMS post (rule 12: the generator qualified two pages on
a single incidental token — "wrong", "approval" — which is not evidence)."""
import sys

sys.path.insert(0, "scripts")
import wp_draft as W

SLUG = "your-approval-gate-kills-20"
ART = f"published/2026-11-17_{SLUG}.md"
SITE = "aichieve.net"
KEEP = "/the-cloud-bill-break-even-when-renting-servers-stops-paying/"
DROP = ("/agent-identity-missed-the-real-breach/", "/kill-switch-misses-half-your-agents/")
ADD = [
    ("Your AI Bill Grew 1.65%", "/your-ai-bill-grew-165-you-cut-the-work/",
     "the same bill read from the finance side"),
    ("Your $200 Cap Still Buys 2.85x", "/your-200-cap-still-buys-2-85x/",
     "a daily AI budget written in a falling unit"),
]

lines = open(ART).read().splitlines()
out, in_block, rebuilt = [], False, False
for ln in lines:
    if ln.startswith("<!-- internal-links:start"):
        in_block = True
        out.append(ln)
        continue
    if in_block and ln.startswith("<!-- internal-links:end"):
        for title, url, why in ADD:
            out.append(f"- [{title}]({url}) — {why}")
        kept = [x for x in out if x.startswith("- [") and KEEP in x]
        out.remove(kept[0])
        out.append(kept[0])
        out.append(ln)
        in_block = False
        rebuilt = True
        continue
    if in_block:
        if ln.startswith("<!-- internal-link hint:"):
            continue                      # the hints describe the picks being replaced
        if ln.startswith("- [") and any(d in ln for d in DROP):
            continue
        if ln.strip() == "" and out and out[-1].strip() == "":
            continue
        out.append(ln)
        continue
    out.append(ln)

assert rebuilt, "related block not found"
md = "\n".join(out) + "\n"
open(ART, "w").write(md)
print("artifact block:")
print("\n".join(l for l in out if l.startswith("- [")))

W.load_env()
url, key = W.supabase_config()
sb = W.Supabase(url, key)
row = sb.articles(slug=SLUG)[0]
meta = row.get("metadata") or {}
sb._call("PATCH", f"{W.ARTICLES_TABLE}?id=eq.{row['id']}", {"content": md})
print("supabase row updated", row["id"])

user, pwd = W.credentials_for(SITE)
wp = W.WordPress("https://cms.giniloh.com", user, pwd)
html = W.md_to_html(md)
post_id = (meta.get("wordpress") or {}).get("post_id") or 1738
wp._call("POST", f"posts/{int(post_id)}", {"content": html})
print("cms post updated", post_id, len(html), "chars")
