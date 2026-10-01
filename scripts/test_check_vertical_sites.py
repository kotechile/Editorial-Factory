#!/usr/bin/env python3
"""Tests for scripts/check_vertical_sites.py — run: python3 scripts/test_check_vertical_sites.py

Hermetic: the routing audit is a pure function of context/verticals.json's registry and the rows the
public.vertical_sites table returns, so every rule (including the WordPress-category coverage) is
pinned without a network call.
"""

from __future__ import annotations

import importlib.util
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("cvs", ROOT / "scripts" / "check_vertical_sites.py")
cvs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cvs)

PASS, FAIL = [], []


def check(name: str, condition: bool, detail: str = ""):
    (PASS if condition else FAIL).append(name)
    print(f"  [{'ok ' if condition else 'FAIL'}] {name}{'' if condition else f'  <- {detail}'}")


def row(vertical_id: str, domain: str = "giniloh.com", **overrides) -> dict:
    base = {"vertical_id": vertical_id, "cms_base_url": f"https://cms.{domain}",
            "site_domain": domain, "frontend_url": f"https://{domain}", "active": True,
            "wp_category_id": 9}
    base.update(overrides)
    return base


print("routing — the destination rules still hold")
good = cvs.audit({"agentic_ai"}, [row("agentic_ai")])
check("a routed vertical with a category passes", good["ok"], str(good["problems"]))
check("...and the category routing is summarised",
      good["routed_by_category"] == {"giniloh.com": {"9": 1}}, str(good["routed_by_category"]))

check("an unrouted vertical fails", not cvs.audit({"agentic_ai", "new_vertical"}, [row("agentic_ai")])["ok"])
check("a stale routing row fails", not cvs.audit({"agentic_ai"}, [row("agentic_ai"), row("dead_vertical")])["ok"])
check("a cms URL off the destination domain fails",
      not cvs.audit({"agentic_ai"}, [row("agentic_ai", cms_base_url="https://cms.example.com")])["ok"])
check("a trailing slash fails",
      not cvs.audit({"agentic_ai"}, [row("agentic_ai", frontend_url="https://giniloh.com/")])["ok"])
check("an active=false row for a live vertical fails",
      not cvs.audit({"agentic_ai"}, [row("agentic_ai", active=False)])["ok"])

print("\ncategories — a vertical with no category is a defect, not a default")
no_category = cvs.audit({"agentic_ai"}, [row("agentic_ai", wp_category_id=None)])
check("a null wp_category_id fails the audit", not no_category["ok"], str(no_category["problems"]))
check("...and the problem names the destination and the fix",
      any("Uncategorized" in p and "0004" in p for p in no_category["problems"]),
      str(no_category["problems"]))

no_column = cvs.audit({"agentic_ai"}, [{k: v for k, v in row("agentic_ai").items() if k != "wp_category_id"}])
check("a missing column fails the audit", not no_column["ok"])
check("...and names the migration to apply",
      any(cvs.CATEGORY_MIGRATION in p for p in no_column["problems"]), str(no_column["problems"]))
check("...only once, not once per vertical",
      sum(1 for p in no_column["problems"] if "does not exist" in p) == 1, str(no_column["problems"]))

print("\nthe live registry and table")
result = cvs.check()
print(f"  routed: {result['routed_verticals']}/{result['declared_verticals']} | "
      f"category column: {result['category_column']} | problems: {len(result['problems'])}")
for problem in result["problems"][:3]:
    print(f"    - {problem}")
check("every vertical declared in verticals.json is routed", result["routed_verticals"] == result["declared_verticals"])
check("the audit reports whether the category migration is applied",
      isinstance(result["category_column"], bool))

print(f"\n{len(PASS)} passed, {len(FAIL)} failed")
if FAIL:
    for name in FAIL:
        print(f"  FAILED: {name}")
sys.exit(1 if FAIL else 0)
