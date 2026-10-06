#!/usr/bin/env python3
"""
scripts/test_sync_crons.py — contract tests for the cron fleet reconciler.

Wired into `scripts/verify.sh` §8. These pin the properties that make the fleet autonomous:

  * every registry vertical's job instruction contains the full pipeline sequence, including the
    `synthesize_topics.py --seed` step — a step that is only in the SOP markdown can be skipped;
  * drift in the *instruction* is detected and reported, not just drift in the schedule (the
    create-only sync skipped existing jobs by name, so a template change never reached the fleet);
  * the reconciler is read-only under --check and never writes to the scheduler store;
  * the EVERGREEN fleet is a second, independent schedule reconciled from the same registry — its
    instruction carries the evidence floor and never inherits the news gate, a registry
    `*_enabled: false` flag is a real setting (the job must not exist), and the two fleets never
    share a (weekday, hour, minute) slot.

No network, no scheduler writes: `plan()` is exercised against synthetic live-state lists, and the
evergreen gate is only read as text.
"""

import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import sync_crons as sc  # noqa: E402

REGISTRY = sc.load_verticals()
BY_ID = {v["id"]: v for v in REGISTRY}


def live_entry(vertical, cadence, prompt=None, enabled=True, job_id="j1", fleet="news"):
    """A live-store entry. prompt=None means "in sync with the registry" for that vertical."""
    base = BY_ID.get(vertical, {"id": vertical, "label": vertical})
    prefix, prompt_fn = (sc.PREFIX, sc.prompt_for) if fleet == "news" else \
                        (sc.EVERGREEN_PREFIX, sc.evergreen_prompt_for)
    return {
        "id": job_id,
        "name": prefix + vertical,
        "vertical": vertical,
        "cadence": cadence,
        "enabled": enabled,
        "prompt": prompt_fn(base) if prompt is None else prompt,
    }


def live_news():
    return [live_entry(v["id"], v["cadence"]) for v in REGISTRY]


def live_evergreen():
    return [live_entry(v["id"], v["evergreen_cadence"], fleet="evergreen")
            for v in REGISTRY if v.get("evergreen_cadence")]


def plan_news(live, registry=None):
    return sc.plan(registry or REGISTRY, live)


def plan_evergreen(live, registry=None):
    return sc.plan(registry or REGISTRY, live, prefix=sc.EVERGREEN_PREFIX,
                   cadence_key="evergreen_cadence", enabled_key="evergreen_enabled",
                   prompt_fn=sc.evergreen_prompt_for)


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
        self.assertIn("NOT approval-gated", prompt)     # site + Supabase persist in the run
        self.assertIn("There is no social distribution step", prompt)  # channel removed 2026-10-06
        self.assertIn("never scores", prompt)           # the helper cannot clear the >=8 gate
        self.assertIn("no valid pair", prompt)          # a legitimate outcome, not a failure
        # No gate, and no social copy to surface: the LinkedIn/Reddit channel was removed, so a
        # prompt that still asks the run to stop and wait would dead-end every article.
        self.assertNotIn("@Simon approve", prompt)
        self.assertNotIn("surface the LinkedIn", prompt)
        self.assertIn("reader site (giniloh.com / wellroost.com", prompt)

    def test_instruction_is_vertical_specific(self):
        prompt = sc.prompt_for({"id": "expat_cross_border_relocation", "label": "Expat"})
        self.assertIn("YYYY-MM-DD_expat_cross_border_relocation_signals.md", prompt)

    def test_every_registry_vertical_carries_the_seed_step(self):
        missing = [v["id"] for v in REGISTRY if "synthesize_topics.py --seed" not in sc.prompt_for(v)]
        self.assertEqual(missing, [], f"verticals whose job instruction would skip the seed step: {missing}")


class EvergreenPromptTemplate(unittest.TestCase):
    def test_instruction_names_the_evergreen_sequence_without_the_news_gate(self):
        prompt = sc.evergreen_prompt_for({"id": "home_ops_execution", "label": "Home Ops"})
        self.assertIn("evergreen_topics", prompt)
        self.assertIn("evergreen_gate.py --brief", prompt)
        self.assertIn("fact_check", prompt)
        self.assertIn("story_draft", prompt)
        self.assertIn("claude_humanizer", prompt)
        # the news gate must not be inherited: novelty is what dead-ends a durable topic
        self.assertNotIn("virality_judge", prompt)
        self.assertNotIn("synthesize_topics.py --seed", prompt)
        self.assertIn("30-day window and the virality Judge DO NOT run here", prompt)

    def test_instruction_carries_the_evidence_floor_and_the_de_dup_rule(self):
        prompt = sc.evergreen_prompt_for({"id": "home_equity_tco", "label": "Home Capital"})
        self.assertIn(">= 3 distinct https sources", prompt)
        self.assertIn("180 days", prompt)
        self.assertIn("persona decision", prompt)
        self.assertIn("no publish", prompt)          # an empty outcome is legitimate, never padded
        self.assertIn("archetype: evergreen", prompt)

    def test_instruction_keeps_the_persistence_rules(self):
        prompt = sc.evergreen_prompt_for({"id": "agentic_ai", "label": "Agentic"})
        self.assertIn("NOT approval-gated", prompt)
        self.assertIn("there is no social", prompt)
        self.assertNotIn("@Simon approve", prompt)
        self.assertNotIn("surface the", prompt)

    def test_instruction_is_vertical_specific(self):
        prompt = sc.evergreen_prompt_for({"id": "gpu_hardware", "label": "GPUs"})
        self.assertIn("YYYY-MM-DD_gpu_hardware_evergreen_brief.md", prompt)

    def test_every_registry_vertical_that_runs_evergreen_names_its_own_brief(self):
        missing = [v["id"] for v in REGISTRY
                   if v.get("evergreen_cadence")
                   and f"YYYY-MM-DD_{v['id']}_evergreen_brief.md" not in sc.evergreen_prompt_for(v)]
        self.assertEqual(missing, [], f"evergreen instructions missing the brief path: {missing}")

    def test_the_two_instructions_are_not_the_same_pipeline(self):
        news = sc.prompt_for(BY_ID["supply_chain"])
        ever = sc.evergreen_prompt_for(BY_ID["supply_chain"])
        self.assertNotEqual(news, ever)


class DriftDetection(unittest.TestCase):
    def test_in_sync_plan_is_empty(self):
        for classes in (plan_news(live_news()), plan_evergreen(live_evergreen())):
            self.assertEqual(list(classes), [[]] * 6)

    def test_missing_vertical_is_reported(self):
        missing, *_ = plan_news(live_news()[:-1])
        self.assertEqual([v["id"] for v, _c, _e in missing], [REGISTRY[-1]["id"]])

    def test_missing_evergreen_job_is_reported(self):
        missing, *_ = plan_evergreen(live_evergreen()[:-1])
        self.assertEqual([v["id"] for v, _c, _e in missing], [REGISTRY[-1]["id"]])

    def test_schedule_drift_is_reported(self):
        live = []
        for v in REGISTRY:
            cadence = "5 3 * * *" if v["id"] == "supply_chain" else v["cadence"]
            live.append(live_entry(v["id"], cadence))
        _m, drifted, *_ = plan_news(live)
        self.assertEqual([v["id"] for v, _c, _j in drifted], ["supply_chain"])

    def test_evergreen_schedule_drift_is_reported(self):
        live = []
        for v in live_evergreen():
            if v["vertical"] == "gpu_hardware":
                v["cadence"] = "0 6 * * 3"
            live.append(v)
        _m, drifted, *_ = plan_evergreen(live)
        self.assertEqual([v["id"] for v, _c, _j in drifted], ["gpu_hardware"])

    def test_instruction_drift_is_reported(self):
        live = []
        for v in REGISTRY:
            prompt = "old instruction without the seed step" if v["id"] == "gpu_hardware" else None
            live.append(live_entry(v["id"], v["cadence"], prompt=prompt))
        *_, stale, _dis = plan_news(live)
        self.assertEqual([v["id"] for v, _j in stale], ["gpu_hardware"])

    def test_evergreen_instruction_drift_is_reported(self):
        live = []
        for v in live_evergreen():
            if v["vertical"] == "gpu_hardware":
                v["prompt"] = "old evergreen instruction"
            live.append(v)
        *_, stale, _dis = plan_evergreen(live)
        self.assertEqual([v["id"] for v, _j in stale], ["gpu_hardware"])

    def test_a_news_job_is_not_read_as_an_evergreen_job(self):
        # The prefixes must not be confusable: read_live() partitions the one store into the two
        # fleets, so a `Full Pipeline: x` job can never satisfy an evergreen cadence (or the
        # reverse) — the failure mode where one fleet's jobs are silently counted as the other's.
        import json
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            store = Path(tmp) / "jobs.json"
            jobs = [{"id": "n1", "name": sc.PREFIX + "gpu_hardware",
                     "schedule": {"expr": BY_ID["gpu_hardware"]["cadence"]}, "enabled": True,
                     "prompt": sc.prompt_for(BY_ID["gpu_hardware"])},
                    {"id": "e1", "name": sc.EVERGREEN_PREFIX + "gpu_hardware",
                     "schedule": {"expr": BY_ID["gpu_hardware"]["evergreen_cadence"]},
                     "enabled": True,
                     "prompt": sc.evergreen_prompt_for(BY_ID["gpu_hardware"])}]
            store.write_text(json.dumps({"jobs": jobs}))
            original, sc.JOBS_PATH = sc.JOBS_PATH, str(store)
            try:
                news = sc.read_live(sc.PREFIX)
                ever = sc.read_live(sc.EVERGREEN_PREFIX)
            finally:
                sc.JOBS_PATH = original
        self.assertEqual([j["id"] for j in news], ["n1"])
        self.assertEqual([j["id"] for j in ever], ["e1"])
        # and a store holding only news jobs leaves the evergreen fleet empty, not mis-read
        all_news = [j for j in (live_news())]
        self.assertEqual(sc.plan(REGISTRY, all_news, prefix=sc.EVERGREEN_PREFIX,
                                 cadence_key="evergreen_cadence", enabled_key="evergreen_enabled",
                                 prompt_fn=sc.evergreen_prompt_for)[0][:1],
                         [])
        self.assertTrue(plan_evergreen(all_news)[1], "news jobs are not evergreen jobs")

    def test_orphan_and_paused_are_separate_from_drift(self):
        live = live_news()
        live.append(live_entry("home_systems_reno", "0 6 * * 1", job_id="retired"))
        live.append(live_entry("gpu_hardware", BY_ID["gpu_hardware"]["cadence"], enabled=False))
        missing, drifted, orphans, paused, _stale, _dis = plan_news(live)
        self.assertEqual([j["vertical"] for j in orphans], ["home_systems_reno"])
        self.assertEqual([j["vertical"] for _v, j in paused], ["gpu_hardware"],
                         "a paused job is left alone — it is not schedule drift")
        self.assertEqual([missing, drifted], [[], []])

    def test_registry_without_cadence_is_reported_not_crashed(self):
        registry = list(REGISTRY) + [{"id": "no_cadence_vertical", "label": "x"}]
        live = live_news()
        missing, *_ = plan_news(live, registry=registry)
        self.assertEqual([v["id"] for v, _c, err in missing if err], ["no_cadence_vertical"])

    def test_evergreen_cadence_is_optional_so_a_news_only_vertical_is_not_missing(self):
        registry = list(REGISTRY) + [{"id": "news_only_vertical", "label": "x",
                                      "cadence": "0 12 * * 3", "news_enabled": True}]
        live = live_news()
        missing, *_ = plan_evergreen(live, registry=registry)
        self.assertEqual(missing, [], "a vertical with no evergreen_cadence has no evergreen run")

    def test_check_mode_never_writes(self):
        calls = []
        original_run, original_check = sc.run, sc.CHECK
        sc.run = lambda cmd: calls.append(cmd)  # any scheduler mutation would land here
        try:
            sc.CHECK = True
            live = [live_entry(v["id"], "1 1 1 1 1") for v in REGISTRY]  # everything drifted
            missing, drifted, _o, _p, stale, _dis = plan_news(live)
            self.assertTrue(missing or drifted or stale)  # the plan is non-empty…
            self.assertEqual(calls, [])                   # …and nothing was written
        finally:
            sc.run, sc.CHECK = original_run, original_check


class EnabledFlags(unittest.TestCase):
    """A `*_enabled: false` flag in the vertical's settings owns the job's existence."""

    def test_news_disabled_reports_the_live_job_as_disabled_not_paused(self):
        registry = [dict(v, news_enabled=False) if v["id"] == "gpu_hardware" else v for v in REGISTRY]
        missing, drifted, _orphans, paused, _stale, disabled = plan_news(live_news(), registry=registry)
        self.assertEqual([v["id"] for v, _j in disabled], ["gpu_hardware"])
        self.assertEqual([missing, drifted, paused], [[], [], []],
                         "disabling is its own class — not a missing job and not an operator pause")

    def test_news_disabled_with_no_live_job_is_the_correct_state(self):
        registry = [dict(v, news_enabled=False) if v["id"] == "gpu_hardware" else v for v in REGISTRY]
        live = [j for j in live_news() if j["vertical"] != "gpu_hardware"]
        missing, drifted, _orphans, paused, _stale, disabled = plan_news(live, registry=registry)
        self.assertEqual([missing, drifted, paused, disabled], [[], [], [], []])

    def test_evergreen_disabled_reports_the_live_job_as_disabled(self):
        registry = [dict(v, evergreen_enabled=False) if v["id"] == "supply_chain" else v
                    for v in REGISTRY]
        _m, _d, _o, _p, _stale, disabled = plan_evergreen(live_evergreen(), registry=registry)
        self.assertEqual([v["id"] for v, _j in disabled], ["supply_chain"])

    def test_a_disabled_vertical_still_runs_its_other_mode(self):
        registry = [dict(v, evergreen_enabled=False) if v["id"] == "home_ops_execution" else v
                    for v in REGISTRY]
        missing, drifted, _o, paused, _stale, disabled = plan_news(live_news(), registry=registry)
        self.assertEqual([missing, drifted, paused, disabled], [[], [], [], []],
                         "turning evergreen off must not disturb the news fleet")


class SchedulesAreDisjoint(unittest.TestCase):
    """Both fleets are journaled onto the same shared model endpoints, so a slot is exclusive."""

    def test_no_two_cadences_share_a_slot(self):
        self.assertEqual(sc.slot_collisions(REGISTRY), [],
                         "two jobs fire in the same (weekday, hour, minute) slot")

    def test_collision_is_detected_when_one_exists(self):
        registry = [dict(v, evergreen_cadence=v["cadence"]) for v in REGISTRY]
        clashes = sc.slot_collisions(registry)
        self.assertTrue(clashes, "the gate must catch an evergreen run sharing its news slot")

    def test_every_vertical_has_both_cadences_and_the_evergreen_band_is_off_peak(self):
        for v in REGISTRY:
            self.assertTrue(v.get("evergreen_cadence"), f"{v['id']} has no evergreen cadence")
            slots = sc.cadence_slots(v["evergreen_cadence"])
            self.assertTrue(slots, f"{v['id']}: unreadable evergreen cadence")
            for dow, hour, minute in slots:
                self.assertIn(minute, (0, 30), f"{v['id']}: off the 30-minute grid")
                if dow in sc.PEAK_DAYS:
                    self.assertFalse(sc.in_peak_hour(hour),
                                     f"{v['id']}: evergreen run inside the DeepSeek peak window")


class PeakWindow(unittest.TestCase):
    """DeepSeek bills weekday tokens at 2x inside 01:00-04:00 and 06:00-10:00 UTC."""

    def test_registry_has_no_peak_cadence(self):
        self.assertEqual(sc.peak_violations(REGISTRY), [],
                         "a registry cadence sits inside the DeepSeek peak windows")

    def test_evergreen_peak_cadence_is_caught_too(self):
        registry = [dict(v, evergreen_cadence="0 7 * * 3") if v["id"] == "gpu_hardware" else v
                    for v in REGISTRY]
        self.assertEqual([v["id"] for v, _c, _m in sc.peak_violations(registry)], ["gpu_hardware"])

    def test_peak_cadence_is_refused_even_when_live_state_matches_it(self):
        # The dangerous case: the store already agrees with a bad registry row, so cadence
        # drift is empty and only the peak rule catches it.
        bad = dict(BY_ID["gpu_hardware"], cadence="0 6 * * 3")
        registry = [bad if v["id"] == "gpu_hardware" else v for v in REGISTRY]
        live = [live_entry(v["id"], v["cadence"]) for v in registry]
        _m, drifted, _o, _p, _s, _dis = plan_news(live, registry=registry)
        self.assertEqual(drifted, [])
        self.assertEqual([v["id"] for v, _c, _msg in sc.peak_violations(registry)], ["gpu_hardware"])

    def test_weekend_cadences_are_never_peak(self):
        self.assertEqual(sc.cadence_verdict("0 6 * * 6")[0], "ok")
        self.assertEqual(sc.cadence_verdict("30 8 * * 0")[0], "ok")

    def test_window_edges_are_off_peak(self):
        # 04:00 and 10:00 close their windows; a pipeline may start there.
        self.assertEqual(sc.cadence_verdict("0 4 * * 2")[0], "ok")
        self.assertEqual(sc.cadence_verdict("0 10 * * 2")[0], "ok")
        self.assertEqual(sc.cadence_verdict("59 3 * * 2")[0], "peak")
        self.assertEqual(sc.cadence_verdict("59 9 * * 2")[0], "peak")


if __name__ == "__main__":
    unittest.main(verbosity=2)
