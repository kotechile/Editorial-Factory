#!/usr/bin/env python3
"""The headline standard, pinned. Every rule the owner listed is one test here.

The point of scoring headlines mechanically is that the drafting stage, the Loop 3 rewrite and the
publish gate all measure the same thing — and that a title which promises something the article never
says cannot pass, however well it reads.
"""
from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import headline_score as hs  # noqa: E402

BODY = ("## By the numbers\n\n"
        "- **29.1% — FAIR Plan hike:** premiums rise Oct 15, 2026 [1].\n"
        "- **700,000 homes** sit on the plan [2].\n\n"
        "## The catch\n\n"
        "California FAIR Plan premiums jump for homeowners who cannot buy private cover, and the "
        "plan's assessment mechanism moves the cost onto every policyholder in the state. " * 8)


def test_a_strong_headline_scores_strong():
    r = hs.score("California FAIR Plan Premiums Jump 29.1%", body=BODY)
    assert r["verdict"] == "STRONG" and r["score"] == 100 and r["failures"] == []


def test_the_6_word_core_rule_bites():
    r = hs.score("Why 70% of Startup Options Go Unexercised", body=BODY)
    assert any("core headline <= 6 words" in f for f in r["failures"])


def test_subtitle_does_not_count_against_the_core():
    r = hs.score("Battery Sizing: Your Installer Uses The Wrong Number", body=BODY)
    assert r["core_words"] == 2 and not any("core headline" in f for f in r["failures"])


def test_opening_on_a_filler_article_is_a_failure():
    r = hs.score("The Agent Safety Gate Moves State", body=BODY)
    assert any("opens on substance" in f for f in r["failures"])
    assert hs.score("Agent Safety Gate Moves State", body=BODY)["score"] > r["score"]


def test_length_ceilings_are_reported():
    long_title = "Washington Cuts the Tariff on the Goods and the Fee on the Ship Snaps Back"
    r = hs.score(long_title, body=BODY)
    assert r["words"] > 10 and r["chars"] > 60
    assert any("<= 10 words" in f for f in r["failures"])


def test_hook_is_required():
    flat = hs.score("Solar Panels Are Available in Stores", body=BODY)
    assert any("carries a hook" in f for f in flat["failures"])


def test_loss_aversion_counts_as_a_hook():
    r = hs.score("Your Battery Sizing Is the Silent Cost", body=BODY)
    assert not any("carries a hook" in f for f in r["failures"])


def test_curiosity_counts_as_a_hook():
    r = hs.score("Why Your Battery Sizing Fails", body=BODY)
    assert not any("carries a hook" in f for f in r["failures"])


def test_a_number_is_expected_when_the_article_states_one():
    r = hs.score("Your Battery Sizing Is Wrong", body=BODY)
    assert any("a number anchors it" in f for f in r["failures"])


def test_named_subject_counts_as_calling_the_reader_out():
    r = hs.score("SpaceX Unlocks Six Windows, Not One", body=BODY)
    assert not any("names the reader" in f for f in r["failures"])


def test_bait_and_switch_is_caught():
    """A headline about something the article never mentions must fail, however punchy it is."""
    r = hs.score("Your Mortgage Rate Collapses Overnight", body=BODY)
    assert any("the promise is in the article" in f for f in r["failures"])


def test_keyword_rule_only_applies_when_a_keyword_is_declared():
    assert hs.score("Battery Sizing Is Wrong", body=BODY)["failures"] == \
        hs.score("Battery Sizing Is Wrong", body=BODY)["failures"]
    r = hs.score("Battery Sizing: The Wrong Number", body=BODY, keyword="battery sizing")
    assert not any("keyword" in f for f in r["failures"])
    r2 = hs.score("Solar Panels Are Wrong", body=BODY, keyword="battery sizing")
    assert any("keyword" in f for f in r2["failures"])


def test_filler_words_are_penalised():
    plain = hs.score("Battery Sizing Is Wrong", body=BODY)["score"]
    fluffed = hs.score("Battery Sizing Is Just About Very Wrong", body=BODY)["score"]
    assert fluffed < plain


def test_short_body_skips_the_honesty_rule():
    """A draft scored before its body exists must not fail on 'the promise is in the article'."""
    r = hs.score("Your Battery Sizing Is Wrong", body="Too short to judge.")
    assert not any("the promise is in the article" in f for f in r["failures"])


def test_artifact_title_reads_frontmatter():
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        p = pathlib.Path(tmp) / "2026-10-11_x.md"
        p.write_text('---\ntitle: "Your Battery Sizing Is Wrong"\nprimary_keyword: battery sizing\n---\n\nBody.\n')
        title, body, keyword = hs.artifact_title(p)
        assert title == "Your Battery Sizing Is Wrong" and keyword == "battery sizing"
