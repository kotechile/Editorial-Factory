#!/usr/bin/env python3
"""Evergreen gate — the code-enforced evidence floor for the evergreen pipeline.

The news pipeline's gate is a *freshness* gate: a candidate that is not new loses on Novelty
(0.40 weight) and the run returns "no publish". That gate cannot score a durable topic, which is
why the evergreen fleet exists (`skills/evergreen_topics.md`) — but a second pipeline with no
code-enforced floor would just be a licence to publish filler, so the floor lives here:

  * at least MIN_SOURCES distinct cited primary sources, on at least MIN_HOSTS distinct hosts
    (three pages of one vendor's site is one source wearing a costume);
  * every cited source fetched live and shown to actually CONTAIN the figure it is cited for
    (the same test the citation hub uses — `citation_hub_dossier.figure_evidence`);
  * a named persona decision and a named de-dup check against a prior artifact that exists;
  * and a `<!-- evergreen-gate: -->` marker recording the row count, so a brief edited after the
    fact reads as stale instead of silently shipping (same contract as the synthesis seed block).

Usage
  python3 scripts/evergreen_gate.py --brief context/recon_proposals/<date>_<vertical>_evergreen_brief.md
  python3 scripts/evergreen_gate.py --brief <path> --no-network    # shape/parse only (no HTTP)
  python3 scripts/evergreen_gate.py --check-artifacts [--no-network]   # every committed brief is fresh
  python3 scripts/evergreen_gate.py --self-test                    # rules pinned, no network

Exit codes: 0 = pass, 1 = gate failed (the reasons are printed), 2 = usage error.
"""

from __future__ import annotations

import argparse
import glob
import hashlib
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

import citation_hub_dossier as chd  # noqa: E402  (fetch_source / figure_evidence — one definition)

MIN_SOURCES = 3
MIN_HOSTS = 2
DEDUP_WINDOW_DAYS = 180

MARKER_START = "<!-- evergreen-gate:start -->"
MARKER_END = "<!-- evergreen-gate:end -->"

REQUIRED_FIELDS = (
    "Vertical",
    "Persona",
    "Decision the reader is facing",
    "Durability",
    "De-dup",
    "Thesis",
)
MIN_FIELD_CHARS = {"Decision the reader is facing": 40, "Durability": 60, "Thesis": 30, "De-dup": 12}

EVIDENCE_HEADER = ("source", "url", "retrieved", "figure", "measured")


class GateFailure(RuntimeError):
    """Raised when a brief cannot pass the evidence floor."""


# --------------------------------------------------------------------------------------- parsing

def parse_brief(text: str) -> dict:
    """Extract the brief's declared fields and its evidence table. Pure text, no network."""
    out = {"fields": {}, "rows": [], "errors": []}

    for name in REQUIRED_FIELDS:
        m = re.search(rf"^\*\*{re.escape(name)}:?\*\*\s*(.*)$", text, re.M)
        value = (m.group(1).strip() if m else "")
        out["fields"][name] = value
        if not value:
            out["errors"].append(f"missing field: **{name}:**")
        elif name in MIN_FIELD_CHARS and len(value) < MIN_FIELD_CHARS[name]:
            out["errors"].append(
                f"**{name}:** is too thin to be checkable ({len(value)} chars, "
                f"needs >= {MIN_FIELD_CHARS[name]})")

    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|") or set(line) <= set("|-: "):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 5:
            continue
        header = " ".join(cells).lower()
        if all(h in header for h in EVIDENCE_HEADER) or cells[0].lower() in ("#", "n", "no"):
            continue
        if not re.match(r"^\d+$", cells[0]):
            continue
        row = {"n": cells[0], "source": cells[1], "url": cells[2], "retrieved": cells[3],
               "figure": cells[4], "measured": cells[5] if len(cells) > 5 else ""}
        out["rows"].append(row)
    return out


def marker_state(text: str, rows: int) -> tuple[bool, str]:
    """(is_fresh, reason) for an existing marker block. A missing block is 'not seeded'."""
    if MARKER_START not in text or MARKER_END not in text:
        return False, "not seeded"
    block = text[text.index(MARKER_START):text.index(MARKER_END)]
    m = re.search(r"rows=(\d+)", block)
    if not m:
        return False, "marker has no row count"
    if int(m.group(1)) != rows:
        return False, f"stale (marker says rows={m.group(1)}, the table has {rows})"
    return True, "fresh"


def render_marker(rows: list[dict], checked_at: str, decision: str, dedup: str) -> str:
    digest = hashlib.sha1(decision.encode("utf-8")).hexdigest()[:10]
    return "\n".join([
        MARKER_START,
        f"<!-- evergreen-gate: helper=evergreen_gate.py rows={len(rows)} "
        f"fetched={sum(1 for r in rows if r.get('verified'))} "
        f"sources={len({r['url'] for r in rows if r.get('verified')})} "
        f"hosts={len({host_of(r['url']) for r in rows if r.get('verified')})} "
        f"decision=\"sha1:{digest}\" dedup=\"{dedup[:60]}\" window_days={DEDUP_WINDOW_DAYS} "
        f"checked_at={checked_at} -->",
        MARKER_END,
    ])


def host_of(url: str) -> str:
    parts = url.split("//", 1)[-1].split("/", 1)[0].lower()
    return parts[4:] if parts.startswith("www.") else parts


# ---------------------------------------------------------------------------------------- checks

def verify_evidence(rows: list[dict], fetch) -> list[dict]:
    """Fetch every cited source and record whether it contains the figure it is cited for."""
    out = []
    for row in rows:
        url = row["url"]
        record = dict(row, status="incomplete", verified=False, reason="")
        parts = url.split("//", 1)
        if len(parts) != 2 or not parts[0].startswith("http") or not host_of(url):
            record.update(status="incomplete", reason=f"not an http(s) URL: {url!r}")
            out.append(record)
            continue
        if not row["figure"].strip():
            record.update(status="incomplete", reason="row cites no figure")
            out.append(record)
            continue
        fetched = fetch(url)
        record["http"] = fetched.get("http", "")
        if fetched.get("status") != "fetched":
            record.update(status=fetched.get("status", "unreachable"),
                          reason=fetched.get("reason", "source could not be retrieved"))
            out.append(record)
            continue
        evidence = chd.figure_evidence(row["figure"], fetched.get("text", ""))
        if not evidence:
            record.update(status="figure_absent",
                          reason=f"{row['figure']!r} does not appear in the fetched source")
        else:
            record.update(status="verified", verified=True, evidence=evidence[:300])
        out.append(record)
    return out


def check_dedup(value: str) -> tuple[bool, str]:
    """The de-dup line must name a prior artifact that actually exists.

    This verifies the *claim* rather than pretending to judge similarity: a token-overlap test on
    a one-line thesis produces both false retreads and false passes, so the rule is that the author
    names the nearest prior artifact and the gate proves the author looked.
    """
    refs = re.findall(r"\d{4}-\d{2}-\d{2}[A-Za-z0-9_.\-]*|[a-z0-9][a-z0-9\-]{8,}", value)
    if not refs:
        return False, "names no prior artifact (a date or slug) it was de-duped against"
    roots = [REPO / "published", REPO / "context" / "drafts", REPO / "context" / "recon_proposals"]
    for ref in refs:
        for root in roots:
            if root.exists() and any(ref in p.name for p in root.glob("*.md")):
                return True, f"matched a prior artifact: {ref}"
    return False, f"names {refs[0]!r}, which matches no file in published/, drafts/ or recon_proposals/"


def gate(text: str, fetch, no_network: bool = False) -> dict:
    """Run the floor over one brief's text. Returns a report dict; never raises for a bad brief."""
    parsed = parse_brief(text)
    report = {"errors": list(parsed["errors"]), "rows": parsed["rows"], "verified": [],
              "hosts": [], "dedup": ""}

    if not parsed["rows"]:
        report["errors"].append("no evidence table rows (see skills/evergreen_topics.md)")
    if len(parsed["rows"]) < MIN_SOURCES:
        report["errors"].append(
            f"{len(parsed['rows'])} evidence row(s); the floor is {MIN_SOURCES} primary sources")

    if parsed["rows"] and not no_network:
        report["verified"] = verify_evidence(parsed["rows"], fetch)
    elif parsed["rows"]:
        report["verified"] = [dict(r, status="skipped", verified=False, reason="--no-network")
                              for r in parsed["rows"]]

    verified = [r for r in report["verified"] if r.get("verified")]
    if parsed["rows"] and not no_network:
        for r in report["verified"]:
            if not r.get("verified"):
                report["errors"].append(f"source {r['n']} ({r['url']}) {r['status']}: {r['reason']}")
        if len(verified) < MIN_SOURCES:
            report["errors"].append(
                f"{len(verified)} of {len(parsed['rows'])} cited sources verified; the floor is "
                f"{MIN_SOURCES}")

    hosts = sorted({host_of(str(r["url"])) for r in (verified or parsed["rows"])
                    if str(r["url"]).startswith("http")})
    report["hosts"] = hosts
    report["decision"] = parsed["fields"].get("Decision the reader is facing", "")
    if parsed["rows"] and len(hosts) < MIN_HOSTS:
        report["errors"].append(
            f"{len(hosts)} distinct host(s) ({', '.join(hosts) or 'none'}); the floor is {MIN_HOSTS} "
            f"— several pages of one site are one source")

    dedup_value = parsed["fields"].get("De-dup", "")
    if dedup_value:
        ok, why = check_dedup(dedup_value)
        report["dedup"] = why
        if not ok:
            report["errors"].append(f"de-dup check unproven: {why}")

    if parsed["fields"].get("Durability"):
        # A durable topic states when its figures were true; a figure with no date cannot be
        # checked by a reader in six months, which is the whole point of the archetype.
        if not re.search(r"\bas of\b|undated|no expiry|does not expire|still true", dedup_value + " " +
                         parsed["fields"]["Durability"], re.I):
            report["errors"].append(
                "**Durability:** does not say what the figures are true *as of* (or why they do not "
                "expire) — an undated figure is a news fact wearing an evergreen label")

    report["ok"] = not report["errors"]
    return report


def print_report(path: Path, report: dict) -> None:
    print(f"evergreen gate: {path}")
    for row in report["verified"] or report["rows"]:
        tick = "OK " if row.get("verified") else "!!!"
        print(f"  {tick} [{row['n']}] {row['status']:<12} {row['url']}")
        if row.get("evidence"):
            print(f"       evidence: …{row['evidence'][:110]}…")
        elif row.get("reason"):
            print(f"       {row['reason']}")
    print(f"  hosts: {', '.join(report['hosts']) or 'none'}")
    if report["dedup"]:
        print(f"  de-dup: {report['dedup']}")
    for err in report["errors"]:
        print(f"  FAIL: {err}")
    print("  => " + ("PASS" if report["ok"] else "FAIL"))


def write_marker(path: Path, text: str, report: dict) -> str:
    checked_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    # The marker must record what was *verified*, not what was parsed: render it from the post-fetch
    # records (same length as the table, so `rows=` still detects an edited brief), or the audit
    # artifact reads fetched=0 on a brief whose sources all passed.
    block = render_marker(report.get("verified") or report["rows"], checked_at,
                          report.get("decision", ""), report["dedup"] or "")
    if MARKER_START in text and MARKER_END in text:
        start = text.index(MARKER_START)
        end = text.index(MARKER_END) + len(MARKER_END)
        text = text[:start] + block + text[end:]
    else:
        text = text.rstrip() + "\n\n## Gate result\n\n" + block + "\n"
    path.write_text(text, encoding="utf-8")
    return checked_at


def brief_paths() -> list[Path]:
    return sorted(Path(p) for p in glob.glob(str(REPO / "context" / "recon_proposals" / "*_evergreen_brief.md")))


def check_artifacts(no_network: bool) -> int:
    """Every committed evergreen brief carries a fresh marker (the verify.sh entry point)."""
    paths = brief_paths()
    if not paths:
        print("evergreen gate: no committed evergreen briefs yet")
        return 0
    failed = 0
    for path in paths:
        text = path.read_text(encoding="utf-8")
        parsed = parse_brief(text)
        fresh, why = marker_state(text, len(parsed["rows"]))
        if not fresh:
            print(f"FAIL: {path.name}: marker {why} — re-run "
                  f"`python3 scripts/evergreen_gate.py --brief {path.relative_to(REPO)}`")
            failed += 1
            continue
        if not no_network:
            report = gate(text, chd.fetch_source)
            if not report["ok"]:
                print_report(path, report)
                failed += 1
                continue
        print(f"  ok: {path.name} (marker fresh, rows={len(parsed['rows'])})")
    return 1 if failed else 0


# ------------------------------------------------------------------------------------- fixtures

def self_test() -> int:
    """Pin the floor's rules without a network: a stubbed fetch stands in for the live sources."""
    good_source = ("Grid resilience report 2026. Storm-related outages cost the median household "
                   "$412 in 2026 across 18 tracked events.")
    other_source = ("Permit cycle times: the median residential permit took 41 days in 2026.")
    third_source = ("Water heater standards: condensing units cut gas use by 22 percent in 2026.")
    pages = {
        "https://example.org/grid": good_source,
        "https://example.net/permits": other_source,
        "https://example.com/water-heaters": third_source,
    }

    def fetch(url):
        if url not in pages:
            return {"status": "unreachable", "http": "", "reason": "HTTP 404", "text": ""}
        return {"status": "fetched", "http": "200", "text": pages[url], "sha256": "x"}

    def brief(rows, *, decision="Whether to buy a standby generator or harden the roof first, "
                               "given the 2026 outage season.",
              durability="Figures are as of the 2026 reporting cycle and the underlying costs do "
                         "not expire — they are re-indexed annually.",
              dedup="2026-10-02_moss-landing-burns-home-becomes-the-grid (different thesis: grid "
                    "battery failure, not household spend)"):
        lines = [
            "# Evergreen Brief: home_equity_tco — 2026-10-06",
            "**Archetype:** evergreen",
            "**Vertical:** home_equity_tco",
            "**Persona:** pro_homeowner",
            f"**Decision the reader is facing:** {decision}",
            f"**Durability:** {durability}",
            f"**De-dup:** {dedup}",
            "**Thesis:** Household outage costs now exceed the amortized cost of the hardening "
            "they would justify.",
            "",
            "| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |",
            "|---|---|---|---|---|---|",
        ]
        for i, (url, figure, measured) in enumerate(rows, 1):
            lines.append(f"| {i} | source {i} | {url} | 2026-10-06 | {figure} | {measured} |")
        return "\n".join(lines) + "\n"

    checks = []

    def check(name, condition, detail=""):
        checks.append((name, bool(condition), detail))

    ok_brief = brief([("https://example.org/grid", "$412", "measured"),
                      ("https://example.net/permits", "41 days", "measured"),
                      ("https://example.com/water-heaters", "22 percent", "vendor claim")])
    r = gate(ok_brief, fetch)
    check("three verified sources on three hosts pass", r["ok"], str(r["errors"]))
    # The marker is the audit artifact: it must record what was verified, not what was parsed
    # (a live run once wrote fetched=0 sources=0 hosts=0 on a brief whose sources all passed).
    rendered = render_marker(r["verified"], "2026-10-06T00:00:00+00:00", r["decision"], r["dedup"])
    check("the marker records the verified counts",
          "rows=3 fetched=3 sources=3 hosts=3" in rendered, rendered)
    fresh, why = marker_state(ok_brief, 3)
    check("an unseeded brief is 'not seeded'", not fresh and why == "not seeded", why)

    r = gate(brief([("https://example.org/grid", "$412", "measured")]), fetch)
    check("one source fails the floor", not r["ok"], str(r["errors"]))
    check("the floor is named in the failure",
          any("floor is 3" in e for e in r["errors"]), str(r["errors"]))

    r = gate(brief([("https://example.org/grid", "$412", "measured"),
                    ("https://example.org/p2", "41 days", "measured"),
                    ("https://example.org/p3", "22 percent", "measured")]), fetch)
    check("three pages of one host is one source", not r["ok"], str(r["errors"]))
    check("the host floor is named", any("distinct host" in e for e in r["errors"]), str(r["errors"]))

    r = gate(brief([("https://example.org/grid", "$999", "measured"),
                    ("https://example.net/permits", "41 days", "measured"),
                    ("https://example.com/water-heaters", "22 percent", "measured")]), fetch)
    check("a figure absent from its source fails", not r["ok"], str(r["errors"]))

    r = gate(brief([("https://example.org/grid", "$412", "measured"),
                    ("https://example.net/permits", "41 days", "measured"),
                    ("https://example.com/missing", "22 percent", "measured")]), fetch)
    check("an unreachable source fails", not r["ok"], str(r["errors"]))

    r = gate(brief([("https://example.org/grid", "$412", "measured"),
                    ("https://example.net/permits", "41 days", "measured"),
                    ("https://example.com/water-heaters", "22 percent", "measured")],
                   dedup="nothing in particular"), fetch)
    check("an unproven de-dup fails", not r["ok"], str(r["errors"]))

    r = gate(brief([("https://example.org/grid", "$412", "measured"),
                    ("https://example.net/permits", "41 days", "measured"),
                    ("https://example.com/water-heaters", "22 percent", "measured")],
                   decision="?"), fetch)
    check("a placeholder decision fails", not r["ok"], str(r["errors"]))

    r = gate(brief([("https://example.org/grid", "$412", "measured"),
                    ("https://example.net/permits", "41 days", "measured"),
                    ("https://example.com/water-heaters", "22 percent", "measured")],
                   durability="It stays true."), fetch)
    check("a durability claim with no as-of date fails", not r["ok"], str(r["errors"]))
    check("the as-of rule is named", any("as of" in e for e in r["errors"]), str(r["errors"]))

    r = gate(ok_brief, fetch, no_network=True)
    check("--no-network reports shape only", "skipped" in str(r["verified"]), "")

    # marker staleness: a row added after the marker was written must read as stale
    seeded = ok_brief + "\n## Gate result\n\n" + render_marker(
        [{"url": "https://example.org/grid", "verified": True},
         {"url": "https://example.net/permits", "verified": True},
         {"url": "https://example.com/water-heaters", "verified": True}],
        "2026-10-06T00:00:00+00:00", "$412", "2026-10-02_moss") + "\n"
    fresh, why = marker_state(seeded, 3)
    check("a marker matching the table is fresh", fresh, why)
    edited = seeded.replace("| 3 | source 3 |", "| 4 | source 4 | https://example.org/p9 | 2026-10-06 | x | measured |\n| 3 | source 3 |")
    fresh, why = marker_state(edited, 4)
    check("a marker mismatched with the table is stale", not fresh and "stale" in why, why)

    failed = 0
    for name, ok, detail in checks:
        print(f"  {'PASS' if ok else 'FAIL'}  {name}" + (f"   [{detail}]" if not ok and detail else ""))
        failed += 0 if ok else 1
    print(f"evergreen gate self-test: {len(checks) - failed}/{len(checks)} passed")
    return 1 if failed else 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Evergreen evidence gate")
    ap.add_argument("--brief", help="path to an evergreen brief to verify (writes the marker on pass)")
    ap.add_argument("--check-artifacts", action="store_true",
                    help="verify every committed brief's marker is fresh (used by verify.sh)")
    ap.add_argument("--no-network", action="store_true", help="do not fetch sources (shape/parse only)")
    ap.add_argument("--self-test", action="store_true", help="pin the rules offline")
    args = ap.parse_args()

    if args.self_test:
        return self_test()
    if args.check_artifacts:
        return check_artifacts(args.no_network)
    if not args.brief:
        ap.print_help()
        return 2

    path = Path(args.brief)
    if not path.is_absolute():
        path = (REPO / path).resolve()
    if not path.exists():
        print(f"FAIL: no such brief: {path}")
        return 1
    text = path.read_text(encoding="utf-8")
    report = gate(text, chd.fetch_source, no_network=args.no_network)
    print_report(path, report)
    if not report["ok"]:
        print("\nThe evergreen gate is a floor, not a score: no article is drafted from this brief "
              "until it passes. Fix the rows above, or return \"no publish\" and say why.")
        return 1
    if args.no_network:
        print("\n(--no-network: sources were not fetched, so no marker was written)")
        return 0
    checked_at = write_marker(path, text, report)
    print(f"\nPASS — marker written to {path.name} at {checked_at}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
