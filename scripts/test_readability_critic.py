#!/usr/bin/env python3
"""The reader-side critic, pinned: structure, bullet density, citations, and the prose advisories.

The pieces of copy this rejects are the ones the owner named on 2026-11-06 — an executive summary at
the foot of the page, a bullet carrying two statistics, "more X than Y is Z", the same date pair
explained twice, and a closing sentence that names a rule the body never introduced. None of them is
a Flesch problem, so each case here pins one class on its own.
"""
from __future__ import annotations

import pathlib

import pytest

from scripts import readability_critic as rc

GOOD = """---
title: Eight Gates Shut, 85 Percent Stops
date: {date}
---

<!-- lead -->
A walkout by the 250 watchmen who inspect containers would shut all eight terminals at Long Beach, and those gates move 85% of the port's cargo [1].

<!-- tldr -->

## At a glance

- **The shift:** The union served notice on 2 November and the employers asked for a delay.
- **The number:** 85% of Long Beach cargo moves through the eight gates at risk.
- **The risk:** A single closed gate stops every container behind it, whatever the crew size.

<!-- tension -->

## 2 November Set The Clock

The walkout notice arrived on 2 November and gave the employers ten days to reach a deal [1]. The two sides met twice that week, and the terminal operators asked for an extension on 9 November [2].

## By the numbers

- **85% of Long Beach cargo:** The share of the port's containers that passes the eight gates at risk [1].
- **250 watchmen:** The inspectors who would stop work at those terminals on 12 November [2].

<!-- tactical-insight -->

## What the Shippers Watch

Shippers with holiday inventory booked through Long Beach are already rerouting to Oakland, and the freight forwarders I follow say the trucking schedules are the tell [3]. If the notice holds past the 10-day window, the rail connections inland are the next thing to slip.

<!-- nuanced-takeaway -->

## The Catch

A settlement can land at any hour, and the last two notices at this port were withdrawn the day before they took effect [2]. The risk is real without being certain.

## Sources

1. Port of Long Beach daily rail report — https://example.gov/rail
2. ILWU Local 13 notice — https://example.org/notice
3. Journal of Commerce terminal report — https://example.net/terminals
"""

BAD = """---
title: Gates And Clocks And Everything Between
date: {date}
---

<!-- lead -->
A gate is one shared function rather than a share of one, and the notice runs deeper into its stay than the window is long [1][2].

<!-- tension -->

## The big picture:

The notice arrived on 2 November and gave the employers ten days, and the extension came on 9 November [1]. The employers asked again on 2 November for more time [2].

## By the numbers

- **85% of Long Beach cargo — eight gates:** the 250 watchmen are about 2% of the workforce and the 1,900 dockworkers at the other terminals are not covered by the notice at all [3].
- **11 days:** the union served notice on 2 November and the deadline moved to 12 November, which the employers accepted [1].

<!-- tactical-insight -->

## What I'd watch:

The shippers are rerouting and the forwarders are watching the trucking schedules [3].

<!-- nuanced-takeaway -->

## The catch

That is the honest limitation, and the union could still settle [2]. Under the two 30-day clocks on a late container's bill, the dispute would run past the holiday.

<!-- tldr -->

## At a glance

- **The shift:** notice served.

## Sources

[1] Port notice — https://example.org/a [2] Union notice — https://example.org/b [3] Trade press — https://example.net/c
"""


def article(template: str, date: str = "2026-11-06") -> str:
    return template.format(date=date)


# --------------------------------------------------------------------------- the good shape

def test_a_clean_article_passes_every_checked_class():
    report = rc.findings(article(GOOD))
    assert report["fails"] == [], report["fails"]
    assert report["held"] is True


def test_at_a_glance_sits_directly_under_the_lede():
    text = article(GOOD)
    order = [name for name, _ in rc.sections(text)]
    assert order[:2] == ["lead", "tldr"], order


# --------------------------------------------------------------------------- 1. structure

def test_at_a_glance_at_the_foot_of_the_piece_fails():
    text = article(GOOD).replace("<!-- tldr -->\n\n## At a glance", "## At a glance")
    text = text.replace("<!-- nuanced-takeaway -->", "<!-- tldr -->\n\n## At a glance\n\n- **The shift:** late.\n- **The number:** 85%.\n- **The risk:** late.\n\n<!-- nuanced-takeaway -->")
    fails = rc.structure_findings(text, rc._registry())
    assert any("immediately under the lede" in f or "out of order" in f for f in fails), fails


def test_missing_glance_labels_fail():
    text = article(GOOD).replace("- **The risk:** A single closed gate stops every container behind it, whatever the crew size.\n", "")
    fails = rc.structure_findings(text, rc._registry())
    assert any("The risk" in f for f in fails), fails


def test_a_second_summary_in_the_glance_box_fails():
    long_box = ("- **The shift:** " + "The union served notice and the employers asked for a delay. " * 4
                + "\n- **The number:** 85% of cargo.\n- **The risk:** a gate closes.\n")
    text = article(GOOD)
    start = text.index("## At a glance")
    end = text.index("<!-- tension -->")
    text = text[:start] + "## At a glance\n\n" + long_box + "\n" + text[end:]
    fails = rc.structure_findings(text, rc._registry())
    assert any("second summary" in f for f in fails), fails


# --------------------------------------------------------------------------- 2. bullets

def test_a_bullet_over_25_words_fails():
    text = article(GOOD).replace(
        "- **250 watchmen:** The inspectors who would stop work at those terminals on 12 November [2].",
        "- **250 watchmen:** The inspectors who would stop work at those terminals on 12 November, "
        "and the employers say they have contingency crews ready to take over the inspection work "
        "if the notice is not withdrawn before the deadline [2].")
    fails = rc.bullets_findings(text, rc._registry())
    assert any("max 25" in f for f in fails), fails


def test_two_figures_in_one_bullet_lead_in_fail():
    text = article(GOOD).replace(
        "- **250 watchmen:** The inspectors who would stop work at those terminals on 12 November [2].",
        "- **250 watchmen — 2% of the union:** The inspectors who would stop work on 12 November [2].")
    fails = rc.bullets_findings(text, rc._registry())
    assert any("one metric per bullet" in f for f in fails), fails


def test_a_two_sentence_bullet_fails():
    text = article(GOOD).replace(
        "- **250 watchmen:** The inspectors who would stop work at those terminals on 12 November [2].",
        "- **250 watchmen:** The inspectors who would stop work at those terminals [2]. They are "
        "2% of the union.")
    fails = rc.bullets_findings(text, rc._registry())
    assert any("more than one sentence" in f for f in fails), fails


# --------------------------------------------------------------------------- 3. citations

def test_two_citation_tags_in_one_sentence_fail():
    fails = rc.citation_findings(article(BAD), rc._registry())
    assert any("[1], [2]" in f for f in fails), fails


def test_a_run_on_source_block_fails():
    fails = rc.citation_findings(article(BAD), rc._registry())
    assert any("vertical list" in f for f in fails), fails


def test_a_vertical_source_list_passes():
    assert rc.citation_findings(article(GOOD), rc._registry()) == []


# --------------------------------------------------------------------------- 4. prose (advisory)

def test_riddle_syntax_is_flagged():
    found = rc.read_twice_findings(article(BAD))
    assert any("abstract symmetry" in f or "abstract comparison" in f for f in found), found


def test_stacked_prepositional_phrases_are_flagged():
    found = rc.read_twice_findings(
        "The fee is set on the rate for the box in the yard at the gate by the carrier.")
    assert any("prepositional phrases in a row" in f for f in found), found


def test_a_clean_sentence_is_not_flagged():
    assert rc.read_twice_findings(
        "The gate shuts and 85% of the port's cargo stops with it.") == []


def test_a_date_pair_explained_twice_is_flagged():
    found = rc.timeline_findings(article(BAD))
    assert any("set the timeline once" in f for f in found), found


def test_a_chronology_stated_once_is_not_flagged():
    assert rc.timeline_findings(article(GOOD)) == []


def test_a_cold_concept_in_the_closing_paragraph_is_flagged():
    found = rc.closing_findings(article(BAD))
    assert any("30-day clocks" in f for f in found), found


def test_a_closing_that_reuses_an_introduced_term_is_not_flagged():
    assert rc.closing_findings(article(GOOD)) == []


# --------------------------------------------------------------------------- grandfathering

def test_artifacts_before_the_standard_are_never_held():
    old = article(BAD, date="2026-11-05")
    report = rc.findings(old)
    assert report["fails"], "the shape is still reported"
    assert report["held"] is False
    assert rc.failures_for_text(old) == []


def test_the_gate_reads_only_the_holding_classes():
    text = article(BAD)
    report = rc.findings(text)
    assert report["fails"]
    assert all(f.split(":")[0] in rc._registry()["hold"] for f in report["fails"])
    applied = rc.failures_for_text(text)
    assert applied, "a 2026-11-06 piece is held on the classes that had landed"
    assert all(f.split(":")[0] in report["enforced"] for f in applied), applied
    assert any("read_twice" in a or "timeline" in a or "closing" in a
               for a in report["advisories"])


# ---------------------------------------------------------- jargon: no private shorthand nouns

def test_a_private_shorthand_noun_fails():
    text = article(GOOD).replace(
        "the terminal operators asked for an extension",
        "the agency keeps the fact in the yard and the terminal operators asked for an extension")
    reg = rc._registry()
    found = rc.jargon_findings(text, reg)
    assert any("the fact" in f for f in found), found
    assert any("jargon:" in f for f in rc.failures_for_text(article(GOOD, date="2026-11-07")
                                                            .replace(
        "the terminal operators asked for an extension",
        "the agency keeps the fact in the yard and the terminal operators asked for an extension")))


def test_the_ordinary_idiom_the_fact_that_is_not_shorthand():
    text = article(GOOD).replace(
        "Shippers with holiday inventory booked through Long Beach are already rerouting",
        "Despite the fact that holiday inventory is booked through Long Beach, shippers are already rerouting")
    assert rc.jargon_findings(text, rc._registry()) == []


def test_role_and_layer_shorthand_fail():
    reg = rc._registry()
    for phrase, label in (("so the hop owner can price it", "hop owner"),
                          ("and the state rides the wire", "the wire"),
                          ("then the line moved in the revision", "the line")):
        text = article(GOOD).replace("The risk is real without being certain.",
                                    f"{phrase.capitalize()}. The risk is real without being certain.")
        assert any(label in f for f in rc.jargon_findings(text, reg)), (phrase,
                                                                       rc.jargon_findings(text, reg))


# ---------------------------------------------------------------- enumeration: counted headings

def test_a_heading_promising_three_items_needs_three_labelled_items():
    text = article(GOOD).replace(
        "## What the Shippers Watch\n\nShippers",
        "## Three Places the Cargo Waits\n\nShippers")
    found = rc.enumeration_findings(text, rc._registry())
    assert any("promises 3 items" in f for f in found), found


def test_a_numbered_list_satisfies_the_enumeration_rule():
    text = article(GOOD).replace(
        "## What the Shippers Watch\n\nShippers",
        "## Three Places the Cargo Waits\n\n"
        "1. **The gate.** Nothing enters the terminal without an inspection slot.\n"
        "2. **The rail ramp.** Inland boxes wait for a train that is already full.\n"
        "3. **The yard.** Chassis sit where the last driver left them.\n\nShippers")
    assert rc.enumeration_findings(text, rc._registry()) == []


def test_a_heading_that_names_a_date_is_not_an_enumeration():
    # "2 November Set The Clock" promises nothing; the count rule needs a plural noun.
    assert rc.enumeration_findings(article(GOOD), rc._registry()) == []


# --------------------------------------------------------------------- matrix: 3+ comparisons

def test_three_prose_comparisons_without_a_table_fail():
    text = article(GOOD).replace(
        "The risk is real without being certain.",
        "The gate version needs 1,898 lines against 1,255, six steps against two, and ten parts "
        "against four [1]. The risk is real without being certain.")
    found = rc.matrix_findings(text, rc._registry())
    assert any("comparison" in f for f in found), found


def test_a_table_satisfies_the_matrix_rule():
    text = article(GOOD).replace(
        "The risk is real without being certain.",
        "The gate version needs 1,898 lines against 1,255, six steps against two, and ten parts "
        "against four [1].\n\n"
        "| Pattern | Overhead | Failure mode |\n| :--- | :--- | :--- |\n"
        "| Tool call | 1,255 lines | forgets |\n| Task | 1,898 lines | unhandled states |\n\n"
        "The risk is real without being certain.")
    assert rc.matrix_findings(text, rc._registry()) == []


# --------------------------------------------------------------- sources: a list on the page

def test_source_lines_without_a_list_marker_fail():
    text = article(GOOD).replace(
        "1. Port of Long Beach daily rail report — https://example.gov/rail\n"
        "2. ILWU Local 13 notice — https://example.org/notice\n"
        "3. Journal of Commerce terminal report — https://example.net/terminals",
        "[1] Port of Long Beach daily rail report — https://example.gov/rail\n"
        "[2] ILWU Local 13 notice — https://example.org/notice\n"
        "[3] Journal of Commerce terminal report — https://example.net/terminals")
    found = rc.sources_findings(text, rc._registry())
    assert any("no list marker" in f for f in found), found


def test_a_marked_source_list_passes():
    assert rc.sources_findings(article(GOOD), rc._registry()) == []


# ------------------------------------------------------------- density + dangling (advisory)

def test_dense_prose_is_reported_but_never_holds():
    dense = ("The commission reviewed the terminal schedule and the inland rail plan that the "
             "operators submitted before the notice arrived, and it found that neither document "
             "described the contingency the employers had promised in the previous round. ") * 4
    assert rc.density_findings(dense, rc._registry()), "a body of long sentences is reported"
    assert "density" not in rc._registry()["hold"], "density is advisory and can never hold"


def test_a_dangling_reference_is_advisory_only():
    text = article(GOOD).replace(
        "The risk is real without being certain.",
        "That is the middle option, and the risk is real without being certain.")
    report = rc.findings(text)
    assert any("middle option" in a for a in report["advisories"]), report["advisories"]
    assert not any(f.startswith("dangling:") for f in rc.failures_for_text(text))


def test_a_rule_landing_later_never_holds_an_earlier_piece():
    text = article(GOOD).replace(
        "The risk is real without being certain.",
        "The agency keeps the fact in the yard. The risk is real without being certain.")
    old = text.replace("date: 2026-11-06", "date: 2026-11-05")
    assert rc.jargon_findings(old, rc._registry()), "the shape is still reported"
    assert rc.failures_for_text(old) == []


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q"]))
