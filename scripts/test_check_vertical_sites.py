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
FRONTS = {"giniloh.com", "wellroost.com", "aichieve.net"}
good = cvs.audit({"agentic_ai"}, [row("agentic_ai")], fronts=FRONTS)
check("a routed vertical with a category passes", good["ok"], str(good["problems"]))
check("...and the category routing is summarised",
      good["routed_by_category"] == {"giniloh.com": {"9": 1}}, str(good["routed_by_category"]))

check("an unrouted vertical fails", not cvs.audit({"agentic_ai", "new_vertical"}, [row("agentic_ai")])["ok"])
check("a row for a vertical this registry does not declare is reported, not failed",
      cvs.audit({"agentic_ai"}, [row("agentic_ai"), row("dead_vertical")])["ok"]
      and any("dead_vertical" in n for n in
              cvs.audit({"agentic_ai"}, [row("agentic_ai"), row("dead_vertical")])["notices"]),
      str(cvs.audit({"agentic_ai"}, [row("agentic_ai"), row("dead_vertical")])))
check("a cms URL off the estate fails",
      not cvs.audit({"agentic_ai"}, [row("agentic_ai", cms_base_url="https://cms.example.com")],
                    fronts=FRONTS)["ok"])
check("...but a CMS another front owns is fine (one CMS serves several fronts)",
      cvs.audit({"agentic_ai"}, [row("agentic_ai", domain="aichieve.net",
                                     cms_base_url="https://cms.giniloh.com")],
                fronts=FRONTS)["ok"],
      str(cvs.audit({"agentic_ai"}, [row("agentic_ai", domain="aichieve.net",
                                         cms_base_url="https://cms.giniloh.com")],
                    fronts=FRONTS)["problems"]))
check("a routing row for a domain that is not a reader front fails",
      not cvs.audit({"agentic_ai"}, [row("agentic_ai", domain="example.com",
                                         cms_base_url="https://cms.example.com")],
                    fronts=FRONTS)["ok"])
check("a trailing slash fails",
      not cvs.audit({"agentic_ai"}, [row("agentic_ai", frontend_url="https://giniloh.com/")])["ok"])
check("an active=false row for a live vertical fails",
      not cvs.audit({"agentic_ai"}, [row("agentic_ai", active=False)])["ok"])
check("without the front registry the URL rules fall back to the cms.<domain> shape",
      cvs.audit({"agentic_ai"}, [row("agentic_ai", cms_base_url="https://giniloh.com")])["ok"] is False)

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

print("\nthe CMS's own vertical taxonomy — the term a front routes on")
# The push resolves this term on the destination and fails closed when it is missing
# (scripts/wp_draft.py resolve_vertical_term), so the coverage belongs in the audit that runs
# BEFORE a publish run: a new vertical routed to cms.giniloh.com with no term there is a push that
# would refuse at 17:30, and the fix is one term.
covered = cvs.audit({"agentic_ai"}, [row("agentic_ai")], {"giniloh.com": {"agentic_ai"}})
check("a vertical with a term on its CMS passes", covered["ok"], str(covered["problems"]))
check("...and the coverage is reported", covered["cms_vertical_terms"] == {"giniloh.com": ["agentic_ai"]},
      str(covered["cms_vertical_terms"]))

gap = cvs.audit({"agentic_ai", "brand_new_vertical"},
                [row("agentic_ai"), row("brand_new_vertical")],
                {"giniloh.com": {"agentic_ai"}})
check("a routed vertical with no CMS term fails the audit", not gap["ok"], str(gap["problems"]))
check("...naming the term to create and where to create it",
      any("brand_new_vertical" in p and "wp-json/wp/v2/vertical" in p for p in gap["problems"]),
      str(gap["problems"]))
check("...and not reporting the covered one", not any("'agentic_ai'" in p for p in gap["problems"]),
      str(gap["problems"]))

unsupported = cvs.audit({"agentic_ai"}, [row("agentic_ai", domain="wellroost.com")],
                        {"wellroost.com": None})
check("a CMS with no vertical taxonomy is a notice, not a failure", unsupported["ok"],
      str(unsupported["problems"]))
check("...said out loud, with the reason", any("registers no 'vertical' taxonomy" in n
                                              for n in unsupported["notices"]), str(unsupported["notices"]))
check("...and reported as None (not an empty term list) in the coverage",
      unsupported["cms_vertical_terms"] == {"wellroost.com": None},
      str(unsupported["cms_vertical_terms"]))

unreadable = cvs.audit({"agentic_ai"}, [row("agentic_ai")], {},
                       {"giniloh.com": "could not reach https://cms.giniloh.com"})
check("a CMS that could not be read is a notice, not a failure", unreadable["ok"],
      str(unreadable["problems"]))
check("...and is not silently treated as covered", unreadable["cms_vertical_terms"] == {"giniloh.com": "unreadable"},
      str(unreadable["cms_vertical_terms"]))

check("no CMS probe passed => the audit is exactly the routing check it was",
      "cms_vertical_terms" in cvs.audit({"agentic_ai"}, [row("agentic_ai")])
      and cvs.audit({"agentic_ai"}, [row("agentic_ai")])["cms_vertical_terms"] == {})

print("\nthe live registry and table")
result = cvs.check()
print(f"  routed: {result['routed_verticals']}/{result['declared_verticals']} | "
      f"category column: {result['category_column']} | problems: {len(result['problems'])}")
for domain, terms in result.get("cms_vertical_terms", {}).items():
    print(f"    {domain}: {'no vertical taxonomy' if terms is None else terms if terms == 'unreadable' else f'{len(terms)} vertical term(s)'}")
for notice in result.get("notices", []):
    print(f"    note: {notice}")
for problem in result["problems"][:3]:
    print(f"    - {problem}")
check("every vertical declared in verticals.json is routed",
      not any("has no destination row" in p for p in result["problems"]), str(result["problems"])[:300])
check("the audit reports whether the category migration is applied",
      isinstance(result["category_column"], bool))

print(f"\n{len(PASS)} passed, {len(FAIL)} failed")
if FAIL:
    for name in FAIL:
        print(f"  FAILED: {name}")
sys.exit(1 if FAIL else 0)
