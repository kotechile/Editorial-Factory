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
import growth_os as gos  # noqa: E402
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
calc = gos.generate_internal_link_map("routing", "agentic_ai", max_links=5)
check("a calculator is a valid target", any(l["kind"] == "calculator" for l in calc),
      [(l["kind"], l["url"]) for l in calc])

print("\nanchor text and reader-facing rendering")
check("a leading stopword is trimmed from the anchor",
      gos._anchor_for({"title": "The Big Shift In Routing"}, set()) == "Big Shift In Routing",
      gos._anchor_for({"title": "The Big Shift In Routing"}, set()))
long_title = " ".join(f"word{i}" for i in range(1, 30))
long_anchor = gos._anchor_for({"title": long_title}, set())
check("a long title is trimmed at a word boundary, never mid-word",
      long_anchor.endswith("…") and all(w in long_title.split() for w in long_anchor.rstrip("…").split()),
      long_anchor)
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

print("\nindex guard")
check("a candidate URL is reduced to its last path segment",
      bli.path_segment("https://a.com/calculators/lease-break/") == "lease-break")
check("a slug becomes a readable title", bli.title_from_slug("ny-heat-pump-rebate") == "Ny Heat Pump Rebate")

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

print(f"\n{len(PASS)} passed, {len(FAIL)} failed")
for name in FAIL:
    print(f"  FAILED: {name}")
raise SystemExit(1 if FAIL else 0)
