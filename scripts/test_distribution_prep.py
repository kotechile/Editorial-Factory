#!/usr/bin/env python3
"""
scripts/test_distribution_prep.py — tests for the distribution *preparation* step.

Preparation is easy to get wrong in two directions: posting something by accident (it must never
post), and breaking a publish because a dashboard was down (it must degrade). Both are pinned here,
plus the coverage rule the `--check` mode uses. No live calls: the network cases point at a closed
port on localhost.

Run directly or via `scripts/verify.sh` §8.
"""

import contextlib
import importlib.util
import io
import os
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import seed_distribution as sd  # noqa: E402

UNREACHABLE = "http://127.0.0.1:9"   # discard port: connection refused, no DNS, no traffic


def load_publish_module():
    spec = importlib.util.spec_from_file_location("publish_module", HERE / "publish.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run(argv):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(io.StringIO()):
        code = sd.main(argv)
    return code, buf.getvalue()


class Coverage(unittest.TestCase):
    def test_card_matches_on_source_id_with_or_without_the_date_prefix(self):
        tasks = [{"source_id": "2026-09-26_tariff-cliff-already-priced-in"},
                 {"source_id": "maskills-multi-agent-skills-optimization"}]
        articles = {"2026-09-26_tariff-cliff-already-priced-in.md": {"tariff-cliff-already-priced-in",
                                                                    "2026-09-26_tariff-cliff-already-priced-in"},
                    "2026-09-24_maskills-multi-agent-skills-optimization.md": {"maskills-multi-agent-skills-optimization"},
                    "2026-09-30_brand-new-piece.md": {"brand-new-piece", "2026-09-30_brand-new-piece"}}
        self.assertEqual(sd.uncovered(articles, tasks), ["2026-09-30_brand-new-piece.md"])

    def test_published_articles_reads_the_frontmatter_slug(self):
        articles = sd.published_articles()
        self.assertTrue(articles, "expected published articles in the repo")
        for candidates in articles.values():
            self.assertTrue(all(candidates), "every candidate slug must be non-empty")


class Safety(unittest.TestCase):
    def test_dry_run_sends_nothing(self):
        code, out = run(["--dry-run"])
        self.assertEqual(code, 0)
        self.assertIn(f"POST ", out)
        self.assertIn(sd.SEED_PATH, out)          # the seeding endpoint…
        self.assertIn("published articles:", out)  # …and what it would cover

    def test_missing_secret_is_a_clean_error_not_a_call(self):
        """Without a secret the guard must stop before issuing a request the dashboard would reject."""
        saved_env, saved_loader = os.environ.pop("PRESSFLOW_AUTH_SECRET", None), sd.load_env
        sd.load_env = lambda: None                 # do not repopulate it from the repo .env
        try:
            code, _ = run([])
            self.assertEqual(code, 2, "the guard must exit 2 with a message, not call the dashboard")
        finally:
            sd.load_env = saved_loader
            if saved_env is not None:
                os.environ["PRESSFLOW_AUTH_SECRET"] = saved_env

    def test_the_prep_script_can_only_talk_to_the_seed_and_queue_endpoints(self):
        """Preparation, not distribution: no posting endpoint may ever appear in this module."""
        import re
        source = (HERE / "seed_distribution.py").read_text(encoding="utf-8")
        endpoints = set(re.findall(r"[\"'](/api/[^\"']+)[\"']", source))
        self.assertEqual(endpoints, {sd.SEED_PATH, sd.QUEUE_PATH}, endpoints)

    def test_unreachable_dashboard_returns_an_error_not_an_exception(self):
        saved = os.environ.get("PRESSFLOW_AUTH_SECRET")
        os.environ["PRESSFLOW_AUTH_SECRET"] = "test-secret"
        try:
            code, _ = run(["--url", UNREACHABLE])
            self.assertEqual(code, 2)
        finally:
            if saved is None:
                os.environ.pop("PRESSFLOW_AUTH_SECRET", None)
            else:
                os.environ["PRESSFLOW_AUTH_SECRET"] = saved

    def test_publish_step_degrades_when_the_dashboard_is_unreachable(self):
        """A publish must never fail because the prep call could not reach the dashboard."""
        publish = load_publish_module()
        saved = {k: os.environ.get(k) for k in ("PRESSFLOW_AUTH_SECRET", "PRESSFLOW_BASE_URL")}
        os.environ["PRESSFLOW_AUTH_SECRET"] = "test-secret"
        os.environ["PRESSFLOW_BASE_URL"] = UNREACHABLE
        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf):
                result = publish.seed_distribution_prep()
        finally:
            for key, value in saved.items():
                if value is None:
                    os.environ.pop(key, None)
                else:
                    os.environ[key] = value
        self.assertFalse(result)
        self.assertIn("distribution prep skipped", buf.getvalue())


if __name__ == "__main__":
    unittest.main(verbosity=2)
