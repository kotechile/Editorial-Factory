#!/usr/bin/env python3
"""What the reviewer audit actually catches — pinned against the artifacts that produced each class.

Every case here is a real failure from the desk's own corpus, not a hypothetical. The point of the
suite is direction: a lost figure must fail, a faithful rewrite must pass, and a legitimate round of
a figure (26.92 -> 27) must not be called a loss, or the gate becomes noise the next reviewer
ignores. The gate is also the enforcement for rules that used to live only as prose in
`skills/claude_humanizer.md` §7, so the classes that recurred after being documented are the ones
tested first.

    python3 scripts/test_review_audit.py
"""
from __future__ import annotations

import pathlib
import sys

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import review_audit as ra  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
DRAFTS = ROOT / "context" / "drafts"


def article(*, body_prose: str, title: str = "A Short Headline") -> str:
    """A minimal artifact with the desk's markers, a numbers section and one source."""
    return (
        "---\n"
        f'title: "{title}"\n'
        "vertical: test_vertical\n"
        "date: 2026-10-27\n"
        "---\n\n"
        "<!-- lead -->\n"
        f"{body_prose}\n\n"
        "<!-- tension -->\n\n## The big picture:\n\n"
        "A second paragraph with one figure, 62.1% of trips [1]. My read is that the shape holds.\n\n"
        "<!-- tactical-insight -->\n\n## What I'd watch:\n\n"
        "Another paragraph that carries 39.58 dollars an hour [2]. What I am watching next is the "
        "window.\n\n"
        "<!-- nuanced-takeaway -->\n\n## The catch\n\n"
        "A caveat paragraph, 13.41 cents a kilowatt hour [2]. I keep the caveat in view.\n\n"
        "<!-- tldr -->\n\n## At a glance\n\n"
        "- **The Big Shift:** one line [1].\n\n"
        "## Sources\n\n"
        "[1] Example — https://example.org/a\n"
        "[2] Example — https://example.org/b\n"
    )


DRAFT = article(body_prose=(
    "An estimated arrival misses by 26.92 hours beyond a week [1], and the share runs from 22.5% "
    "down to 10.9% of the voyage [1]. At 24 to 72 hours the figure is 6.89 hours [1]."
))


def test_a_faithful_rewrite_passes():
    """Same facts, re-voiced: no hard failure."""
    final = article(body_prose=(
        "Beyond a week the guess misses by 26.92 hours [1]. Put the same error as a share of the "
        "voyage and it runs from 22.5% down to 10.9% [1]; at 24 to 72 hours it is 6.89 hours [1]."
    ))
    result = ra.audit(DRAFT, final, min_words=0)
    assert result["ok"], result["hard"]


def test_a_lost_share_figure_fails_with_its_draft_sentence():
    """The 2026-10-27 class: "22.5% down to 10.9%" became "roughly a tenth to a fifth"."""
    final = article(body_prose=(
        "Beyond a week the guess misses by 26.92 hours [1]. As a share it stays at roughly a tenth "
        "to a fifth of the voyage [1]; at 24 to 72 hours it is 6.89 hours [1]."
    ))
    result = ra.audit(DRAFT, final, min_words=0)
    lost = [h for h in result["hard"] if "figure lost" in h]
    assert any("22.5%" in h for h in lost) and any("10.9%" in h for h in lost)
    # the feedback has to quote the claim, not just the number
    assert any("down to 10.9%" in h for h in lost)


def test_a_rounded_figure_is_not_a_loss():
    """26.92 -> "about 27 hours" is legitimate rounding, not a dropped claim."""
    final = article(body_prose=(
        "Beyond a week the guess misses by 27 hours [1]. As a share it runs from 22.5% down to "
        "10.9% [1]; at 24 to 72 hours it is 6.89 hours [1]."
    ))
    result = ra.audit(DRAFT, final, min_words=0)
    assert not [h for h in result["hard"] if "figure lost" in h], result["hard"]


def test_an_invented_figure_is_reported():
    final = article(body_prose=(
        "An estimated arrival misses by 26.92 hours beyond a week [1], and 22.5% down to 10.9% of "
        "the voyage [1]. At 24 to 72 hours the figure is 6.89 hours [1], and 84% of lanes are late."
    ))
    result = ra.audit(DRAFT, final, min_words=0)
    assert any("not in the draft or the brief" in a and "84" in a for a in result["advisories"])


def test_a_figure_the_brief_authorises_is_not_invented():
    brief = "| 1 | study | https://example.org/a | 2026-10-27 | 84% | lanes late |"
    final = article(body_prose=(
        "An estimated arrival misses by 26.92 hours beyond a week [1], 22.5% down to 10.9% of the "
        "voyage [1], and 6.89 hours at 24 to 72 hours [1], with 84% of lanes late."
    ))
    result = ra.audit(DRAFT, final, brief, min_words=0)
    assert not [a for a in result["advisories"] if "84" in a], result["advisories"]


def test_a_dropped_citation_fails():
    final = article(body_prose=(
        "An estimated arrival misses by 26.92 hours beyond a week [1], 22.5% down to 10.9% of the "
        "voyage [1], and 6.89 hours at 24 to 72 hours [1]."
    )).replace("[2] Example — https://example.org/b", "")
    result = ra.audit(DRAFT, final, min_words=0)
    # the marker [2] survives in the body, but its source row is gone: a source line changed
    assert any("source line" in h for h in result["hard"]) or any("citation [2]" in h for h in result["hard"])


def test_a_self_graded_gate_report_is_a_failure_not_a_report():
    final = DRAFT.replace("26.92", "26.92").rstrip() + (
        "\n\n## Gate report\n\nlead: PASS — direct opening.\ntldr: PASS — schema followed.\n"
    )
    result = ra.audit(DRAFT, final, min_words=0)
    assert any("Gate report" in h for h in result["hard"])


def test_leaked_deliberation_is_a_failure():
    final = article(body_prose=(
        "The user wants me to rewrite this draft. Let me analyze what I need to do. An estimated "
        "arrival misses by 26.92 hours beyond a week [1], 22.5% down to 10.9% of the voyage [1], "
        "and 6.89 hours at 24 to 72 hours [1]."
    ))
    result = ra.audit(DRAFT, final, min_words=0)
    assert any("leaked deliberation" in h for h in result["hard"])


def test_rhythm_variance_is_measured_not_just_the_mean():
    """Uniform 15-word sentences: mean and short% both look healthy, variance collapses."""
    flat = " ".join(
        "The crew reviewed the arrival estimate again before the ship reached the next port."
        for _ in range(9))
    varied = (
        "It missed. The arrival estimate came back 26.92 hours late on a voyage past a week, and "
        "nobody on the desk was surprised, because the error had been climbing with distance all "
        "along [1]. Why? Because every extra day adds guesswork. 22.5% down to 10.9% is the share "
        "it costs [1]. Six point eight nine hours is the 24-to-72-hour figure [1]."
    )
    final_flat = article(body_prose=flat + " 62.1% of trips [1]. 39.58 dollars [2]. 13.41 cents [2].")
    final_varied = article(body_prose=varied + " 62.1% of trips [1]. 39.58 dollars [2]. 13.41 cents [2].")
    flat_r = ra.audit(DRAFT, final_flat, min_words=0)["flow"]["rhythm"]
    varied_r = ra.audit(DRAFT, final_varied, min_words=0)["flow"]["rhythm"]
    assert flat_r["sd"] < varied_r["sd"]
    assert varied_r["short_pct"] > flat_r["short_pct"]


def test_a_missing_observer_cue_fails_the_stage():
    """verify.sh §9 fails a build without one; the reviewer must not hand it a body that will."""
    final = article(body_prose=(
        "An estimated arrival misses by 26.92 hours beyond a week [1], 22.5% down to 10.9% of the "
        "voyage [1], and 6.89 hours at 24 to 72 hours [1]."
    )).replace("My read is that the shape holds.", "The shape holds across the bands.")
    result = ra.audit(DRAFT, final, min_words=0)
    assert any("no first-person sentence" in h for h in result["hard"]), result["hard"]


def test_an_observer_cue_in_any_first_person_verb_passes():
    """The gate must read the sentence, not its own verb list ("What I find limiting…")."""
    final = article(body_prose=(
        "An estimated arrival misses by 26.92 hours beyond a week [1], 22.5% down to 10.9% of the "
        "voyage [1], and 6.89 hours at 24 to 72 hours [1]."
    )).replace("My read is that the shape holds.",
               "What I find limiting about the tolerance is how little it buys.")
    assert ra.audit(DRAFT, final, min_words=0)["cues"]["missing"] == []


def test_an_observer_cue_in_the_writers_own_words_passes():
    final = article(body_prose=(
        "An estimated arrival misses by 26.92 hours beyond a week [1], 22.5% down to 10.9% of the "
        "voyage [1], and 6.89 hours at 24 to 72 hours [1]."
    ))
    assert ra.audit(DRAFT, final, min_words=0)["cues"]["missing"] == []


def test_a_sentence_repeated_verbatim_is_a_failure():
    """The 2026-10-27 reviewer output carried the same 27-word sentence in two sections."""
    shared = ("In percentage terms the same table runs from 22.5% down to 10.9%, so the estimate "
              "stays at roughly a tenth to a fifth of the voyage at every length [1].")
    final = article(body_prose=(
        "Beyond a week the guess misses by 26.92 hours [1]. " + shared + " At 24 to 72 hours it is "
        "6.89 hours [1], and the tactical window below is why that matters."
    )).replace("What I am watching next is the window.", "What I am watching next is the window. " + shared)
    result = ra.audit(DRAFT, final, min_words=0)
    assert any("repeated verbatim" in h for h in result["hard"]), result["hard"]


def test_boilerplate_observer_cues_are_flagged():
    final = article(body_prose=(
        "An estimated arrival misses by 26.92 hours [1]. The part I keep circling is the share: "
        "22.5% down to 10.9% of the voyage [1], and 6.89 hours at 24 to 72 hours [1]."
    ))
    result = ra.audit(DRAFT, final, min_words=0)
    assert any("boilerplate observer cue" in a for a in result["advisories"])


def test_score_prefers_a_clean_varied_rewrite_over_a_flat_one():
    """Two candidates that both keep the facts: the one that keeps a rhythm wins."""
    varied = article(body_prose=(
        "Beyond a week the guess misses by 26.92 hours [1]. It runs from 22.5% down to 10.9% of the "
        "voyage [1]. Short lanes, though, are a different animal: nobody plans a truck leg from a "
        "share that only bites on the ocean [1]. At 24 to 72 hours the figure is 6.89 hours [1], "
        "which is 11.97 hours at three to seven days [1]. A planner reads that table twice before "
        "trusting a flat twelve-hour rule [1]."
    ))
    flat = article(body_prose=(
        "The guess misses by 26.92 hours beyond a week and the share runs from 22.5% down to 10.9% "
        "of the voyage and at 24 to 72 hours the figure is 6.89 hours and at three to seven days "
        "the figure is 11.97 hours for the same table and the same study and the same measure today."
    ))
    assert ra.score(ra.audit(DRAFT, varied, min_words=0)) >= ra.score(ra.audit(DRAFT, flat, min_words=0))


@pytest.mark.parametrize("slug", [
    "2026-10-27_your-eta-misses-27-hours",          # lost 22.5% / 10.9%
    "2026-10-27_your-gpu-break-even-is-37-percent-busy",  # lost 13.41 / 22,269, filler x4
])
def test_the_real_artifacts_that_failed_now_fail_the_audit(slug):
    """The fixtures that motivated the gate. Skipped when the corpus is not checked out."""
    draft = DRAFTS / f"{slug}_draft.md"
    final = DRAFTS / f"{slug}_final.md"
    if not (draft.exists() and final.exists()):
        pytest.skip(f"{slug} not in this checkout")
    result = ra.audit(draft.read_text(), final.read_text())
    assert not result["ok"], "the audit passed a rewrite that lost load-bearing figures"


def test_the_audit_runs_clean_on_a_published_artifact_that_was_hand_checked():
    """Direction check: an artifact with no loss and varied rhythm must not fail the hard gate."""
    final = article(body_prose=(
        "Beyond a week the guess misses by 26.92 hours [1]. Short lanes are different. The share "
        "runs from 22.5% down to 10.9% of the voyage [1], and 6.89 hours covers 24 to 72 [1]."
    ))
    assert ra.audit(DRAFT, final, min_words=0)["ok"]


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q"]))
