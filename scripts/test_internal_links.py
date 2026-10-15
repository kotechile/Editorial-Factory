#!/usr/bin/env python3
"""Tests for internal linking — run: python3 scripts/test_internal_links.py

Hermetic: the candidate index is a fixture in a temp file and no site is contacted. The last section
inspects the real context/internal_links.json when one has been built, without fetching anything.

The rules under test are the ones that decide whether a reader gets a useful link or a broken one:
  * only pages that are live on the SAME site (both Astro fronts answer 200 with the homepage for an
    unknown URL, so a link to a page that is not live silently sends the reader home);
  * never the article itself;
  * never a page that shares only the domain — an irrelevant internal link dilutes the anchor and
    costs the reader's attention;
  * and the links must reach the published post as real <a href>, with the operator's placement
    hints left behind as comments.
"""

from __future__ import annotations

import json
import pathlib
import re
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_internal_link_index as bli  # noqa: E402
import frontends as fe  # noqa: E402
import growth_os as gos  # noqa: E402
import internal_links as il  # noqa: E402
import seo_machine as sm  # noqa: E402
import wp_draft as wd  # noqa: E402

PASS, FAIL = [], []


def check(name, condition, detail=""):
    (PASS if condition else FAIL).append(name)
    print(f"  [{'ok ' if condition else 'FAIL'}] {name}{'' if condition else f'  <- {detail}'}")


def article(site, slug, title, url, categories=(), category_ids=(), excerpt="", live=True, kind="article"):
    return {"site": site, "kind": kind, "id": 1, "slug": slug, "title": title, "url": url,
            "categories": list(categories), "category_ids": list(category_ids), "excerpt": excerpt,
            "modified": "2026-09-30T00:00:00", "live": live}


FIXTURE = {
    "generated_at": "2026-10-01T00:00:00+00:00",
    "site_source": "fixture",
    "sites": {"a.com": {"cms": "https://cms.a.com", "frontend": "https://a.com"},
              "b.com": {"cms": "https://cms.b.com", "frontend": "https://b.com"}},
    "categories": {"a.com": {"9": "Autonomous & Agentic Workflows"}},
    "candidates": [
        # Topical overlap, but this is the article being written — must never link to itself.
        article("a.com", "agent-routing-benchmarks", "The Agent Routing Benchmarks",
                "https://a.com/agent-routing-benchmarks/", ["Autonomous & Agentic Workflows"], [9],
                "routing benchmarks"),
        # Topical overlap, same site.
        article("a.com", "orchestration-cost", "Multi Agent Orchestration Cost Models",
                "https://a.com/orchestration-cost/", ["Autonomous & Agentic Workflows"], [9],
                "orchestration cost at scale"),
        # Same site, no overlap, different category — the relevance floor must reject it.
        article("a.com", "ai-proof-jobs", "Best AI Proof Jobs in a Changing Market",
                "https://a.com/ai-proof-jobs/", ["Career & AI Resilience"], [8], "career advice"),
        # Same site and same category but no word overlap — a valid category match.
        article("a.com", "quarterly-roundup", "Quarterly Telemetry Roundup",
                "https://a.com/quarterly-roundup/", ["Autonomous & Agentic Workflows"], [9], "quarterly"),
        # Right topic, wrong site: a cross-site link is not an internal link.
        article("b.com", "other-site-routing", "Agent Routing Benchmarks Explained",
                "https://b.com/other-site-routing/", [], [], "routing benchmarks"),
        # Published in the CMS but absent from the frontend sitemap.
        article("a.com", "not-live-yet", "Agent Routing Benchmarks Not Live",
                "https://a.com/not-live-yet/", [], [], "routing benchmarks", live=False),
        article("a.com", "routing-calculator", "Routing calculator",
                "https://a.com/calculators/routing/", [], [], "", kind="calculator"),
        # A calculator that shares TWO subject tokens: the evidence bar a mere topical match needs.
        article("a.com", "fleet-routing-calculator", "Routing Benchmarks Calculator",
                "https://a.com/calculators/fleet-routing/", [], [], "", kind="calculator"),
        # The destination's own category hub, live on the frontend.
        article("a.com", "autonomous-agentic-workflows", "Autonomous Agentic Workflows",
                "https://a.com/categories/autonomous-agentic-workflows/", [], [], "", kind="category"),
    ],
    "not_live": [],
}

_tmp = tempfile.TemporaryDirectory()
INDEX_FILE = pathlib.Path(_tmp.name) / "internal_links.json"
INDEX_FILE.write_text(json.dumps(FIXTURE), encoding="utf-8")

# Point the module at the fixture and pin the vertical's routing (no Supabase call in a test run).
gos.INTERNAL_LINK_INDEX = INDEX_FILE
gos._site_for_vertical = lambda vertical: ({"site_domain": "a.com", "frontend_url": "https://a.com",
                                           "wp_category_id": 9} if vertical else None)

print("candidate selection")
links = gos.generate_internal_link_map("agent routing benchmarks", "agentic_ai", max_links=5)
urls = [l["url"] for l in links]
check("links are proposed from the real corpus", bool(links), links)
check("an article is never linked to itself",
      "https://a.com/agent-routing-benchmarks/" not in urls, urls)
check("a cross-site page is never offered as an internal link",
      not any("b.com" in u for u in urls), urls)
check("a page that is not live is never offered",
      "https://a.com/not-live-yet/" not in urls, urls)
check("every offered link is https and absolute", all(u.startswith("https://") for u in urls), urls)
check("a same-site page with no topical overlap and no shared category is rejected",
      "https://a.com/ai-proof-jobs/" not in urls, urls)
short_token = gos.generate_internal_link_map("ai", "unrouted_vertical", max_links=5)
check("a match on a short token alone ('ai') is not enough to link",
      not any("ai-proof-jobs" in l["url"] for l in short_token),
      [l["url"] for l in short_token])
check("scores are ordered high to low",
      all(a["relevance_score"] >= b["relevance_score"] for a, b in zip(links, links[1:])),
      [l["relevance_score"] for l in links])

print("\ncategory and calculator matches")
cat_links = gos.generate_internal_link_map("agentic orchestration", "agentic_ai", max_links=5)
cat_urls = [l["url"] for l in cat_links]
check("a same-category page qualifies on the category alone",
      "https://a.com/quarterly-roundup/" in cat_urls, cat_urls)
check("...and says why", any("same category" in l["why"] for l in cat_links),
      [l["why"] for l in cat_links])
calc = gos.generate_internal_link_map("routing benchmarks", "agentic_ai", max_links=5)
check("a calculator is a valid target when it shares real subject matter",
      any(l["kind"] == "calculator" and "fleet-routing" in l["url"] for l in calc),
      [(l["kind"], l["url"]) for l in calc])
check("...but ONE shared word is not evidence, not even for a calculator (measured: a single "
      "'just'/'test'/'billion' was offering readers an unrelated article)",
      not any("calculators/routing/" in l["url"] for l in calc), str([l["url"] for l in calc]))
hub = gos.generate_internal_link_map("something the corpus says nothing about", "agentic_ai", max_links=5)
check("the article's own category hub is a valid target on a sparse corpus (it is the section the "
      "article will be listed on)",
      any(l["kind"] == "category" and l["url"].endswith("/categories/autonomous-agentic-workflows/")
          for l in hub), str(hub))
check("...and says why", any("own category hub" in l["why"] for l in hub), str([l["why"] for l in hub]))

print("\nanchor text and reader-facing rendering")
check("a leading stopword is trimmed from the anchor",
      gos._anchor_for({"title": "The Big Shift In Routing"}, set()) == "Big Shift In Routing",
      gos._anchor_for({"title": "The Big Shift In Routing"}, set()))
long_title = " ".join(f"word{i}" for i in range(1, 30))
long_anchor = gos._anchor_for({"title": long_title}, set())
check("a long title is trimmed at a word boundary, never mid-word",
      long_anchor.endswith("…") and all(w in long_title.split() for w in long_anchor.rstrip("…").split()),
      long_anchor)
check("a subtitle title anchors on its head phrase",
      gos._anchor_for({"title": "NY Heat Pump Rebate: Double Payouts for Sealed Homes"}, set())
      == "NY Heat Pump Rebate",
      gos._anchor_for({"title": "NY Heat Pump Rebate: Double Payouts for Sealed Homes"}, set()))
check("no links => no section (an empty heading is worse than none)",
      sm._format_related_reading([]) == "")
check("no links => the operator comment says so",
      sm._format_link_hints([]).startswith("<!--") and "none" in sm._format_link_hints([]))

related = sm._format_related_reading(links)
check("the section is a real markdown list of links",
      related.startswith("## Related reading") and related.count("- [") == len(links), related[:120])
check("the operator hints are comments, not prose",
      all(l.startswith("<!--") and l.endswith("-->") for l in sm._format_link_hints(links).splitlines()))

doc = f"""---
vertical: "agentic_ai"
---

## The Router Moves Upfront

Prose about routing.

{related}

## Sources
[1] METR — https://arxiv.org/abs/2503.14499

<!-- internal-links -->
{sm._format_link_hints(links)}
"""
reader = wd.reader_markdown(doc)
check("the operator hint never reaches the reader copy", "internal-link hint" not in reader)
check("...but the Related reading links do", "## Related reading" in reader)

html = wd.md_to_html(doc)
check("the links reach the post as real anchors", html.count("<a href=\"https://a.com/") == len(links),
      html.count("<a href=\"https://a.com/"))
check("the hint comments do not", "internal-link hint" not in html)
check("no operator notation leaks into the post",
      "Anchor:" not in html and "- **Anchor" not in html)

print("\nthe artifact pass — the block that reaches a destination")
ARTIFACT = """---
title: "The Router Moves Upfront"
vertical: "agentic_ai"
slug: "the-router-moves-upfront"
---

<!-- lead -->
Routing decisions used to be made per request, and the bill showed it. Three teams measured a
43% drop in token spend after moving the choice into the plan [1].

<!-- tension -->
## Why Now

The orchestration layer finally has the context to decide.

<!-- internal-links -->

<!-- tldr -->
## Key Takeaways

**The Big Shift:** the model choice moved into the plan.

<!-- linkedin -->
Internal variant, never reader-visible.

<!-- schema -->
```json
{"@context":"https://schema.org"}
```
"""
WRITTEN, notes, used = il.enrich(ARTIFACT, vertical="agentic_ai", links=links)
check("the block is written under the marker the drafting stage left",
      "<!-- internal-links -->" in WRITTEN
      and WRITTEN.index("## Related reading") > WRITTEN.index("<!-- internal-links -->"), WRITTEN[:200])
check("...as real markdown links, so the destination gets anchors", WRITTEN.count("- [") == len(links), WRITTEN)
check("...wrapped in the delimiters that make a re-run an update, not a second list",
      il.BLOCK_START in WRITTEN and il.BLOCK_END in WRITTEN)
check("...and the decision is reported, never silent", bool(notes), str(notes)[:200])
check("the hints are comments, so no reader ever sees them",
      all(l.startswith("<!--") and l.endswith("-->") for l in il.render_link_hints(links).splitlines()))
check("what was written can be read back (the same list)",
      [l["url"] for l in il.read_links(WRITTEN)] == urls, str(il.read_links(WRITTEN)))
check("the frontmatter survives untouched", WRITTEN.startswith('---\ntitle: "The Router Moves Upfront"'))

AGAIN, notes2, _ = il.enrich(WRITTEN, vertical="agentic_ai", links=links)
check("re-running replaces the block instead of stacking a second list", AGAIN == WRITTEN, AGAIN[-400:])
check("...and the re-run is reported as an update, not as a second set of links",
      any("already up to date" in n or "replaced" in n for n in notes2), str(notes2))

CORPUS_MOVED, notes3, _ = il.enrich(ARTIFACT, vertical="agentic_ai", links=[])
check("a link that is no longer offered is REMOVED (stale links do not rot in the post)",
      "## Related reading" not in CORPUS_MOVED and "a.com" not in CORPUS_MOVED, CORPUS_MOVED)
check("...and the gap is stated instead of an empty heading",
      any("no internal link" in n or "no live page" in n for n in notes3), str(notes3))

NO_MARKER = ARTIFACT.replace("<!-- internal-links -->\n", "")
PLACED, place_notes, _ = il.enrich(NO_MARKER, vertical="agentic_ai", links=links)
check("a marker the artifact lacks is inserted before <!-- tldr --> (not after the LinkedIn variant)",
      PLACED.index("<!-- internal-links -->") < PLACED.index("<!-- tldr -->")
      and "Related reading" in PLACED, str(place_notes))
check("...and the insertion is reported", any("inserted" in n for n in place_notes), str(place_notes))

OFF_SITE, off_notes, off_used = il.enrich(ARTIFACT, vertical="agentic_ai", site_domain="a.com", links=links + [
    {"anchor_text": "Wrong site", "url": "https://b.com/other-site-routing/", "kind": "article",
     "category": "", "relevance_score": 99, "why": "fixture"}])
check("a link to the other site is dropped even when the scorer offers it (a routing lookup that "
      "degraded must not turn an internal link into a cross-site one)",
      [l["url"] for l in off_used] == urls and any("not on a.com" in n for n in off_notes),
      f"{off_used} {off_notes}")

print("\nthe marker's own region is never treated as disposable")
INLINE = """---
title: "Go Deeper Fixture"
vertical: "agentic_ai"
---

<!-- lead -->
A lead long enough to be a real lead paragraph in this fixture, with a figure [1].

**Go deeper:** <!-- internal-links -->
- **The Big Shift:** the insurer raises rates 29.1% on October 15.
- **Why It Matters:** the pool holds only a fraction of the risk it carries.

## Sources
[1] KQED — https://example.com/a
"""
KEPT, kept_notes, _ = il.enrich(INLINE, vertical="agentic_ai", links=links)
check("reader copy under the marker survives (the marker is often inline, e.g. '**Go deeper:** …')",
      "- **The Big Shift:** the insurer raises rates 29.1%" in KEPT
      and "the pool holds only a fraction" in KEPT, KEPT)
check("...and the links are added as well", KEPT.count("- [") == len(links))
check("...and the pass says it left them alone instead of claiming a cleanup",
      any("left" in n and "not link material" in n for n in kept_notes), str(kept_notes))

LEFTOVERS = INLINE.replace(
    "- **The Big Shift:** the insurer raises rates 29.1% on October 15.\n"
    "- **Why It Matters:** the pool holds only a fraction of the risk it carries.",
    "- https://a.com/stale-leftover-link/\n- /agentic-ai/mcp-protocol-overview")
CLEANED, clean_notes, _ = il.enrich(LEFTOVERS, vertical="agentic_ai", links=links)
check("leftover link lines (a bare URL, a site-relative path) ARE cleared out, so the reader never "
      "sees them as literal text",
      "stale-leftover-link" not in CLEANED and "mcp-protocol-overview" not in CLEANED, CLEANED)
check("...and that is reported", any("leftover link material" in n for n in clean_notes), str(clean_notes))

print("\nnever a link at the reader's expense")
NO_VERTICAL, no_v_notes, no_v_used = il.enrich(ARTIFACT, vertical=None)
check("no vertical => no link at all (the destination cannot be resolved, so nothing is guessed)",
      not no_v_used and "## Related reading" not in NO_VERTICAL and any("no vertical" in n for n in no_v_notes),
      str(no_v_notes))
topic = il.topic_for("The Router Moves Upfront", ARTIFACT)
check("the topic is the headline plus the lead's first sentence",
      topic.startswith("The Router Moves Upfront") and "Routing decisions used to be made" in topic,
      topic)
check("...and for a row it comes from the row's headline",
      il.topic_from_row({"headline": "Token Prices Just Halved"}, "Lead sentence here about pricing.")
      .startswith("Token Prices Just Halved"),
      il.topic_from_row({"headline": "Token Prices Just Halved"}, "Lead sentence here about pricing."))
check("a cross-site URL is not accepted as internal", il.same_site("https://b.com/x/", "a.com") is False
      and il.same_site("https://www.a.com/x/", "a.com") is True)
own = gos.generate_internal_link_map("a completely unrelated topic string", "agentic_ai",
                                     exclude_slugs=("agent-routing-benchmarks",))
check("refreshing a published article cannot link it to itself (its own slug is excluded)",
      "https://a.com/agent-routing-benchmarks/" not in [l["url"] for l in own],
      [l["url"] for l in own])

print("\nthe block reaches the post through the connector")
LATE = """---
title: "Below the LinkedIn Variant"
vertical: "agentic_ai"
---

<!-- lead -->
A lead paragraph long enough to be a real lead paragraph for this fixture [1].

<!-- linkedin -->
Internal variant.

<!-- schema -->
```json
{"@context":"https://schema.org"}
```

<!-- internal-links -->
"""
ENRICHED, _, _ = il.enrich(LATE, vertical="agentic_ai", links=links)
check("an artifact whose marker sits AFTER <!-- linkedin --> still gets its links rendered",
      ENRICHED.index("<!-- internal-links -->") > ENRICHED.index("<!-- linkedin -->")
      and all(u in wd.md_to_html(ENRICHED) for u in urls), wd.md_to_html(ENRICHED)[-300:])
check("...without leaking the LinkedIn variant or the machine schema",
      "Internal variant" not in wd.md_to_html(ENRICHED) and "application/ld+json" not in wd.md_to_html(ENRICHED))
check("...and no operator hint reaches the reader", "internal-link hint" not in wd.md_to_html(ENRICHED))

print("\nindex guard")
check("a candidate URL is reduced to its last path segment",
      fe.slug_of("https://giniloh.com/calculators/lease-break/") == "lease-break")
check("a section page is a candidate, a nested permutation of it is not",
      fe.is_candidate_shape("https://giniloh.com/calculators/lease-break/", "giniloh.com") is True
      and fe.is_candidate_shape("https://giniloh.com/calculators/career-ai-resilience/chief-executives/",
                                "giniloh.com") is False,
      "a per-role calculator page (1,029 of them on one live site) is not a link target")
check("...and a tool URL is only a candidate on the front that publishes that shape",
      fe.is_candidate_shape("https://aichieve.net/tools/gpu-compute/", "aichieve.net") is True
      and fe.is_candidate_shape("https://aichieve.net/calculators/gpu-compute/", "aichieve.net") is False
      and fe.is_candidate_shape("https://giniloh.com/calculators/gpu-compute/", "giniloh.com") is True,
      "giniloh publishes /calculators/<slug>/, aichieve /tools/<slug>/ — the same tool, two paths")
check("site furniture is not a target",
      fe.is_candidate_shape("https://giniloh.com/about/", "giniloh.com") is False
      and fe.is_candidate_shape("https://giniloh.com/wage-floor-sets-robot-payback/", "giniloh.com") is True)
check("a slug becomes a readable title", bli.humanise_slug("ny-heat-pump-rebate") == "Ny Heat Pump Rebate")
check("the registry names the three fronts, giniloh.com first (it owns the reader URL of a shared slug)",
      fe.domains()[:3] == ["giniloh.com", "wellroost.com", "aichieve.net"], fe.domains())
check("a front's served categories are read from its own sitemap",
      fe.served_categories("aichieve.net", ["https://aichieve.net/",
                                            "https://aichieve.net/x/",
                                            "https://aichieve.net/categories/supply-chain-operations/",
                                            "https://aichieve.net/categories/ai-stack-tool-tco/"])
      == {"supply-chain-operations", "ai-stack-tool-tco"})

# The check must reject a corpus that is not honest about where its pages live (a cms.* host in the
# corpus is the old, wrong model), and it must be hermetic here: the sitemap re-read is stubbed.
# (The shipped-index section captures bli.INDEX_JSON right below, so this borrow MUST be given back.)
_guard_saved_index = bli.INDEX_JSON
_real_discover = bli.sc.discover_sitemaps
bli.sc.discover_sitemaps = lambda frontend, **kw: ["https://a.com/agent-routing-benchmarks/"]
_bad = pathlib.Path(_tmp.name) / "cms_host.json"
_bad.write_text(json.dumps({"generated_at": "2026-10-15T00:00:00+00:00",
                            "sites": {"a.com": {"cms": "https://cms.a.com", "frontend": "https://a.com"}},
                            "candidates": [{"site": "a.com", "kind": "article", "slug": "x",
                                            "url": "https://cms.a.com/x/", "live": True}]}),
                encoding="utf-8")
bli.INDEX_JSON = _bad
check("the guard fails on a candidate URL that is on a CMS host", bli.check() == 1)
_foreign = pathlib.Path(_tmp.name) / "foreign_host.json"
_foreign.write_text(json.dumps({"generated_at": "2026-10-15T00:00:00+00:00",
                                "sites": {"a.com": {"cms": "https://cms.a.com", "frontend": "https://a.com"}},
                                "candidates": [{"site": "a.com", "kind": "article", "slug": "x",
                                                "url": "https://b.com/x/", "live": True}]}),
                    encoding="utf-8")
bli.INDEX_JSON = _foreign
check("the guard fails on a candidate URL hosted on a different front", bli.check() == 1)
bli.sc.discover_sitemaps = _real_discover
bli.INDEX_JSON = _guard_saved_index

_empty = pathlib.Path(_tmp.name) / "empty.json"
_empty.write_text(json.dumps({"generated_at": "2026-10-01T00:00:00+00:00", "candidates": []}), encoding="utf-8")
_real_index_json = bli.INDEX_JSON
bli.INDEX_JSON = _empty
check("the guard fails on an index with no candidates", bli.check() == 1)
bli.INDEX_JSON = pathlib.Path(_tmp.name) / "missing.json"
check("the guard fails when the index is absent", bli.check() == 1)
bli.INDEX_JSON = _real_index_json

if _real_index_json.exists():
    print("\nthe shipped index")
    shipped = json.loads(_real_index_json.read_text(encoding="utf-8"))
    cands = shipped["candidates"]
    sites = set(shipped["sites"])
    check("the shipped index holds candidates", len(cands) > 0, len(cands))
    check("every shipped candidate is live and carries a URL",
          all(c.get("live") and c.get("url", "").startswith("https://") for c in cands))
    check("every shipped candidate belongs to one of the indexed sites",
          all(c["site"] in sites for c in cands),
          sorted({c["site"] for c in cands} - sites))
    check("every shipped URL lives on its own site's domain",
          all(c["site"] in c["url"] for c in cands),
          [c["url"] for c in cands if c["site"] not in c["url"]][:3])
    check("articles are the bulk of the corpus",
          len([c for c in cands if c["kind"] == "article"]) >= 20,
          len([c for c in cands if c["kind"] == "article"]))
else:
    print("\nthe shipped index (not built yet — skipping its inspection)")

# The CLI path must exclude the artifact it is enriching, exactly as `ensure_for_row` does: a
# re-enrichment of a page that is ALREADY live finds the article itself in the index, so a missing
# exclusion links the post to itself (observed 2026-10-10 on a re-published evergreen artifact).
print("\ncli self-exclusion")
check("a dated artifact's slug is derived from its filename",
      il._artifact_slug(pathlib.Path("published/2026-10-10_my-slug.md")) == "my-slug",
      il._artifact_slug(pathlib.Path("published/2026-10-10_my-slug.md")))
check("an undated draft keeps its whole stem",
      il._artifact_slug(pathlib.Path("context/drafts/my-slug_final.md")) == "my-slug_final",
      il._artifact_slug(pathlib.Path("context/drafts/my-slug_final.md")))
_captured = {}
_real_resolve = il.resolve_links
il.resolve_links = lambda topic, vertical, max_links=3, exclude_slugs=(), **kw: (
    _captured.update(exclude_slugs=tuple(exclude_slugs)) or [])
try:
    with tempfile.TemporaryDirectory() as _dir:
        _p = pathlib.Path(_dir) / "2026-10-10_my-slug.md"
        _p.write_text("---\ntitle: My Slug\nvertical: agentic_ai\n---\n\n<!-- lead -->\nLead text.\n",
                      encoding="utf-8")
        sys.argv = ["internal_links.py", str(_p), "--apply"]
        il.main()
    check("the CLI passes the artifact's own slug to the scorer",
          _captured.get("exclude_slugs") == ("my-slug",), str(_captured))
finally:
    il.resolve_links = _real_resolve

print("\nstamping: one stored body, every front that serves it")
STAMP_INDEX = {
    "generated_at": "2026-10-15T00:00:00+00:00",
    "site_source": "fixture",
    "sites": {"a.com": {"cms": "https://cms.a.com", "frontend": "https://a.com"},
              "b.com": {"cms": "https://cms.b.com", "frontend": "https://b.com"}},
    "hub_slugs": {"a.com": ["supply-chain-operations", "money-wealth"],
                  "b.com": ["supply-chain-operations"]},
    "categories": {"a.com": {"10": "Supply Chain & Operations", "11": "Money & Wealth"}},
    # A corpus must hold something: `load_internal_link_index()` treats an empty candidate list as "no
    # corpus" and falls back, which would make every case below pass or fail for the wrong reason.
    "candidates": [{"site": "a.com", "kind": "article", "slug": "wage-floor", "title": "Wage Floor",
                    "url": "https://a.com/wage-floor/", "path": "/wage-floor/",
                    "sites_live": {"a.com": "/wage-floor/", "b.com": "/wage-floor/"},
                    "categories": ["Supply Chain & Operations"], "category_slugs": ["supply-chain-operations"],
                    "category_ids": [], "excerpt": "", "live": True}],
    "not_live": [],
}
_stamp_file = pathlib.Path(_tmp.name) / "stamp_index.json"
_stamp_file.write_text(json.dumps(STAMP_INDEX), encoding="utf-8")


def stamped(anchor, url, sites_live, serve, kind="article"):
    """A scored link as `generate_internal_link_map` returns it: the candidate's `sites_live` map plus
    the render set the scorer resolved (`serve`). The renderer must not work either out for itself."""
    return {"anchor_text": anchor, "url": url, "kind": kind, "why": "fixture",
            "relevance_score": 9, "category": "", "sites_live": sites_live, "path": "/",
            "serve": list(serve)}


_real_index, _real_routing = gos.INTERNAL_LINK_INDEX, gos._site_for_vertical
gos.INTERNAL_LINK_INDEX = _stamp_file


def _routing(vertical):
    """The fixture's routing row: each vertical routes to its own category (a.com, ids 10 and 11).

    A constant id would make every vertical resolve to one category, so the render-set cases could
    not distinguish a category two fronts serve from one only a.com serves — the two behaviours this
    block exists to pin.
    """
    if not vertical:
        return None
    return {"site_domain": "a.com", "frontend_url": "https://a.com",
            "wp_category_id": {"supply_chain": 10, "money_wealth": 11}.get(vertical, 10)}


gos._site_for_vertical = _routing
try:
    BOTH = [stamped("Cloud Uptime SLAs", "https://a.com/sla-credit/",
                    {"a.com": "/sla-credit/", "b.com": "/sla-credit/"}, serve=["a.com", "b.com"]),
            stamped("Gone From B", "https://a.com/only-on-a/", {"a.com": "/only-on-a/"},
                    serve=["a.com", "b.com"]),
            stamped("Tool", "https://a.com/calculators/gpu-compute/",
                    {"a.com": "/calculators/gpu-compute/", "b.com": "/tools/gpu-compute/"},
                    serve=["a.com", "b.com"], kind="calculator")]
    check("the render set rides on the links (the scorer resolved it, the renderer reads it)",
          il.renderers_for(BOTH) == ["a.com", "b.com"], il.renderers_for(BOTH))
    check("...and a link whose set is only one front reports only that front",
          il.renderers_for([stamped("X", "https://a.com/x/", {"a.com": "/x/"}, serve=["a.com"])])
          == ["a.com"])
    check("...and links with no render set at all stamp nothing",
          il.renderers_for([{"anchor_text": "X", "url": "https://a.com/x/"}]) == [])
    SHARED, shared_notes, used_shared = il.enrich(ARTIFACT, vertical="supply_chain", links=list(BOTH))
    check("a link live on both fronts is stamped as the relative path they share",
          [l.get("href") for l in used_shared if l["anchor_text"] == "Cloud Uptime SLAs"] == ["/sla-credit/"],
          str(used_shared))
    check("...so the stored body carries no other front's domain",
          "https://a.com/sla-credit/" not in SHARED and "(/sla-credit/)" in SHARED, SHARED[-400:])
    check("a target that is not live on EVERY front serving the article is dropped",
          not any(l["anchor_text"] == "Gone From B" for l in used_shared)
          and any("not live on every front" in n and "b.com" in n for n in shared_notes),
          str(shared_notes))
    check("a target the fronts publish at different paths is dropped, never stamped wrongly",
          not any(l["anchor_text"] == "Tool" for l in used_shared)
          and any("different paths" in n for n in shared_notes), str(shared_notes))
    check("what was stamped can be read back (the CLI and --check count relative links)",
          [l["url"] for l in il.read_links(SHARED)] == ["/sla-credit/"], str(il.read_links(SHARED)))
    check("a stamped block is idempotent (a second pass writes nothing)",
          il.enrich(SHARED, vertical="supply_chain", links=list(BOTH))[0] == SHARED)

    ONE_FRONT = [stamped(l["anchor_text"], l["url"], l["sites_live"], serve=["a.com"],
                         kind=l["kind"]) for l in BOTH]
    SINGLE, _, single_used = il.enrich(ARTIFACT, vertical="money_wealth", links=list(ONE_FRONT))
    check("when only one front serves the article, a target live there is kept",
          any(l["anchor_text"] == "Gone From B" for l in single_used), str(single_used))
    check("...and it is still stamped relative, so a later pull cannot break it",
          all((l.get("href") or "").startswith("/") for l in single_used), str(single_used))
    check("a caller's own links (no corpus metadata) are never restamped",
          all(l.get("href") is None for l in il.enrich(ARTIFACT, vertical="supply_chain",
                                                      links=[{"anchor_text": "X", "url": "https://a.com/x/"}])[2]))

    # Regression, 2026-10-15: the first revision of the stamper resolved the render set itself, which
    # meant calling routing — and routing reaches `wp_draft.supabase_config()`, which EXITS THE PROCESS
    # when the credentials are absent (`except Exception` cannot catch SystemExit). Proven here on the
    # one path that matters: stamping a link must not need the database at all.
    def _explode(vertical):
        raise RuntimeError("routing must not be consulted while stamping a link")

    _saved_routing = gos._site_for_vertical
    gos._site_for_vertical = _explode
    try:
        _, guard_notes, guard_used = il.enrich(ARTIFACT, vertical="supply_chain", links=list(BOTH))
        check("stamping a link never consults routing (a publish cannot die on a missing Supabase key)",
              [l.get("href") for l in guard_used if l["anchor_text"] == "Cloud Uptime SLAs"] == ["/sla-credit/"],
              f"{guard_used} {guard_notes}")
    finally:
        gos._site_for_vertical = _saved_routing
finally:
    gos.INTERNAL_LINK_INDEX, gos._site_for_vertical = _real_index, _real_routing

print("\ncategory matching moved from WordPress ids to the hub slug the front publishes")
gos.INTERNAL_LINK_INDEX = _stamp_file
gos._site_for_vertical = _routing
try:
    _slug_index = json.loads(_stamp_file.read_text(encoding="utf-8"))
    _slug_index["candidates"] = [
        {"site": "a.com", "kind": "article", "slug": "quarterly-roundup", "title": "Quarterly Roundup",
         "url": "https://a.com/quarterly-roundup/", "categories": ["Supply Chain & Operations"],
         "category_slugs": ["supply-chain-operations"], "category_ids": [], "excerpt": "", "live": True},
        {"site": "a.com", "kind": "article", "slug": "unrelated", "title": "Nothing In Common",
         "url": "https://a.com/unrelated/", "categories": ["Money & Wealth"],
         "category_slugs": ["money-wealth"], "category_ids": [], "excerpt": "", "live": True},
    ]
    _stamp_file.write_text(json.dumps(_slug_index), encoding="utf-8")
    _links = gos.generate_internal_link_map("something unrelated to both", "supply_chain", max_links=5)
    _urls = [l["url"] for l in _links]
    check("a page in the destination's own hub category qualifies on the slug alone",
          "https://a.com/quarterly-roundup/" in _urls, _urls)
    check("...and a page in another category does not", "https://a.com/unrelated/" not in _urls, _urls)
    check("the scorer hands the renderer what it needs to stamp (sites_live + path + serve)",
          all("sites_live" in l and "path" in l and "serve" in l for l in _links), str(_links[:1]))
    check("...and the render set it hands over is every front publishing that category hub",
          all(l["serve"] == ["a.com", "b.com"] for l in _links), str([l["serve"] for l in _links]))
finally:
    gos.INTERNAL_LINK_INDEX, gos._site_for_vertical = _real_index, _real_routing

print(f"\n{len(PASS)} passed, {len(FAIL)} failed")
for name in FAIL:
    print(f"  FAILED: {name}")
raise SystemExit(1 if FAIL else 0)
