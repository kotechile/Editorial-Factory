#!/usr/bin/env python3
"""The Vibe lexicon at the publish gate: what it holds, what it grandfathers, and that a broken
install holds copy instead of passing it.

Policy under test:
  * a banned AI-ism or a throat-clearing opener in the reader-facing body fails the gate;
  * an artifact dated before `enforced_from` is scored but never held;
  * real domain terms (test harness, landscape design, EmPOWER, leverage ratio) are not violations;
  * a missing or partial lexicon fails CLOSED — unscorable copy is held, never published.
"""
from __future__ import annotations

import json
import pathlib
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import vibe_lexicon as vl  # noqa: E402

NEW = "2026-10-22_rates.md"
OLD = "2026-10-14_rates.md"

BODY_BANNED = "Operators delve into the ledger every quarter.\n"
BODY_OPENER = "Welcome to the desk. Rates move on Thursday.\n"
BODY_CLEAN = "The filing fee is $412. It clears in four business days.\n"
BODY_EXCEPTIONS = (
    "The test harness ran green. Landscape design budgets rose 12%. "
    "EmPOWER reimbursed $4,200. The leverage ratio is 3.2x.\n"
)


def test_banned_term_fails_a_new_artifact():
    fails, notes = vl.check(BODY_BANNED, path=NEW)
    assert fails and "delve" in fails[0]
    assert notes == []


def test_opener_fails_a_new_artifact():
    fails, _ = vl.check(BODY_OPENER, path=NEW)
    assert fails and any("opener" in f for f in fails)


def test_clean_copy_passes():
    assert vl.check(BODY_CLEAN, path=NEW) == ([], [])


def test_artifact_before_enforced_from_is_grandfathered_not_failed():
    fails, notes = vl.check(BODY_BANNED, path=OLD)
    assert fails == []
    assert notes and "grandfathered" in notes[0]


def test_domain_exceptions_are_masked():
    assert vl.check(BODY_EXCEPTIONS, path=NEW) == ([], [])


def test_frontmatter_date_is_used_when_the_filename_carries_none():
    body = "---\ndate: 2026-10-01\n---\n\n" + BODY_BANNED
    fails, notes = vl.check(body, path="rates.md")
    assert fails == [] and notes


def test_missing_lexicon_fails_closed(tmp_path, monkeypatch):
    monkeypatch.setattr(vl, "LEXICON_PATH", tmp_path / "nope.json")
    fails, notes = vl.check(BODY_CLEAN, path=NEW)
    assert fails and "missing" in fails[0]
    assert notes == []


def test_unparseable_lexicon_fails_closed(tmp_path, monkeypatch):
    broken = tmp_path / "lexicon.json"
    broken.write_text("{not json")
    monkeypatch.setattr(vl, "LEXICON_PATH", broken)
    fails, _ = vl.check(BODY_CLEAN, path=NEW)
    assert fails and "missing or unreadable" in fails[0]


def test_partial_lexicon_fails_closed(tmp_path, monkeypatch):
    partial = tmp_path / "lexicon.json"
    partial.write_text(json.dumps({"enforced_from": "2026-10-20", "banned": [], "openers": []}))
    monkeypatch.setattr(vl, "LEXICON_PATH", partial)
    fails, _ = vl.check(BODY_CLEAN, path=NEW)
    assert fails and "incomplete" in fails[0]


def test_the_repo_lexicon_scores_the_corpus():
    """The shipped lexicon must parse, carry its rules, and stay wired to the gate."""
    lex = json.loads((ROOT / "context" / "vibe" / "lexicon.json").read_text())
    assert lex["banned"] and lex["openers"] and lex["enforced_from"]
    assert vl.enforced_from() == lex["enforced_from"]
