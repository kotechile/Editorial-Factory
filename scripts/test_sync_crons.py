#!/usr/bin/env python3
"""
scripts/test_sync_crons.py — contract tests for the cron fleet reconciler.

Wired into `scripts/verify.sh` §8. These pin the properties that make the fleet autonomous:

  * every registry vertical's job instruction contains the full pipeline sequence, including the
    `synthesize_topics.py --seed` step — a step that is only in the SOP markdown can be skipped;
  * drift in the *instruction* is detected and reported, not just drift in the schedule (the
    create-only sync skipped existing jobs by name, so a template change never reached the fleet);
  * the reconciler is read-only under --check and never writes to the scheduler store.

No network, no scheduler writes: `plan()` is exercised against synthetic live-state lists.
"""

import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import sync_crons as sc  # noqa: E402

REGISTRY = sc.load_verticals()
BY_ID = {v["id"]: v for v in REGISTRY}


def live_entry(vertical, cadence, prompt=None, enabled=True, job_id="j1"):
    """A live-store entry. prompt=None means "in sync with the registry" for that vertical."""
    base = BY_ID.get(vertical, {"id": vertical, "label": vertical})
    return {
        "id": job_id,
        "name": sc.PREFIX + vertical,
        "vertical": vertical,
        "cadence": cadence,
        "enabled": enabled,
        "prompt": sc.prompt_for(base) if prompt is None else prompt,
    }


class PromptTemplate(unittest.TestCase):
    def test_instruction_names_the_whole_sequence_including_the_seed_step(self):
        prompt = sc.prompt_for({"id": "supply_chain", "label": "Supply Chain"})
        self.assertIn("radar_30day", prompt)
        self.assertIn("synthesize_topics.py --seed", prompt)
        self.assertIn("virality_judge", prompt)
        self.assertIn("fact_check", prompt)
        self.assertIn("story_draft", prompt)
        self.assertIn("claude_humanizer", prompt)
        self.assertLess(prompt.index("synthesize_topics --seed"), prompt.index("virality_judge"),
                        "the seed step must run before the Judge reads the file")

    def test_instruction_keeps_the_safety_rails(self):
        prompt = sc.prompt_for({"id": "agentic_ai", "label": "Agentic"})
        self.assertIn("@Simon approve", prompt)
        self.assertIn("do not publish without approval", prompt)
        self.assertIn("never scores", prompt)          # the helper cannot clear the >=8 gate
        self.assertIn("no valid pair", prompt)         # a legitimate outcome, not a failure

    def test_instruction_is_vertical_specific(self):
        prompt = sc.prompt_for({"id": "expat_cross_border_relocation", "label": "Expat"})
        self.assertIn("YYYY-MM-DD_expat_cross_border_relocation_signals.md", prompt)

    def test_every_registry_vertical_carries_the_seed_step(self):
        missing = [v["id"] for v in REGISTRY if "synthesize_topics.py --seed" not in sc.prompt_for(v)]
        self.assertEqual(missing, [], f"verticals whose job instruction would skip the seed step: {missing}")


class DriftDetection(unittest.TestCase):
    def test_in_sync_plan_is_empty(self):
        live = [live_entry(v["id"], v["cadence"]) for v in REGISTRY]
        missing, drifted, orphans, paused, stale = sc.plan(REGISTRY, live)
        self.assertEqual([missing, drifted, orphans, paused, stale], [[], [], [], [], []])

    def test_missing_vertical_is_reported(self):
        live = [live_entry(v["id"], v["cadence"]) for v in REGISTRY[:-1]]
        missing, *_ = sc.plan(REGISTRY, live)
        self.assertEqual([v["id"] for v, _c, _e in missing], [REGISTRY[-1]["id"]])

    def test_schedule_drift_is_reported(self):
        live = []
        for v in REGISTRY:
            cadence = "5 3 * * *" if v["id"] == "supply_chain" else v["cadence"]
            live.append(live_entry(v["id"], cadence))
        _m, drifted, *_ = sc.plan(REGISTRY, live)
        self.assertEqual([v["id"] for v, _c, _j in drifted], ["supply_chain"])

    def test_instruction_drift_is_reported(self):
        live = []
        for v in REGISTRY:
            prompt = "old instruction without the seed step" if v["id"] == "gpu_hardware" else None
            live.append(live_entry(v["id"], v["cadence"], prompt=prompt))
        *_, stale = sc.plan(REGISTRY, live)
        self.assertEqual([v["id"] for v, _j in stale], ["gpu_hardware"])

    def test_orphan_and_paused_are_separate_from_drift(self):
        live = [live_entry(v["id"], v["cadence"]) for v in REGISTRY]
        live.append(live_entry("home_systems_reno", "0 6 * * 1", job_id="retired"))
        live.append(live_entry("gpu_hardware", "0 7 * * 3", enabled=False))
        missing, drifted, orphans, paused, stale = sc.plan(REGISTRY, live)
        self.assertEqual([j["vertical"] for j in orphans], ["home_systems_reno"])
        self.assertEqual([j["vertical"] for _v, j in paused], ["gpu_hardware"],
                         "a paused job is left alone — it is not schedule drift")
        self.assertEqual([missing, drifted], [[], []])

    def test_registry_without_cadence_is_reported_not_crashed(self):
        registry = list(REGISTRY) + [{"id": "no_cadence_vertical", "label": "x"}]
        live = [live_entry(v["id"], v["cadence"]) for v in REGISTRY]
        missing, *_ = sc.plan(registry, live)
        self.assertEqual([v["id"] for v, _c, err in missing if err], ["no_cadence_vertical"])

    def test_check_mode_never_writes(self):
        calls = []
        original_run, original_check = sc.run, sc.CHECK
        sc.run = lambda cmd: calls.append(cmd)  # any scheduler mutation would land here
        try:
            sc.CHECK = True
            live = [live_entry(v["id"], "1 1 1 1 1") for v in REGISTRY]  # everything drifted
            missing, drifted, _o, _p, stale = sc.plan(REGISTRY, live)
            self.assertTrue(missing or drifted or stale)  # the plan is non-empty…
            self.assertEqual(calls, [])                   # …and nothing was written
        finally:
            sc.run, sc.CHECK = original_run, original_check


if __name__ == "__main__":
    unittest.main(verbosity=2)
