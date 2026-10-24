#!/usr/bin/env python3
"""The article-shape standard, pinned: figure repetition, inline decision link, opening advisories.

Every case is a shape the reader-side critique of 2026-10-24 found in a live piece, and none of them
depends on the story's vertical or category.
"""
from __future__ import annotations

import pathlib

import pytest

from scripts import article_shape as shape

BASE = """---
title: A test article
date: {date}
---

<!-- lead -->
{lead}

<!-- tension -->

## The big picture:

{tension}

<!-- tactical-insight -->

## What I'd watch:

{tactical}

<!-- nuanced-takeaway -->

## The catch

{nuance}

<!-- internal-links -->

## Related reading

- [Another piece](/another-piece/) — more on this

<!-- tldr -->

## At a glance

- **The shift:** {tldr}

## Sources
[1] Example. https://example.com
"""

LINK = "[the payback math](/the-payback-math/)"


def article(*, date="2026-10-24", lead="Carriers are leaving whole regions because reinsurance costs "
                                     "reset what they will cover. Florida gives 120 days of notice.",
            tension="A carrier must give 120 days of warning before a policy ends.",
            tactical="Watch the postmark: 120 days is the whole case.",
            nuance="The clock buys time, not cover, and 120 days is not a national rule.",
            tldr="120 days in Florida."):
    return BASE.format(date=date, lead=lead, tension=tension, tactical=tactical, nuance=nuance,
                       tldr=tldr)


# ─────────────────────────────────────────────────────────────────────────────
# a figure is stated once
# ─────────────────────────────────────────────────────────────────────────────

def test_a_figure_restated_across_three_sections_fails():
    report = shape.problems(article())
    assert report["held"] is True
    assert any("120 days" in f and "restated in" in f for f in report["fails"]), report["fails"]


def test_a_figure_in_the_lead_and_the_body_once_passes():
    report = shape.problems(article(tension="A carrier redraws a regional fire map.",
                                    tactical="Watch the postmark against the end date.",
                                    nuance="The clock buys time, not a free year."))
    assert not any("120 days" in f for f in report["fails"]), report["fails"]


def test_the_tldr_may_summarise_a_figure():
    """The summary section is allowed to repeat a number: that is what a summary is for."""
    report = shape.problems(article(tension="A carrier redraws a regional fire map.",
                                    tactical="Watch the postmark against the end date.",
                                    nuance="The clock buys time, not a free year.",
                                    tldr="120 days in Florida, and the clock runs from the end date."))
    assert not any("120 days" in f for f in report["fails"]), report["fails"]


def test_units_normalise_so_a_restatement_is_seen():
    assert shape.figures("120 days") == shape.figures("120-day")
    assert shape.figures("$37,270") == shape.figures("$37270")


def test_two_sections_sharing_three_figures_suggests_a_table():
    report = shape.problems(article(
        tension="The bill runs $37,270 against $3,805 for 122 hours of work.",
        tactical="Read the postmark.",
        nuance="The bill runs $37,270 against $3,805 for 122 hours of work."))
    assert any("comparison table" in a for a in report["advisories"]), report["advisories"]


# ─────────────────────────────────────────────────────────────────────────────
# the closure lands on a decision
# ─────────────────────────────────────────────────────────────────────────────

def test_a_body_with_no_inline_link_fails():
    report = shape.problems(article())
    assert any("inline internal link" in f for f in report["fails"]), report["fails"]


def test_a_body_carrying_a_decision_link_passes():
    report = shape.problems(article(
        tension="A carrier redraws a regional fire map.",
        tactical="Watch the postmark against the end date.",
        nuance="The clock buys time, not a free year. " + LINK + " runs the same sum from the other side."))
    assert not any("inline internal link" in f for f in report["fails"]), report["fails"]


def test_the_generated_related_reading_block_does_not_count_as_the_decision_link():
    """Every article has one, so it proves nothing about the piece landing on an action."""
    report = shape.problems(article())
    assert any("Related-reading block does not count" in f for f in report["fails"])


# ─────────────────────────────────────────────────────────────────────────────
# the opening advisory (never a hold)
# ─────────────────────────────────────────────────────────────────────────────

def test_an_opening_that_stacks_figures_is_flagged_not_held():
    report = shape.problems(article(
        lead="Florida gives 120 days, California 75 and Washington 60 days of warning."))
    assert any("figures" in a and "opening" in a.lower() for a in report["advisories"])
    assert not any("opening" in f for f in report["fails"])


def test_an_opening_with_no_cause_is_flagged():
    report = shape.problems(article(lead="Florida gives 120 days of warning before a policy ends."))
    assert any("WHY" in a for a in report["advisories"]), report["advisories"]


# ─────────────────────────────────────────────────────────────────────────────
# grandfathering
# ─────────────────────────────────────────────────────────────────────────────

def test_an_artifact_before_the_standard_is_reported_but_never_held(tmp_path):
    text = article(date="2026-10-01")
    report = shape.problems(text)
    assert report["held"] is False
    path = tmp_path / "2026-10-01_x.md"
    path.write_text(text)
    assert shape.failures(path) == []


def test_a_held_artifact_fails_the_gate(tmp_path):
    path = tmp_path / "2026-10-24_x.md"
    path.write_text(article())
    fails = shape.failures(path)
    assert fails and any("120 days" in f for f in fails)
