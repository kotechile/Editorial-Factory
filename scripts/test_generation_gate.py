#!/usr/bin/env python3
"""Contract tests for the generation gate and the control record.

The gate is the one thing standing between an owner switch in PressFlow and a pipeline spending
money, so the decision function is tested without a network: Supabase is stubbed, the registry is
a temp file, and every case asserts the exit-facing verdict (allowed + reason word).
"""
import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import generation_gate as gate  # noqa: E402

VERTICALS = {"verticals": [
    {"id": "on_vertical", "news_enabled": True, "evergreen_enabled": True, "review_enabled": True},
    {"id": "news_off", "news_enabled": False, "evergreen_enabled": True, "review_enabled": False},
]}


class DecideTests(unittest.TestCase):
    def test_master_switch_off_blocks_every_article_mode(self):
        control = {"articles_enabled": False, "updated_by": "jorge", "updated_at": "2026-11-16T10:00:00Z"}
        for mode in ("news", "evergreen", "review"):
            allowed, word, reason = gate.decide(control, mode, "on_vertical", VERTICALS["verticals"][0])
            self.assertFalse(allowed, f"{mode} should be blocked by the master switch")
            self.assertEqual(word, "articles")
            self.assertIn("switched OFF", reason)
            self.assertIn("jorge", reason)

    def test_vertical_disabled_in_control_record_blocks(self):
        control = {"articles_enabled": True,
                   "disabled_verticals": {"on_vertical": {"at": "2026-11-16T10:00:00Z", "by": "jorge"}}}
        allowed, word, reason = gate.decide(control, "news", "on_vertical", VERTICALS["verticals"][0])
        self.assertFalse(allowed)
        self.assertEqual(word, "vertical")
        self.assertIn("switched OFF in PressFlow", reason)

    def test_registry_mode_flag_still_blocks(self):
        control = {"articles_enabled": True, "disabled_verticals": {}}
        allowed, word, _ = gate.decide(control, "news", "news_off", VERTICALS["verticals"][1])
        self.assertFalse(allowed)
        self.assertEqual(word, "vertical")
        # the other modes stay open for the same vertical
        self.assertTrue(gate.decide(control, "evergreen", "news_off", VERTICALS["verticals"][1])[0])

    def test_unknown_vertical_fails_open(self):
        # A registry row that cannot be read must not stop the fleet; the master switch still applies.
        allowed, word, _ = gate.decide({"articles_enabled": True}, "news", "ghost", None)
        self.assertTrue(allowed)
        self.assertEqual(word, "vertical-missing")

    def test_software_switch_is_independent(self):
        control = {"articles_enabled": True, "software_enabled": False,
                   "updated_by": "jorge", "updated_at": "2026-11-16T10:00:00Z"}
        allowed, word, reason = gate.decide(control, "software")
        self.assertFalse(allowed)
        self.assertEqual(word, "software")
        self.assertIn("software generation", reason)
        # articles stay open when only software is off
        self.assertTrue(gate.decide(control, "news", "on_vertical", VERTICALS["verticals"][0])[0])

    def test_missing_flags_default_to_on(self):
        allowed, word, _ = gate.decide({}, "news", "on_vertical", VERTICALS["verticals"][0])
        self.assertTrue(allowed)
        self.assertEqual(word, "ok")


class RecordTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="gate-")
        self.control_path = os.path.join(self.tmp, "generation_control.json")
        self.orig_control_path = gate.CONTROL_PATH
        gate.CONTROL_PATH = self.control_path
        with open(self.control_path, "w") as f:
            json.dump({"_note": "keep me", "articles_enabled": True, "software_enabled": True}, f)
        self.orig_get = gate.supabase_get
        self.orig_write = gate.supabase_write
        # Supabase unreachable: both helpers report an error, so every path here is the file path.
        gate.supabase_get = lambda *a, **k: (None, "stubbed offline")
        gate.supabase_write = lambda *a, **k: (None, "stubbed offline")

    def tearDown(self):
        gate.CONTROL_PATH = self.orig_control_path
        gate.supabase_get = self.orig_get
        gate.supabase_write = self.orig_write

    def test_read_control_falls_back_to_the_file_and_says_so(self):
        control, source, warning = gate.read_control()
        self.assertEqual(source, "file")
        self.assertTrue(control["articles_enabled"])
        self.assertIn("stubbed offline", warning or "")

    def test_write_control_keeps_the_documentation_note(self):
        gate.write_control({"articles_enabled": False}, by="tester")
        with open(self.control_path) as f:
            saved = json.load(f)
        self.assertFalse(saved["articles_enabled"])
        self.assertEqual(saved["_note"], "keep me")
        self.assertEqual(saved["updated_by"], "tester")

    def test_dispatch_stamp_does_not_look_like_a_switch_change(self):
        gate.write_control({"articles_enabled": True}, by="jorge")
        before = gate.read_control()[0]
        gate.write_control({"software_run_handled_at": "2026-11-16T12:00:00+00:00"}, touch=False)
        after = gate.read_control()[0]
        self.assertEqual(after["updated_by"], before["updated_by"])
        self.assertEqual(after["updated_at"], before["updated_at"])
        self.assertEqual(after["software_run_handled_at"], "2026-11-16T12:00:00+00:00")


if __name__ == "__main__":
    unittest.main(verbosity=2)
