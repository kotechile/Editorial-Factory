#!/usr/bin/env python3
"""scripts/test_check_offpeak_crons.py — contract tests for the DeepSeek off-peak gate.

Wired into `scripts/verify.sh`. These pin the properties that make the gate trustworthy:

  * the window boundaries are what DeepSeek's 2x band actually is — Mon-Fri 01:00-04:00 and
    06:00-10:00 UTC, with 04:00 and 10:00 themselves off-peak, and weekend days exempt;
  * the rule cannot be satisfied by accident: a wildcard hour, a `*/2` hour, or a recurring
    interval is reported rather than waved through;
  * the gate skips exactly what costs nothing (paused jobs, `no_agent` script jobs) and nothing
    else;
  * the committed registry has no weekday cadence inside a window — this is what stops the fleet
    drifting back into the 2x band on the next vertical addition.

No network, no scheduler writes: pure functions over synthetic job dicts.
"""
import sys
import unittest
from datetime import datetime, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import check_offpeak_crons as co  # noqa: E402
import sync_crons as sc  # noqa: E402


class WindowBoundaries(unittest.TestCase):
    def test_hours_inside_the_two_windows_are_peak(self):
        for cadence in ("0 1 * * 1", "59 2 * * 3", "0 3 * * 5", "0 6 * * 2", "30 8 * * 4", "59 9 * * 5"):
            self.assertEqual(sc.cadence_verdict(cadence)[0], "peak", cadence)

    def test_window_edges_and_the_gap_are_off_peak(self):
        for cadence in ("0 0 * * 1", "0 4 * * 1", "30 5 * * 1", "0 10 * * 1", "0 10 * * 5", "0 23 * * 1"):
            self.assertEqual(sc.cadence_verdict(cadence)[0], "ok", cadence)

    def test_weekends_are_off_peak_all_day(self):
        for cadence in ("0 1 * * 6", "0 6 * * 0", "30 9 * * 7", "0 8 * * 6,0"):
            self.assertEqual(sc.cadence_verdict(cadence)[0], "ok", cadence)

    def test_weekday_and_weekend_mixed_cadence_is_peak(self):
        self.assertEqual(sc.cadence_verdict("0 6 * * 1,6")[0], "peak")

    def test_wildcard_and_pattern_hours_cannot_be_proven_off_peak(self):
        self.assertEqual(sc.cadence_verdict("* * * * 1")[0], "peak")
        self.assertEqual(sc.cadence_verdict("0 */2 * * 1")[0], "peak")
        self.assertEqual(sc.cadence_verdict("0 6,14 * * 1")[0], "peak")

    def test_unparseable_cadence_is_unknown_not_ok(self):
        self.assertEqual(sc.cadence_verdict("every 2h")[0], "unknown")
        self.assertEqual(sc.cadence_verdict("")[0], "unknown")
        self.assertEqual(sc.cadence_verdict("0 6 * * Q")[0], "unknown")


class LiveFleetRule(unittest.TestCase):
    """The rule the store is judged by."""

    @staticmethod
    def job(name, schedule, enabled=True, no_agent=False):
        return {"id": name[:8], "name": name, "schedule": schedule,
                "enabled": enabled, "no_agent": no_agent}

    def verdicts(self, jobs):
        return {f[0]: f[2] for f in co.check_jobs(jobs)}

    def test_paused_and_no_agent_jobs_are_skipped(self):
        jobs = [
            self.job("paused", {"kind": "cron", "expr": "0 6 * * 1"}, enabled=False),
            self.job("script", {"kind": "cron", "expr": "0 6 * * 1"}, no_agent=True),
            self.job("live", {"kind": "cron", "expr": "0 6 * * 1"}),
        ]
        self.assertEqual(self.verdicts(jobs), {"paused": "skip", "script": "skip", "live": "peak"})

    def test_off_peak_cron_job_passes(self):
        jobs = [self.job("pipeline", {"kind": "cron", "expr": "30 10 * * 1,4"})]
        self.assertEqual(self.verdicts(jobs), {"pipeline": "ok"})

    def test_recurring_interval_is_reported_not_waved_through(self):
        jobs = [self.job("hourly", {"kind": "interval", "expr": "every 2h"})]
        self.assertEqual(self.verdicts(jobs), {"hourly": "recurring"})

    def test_one_shot_is_judged_by_its_timestamp(self):
        monday_peak = datetime(2026, 10, 5, 6, 30)     # Monday 06:30 UTC
        saturday_peak = datetime(2026, 10, 3, 6, 30)   # Saturday 06:30 UTC
        self.assertEqual(co.verdict_for_stamp(monday_peak.isoformat())[0], "peak")
        self.assertEqual(co.verdict_for_stamp(saturday_peak.isoformat())[0], "ok")
        self.assertEqual(co.verdict_for_stamp("2026-10-05T10:00:00")[0], "ok")
        self.assertEqual(co.verdict_for_stamp("not-a-date")[0], "unknown")

    def test_host_clock_is_utc(self):
        # Cron hours are read on the host clock; the windows are UTC. A host clock elsewhere
        # silently re-labels every cadence in the fleet, so this must stay UTC.
        self.assertEqual(co.host_offset_minutes(), 0,
                         "the DeepSeek peak audit assumes the scheduler host clock is UTC")


class CommittedRegistry(unittest.TestCase):
    def test_no_registry_vertical_is_scheduled_inside_a_peak_window(self):
        offenders = [(v["id"], v["cadence"]) for v, _c, _m in sc.peak_violations(sc.load_verticals())]
        self.assertEqual(offenders, [], f"registry cadences inside the DeepSeek 2x windows: {offenders}")

    def test_weekday_slots_stay_unique_and_after_the_morning_peak(self):
        slots = {}
        for v in sc.load_verticals():
            minute, hour, _dom, _mon, dow = v["cadence"].split()
            for day in dow.split(","):
                if int(day) in (0, 6, 7):
                    continue
                slot = f"{int(hour):02d}:{int(minute):02d}"
                self.assertGreaterEqual(int(hour) * 60 + int(minute), 10 * 60 + 30,
                                        f"{v['id']} fires {slot} UTC, inside the 06:00-10:00 window")
                key = (day, slot)
                self.assertNotIn(key, slots,
                                 f"two pipelines share slot {slot} on weekday {day}: "
                                 f"{slots.get(key)} and {v['id']}")
                slots[key] = v["id"]

    def test_registry_file_is_the_one_the_live_fleet_is_reconciled_from(self):
        self.assertTrue(str(sc.REPO).endswith("editorial-factory"), sc.REPO)
        self.assertTrue(sc.JOBS_PATH.endswith("cron/jobs.json"), sc.JOBS_PATH)


if __name__ == "__main__":
    unittest.main(verbosity=2)
