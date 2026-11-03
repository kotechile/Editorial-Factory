#!/usr/bin/env python3
"""What the accessibility floor actually measures.

The floor is about the article's prose. Three machine-written blocks sit in every published artifact
and none of them is prose the writer chose: the frontmatter, the `## Sources` list, and the
`## Related reading` block the persistence pass injects after Loop 3 already measured and passed the
body. Counting the last one put 21 of 70 published artifacts under the floor while the per-run gate
said PASS — the desk's own floor has to be reproducible from the artifact.
"""
from __future__ import annotations

import pathlib
import sys

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import check_accessibility as ca  # noqa: E402

ARTICLE = """---
title: A Short Headline
primary_keyword: tco
---

## The setup

The plan is simple. You size the bank for the loads. Then you test it.

## Related reading

- [A Very Long And Complicated Internal Link Title](https://example.com/some-long-slug/) — more on Stuff
- [Another Considerably Overwritten Editorial Link Title](https://example.com/other-slug/) — more on Stuff

## Sources

1. A source that is long and lexically dense with considerable terminology.
"""


def test_machine_written_blocks_are_not_counted_as_prose(tmp_path):
    path = tmp_path / "a.md"
    path.write_text(ARTICLE)
    body = ca.body_of(str(path))
    assert "A Short Headline" not in body          # frontmatter
    assert "Related reading" not in body           # injected after the rewrite
    assert "A Very Long And Complicated" not in body
    assert "Sources" not in body
    assert "The plan is simple." in body           # the prose survives


def test_the_prose_alone_is_what_passes_or_fails(tmp_path):
    path = tmp_path / "a.md"
    path.write_text(ARTICLE)
    assert ca.measure(str(path))["flesch"] > 60     # short sentences, short words


def test_dense_prose_still_fails(tmp_path):
    """The floor must still bite: excluding the blocks cannot rescue a genuinely dense body."""
    dense = ARTICLE.replace(
        "The plan is simple. You size the bank for the loads. Then you test it.",
        "Notwithstanding the considerable methodological complexity inherent in contemporary "
        "battery-sizing methodologies, practitioners invariably underestimate the consequences "
        "of uninterrupted critical-load requirements during extended infrastructural outages.")
    path = tmp_path / "b.md"
    path.write_text(dense)
    assert ca.measure(str(path))["flesch"] < 50


# --- sentence rhythm: the direction Flesch never measures --------------------------------
# A body of short declaratives scores WELL on Flesch, so the readability floor alone can never
# catch it. These fixtures pin both halves: the staccato body must be flagged, the connected
# body must not be, and the flag must never hold a publish (it is advisory).

STACCATO = """---
title: Battery bank plan
---

You size the bank. You test it. Then you ship. It works. The loads matter. The bank holds.
The test runs. It passes. You ship. It works.
"""

CONNECTED = """---
title: Battery bank plan
---

You size the battery bank against the critical loads, and then you test it under the outage the
whole design exists to survive. The loads matter more than the headline capacity, because a bank
that carries the daily cycle but folds at hour nine is not sized at all. Most teams test the bank
at the wrong moment, and the test passes for a reason that has nothing to do with the design.
"""


def _write(tmp_path, name, text):
    path = tmp_path / name
    path.write_text(text)
    return str(path)


def test_staccato_body_trips_the_rhythm_advisory(tmp_path):
    diag = ca.measure(_write(tmp_path, "s.md", STACCATO))
    assert any("rhythm:" in w for w in diag["warnings"]), diag["warnings"]
    assert diag["sentence_mean"] < ca.RHYTHM_MEAN_MIN


def test_connected_prose_does_not_trip_the_rhythm_advisory(tmp_path):
    diag = ca.measure(_write(tmp_path, "c.md", CONNECTED))
    assert not any("rhythm:" in w for w in diag["warnings"]), diag["warnings"]
    assert diag["sentence_mean"] >= ca.RHYTHM_MEAN_MIN


def test_rhythm_is_advisory_and_never_holds_a_publish(tmp_path):
    """Choppy prose must be reported, not failed: the publish gate reads `fails` only."""
    diag = ca.measure(_write(tmp_path, "s2.md", STACCATO))
    assert not [f for f in diag["fails"] if "rhythm" in f]
    assert diag["verdict"] == "PASS"


# --- figure load: the failure Flesch rewards ------------------------------------------------
# Digits are short, low-syllable words, so a paragraph that walks the reader through a derivation
# scores WELL on Flesch while reading like a worksheet. Measured on the published corpus, the
# median share of prose sentences carrying a figure was 41% and 95 of 269 sat above 45%. These
# fixtures pin the measure: a derivation chain trips it, a body where the meaning gets its own
# sentence does not, the "By the numbers" bullets are never counted, and it stays advisory.

DERIVATION = """---
title: Standby draw
---

The household bought 10,791 kilowatt-hours in 2022. Five percent of that is 540 kilowatt-hours.
Holding one watt for a year takes 8.76 kilowatt-hours. Divide 540 by 8.76 and the answer is
61.6 watts. Forty chargers at 0.5 watts draw 20 watts. That is a third of 540 kilowatt-hours.
The high end is 1,079 kilowatt-hours, which is 123 watts of continuous draw all year long.
"""

MEANING_FIRST = """---
title: Standby draw
---

The household bought 10,791 kilowatt-hours in 2022, and the idle share of that is a steady draw
of about 62 watts running every hour of the year. Picture one old bulb left on in an empty room,
because that is the size of the thing nobody switched on. The obvious culprits, the wall
chargers, were capped at half a watt each in 2008. Forty of them now add up to a fraction of
the load the lab measures, so the hunt has to go where the whole watts are. That is the set-top
box, the receiver, and the old chest freezer in the basement. None of them is on a guide's list
of things to unplug. All of them are warm to the touch long after the room has gone dark.
"""


def test_derivation_chain_trips_the_figure_advisory(tmp_path):
    diag = ca.measure(_write(tmp_path, "d.md", DERIVATION))
    assert any("figure load:" in w for w in diag["warnings"]), diag["warnings"]
    assert diag["figure_pct"] > ca.FIGURE_DENSITY_MAX


def test_meaning_first_prose_does_not_trip_the_figure_advisory(tmp_path):
    diag = ca.measure(_write(tmp_path, "m.md", MEANING_FIRST))
    assert not any("figure load:" in w for w in diag["warnings"]), diag["warnings"]
    assert diag["figure_pct"] <= ca.FIGURE_DENSITY_MAX


def test_numbers_bullets_are_not_counted_as_prose(tmp_path):
    """The mandated 'By the numbers' block is where figures belong; counting it would flag every
    article that has one."""
    bullets = MEANING_FIRST + """
## By the numbers

- **62 to 123 watts — Always-on load:** The lab's share works out to a steady draw.
- **$93 to $187 — Annual cost:** The same band priced at the 2025 average rate.
- **$1.56 — One watt a year:** The lab's own rule, re-priced at today's rate.
"""
    diag = ca.measure(_write(tmp_path, "b2.md", bullets))
    assert diag["figure_pct"] == ca.measure(_write(tmp_path, "m2.md", MEANING_FIRST))["figure_pct"]


def test_figure_load_is_advisory_and_never_holds_a_publish(tmp_path):
    diag = ca.measure(_write(tmp_path, "d2.md", DERIVATION))
    assert not [f for f in diag["fails"] if "figure" in f]
    assert diag["verdict"] == "PASS"


# --- the numbers block: kept, but small ------------------------------------------------------
# Relaxing the block to "optional" removed it from the page and the owner noticed immediately
# (2026-11-03). It stays a house section; what it may not be is a four-bullet recap of the body.

def test_missing_numbers_block_is_reported(tmp_path):
    diag = ca.measure(_write(tmp_path, "nb.md", MEANING_FIRST))
    assert any("missing the '## By the numbers' block" in w for w in diag["warnings"]), diag["warnings"]


def test_a_three_bullet_numbers_block_clears_the_warning(tmp_path):
    body = MEANING_FIRST + """
## By the numbers

- **62 to 123 watts — The band:** Five to ten percent of a year of use [1].
- **$93 to $187 — What it costs:** The same band at the 2025 rate [1][7].
- **$1.56 — One watt, one year:** The lab's rule re-priced [2].
"""
    diag = ca.measure(_write(tmp_path, "nb3.md", body))
    assert not any("By the numbers" in w for w in diag["warnings"]), diag["warnings"]


def test_a_five_bullet_numbers_block_is_reported(tmp_path):
    body = MEANING_FIRST + """
## By the numbers

- **62 watts — a:** x [1].
- **123 watts — b:** y [1].
- **$93 — c:** z [1].
- **$187 — d:** w [1].
- **$1.56 — e:** v [2].
"""
    diag = ca.measure(_write(tmp_path, "nb5.md", body))
    assert any("carries 5 bullets" in w for w in diag["warnings"]), diag["warnings"]


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q"]))
