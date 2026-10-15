#!/usr/bin/env python3
"""Tests for the CMS link rewriter — run: python3 scripts/test_fix_cms_links.py

Hermetic: every body is an inline fixture (shaped like the real post bodies, which are HTML with the
generated `## Related reading` block rendered as `<h2>` + `<ul>`), no CMS, no network, no writes.

The rules under test decide whether a reader on aichieve.net gets a link that stays on aichieve.net after
the next front-end rebuild — and, just as important, whether the repair can damage anything else in the
body while doing it.
"""

from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import fix_cms_links as fx  # noqa: E402

PASS, FAIL = [], []


def check(name, condition, detail=""):
    (PASS if condition else FAIL).append(name)
    print(f"  [{'ok ' if condition else 'FAIL'}] {name}" + ("" if condition else f"  <- {detail}"))


# Two fronts publish the same article corpus at root-level paths; giniloh publishes its tools under
# /calculators/<slug>/ and aichieve under /tools/<slug>/ — the disagreement that cannot be stamped.
PATHS = {
    "giniloh.com": {"/sla-credit-is-not-insurance/", "/wage-floor-sets-robot-payback/",
                    "/calculators/gpu-compute/", "/categories/supply-chain-operations/"},
    "aichieve.net": {"/sla-credit-is-not-insurance/", "/wage-floor-sets-robot-payback/",
                     "/tools/gpu-compute/", "/categories/supply-chain-operations/"},
    "wellroost.com": {"/battery-payback-five-state-gap/"},
}

BODY = """<p>Lead paragraph with a <a href="https://giniloh.com/sla-credit-is-not-insurance/">SLA credit</a> reference.</p>
<h2>The Strategy Brief</h2>
<ul><li>Point one.</li></ul>
<h2>Related reading</h2>
<ul>
<li><a href="https://giniloh.com/wage-floor-sets-robot-payback/">$17.00 Warehouse Payback</a></li>
<li><a href="/categories/supply-chain-operations/">Supply Chain &amp; Operations</a></li>
<li><a href="https://giniloh.com/calculators/gpu-compute/">GPU Compute Calculator</a></li>
<li><a href="https://giniloh.com/a-page-that-no-front-serves/">Retired Target</a></li>
<li><a href="https://giniloh.com/your-cluster-hidden-clock/">Your Cluster's Hidden Clock</a></li>
</ul>
<p>Trailing prose that must not move, with an <a href="https://example.com/x">external link</a>.</p>
"""

print("one article, two fronts serving it")
out, changes, notes = fx.rewrite_body(BODY, slug="your-cluster-hidden-clock",
                                      serve={"giniloh.com", "aichieve.net"}, paths=PATHS)
urls = {c["old_href"]: c["new_href"] for c in changes}
check("an article link shared by both fronts becomes the relative path",
      urls.get("https://giniloh.com/sla-credit-is-not-insurance/") == "/sla-credit-is-not-insurance/",
      str(changes))
check("...and so does the one in the generated block",
      urls.get("https://giniloh.com/wage-floor-sets-robot-payback/") == "/wage-floor-sets-robot-payback/")
check("an absolute URL to the article's own page is NOT rewritten (a self-link is not a link fix)",
      "https://giniloh.com/your-cluster-hidden-clock/" not in urls, str(urls))
check("...and it is reported as what it is",
      any(n["class"] == "self-link" for n in notes), str(notes))
check("a relative anchor that already resolves is left alone",
      '<a href="/categories/supply-chain-operations/">' in out, out)
check("a tool published at different paths is left and reported",
      "https://giniloh.com/calculators/gpu-compute/" in out
      and any(n["class"] == "divergent" for n in notes), str(notes))
check("a target no front serves is left and reported",
      "https://giniloh.com/a-page-that-no-front-serves/" in out
      and any(n["class"] == "retired" for n in notes), str(notes))
check("an external link is untouched", '<a href="https://example.com/x">' in out)

print("\nthe invariant that makes this safe")
check("ONLY href values changed: masking every href restores the original exactly",
      fx.mask_hrefs(out) == fx.mask_hrefs(BODY))
check("the number of anchors is unchanged",
      len(fx._HREF.findall(out)) == len(fx._HREF.findall(BODY)))
check("no reader copy was added or removed (masked bodies are byte-identical)",
      fx.mask_hrefs(out) == fx.mask_hrefs(BODY) and len(out) < len(BODY))
check("the rewrite is idempotent: a second pass finds nothing to change",
      fx.rewrite_body(out, slug="your-cluster-hidden-clock",
                      serve={"giniloh.com", "aichieve.net"}, paths=PATHS)[1] == [],
      str(fx.rewrite_body(out, slug="your-cluster-hidden-clock",
                          serve={"giniloh.com", "aichieve.net"}, paths=PATHS)[1]))

print("\nthe case the repair exists for: a giniloh.com post that only aichieve.net now serves")
moved, moved_changes, moved_notes = fx.rewrite_body(BODY, slug="your-cluster-hidden-clock",
                                                    serve={"aichieve.net"}, paths=PATHS)
check("its giniloh.com anchors are cross-site THERE, so they are rewritten",
      {c["old_href"]: c["new_href"] for c in moved_changes}.get(
          "https://giniloh.com/sla-credit-is-not-insurance/") == "/sla-credit-is-not-insurance/"
      and all(c["class"] == "cross-site" for c in moved_changes), str(moved_changes))
check("...while a target aichieve does not publish is left and reported, never guessed",
      "https://giniloh.com/a-page-that-no-front-serves/" in moved
      and any(n["class"] == "retired" for n in moved_notes), str(moved_notes))

print("\nwhen only one front serves the article, and it IS the anchor's own front")
one, one_changes, one_notes = fx.rewrite_body(BODY, slug="your-cluster-hidden-clock",
                                              serve={"giniloh.com"}, paths=PATHS)
check("a giniloh.com post served only by giniloh.com is left alone: those links are already internal",
      one == BODY and one_changes == [], str(one_changes))
check("...and every one of them is reported as same-front, not silently dropped",
      len([n for n in one_notes if n["class"] == "same-front"]) == 3, str(one_notes))
opt, opt_changes, _ = fx.rewrite_body(BODY, slug="your-cluster-hidden-clock", serve={"giniloh.com"},
                                      paths=PATHS, include_same_front=True)
check("--include-same-front makes them relative as well, for a deliberate wider pass",
      'href="/sla-credit-is-not-insurance/"' in opt
      and all(c["class"] == "same-front" for c in opt_changes) and opt_changes, str(opt_changes))

print("\nwhen the corpus has no entry for the post (a hand-written back-catalogue piece)")
none, none_changes, none_notes = fx.rewrite_body(BODY, slug="a-hand-written-piece",
                                                 serve={"giniloh.com"}, paths=PATHS)
check("nothing is guessed: with one serving front, its own absolute URLs are left and reported",
      none_changes == [] and any(n["class"] == "same-front" for n in none_notes), str(none_notes))
check("...and a target that front does not publish is reported as retired, never dropped",
      none.count("a-page-that-no-front-serves") == 1 and any(n["class"] == "retired" for n in none_notes),
      str(none_notes))
check("...so the pass is a no-op for a post whose links are already internal",
      none == BODY)

print("\nself-links are only removed when explicitly asked")
no_self, self_changes, _ = fx.rewrite_body(
    '<ul><li><a href="https://giniloh.com/your-cluster-hidden-clock/">Self</a></li></ul>',
    slug="your-cluster-hidden-clock", serve={"giniloh.com", "aichieve.net"}, paths=PATHS)
check("by default a self-link is left in place (reader copy is the owner's call)",
      "your-cluster-hidden-clock" in no_self, no_self)
dropped, dropped_changes, _ = fx.rewrite_body(
    '<ul><li><a href="https://giniloh.com/your-cluster-hidden-clock/">Self</a></li></ul>',
    slug="your-cluster-hidden-clock", serve={"giniloh.com", "aichieve.net"}, paths=PATHS,
    drop_self_links=True)
check("...and with --drop-self-links the anchor goes",
      "your-cluster-hidden-clock" not in dropped and any(c["class"] == "self-link" for c in dropped_changes),
      dropped)

print("\nverification refuses a body it cannot vouch for")
_ok, ch, _ = fx.rewrite_body(BODY, slug="your-cluster-hidden-clock",
                             serve={"giniloh.com", "aichieve.net"}, paths=PATHS)
check("a correct rewrite verifies clean",
      fx.verify_write(BODY, out, ch, "your-cluster-hidden-clock",
                      {"giniloh.com", "aichieve.net"}, PATHS) == [],
      str(fx.verify_write(BODY, out, ch, "your-cluster-hidden-clock",
                          {"giniloh.com", "aichieve.net"}, PATHS)))
check("a body that lost reader copy is caught",
      any("somewhere other than an href" in p for p in
          fx.verify_write(BODY, BODY.replace("<li>Point one.</li>", ""), ch, "x",
                          {"giniloh.com"}, PATHS)))
check("a body that gained an anchor is caught",
      any("number of anchors" in p for p in
          fx.verify_write(BODY, BODY + '<a href="/x/">x</a>', ch, "x", {"giniloh.com"}, PATHS)))
check("a rewrite that left an absolute sibling anchor is caught",
      any("still absolute" in p for p in
          fx.verify_write(BODY, BODY, [{"old_href": "https://giniloh.com/sla-credit-is-not-insurance/",
                                        "new_href": "https://giniloh.com/wage-floor-sets-robot-payback/",
                                        "class": "cross-site"}],
                          "some-other-article", {"giniloh.com", "aichieve.net"}, PATHS)))

print(f"\n{len(PASS)} passed, {len(FAIL)} failed")
for name in FAIL:
    print(f"  FAILED: {name}")
raise SystemExit(1 if FAIL else 0)
