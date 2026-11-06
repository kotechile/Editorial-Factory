#!/usr/bin/env python3
"""The pre-publish gate: what it decides, and that it decides it safely.

Policy under test (owner, 2026-10-10): an article that fails the mechanical gates is rewritten once,
and if it still fails it is held back as a draft — it is never published un-evaluated, and the
rewrite is never allowed to damage the artifact it edits.
"""
from __future__ import annotations

import pathlib
import subprocess
import sys
import types

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import publish_gate as pg  # noqa: E402

GOOD = """---
title: "Battery Sizing For The Loads You Actually Own"
primary_keyword: battery sizing
persona: pro_homeowner
---

## The number everyone uses

A home battery is sized against the critical loads it must carry. That is a short list. Your annual
bill is a long one. So the two numbers differ, and the second one is the one you can check.

<!-- tension -->

The installer quotes a year of consumption. The outage does not last a year. It lasts three days.

## What to do instead

List the loads. Add the hours. Then size the bank for that list. Keep the fridge on. Drop the oven.

<!-- tldr -->

Size the bank for the outage, not for the year.

## Sources

1. U.S. EIA FAQ: average residential electricity use. https://www.eia.gov/tools/faqs/
2. FEMA, Power Outages. https://www.ready.gov/power-outages
"""

DENSE = GOOD.replace(
    "A home battery is sized against the critical loads it must carry. That is a short list.",
    "Notwithstanding the considerable methodological complexity inherent in contemporary residential "
    "battery-sizing methodologies, practitioners invariably underestimate the consequences of "
    "uninterrupted critical-load requirements during extended infrastructural interruptions.")


@pytest.fixture()
def repo(tmp_path, monkeypatch):
    """A throwaway repo root, so nothing here touches the real artifacts."""
    (tmp_path / "published").mkdir()
    (tmp_path / "context" / "drafts").mkdir(parents=True)
    monkeypatch.setattr(pg, "ROOT", tmp_path)
    monkeypatch.setattr(pg, "voice_problems", lambda: {})
    return tmp_path


def write(repo, name="2026-10-11_battery-sizing.md", text=GOOD):
    path = repo / "published" / name
    path.write_text(text)
    return path


def test_a_clean_artifact_publishes(repo):
    write(repo)
    report = pg.gate("battery-sizing", root=repo)
    assert report["verdict"] == "publish" and report["failures"] == []


def test_a_missing_artifact_cannot_publish(repo):
    report = pg.gate("never-written", root=repo)
    assert report["verdict"] == "no-artifact"
    assert "no artifact" in report["failures"][0]


def test_missing_sources_is_a_publish_failure(repo):
    write(repo, text=GOOD.split("## Sources")[0])
    report = pg.gate("battery-sizing", root=repo, rewrite=False)
    assert report["verdict"] == "draft"
    assert any("Sources" in f for f in report["failures"])


def test_a_banned_ai_tell_is_a_publish_failure(repo):
    write(repo, text=GOOD.replace("## What to do instead", "## What to do instead\n\nMoreover, "
                                                             "this is a game-changing shift."))
    report = pg.gate("battery-sizing", root=repo, rewrite=False)
    assert report["verdict"] == "draft"
    assert any("game-changing" in f or "moreover" in f for f in report["failures"])


def test_dense_prose_is_a_publish_failure(repo):
    write(repo, text=DENSE)
    report = pg.gate("battery-sizing", root=repo, rewrite=False)
    assert report["verdict"] == "draft"
    assert any("accessibility" in f for f in report["failures"])


def test_a_voice_problem_is_a_publish_failure(repo, monkeypatch):
    write(repo)
    monkeypatch.setattr(pg, "voice_problems",
                        lambda: {"published/2026-10-11_battery-sizing.md": ["the body reads as an "
                                                                            "advisor"]})
    report = pg.gate("battery-sizing", root=repo, rewrite=False)
    assert report["verdict"] == "draft"
    assert any("voice:" in f for f in report["failures"])


def test_one_rewrite_clears_the_gate(repo, monkeypatch):
    """The whole point: try to fix it before refusing to publish it."""
    path = write(repo, text=DENSE)
    calls = []

    def fake_rewrite(p, **_):
        calls.append(p)
        p.write_text(GOOD)
        return {"attempted": True, "verdict": "rewritten", "flesch_after": 62.0, "command": "stub"}

    monkeypatch.setattr(pg, "attempt_rewrite", fake_rewrite)
    report = pg.gate("battery-sizing", root=repo)
    assert calls == [path]
    assert report["verdict"] == "publish-after-rewrite" and report["failures"] == []


def test_a_failed_rewrite_still_holds_the_article(repo, monkeypatch):
    write(repo, text=DENSE)
    monkeypatch.setattr(pg, "attempt_rewrite",
                        lambda p, **_: {"attempted": True, "verdict": "no-change", "command": "stub"})
    report = pg.gate("battery-sizing", root=repo)
    assert report["verdict"] == "draft"
    assert any("accessibility" in f for f in report["failures"])


def test_rewrite_is_surgical_frontmatter_and_sources_untouched(repo, monkeypatch):
    """A frontier model must never re-emit the artifact's seals or its Sources list — and the
    staging file must never land on the artifact's OWN tracked draft/_final pair (it did once, and
    the cleanup deleted them)."""
    path = write(repo)
    original_fm, original_body, original_sources = pg._split(path.read_text())
    drafts = repo / "context" / "drafts"
    sentinel_draft = drafts / "2026-10-11_battery-sizing_draft.md"
    sentinel_final = drafts / "2026-10-11_battery-sizing_final.md"
    sentinel_draft.write_text("the run's own draft — not the gate's to touch")
    sentinel_final.write_text("the run's own final — not the gate's to touch")

    def fake_run(cmd, **kwargs):
        staged = repo / cmd[-1]
        assert staged.name != sentinel_draft.name        # staged somewhere of its own
        staged.with_name(staged.name.replace("_draft.md", "_final.md")).write_text(
            original_fm + "\n\n## The number everyone uses\n\nA shorter body.\n\n" + original_sources)
        return subprocess.CompletedProcess(cmd, 0, stdout="WROTE stub", stderr="")

    monkeypatch.setattr(pg.subprocess, "run", fake_run)
    result = pg.attempt_rewrite(path)

    fm, body, sources = pg._split(path.read_text())
    assert result["verdict"] == "rewritten"
    assert fm == original_fm and sources == original_sources     # seals and audit trail intact
    assert "A shorter body." in body and original_body != body
    assert sentinel_draft.read_text().startswith("the run's own draft")
    assert sentinel_final.read_text().startswith("the run's own final")
    assert not [p for p in drafts.iterdir() if "gate-rewrite" in p.name]   # its own files cleaned up


def test_rewrite_does_not_run_on_a_live_post(repo, monkeypatch):
    """gate(rewrite=False) is what wp_draft passes for an already-published post."""
    write(repo, text=DENSE)
    monkeypatch.setattr(pg, "attempt_rewrite",
                        lambda p, **_: pytest.fail("the gate rewrote a live post"))
    report = pg.gate("battery-sizing", root=repo, rewrite=False)
    assert report["verdict"] == "draft" and report["rewrite"] is None


def test_a_grandfathered_article_is_never_held_or_rewritten_for_its_headline(repo, monkeypatch):
    """Owner, 2026-10-10: the headline standard applies to future articles only — an older piece is
    scored and reported, never rewritten and never held on style."""
    write(repo, name="2026-10-05_old-style.md",
          text=GOOD.replace('title: "Battery Sizing For The Loads You Actually Own"',
                            'title: "The Complicated Story Of How Battery Sizing Works In Every '
                            'Modern Home Across The Country Today"'))
    monkeypatch.setattr(pg, "title_candidates",
                        lambda *a, **k: pytest.fail("the gate re-cut a grandfathered headline"))
    monkeypatch.setattr(pg, "attempt_rewrite",
                        lambda *a, **k: pytest.fail("the gate rewrote a grandfathered article"))
    report = pg.gate("old-style", root=repo)
    assert report["verdict"] == "publish"
    assert report["title"]["grandfathered"] is True and report["title"]["hold"] is False


def test_a_new_article_with_a_broken_headline_is_held(repo, monkeypatch):
    """From ENFORCED_FROM on, a headline that is not a headline (17 words) holds the article."""
    write(repo, name="2026-10-11_new-style.md",
          text=GOOD.replace('title: "Battery Sizing For The Loads You Actually Own"',
                            'title: "The Complicated Story Of How Battery Sizing Works In Every '
                            'Modern Home Across The Country Today"'))
    monkeypatch.setattr(pg, "title_candidates", lambda *a, **k: [])
    report = pg.gate("new-style", root=repo)
    assert report["verdict"] == "draft"
    assert any("headline" in f for f in report["failures"])


def test_artifact_lookup_prefers_the_published_copy(repo):
    (repo / "context" / "drafts" / "2026-10-11_battery-sizing_final.md").write_text(GOOD)
    published = write(repo)
    assert pg.artifact_for("battery-sizing", repo) == published


def test_banned_list_comes_from_verify_sh():
    """One source of truth: the list is parsed out of the repo's own gate, not duplicated here."""
    phrases = pg.banned_phrases()
    assert "game-changing" in phrases and "delve into" in phrases


# ─────────────────── the reader-side critic is wired into the push (owner, 2026-11-06) ───────────────────
# The pieces the owner called hard to read cleared every other gate, so the shape checks live in
# scripts/readability_critic.py and are re-run here. These two cases pin the wiring in both directions:
# a summary at the foot of the page does not publish, and the same copy with the summary under the lede
# does. The house fixture above is dated before the standard, so it is grandfathered and unaffected.
NEW_SHAPE = """---
title: "Battery Sizing For The Loads You Own"
persona: pro_homeowner
date: 2026-11-06
---

<!-- lead -->
A home battery is sized against the critical loads it must carry, and that list is much shorter than a year of your bill [1]. The installer who quotes the year has answered a question you did not ask.

<!-- tldr -->

## At a glance

- **The shift:** Installers size the bank against annual use, not against the outage.
- **The number:** Three days is the outage the critical-load list has to carry.
- **The risk:** a year of consumption oversizes the bank and hides the loads that matter.

<!-- tension -->

## The number everyone uses

The installer quotes a year of consumption, and the outage it has to ride through lasts about three days [1]. The list of loads you cannot lose is short, and sizing against the year buries it under a figure nobody can check.

<!-- tactical-insight -->

## What I'd watch

The installers closest to this quote a critical-load list before they quote a bank size. I keep coming back to how rarely the list is written down, and [the sizing planner](/battery-sizing-planner/) is where that arithmetic gets done in public.

<!-- nuanced-takeaway -->

## The catch

A three-day outage is an assumption, and a longer one changes the answer [2]. My reading is that the assumption is worth stating out loud.

## Sources

1. U.S. Energy Information Administration FAQ — https://www.eia.gov/tools/faqs/
2. Federal Emergency Management Agency, Power Outages — https://www.ready.gov/power-outages
"""


def new_shape(**overrides) -> str:
    text = NEW_SHAPE
    for key, value in overrides.items():
        text = text.replace(value[0], value[1])
    return text


def test_the_summary_under_the_lede_publishes(repo):
    path = write(repo, name="2026-11-06_battery-sizing.md", text=NEW_SHAPE)
    assert pg.text_failures(path) == []


def test_a_summary_at_the_foot_of_the_piece_holds_the_push(repo):
    # The exact shape the owner reported: everything present, the executive summary last.
    text = NEW_SHAPE
    glance = text[text.index("<!-- tldr -->"):text.index("<!-- tension -->")]
    foot = text.replace(glance, "")
    foot = foot.replace("<!-- nuanced-takeaway -->", glance + "<!-- nuanced-takeaway -->")
    path = write(repo, name="2026-11-06_battery-sizing-foot.md", text=foot)
    failures = pg.text_failures(path)
    assert any("critic:" in f and ("immediately under the lede" in f or "out of order" in f)
               for f in failures), failures


def test_a_two_statistic_bullet_holds_the_push(repo):
    text = NEW_SHAPE.replace(
        "- **The number:** Three days is the outage the critical-load list has to carry.",
        "- **The number — 3 days at 41% of annual use:** the outage the critical-load list has to carry.")
    path = write(repo, name="2026-11-06_battery-sizing-bullet.md", text=text)
    failures = pg.text_failures(path)
    assert any("one metric per bullet" in f for f in failures), failures


def test_the_gate_reports_the_prose_findings_without_holding_them(repo, monkeypatch):
    # A read-twice sentence is advisory: it goes to the rewrite, never to the verdict.
    text = NEW_SHAPE.replace(
        "The list of loads you cannot lose is short,",
        "A gate is one shared function rather than a share of one, and the list of loads you cannot lose is short,")
    path = write(repo, name="2026-11-06_battery-sizing-prose.md", text=text)
    assert pg.text_failures(path) == []
    import readability_critic as critic
    notes = critic.advisories(path)
    assert any("read_twice" in n for n in notes), notes
