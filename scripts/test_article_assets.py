#!/usr/bin/env python3
"""Tests for scripts/article_assets.py — run: python3 scripts/test_article_assets.py

Hermetic: the derived metadata and the chartability rules are pure functions of the artifact text.
The regression cases are the shapes the real corpus produces (mixed units, a second figure inside a
bullet, a growth rate above 100%, a marker with no block).
"""

from __future__ import annotations

import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import article_assets as aa  # noqa: E402
import chart_generator as cg  # noqa: E402

PASS, FAIL = [], []


def check(name: str, condition: bool, detail: str = ""):
    (PASS if condition else FAIL).append(name)
    print(f"  [{'ok ' if condition else 'FAIL'}] {name}{'' if condition else f'  <- {detail}'}")


ARTICLE = """---
title: "Disney+ and Hulu Just Raised Prices 13% — Right After Doubling Profits"
vertical: personal_microeconomics_tinkering_tax
date: 2026-09-26
slug: disney-hulu-fourth-hike-subscription-creep
---

<!-- lead -->
On Sept. 23, Disney+ and Hulu pushed their ad-free streaming plans up 13 percent to $21.49 a month. This marks the fourth price hike in four years [1][3]. The latest increase landed weeks after the two services reported a bigger jump.

<!-- tension -->
## Where This Bites

**By the numbers:**
- **13% / $2.50:** The price jump for both ad-free tiers [1].
- **4% / $0.50:** The tiny increase for the ad-supported tier [2].
- **+116%:** The growth in combined operating income [6].
- **~3×:** The rate prices outpaced inflation [4].

## Sources
[1] Example — https://example.com/a
"""

print("frontmatter parsing")
fm, body = aa.split_frontmatter(ARTICLE)
check("frontmatter keys are read", fm["slug"] == "disney-hulu-fourth-hike-subscription-creep")
check("the body excludes the frontmatter", body.lstrip().startswith("<!-- lead -->"))

print("\nSEO metadata — derived, never invented")
filled, notes = aa.ensure_seo_metadata(dict(fm), body)
check("meta_title derived from the title", filled["meta_title"].startswith("Disney+ and Hulu"), str(filled.get("meta_title")))
check("...and marked as derived", filled["meta_title_source"] == "derived_from_title")
check("meta_description derived from the lead paragraph",
      filled["meta_description"].startswith("On Sept. 23, Disney+"), str(filled.get("meta_description")))
check("...marked as derived", filled["meta_description_source"] == "derived_from_lead")
check("...and the [1][3] markers do not leave ' .' artifacts",
      " ." not in filled["meta_description"] and "[" not in filled["meta_description"],
      str(filled.get("meta_description")))
check("...within the meta-description budget", len(filled["meta_description"]) <= aa.META_DESC_TARGET + 1,
      str(len(filled["meta_description"])))
check("the description ends on a sentence, not mid-clause",
      filled["meta_description"].rstrip().endswith((".", "…", "!", "?")), filled["meta_description"])

authored = {"title": "T", "meta_title": "An editor's own title", "meta_description": "An editor's own description."}
kept, _ = aa.ensure_seo_metadata(dict(authored), body)
check("a value the artifact already carries wins (no overwrite)",
      kept["meta_title"] == "An editor's own title" and kept["meta_description"] == "An editor's own description.")

print("\ncharts — only a real, single-unit series")
series, reason = aa.chart_series(ARTICLE)
check("only the percentages that are series points are charted",
      [v for _, v, _ in series] == [13.0, 4.0], str(series))
check("the 116% growth rate is excluded (not a share on a 0-100 axis)",
      all(v <= 100 for _, v, _ in series))
check("...and the reason names the figure it skipped",
      "+116%" in reason or "above 100" in reason, reason)
check("each point carries its own citation marker as the note",
      series[0][2] == "[1]" and series[1][2] == "[2]", str(series))

mixed = ARTICLE.replace("- **13% / $2.50:** The price jump for both ad-free tiers [1].\n", "")
mixed = mixed.replace("- **4% / $0.50:** The tiny increase for the ad-supported tier [2].\n",
                      "- **13%:** The price jump [1].\n")
check("one chartable point is not a series => no chart is emitted",
      "<svg" not in aa.inject_chart(mixed)[0]
      and "1 chartable percentage point(s)" in aa.inject_chart(mixed)[1], aa.inject_chart(mixed)[1][:90])

comparison = ARTICLE.replace(
    "- **4% / $0.50:** The tiny increase for the ad-supported tier [2].\n",
    "- **4%:** The tiny increase, against the 8% the plan asked for [2].\n")
compare_series, compare_reason = aa.chart_series(comparison)
check("a bullet that states a second figure is a comparison, not a series point",
      [v for _, v, _ in compare_series] == [13.0], str(compare_series))

no_numbers = ARTICLE.split("**By the numbers:**")[0] + "## Sources\n[1] x\n"
check("no numbers section => no chart, with a reason",
      aa.chart_series(no_numbers)[0] == [] and "no `**By the numbers:**`" in aa.chart_series(no_numbers)[1])

print("\ninjection — idempotent, positioned with its figures")
injected, note = aa.inject_chart(ARTICLE)
check("the chart is embedded as SVG markup", "<svg" in injected and "&lt;svg" not in injected)
check("...with a real data value, not a placeholder", ">13%<" in injected and ">50.0%" not in injected)
check("...after the bullets it charts and before the next heading",
      injected.index("</svg>") > injected.index("outpaced inflation") > injected.index("By the numbers"),
      "ordering")
check("...and the caption does not claim hub-grade telemetry",
      "Audited Field Telemetry" not in injected)
check("re-running does not add a second chart", aa.inject_chart(injected)[0].count("<svg") == 1)
check("the note reports the decision", note.startswith("chart added: 2 point(s)"), note)

no_chart, why = aa.inject_chart(no_numbers)
check("an unchartable artifact is returned unchanged, with the reason stated",
      no_chart == no_numbers and why.startswith("no chart:"), why)

whole, notes = aa.ensure_assets(ARTICLE)
check("one pass yields frontmatter metadata AND the chart",
      "meta_description:" in whole and "<svg" in whole and "meta_description_source: derived_from_lead" in whole)
check("...and is idempotent", aa.ensure_assets(whole)[0] == whole)

print("\nchart labels — bounded by the renderer's own allowance")


def row_labels(markdown: str) -> list[str]:
    """The chart's row labels (x=20, but not the title at y=36 nor the caption at y=52)."""
    match = re.search(r"<svg\b[\s\S]*?</svg>", markdown)
    if not match:
        return []
    return [text for y, text in re.findall(r'<text x="20" y="(\d+)"[^>]*>([^<]*)</text>', match.group(0))
            if y not in ("36", "52")]


LONG_LABEL = ARTICLE.replace(
    "- **13% / $2.50:** The price jump for both ad-free tiers [1].\n",
    "- **37%:** Autonomous agentic workflow adoption across regulated enterprises [1].\n")
long_series, _ = aa.chart_series(LONG_LABEL)
check("a sentence-fragment metric is reduced to a name, not handed back for ellipsis",
      all(len(label) <= cg.LABEL_MAX for label, _, _ in long_series), str(long_series))
injected_long, _ = aa.inject_chart(LONG_LABEL)
check("...so the rendered row labels carry no ellipsis (a figure readers quote verbatim)",
      bool(row_labels(injected_long)) and all("\u2026" not in label for label in row_labels(injected_long)),
      str(row_labels(injected_long)))
check("narrative lead-ins are cleaned into descriptive metric names",
      aa.clean_metric_label("88% price jump", "Diesel fuel started the year near $3.46 a gallon and almost doubled in just a few short months [2].") == "Diesel price jump")
check("corporate acronyms and narrative fillers are simplified without clipping",
      aa.clean_metric_label("21% to 29.5%", "The leap in the United Parcel Service (UPS) fuel fee on Sept. 21, before the carrier changed its math to slow the drop [2].") == "UPS fuel fee")
check("structured em-dash metric titles are preserved directly",
      aa.clean_metric_label("88% — Diesel price jump", "Prices surged from $3.46/gal [2].") == "Diesel price jump" and
      aa.clean_metric_label("21% to 29.5% — UPS fuel fee", "The fuel fee jumped on Sept. 21 [2].") == "UPS fuel fee")
check("...and every corpus label fits the same ceiling",
      all(len(label) <= cg.LABEL_MAX
          for path in sorted(pathlib.Path(aa.__file__).parent.parent.glob("published/*.md"))
          for label, _, _ in aa.chart_series(path.read_text(encoding="utf-8"))[0]),
      "a published artifact charts a label longer than LABEL_MAX")

print("\nchart title — the artifact's own, the caller's, or the body's own heading")
body_only = aa.split_frontmatter(ARTICLE)[1]
titled, _ = aa.inject_chart(body_only, title="The artifact's own headline")
check("a chart built from a frontmatter-less body keeps the caller's headline",
      "The artifact&#x27;s own headline" in titled, titled[:160])
check("...and the generic caption is not used when a real title is available",
      "Verified figures" not in titled)
check("the generic caption is the last resort, only when nothing names the article",
      "Verified figures" in aa.inject_chart(body_only)[0])
head = "# A Heading The Body Carries\n\n" + body_only
check("a body's own top heading is used when no caller title is passed",
      "A Heading The Body Carries" in aa.inject_chart(head)[0])
check("a title the markdown already carries beats the caller's",
      "Verified figures" not in aa.inject_chart(ARTICLE, title="CALLER MUST LOSE")[0]
      and "CALLER MUST LOSE" not in aa.inject_chart(ARTICLE, title="CALLER MUST LOSE")[0])

print("\nreal artifacts (read-only)")
for path in sorted(pathlib.Path(aa.__file__).parent.parent.glob("published/*.md")):
    text = path.read_text(encoding="utf-8")
    fm2, body2 = aa.split_frontmatter(text)
    derived, _ = aa.ensure_seo_metadata(dict(fm2), body2)
    check(f"{path.name[:44]}: every article ends up with a meta_description",
          bool(derived.get("meta_description")) or not body2.strip())
    # A pass over a complete artifact must not rewrite it: the frontmatter is YAML and the parser
    # is a line-based `key: value` reader, so re-serialising the block from that dict destroys a
    # `sources:` list and churns the quoting of every line the pipeline wrote quoted.
    enriched, _enotes = aa.ensure_assets(text)
    check(f"  ...a pass that has nothing to derive leaves the artifact byte-identical",
          enriched == text,
          f"{len(text)} -> {len(enriched)} chars")
    check(f"  ...and no frontmatter line is re-serialised (list items survive verbatim)",
          [line for line in text.split("---")[1].splitlines() if line.strip()]
          == [line for line in enriched.split("---")[1].splitlines() if line.strip()]
          or enriched == text, "a frontmatter line was rewritten")
    series2, reason2 = aa.chart_series(text)
    charted = len(series2) >= aa.CHART_MIN_POINTS
    check(f"  ...chart only when the numbers section is a series "
          f"({'charted' if charted else 'none: ' + reason2.split('(')[0].strip()[:38]})",
          charted or reason2.startswith(("no `**By the numbers:**`", "1 chartable", "0 chartable")))

print(f"\n{len(PASS)} passed, {len(FAIL)} failed")
if FAIL:
    for name in FAIL:
        print(f"  FAILED: {name}")
sys.exit(1 if FAIL else 0)
