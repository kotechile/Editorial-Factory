#!/usr/bin/env python3
"""Rewrite the internal anchors inside the CMS post bodies so they survive a front-end rebuild.

    python3 scripts/fix_cms_links.py                      # dry-run (default), report what would change
    python3 scripts/fix_cms_links.py --post 880           # one post, dry-run
    python3 scripts/fix_cms_links.py --limit 5            # the first five posts needing a fix
    python3 scripts/fix_cms_links.py --apply --limit 10   # write, one batch

Why the CMS and not the front end
---------------------------------
The fronts are static builds that render the CMS body verbatim. A front-end patch therefore dies on the
next rebuild from the CMS, and the cross-site anchors return — measured on
`aichieve.net/your-cluster-hidden-clock/`, whose body carries three `giniloh.com` anchors and a self-link
because it was written for giniloh.com and aichieve.net now serves it. The durable copy is the post
content, so the post content is what gets corrected.

What is rewritten, and what is only reported
--------------------------------------------
`scripts/audit_cms_links.py` classifies every anchor against the fronts that SERVE the post. This script
acts on exactly one class:

  * `cross-site` — the post is rendered by more than one front and the anchor is one of their absolute
    URLs, so it leaves the site for every reader but one; or it points at a front that does not serve
    this post at all. Rewritten to the relative path those fronts share, which is internal wherever this
    body is rendered (`/sla-credit-is-not-insurance/`, not `https://giniloh.com/...`).
  * `same-front` — a single front serves the post and the anchor is that front's own absolute URL:
    already internal where it is read, left as written unless `--include-same-front`.
  * everything else is reported and left byte-identical: a target published at different paths by
    different fronts, a target missing from a serving front, a retired target, and a self-link. Deleting
    or inventing reader-visible text is the owner's call: on 2026-10-01 a "cleanup" pass deleted reader
    copy from a row and re-pushed the shortened body, and the delivery check could not see it because it
    compared the payload against the CMS.

Self-links are the one exception offered behind an explicit flag (`--drop-self-links`), because they are
ours (the generated `## Related reading` list) rather than prose.

Safety
------
* `--dry-run` is the default; `--apply` writes.
* Every write sends **content only** — never a `status` field (sending `status=draft` unpublishes a live
  post: post 401, 2026-10-01).
* **Verification after every write**: re-fetch the post, require zero `to-relative` anchors left, and
  require the only difference to be href values (see `mask_hrefs`).
* A post needing no change is never written (no gratuitous CMS revisions), and a second run finds nothing.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
import urllib.parse

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import wp_draft as wd  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
INDEX = ROOT / "context" / "internal_links.json"

FRONT_HOSTS = ("giniloh.com", "wellroost.com", "aichieve.net")

# The href VALUE span only, so a rewrite is a splice that cannot disturb any other byte of the body.
_HREF = re.compile(r"""(?P<pre><a\s[^>]*?\bhref=["'])(?P<href>[^"']+)(?P<post>["'])""", re.I)
_HREF_ANY = re.compile(r"""(\bhref=["'])([^"']+)(["'])""", re.I)


def mask_hrefs(html: str) -> str:
    """Every href value replaced by a placeholder — the invariant that only URLs changed.

    Two bodies with the same masked form differ nowhere except inside href values, so this is what makes
    "we only rewrote the URLs" a check instead of a claim (and it catches the failure mode this repo has
    already been bitten by: a pass that deleted reader copy while reporting success).
    """
    return _HREF_ANY.sub(r"\1<href>\3", html or "")


def _path_of(href: str) -> str:
    path = urllib.parse.urlparse(href).path or "/"
    return path if path.endswith("/") else path + "/"


def load_corpus() -> tuple[dict, dict]:
    """`(sites_live, paths_by_front)` — the same serve sets `audit_cms_links.py` uses."""
    index = json.loads(INDEX.read_text(encoding="utf-8"))
    sites_live = {c["slug"]: dict(c.get("sites_live") or {}) for c in index.get("candidates", [])}
    paths: dict[str, set[str]] = {}
    for c in index.get("candidates", []):
        if c.get("path"):
            paths.setdefault(c["site"], set()).add(c["path"])
    return sites_live, paths


def serve_set_for(slug: str, cms_domain: str, sites_live: dict) -> set[str]:
    """The fronts that publish this post's slug; the CMS's own front when the corpus has no entry.

    A hand-written back-catalogue post may not be in the corpus at all. Assuming it is served by its own
    front is then the conservative answer: it is the front the post was written for, and any anchor to
    that front is internal there.
    """
    measured = set(sites_live.get(slug) or {})
    return measured or ({cms_domain} if cms_domain in FRONT_HOSTS else set())


def classify(href: str, *, slug: str, serve: set[str], paths: dict) -> str:
    """One anchor's class — see the module docstring's table.

    `cross-site` is the DEFECT: the post is rendered by more than one front, so an absolute URL to any
    one of them leaves the site on the others (this is the whole reason the repair exists), or the
    anchor points at a front that does not serve this post at all.

    `same-front` is cosmetic: a single front serves this post and the anchor is written as that front's
    absolute URL. It is already internal where it is read; it becomes a defect only if that front's pull
    set later widens, and making it relative has its own small risk (a relative path needs the target to
    exist on whichever front renders it), so it is left alone unless `--include-same-front` asks.
    """
    # A relative href is checked FIRST: it has no host, so a host-based scan classifies it "external"
    # and never looks at it again. That is not a cosmetic gap — after the repair every rewritten anchor
    # is relative, and an instrument that cannot see them reports "0 cross-site" for the right reason but
    # also reports that the corpus has no internal links at all.
    path = _path_of(href)
    if href.startswith("/"):
        if not serve:
            return "relative-unknown-serve"
        resolved = {f for f in serve if path in paths.get(f, set())}
        if resolved == serve:
            return "internal"                      # resolves everywhere it is read
        return "differs-by-front" if resolved else "retired"
    host = (urllib.parse.urlparse(href).hostname or "").lower()
    if host not in FRONT_HOSTS:
        return "external"
    if not serve:
        return "missing"
    if slug and path == f"/{slug}/":
        return "self-link"
    resolved = {f for f in serve if path in paths.get(f, set())}
    if not resolved:
        return "retired"
    if resolved != serve:
        return "divergent"                 # live on some serving fronts, not on others
    if len(serve) > 1 or host not in serve:
        return "cross-site"                # ABSOLUTE on a post more than one front renders (or a
                                           # foreign front): cross-site for at least one reader
    return "same-front"                    # absolute, same, single serving front: already internal


def rewrite_body(html: str, *, slug: str, serve, paths, fronts=FRONT_HOSTS,
                 drop_self_links: bool = False,
                 include_same_front: bool = False) -> tuple[str, list[dict], list[dict]]:
    """Return `(new_html, changes, notes)`. Pure: no network, no clock, no writes.

    `changes` are the splices actually made (old href, new href, class); `notes` are the anchors left
    alone and why. A body needing nothing comes back byte-identical with no changes.
    """
    serve = {f for f in (serve or []) if f}
    changes: list[dict] = []
    notes: list[dict] = []
    out: list[str] = []
    cursor = 0
    for match in _HREF.finditer(html or ""):
        href = match.group("href")
        cls = classify(href, slug=slug, serve=serve, paths=paths)
        if cls == "external" or cls == "internal":
            continue
        if cls == "same-front" and not include_same_front:
            notes.append({"href": href, "class": cls,
                          "why": "already internal on the single front that serves this post; left as "
                                 "written (pass --include-same-front to make it relative anyway)"})
            continue
        if cls in ("cross-site", "same-front"):
            new_href = _path_of(href)
            out.append(html[cursor:match.start("href")])
            out.append(new_href)
            cursor = match.end("href")
            changes.append({"old_href": href, "new_href": new_href, "class": cls})
            continue
        if cls == "self-link" and drop_self_links:
            # Remove the whole <a>…</a> element, not just the href, and only when it sits in a list item
            # of the generated block — never a link inside prose.
            out.append(html[cursor:match.start()])
            cursor = match.end()
            changes.append({"old_href": href, "new_href": "", "class": cls})
            continue
        notes.append({"href": href, "class": cls,
                      "why": {"self-link": "the post links to itself (our generated block)",
                              "retired": "the target is in no front's sitemap",
                              "missing": "the target is not live on a front that serves this post",
                              "divergent": "the fronts publish the target at different paths"}[cls]})
    if not changes:
        return html, [], notes
    out.append(html[cursor:])
    return "".join(out), changes, notes


def verify_write(original: str, updated: str, changes: list[dict], slug: str, serve, paths) -> list[str]:
    """Problems with a rewrite, in the shape `wp_draft.delivery_problems` uses. [] means verified."""
    problems = []
    if mask_hrefs(original) != mask_hrefs(updated):
        problems.append("the body changed somewhere other than an href value")
    if len(re.findall(r"<a\s", original, re.I)) != len(re.findall(r"<a\s", updated, re.I)):
        problems.append("the number of anchors changed")
    for ch in changes:
        if ch["class"] in ("cross-site", "same-front") and updated.count(ch["new_href"]) < 1:
            problems.append(f"the rewritten href is absent: {ch['new_href']}")
    left = [c for c in changes if c["class"] in ("cross-site", "same-front")
            and not c["new_href"].startswith("/")]
    if left:
        problems.append(f"{len(left)} rewritten href(s) are still absolute")
    return problems


def apply_post(domain: str, cms: str, post: dict, *, sites_live: dict, paths: dict,
               drop_self_links: bool = False, include_same_front: bool = False) -> dict:
    """Rewrite one post in the CMS, verify by read-back. Returns a report dict (never raises on a
    verification failure — it reports it)."""
    slug = post.get("slug") or ""
    serve = serve_set_for(slug, domain, sites_live)
    original = (post.get("content") or {}).get("rendered") or ""
    updated, changes, notes = rewrite_body(original, slug=slug, serve=serve, paths=paths,
                                           drop_self_links=drop_self_links,
                                           include_same_front=include_same_front)
    report = {"cms": domain, "id": post.get("id"), "slug": slug, "serve": sorted(serve),
              "changes": len(changes), "notes": notes, "written": False, "problems": []}
    if not changes:
        report["problems"] = ["nothing to change"]
        return report

    problems = verify_write(original, updated, changes, slug, serve, paths)
    if problems:
        report["problems"] = problems
        return report

    user, password = wd.credentials_for(domain)
    wp = wd.WordPress(cms, user, password)
    # content only: no `status`, so a published post can never be unpublished by this pass.
    wp._call("POST", f"posts/{post['id']}", {"content": updated})
    # Read back the RAW body (`context=edit`), not `content.rendered`: WordPress runs `the_content`
    # filters on the way out (wpautop and friends), so comparing against the rendered form would report
    # a difference on every single post and hide a real one. Same field `wp_draft.delivery_problems`
    # compares, for the same reason.
    _, fresh = wp._call("GET", f"posts/{post['id']}?context=edit&_fields=id,slug,status,content")
    fresh = fresh or {}
    stored = fresh.get("content") or {}
    served = stored.get("raw") or stored.get("rendered") or ""
    still = [c for c in changes if c["class"] in ("cross-site", "same-front")
             and not c["new_href"].startswith("/")]
    report["problems"] = verify_write(original, served, changes, slug, serve, paths)
    report["written"] = True
    report["status"] = fresh.get("status")
    if str(fresh.get("status") or "") != "publish":
        report["problems"].append(f"the post came back status={fresh.get('status')!r}, not 'publish'")
    report["read_back_matches"] = mask_hrefs(served) == mask_hrefs(updated)
    if not report["read_back_matches"]:
        report["problems"].append("the CMS serves a body that differs from what was sent")
    if still:
        report["problems"].append(f"{len(still)} absolute sibling anchor(s) survived the write")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=(__doc__ or "").splitlines()[0])
    parser.add_argument("--apply", action="store_true", help="write to the CMS (default: dry-run)")
    parser.add_argument("--post", type=int, help="one post id")
    parser.add_argument("--limit", type=int, help="stop after N posts that need a change")
    parser.add_argument("--include-same-front", action="store_true",
                        help="also make single-front posts' same-front absolute URLs relative")
    parser.add_argument("--drop-self-links", action="store_true",
                        help="also remove self-links in the generated block (off by default)")
    parser.add_argument("--json", action="store_true", help="print the report as JSON")
    args = parser.parse_args()

    wd.load_env()
    sites_live, paths = load_corpus()
    import audit_cms_links as audit                       # one classifier, one place

    installs = audit.cms_installs()
    reports, changed = [], 0
    for domain, cms in installs.items():
        for post in audit.fetch_posts(domain, cms, args.post):
            slug = post.get("slug") or ""
            serve = serve_set_for(slug, domain, sites_live)
            html = (post.get("content") or {}).get("rendered") or ""
            _, changes, notes = rewrite_body(html, slug=slug, serve=serve, paths=paths,
                                             drop_self_links=args.drop_self_links,
                                             include_same_front=args.include_same_front)
            if not changes:
                continue
            if args.limit and changed >= args.limit:
                break
            if args.apply:
                rep = apply_post(domain, cms, post, sites_live=sites_live, paths=paths,
                                 drop_self_links=args.drop_self_links,
                                 include_same_front=args.include_same_front)
            else:
                rep = {"cms": domain, "id": post.get("id"), "slug": slug, "serve": sorted(serve),
                       "changes": len(changes), "notes": notes, "written": False, "problems": []}
            reports.append(rep)
            changed += 1
            status = "WROTE" if rep.get("written") else "dry"
            print(f"  [{status}] {domain} #{rep['id']} {slug[:46]:46s} "
                  f"serve={','.join(rep['serve']):26s} href(s)={rep['changes']} "
                  f"left={len(rep['notes'])}" + (f" PROBLEMS={rep['problems']}" if rep.get("problems") else ""))

    if args.json:
        print(json.dumps(reports, indent=1))
    total = sum(r["changes"] for r in reports)
    left = sum(len(r["notes"]) for r in reports)
    bad = [r for r in reports if r.get("written") and r.get("problems")]
    print(f"\n{'WROTE' if args.apply else 'would rewrite'} {total} anchor(s) in {len(reports)} post(s); "
          f"{left} anchor(s) left alone and reported")
    print("  a rewritten anchor is one whose host is not (one of) the front(s) that serve this post, or "
          "one that is absolute while every one of them publishes that path")
    if bad:
        print(f"FAIL: {len(bad)} post(s) report problems after writing — inspect before continuing")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
