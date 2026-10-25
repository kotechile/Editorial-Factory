#!/usr/bin/env python3
"""Review gate — the evidence floor for the review / comparison pipeline.

Why a third gate. The news fleet is gated on freshness, the evergreen fleet on durability, and
neither scores a *product* claim. A desk review sells numbers: price, runtime, weight, decibels,
acre rating. Those are exactly the numbers an affiliate-shaped pipeline is tempted to invent, and
an invented price is worse than no article — it is a false claim on a page that carries a buy link.

So the floor is code, and it reuses the evergreen gate's fetcher rather than re-implementing it:

  * every product in the price table carries a number and an `https://` source, and that number
    must appear in a cited source the gate actually fetched;
  * >= 3 verified figures on >= 2 hosts (several pages of one manufacturer are one source);
  * the brief states the date its prices were true, and that date is recent — a six-month-old
    price is a wrong price;
  * a comparison holds 2-4 products, a quick review exactly one primary product;
  * **no hands-on claim.** This pipeline cannot test hardware, so "we tested", "in our tests",
    "our unit" and friends are a failure, not a style note. The article says what the specs and
    owner reports show, and says that it did not handle the unit.

Usage:
  python3 scripts/review_gate.py --brief context/recon_proposals/<date>_<vertical>_review_brief.md
  python3 scripts/review_gate.py --brief <path> --no-network     # shape/parse only
  python3 scripts/review_gate.py --check-artifacts [--no-network]
  python3 scripts/review_gate.py --self-test
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

import citation_hub_dossier as chd          # noqa: E402
import evergreen_gate as eg                 # noqa: E402  (parse_brief / verify_evidence / host_of)

MIN_SOURCES = eg.MIN_SOURCES                # 3 verified figures
MIN_HOSTS = eg.MIN_HOSTS                    # 2 distinct hosts
MAX_PRICE_AGE_DAYS = 60
MAX_PRODUCTS = 4

MARKER_START = "<!-- review-gate:start -->"
MARKER_END = "<!-- review-gate:end -->"

REQUIRED_FIELDS = (
    "Vertical",
    "Persona",
    "Decision the reader is facing",
    "Format",
    "Price as of",
    "Verdict",
    "De-dup",
    "Thesis",
)
MIN_FIELD_CHARS = {
    "Decision the reader is facing": 40,
    "Verdict": 60,
    "Thesis": 30,
    "De-dup": 12,
}
FORMATS = ("quick_review", "comparison")

# A desk review must not imply use. These are the phrases that turn a spec comparison into a
# testimonial, and there is no version of this pipeline where that claim is true.
HANDS_ON = re.compile(
    r"\b(we|our team)\s+(tested|measured|ran|used|tried|put)\b"
    r"|\bin our (tests?|testing|workshop)\b"
    r"|\bhands[- ]on\b"
    r"|\bour (review )?unit\b"
    r"|\bafter \d+ (weeks?|months?) of (testing|use)\b",
    re.I,
)


class GateFailure(RuntimeError):
    """Raised when a brief cannot pass the evidence floor."""


# ------------------------------------------------------------------------------------- parsing

def parse_products(text: str) -> list[dict]:
    """Rows of the price table: | product | price | url | note |.

    Kept separate from the evidence table because they answer different questions — the price
    table names *what is being compared*, the evidence table proves *where each number came from*.
    It reads exactly one table: the first whose header carries both `product` and `price`, ending
    at the blank line or at the next header (the evidence table immediately below it).
    """
    rows: list[dict] = []
    in_table = False
    for line in text.splitlines():
        stripped = line.strip()
        if in_table and not stripped:
            break
        if not stripped.startswith("|") or set(stripped) <= set("|-: "):
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if len(cells) < 3:
            continue
        head = " ".join(cells).lower()
        if "product" in head and "price" in head:
            in_table = True
            continue
        if not in_table:
            continue
        # A second header (the evidence table) or a numbered row means the price table ended.
        if cells[0] in ("#", "n", "no") or re.match(r"^\d+$", cells[0]) or "url" in head:
            break
        rows.append({
            "product": cells[0],
            "price": cells[1],
            "url": cells[2],
            "note": cells[3] if len(cells) > 3 else "",
        })
    return rows


def price_number(value: str) -> int | None:
    digits = re.sub(r"[^0-9]", "", value or "")
    return int(digits) if digits else None


# A listed price and the page that carries it have to be compared in whatever form each was
# written. The pattern used to guard the price check matched whole dollars only, so a consumer
# price written with cents ("$49.97") could never be backed by the page that prints it — the
# gate reported "not backed by any verified evidence row" for a correctly sourced row.
_MONEY = re.compile(r"\$?\d[\d,]*(?:\.\d{1,2})?")


def price_keys(value: str) -> set[int]:
    """Every numeric form of a price, for matching a listed price against a fetched page.

    `$49.97` and `49.97` both key on 4997; a price ending in .00 also keys on its whole-dollar
    form, so a page that drops the cents still backs a listed `$49.00`.
    """
    digits = price_number(value)
    if digits is None:
        return set()
    keys = {digits}
    if re.search(r"\.\d{2}\s*$", (value or "").strip()):
        keys.add(digits // 100)
    return keys


def parse_date(value: str) -> date | None:
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", value or "")
    if not m:
        return None
    try:
        return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None


# -------------------------------------------------------------------------------------- checks

def gate(text: str, fetch, no_network: bool = False, today: date | None = None) -> dict:
    """Run the floor over one review brief. Returns a report; never raises for a bad brief."""
    today = today or datetime.now(timezone.utc).date()
    parsed = eg.parse_brief(text)                      # evidence rows + its own field errors
    evidence = parsed["rows"]
    report = {"errors": [], "rows": evidence, "verified": [], "hosts": [], "products": [],
              "format": "", "price_as_of": "", "dedup": ""}

    fields = {}
    for name in REQUIRED_FIELDS:
        m = re.search(rf"^\*\*{re.escape(name)}:?\*\*\s*(.*)$", text, re.M)
        value = (m.group(1).strip() if m else "")
        fields[name] = value
        if not value:
            report["errors"].append(f"missing field: **{name}:**")
        elif name in MIN_FIELD_CHARS and len(value) < MIN_FIELD_CHARS[name]:
            report["errors"].append(
                f"**{name}:** is too thin to be checkable ({len(value)} chars, "
                f"needs >= {MIN_FIELD_CHARS[name]})")

    fmt = fields.get("Format", "").strip().lower()
    report["format"] = fmt
    if fmt and fmt not in FORMATS:
        report["errors"].append(
            f"**Format:** {fmt!r} is not one of {', '.join(FORMATS)}")

    if fmt and fields.get("Vertical"):
        registry = _registry_ids()
        if registry and fields["Vertical"].strip() not in registry:
            report["errors"].append(
                f"**Vertical:** {fields['Vertical'].strip()!r} is not a registry vertical")

    # --- prices are dated ---------------------------------------------------------------
    price_as_of = fields.get("Price as of", "")
    report["price_as_of"] = price_as_of
    if price_as_of:
        when = parse_date(price_as_of)
        if not when:
            report["errors"].append("**Price as of:** is not a YYYY-MM-DD date")
        elif when > today:
            report["errors"].append(f"**Price as of:** {when} is in the future")
        elif (today - when).days > MAX_PRICE_AGE_DAYS:
            report["errors"].append(
                f"**Price as of:** {when} is {(today - when).days} days old; a price older than "
                f"{MAX_PRICE_AGE_DAYS} days is a wrong price, not a durable one")

    # --- product table ------------------------------------------------------------------
    products = parse_products(text)
    report["products"] = products
    if not products:
        report["errors"].append("no product table (see skills/review_comparison.md)")
    if fmt == "comparison":
        if len(products) < 2:
            report["errors"].append("a comparison needs at least 2 products in the price table")
        if len(products) > MAX_PRODUCTS:
            report["errors"].append(
                f"{len(products)} products; a comparison above {MAX_PRODUCTS} is a catalogue, "
                f"not a decision")
    if fmt == "quick_review" and len(products) > 1:
        report["errors"].append(
            "a quick review has exactly one primary product — use Format: comparison for a "
            "head-to-head")

    for row in products:
        price = price_number(row["price"])
        if price is None or price <= 0:
            report["errors"].append(f"product {row['product']!r} has no numeric price")
        if not str(row["url"]).startswith("http"):
            report["errors"].append(f"product {row['product']!r} cites no http(s) price source")

    # --- evidence floor -----------------------------------------------------------------
    if not evidence:
        report["errors"].append("no evidence table rows (see skills/review_comparison.md)")
    if len(evidence) < MIN_SOURCES:
        report["errors"].append(
            f"{len(evidence)} evidence row(s); the floor is {MIN_SOURCES} cited figures")

    if evidence and not no_network:
        report["verified"] = eg.verify_evidence(evidence, fetch)
        for r in report["verified"]:
            if not r.get("verified"):
                report["errors"].append(f"source {r['n']} ({r['url']}) {r['status']}: {r['reason']}")
    elif evidence:
        report["verified"] = [dict(r, status="skipped", verified=False, reason="--no-network")
                              for r in evidence]

    verified = [r for r in report["verified"] if r.get("verified")]
    if evidence and not no_network and len(verified) < MIN_SOURCES:
        report["errors"].append(
            f"{len(verified)} of {len(evidence)} cited sources verified; the floor is {MIN_SOURCES}")

    hosts = sorted({eg.host_of(str(r["url"])) for r in (verified or evidence)
                    if str(r["url"]).startswith("http")})
    report["hosts"] = hosts
    if evidence and len(hosts) < MIN_HOSTS:
        report["errors"].append(
            f"{len(hosts)} distinct host(s) ({', '.join(hosts) or 'none'}); the floor is "
            f"{MIN_HOSTS} — several pages of one manufacturer are one source")

    # --- every price is backed by a fetched figure --------------------------------------
    # The check that matters: a price is only admissible if some verified evidence row carries
    # that same number. A price with a plausible-looking URL next to it is the exact defect this
    # gate exists for.
    if verified:
        verified_text = " ".join(f"{r.get('figure','')} {r.get('evidence','')}" for r in verified)
        verified_nums: set[int] = set()
        for token in _MONEY.findall(verified_text):
            verified_nums |= price_keys(token)
        for row in products:
            keys = price_keys(row["price"])
            if keys and not (keys & verified_nums):
                report["errors"].append(
                    f"price ${price_number(row['price']):,} for {row['product']!r} is not backed "
                    f"by any verified evidence row — cite the page that shows that price")

    # --- no hands-on claim --------------------------------------------------------------
    hit = HANDS_ON.search(text)
    if hit:
        report["errors"].append(
            f"hands-on claim {hit.group(0)!r}: this pipeline does not handle hardware — a desk "
            f"review must say what the specs and owner reports show, never that we used it")

    # --- verdict names a winner ---------------------------------------------------------
    verdict = fields.get("Verdict", "")
    if verdict and products:
        named = [p["product"] for p in products
                 if p["product"] and re.search(re.escape(p["product"].split()[0]), verdict, re.I)]
        if not named:
            report["errors"].append(
                "**Verdict:** names none of the products in the price table — the reader is left "
                "to guess the recommendation")

    dedup_value = fields.get("De-dup", "")
    if dedup_value:
        ok, why = eg.check_dedup(dedup_value)
        report["dedup"] = why
        if not ok:
            report["errors"].append(f"de-dup check unproven: {why}")

    report["ok"] = not report["errors"]
    return report


def _registry_ids() -> set[str]:
    try:
        import json
        with open(REPO / "context" / "verticals.json") as f:
            return {v["id"] for v in json.load(f).get("verticals", [])}
    except Exception:                                                   # noqa: BLE001
        return set()


# ------------------------------------------------------------------------------------ artifact

def marker_state(text: str, rows: int, products: int) -> tuple[bool, str]:
    if MARKER_START not in text or MARKER_END not in text:
        return False, "not seeded"
    block = text[text.index(MARKER_START):text.index(MARKER_END)]
    m = re.search(r"rows=(\d+)", block)
    p = re.search(r"products=(\d+)", block)
    if not m or not p:
        return False, "marker is missing its counts"
    if int(m.group(1)) != rows or int(p.group(1)) != products:
        return False, (f"stale (marker says rows={m.group(1)} products={p.group(1)}, the brief has "
                       f"rows={rows} products={products})")
    return True, "fresh"


def render_marker(report: dict, checked_at: str) -> str:
    verified = report.get("verified") or report["rows"]
    return "\n".join([
        MARKER_START,
        f"<!-- review-gate: helper=review_gate.py format={report['format'] or 'none'} "
        f"rows={len(report['rows'])} products={len(report['products'])} "
        f"fetched={sum(1 for r in verified if r.get('verified'))} "
        f"hosts={len(report['hosts'])} price_as_of={report['price_as_of'][:10] or 'none'} "
        f"checked_at={checked_at} -->",
        MARKER_END,
    ])


def write_marker(path: Path, text: str, report: dict) -> str:
    checked_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    block = render_marker(report, checked_at)
    if MARKER_START in text and MARKER_END in text:
        start = text.index(MARKER_START)
        end = text.index(MARKER_END) + len(MARKER_END)
        text = text[:start] + block + text[end:]
    else:
        text = text.rstrip() + "\n\n## Gate result\n\n" + block + "\n"
    path.write_text(text, encoding="utf-8")
    return checked_at


def print_report(path: Path, report: dict) -> None:
    print(f"review gate: {path}")
    for row in report["products"]:
        print(f"  product [{row['product']}] {row['price']}  {row['url']}")
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


def brief_paths() -> list[Path]:
    return sorted(Path(p) for p in
                  glob.glob(str(REPO / "context" / "recon_proposals" / "*_review_brief.md")))


def check_artifacts(no_network: bool) -> int:
    paths = brief_paths()
    if not paths:
        print("review gate: no committed review briefs yet")
        return 0
    failed = 0
    for path in paths:
        text = path.read_text(encoding="utf-8")
        report = gate(text, chd.fetch_source, no_network=no_network)
        fresh, why = marker_state(text, len(report["rows"]), len(report["products"]))
        if not fresh:
            print(f"FAIL: {path.name}: marker {why} — re-run "
                  f"`python3 scripts/review_gate.py --brief {path.relative_to(REPO)}`")
            failed += 1
        elif not no_network and not report["ok"]:
            print_report(path, report)
            failed += 1
        else:
            print(f"  ok: {path.name} (marker fresh, products={len(report['products'])})")
    return 1 if failed else 0


# ------------------------------------------------------------------------------------ self-test

def self_test() -> int:
    """Pin the rules without a network."""
    pages = {
        "https://example.org/mower": "The Luba 2 AWD lists at $1,599 with a 1.5 acre rating.",
        "https://example.net/blower": "Two-stage 56V snow blower MSRP $1,299, 21-inch auger.",
        "https://example.com/bench": "Runtime measured at 62 minutes per 7.5Ah pack; weight 38 lb.",
        "https://example.org/meter": "The pin meter lists at $34.98 and senses to a 0.38 inch depth.",
    }

    def fetch(url):
        if url not in pages:
            return {"status": "unreachable", "http": "", "reason": "HTTP 404", "text": ""}
        return {"status": "fetched", "http": "200", "text": pages[url], "sha256": "x"}

    today = date(2026, 10, 24)

    def brief(*, fmt="comparison", products=None, price_as_of="2026-10-20",
              verdict="Buy the Luba 2 AWD for a fenced acre; the two-stage blower wins only "
                      "where snow events exceed ten a year.",
              verdict_override=None, extra="", price_rows=None):
        products = products if products is not None else [
            ("Luba 2 AWD", "$1,599", "https://example.org/mower", "1.5 acre rating"),
            ("56V two-stage", "$1,299", "https://example.net/blower", "21-inch auger"),
        ]
        table = ["| Product | Price | Source | Note |", "|---|---|---|---|"]
        table += [f"| {p} | {pr} | {u} | {n} |" for p, pr, u, n in products]
        rows = price_rows if price_rows is not None else [
            ("1", "Mammotion spec page", "https://example.org/mower", "2026-10-20", "$1,599", ""),
            ("2", "EGO product page", "https://example.net/blower", "2026-10-20", "$1,299", ""),
            ("3", "Runtime bench", "https://example.com/bench", "2026-10-20", "62 minutes", ""),
        ]
        evidence = ["| # | Source | URL | Retrieved | Figure | Measured |", "|---|---|---|---|---|---|"]
        evidence += [f"| {n} | {s} | {u} | {r} | {f} | {m} |" for n, s, u, r, f, m in rows]
        return "\n".join([
            "## Review brief",
            "",
            "**Vertical:** yard_robotics",
            "**Persona:** homeowner_pro",
            "**Decision the reader is facing:** whether to replace a weekly mowing contract with a "
            "robot mower for a fenced one-acre lawn.",
            f"**Format:** {fmt}",
            f"**Price as of:** {price_as_of}",
            f"**Verdict:** {verdict_override or verdict}",
            "**De-dup:** 2026-10-20_yard_robotics_signals covers nav tech, not a price comparison.",
            "**Thesis:** the contract is the benchmark, and the robot only wins after the "
            "residual edging labor is priced in.",
            "",
            *table,
            "",
            *evidence,
            extra,
        ])

    cases: list[tuple[str, bool, str]] = []

    def case(name, text, want_ok, want_reason=""):
        report = gate(text, fetch, today=today)
        ok = report["ok"] == want_ok
        if ok and want_reason:
            ok = any(want_reason in e for e in report["errors"])
        cases.append((name, ok, "; ".join(report["errors"])[:220]))

    # The de-dup line is a claim that a named prior artifact exists, and it is pinned by
    # test_evergreen_gate.py against the real tree. Here the fixture's artifact is synthetic, so
    # the check is stubbed rather than pointed at a file that could be archived later.
    real_check_dedup = eg.check_dedup
    eg.check_dedup = lambda value: (True, "stubbed for the fixture")
    try:
        case("clean comparison passes", brief(), True)
        case("a cents price is backed by the page that prints it", brief(
            products=[
                ("Luba 2 AWD", "$1,599", "https://example.org/mower", "1.5 acre rating"),
                ("Pin meter", "$34.98", "https://example.org/meter", "3/8 inch depth"),
            ],
            price_rows=[
                ("1", "Mammotion spec page", "https://example.org/mower", "2026-10-20", "$1,599", ""),
                ("2", "Meter product page", "https://example.org/meter", "2026-10-20", "$34.98", ""),
                ("3", "Runtime bench", "https://example.com/bench", "2026-10-20", "62 minutes", ""),
            ],
        ), True)
        case("hands-on claim fails", brief(extra="\nWe tested the unit for three weeks.\n"), False,
             "hands-on claim")
        case("comparison with one product fails", brief(products=[
            ("Luba 2 AWD", "$1,599", "https://example.org/mower", "1.5 acre")]), False,
             "at least 2 products")
        case("quick review with two products fails", brief(fmt="quick_review"), False,
             "exactly one primary product")
        case("stale prices fail", brief(price_as_of="2026-06-01"), False, "days old")
        case("unsourced price fails", brief(products=[
            ("Luba 2 AWD", "$1,599", "https://example.org/mower", ""),
            ("56V two-stage", "$2,499", "https://example.net/blower", ""),
        ]), False, "not backed by any verified evidence row")
        case("verdict naming no product fails", brief(verdict_override=(
            "Buy whichever unit has the better warranty, because the category is close.")), False,
            "names none of the products")
        case("unknown format fails", brief(fmt="listicle"), False, "is not one of")
    finally:
        eg.check_dedup = real_check_dedup

    failed = 0
    for name, ok, detail in cases:
        print(f"  {'ok  ' if ok else 'FAIL'} {name}")
        if not ok:
            print(f"       {detail}")
            failed += 1
    print(f"review gate self-test: {len(cases) - failed}/{len(cases)} passed")
    return 1 if failed else 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Review evidence gate")
    ap.add_argument("--brief", help="path to a review brief to verify (writes the marker on pass)")
    ap.add_argument("--check-artifacts", action="store_true")
    ap.add_argument("--no-network", action="store_true", help="do not fetch sources")
    ap.add_argument("--self-test", action="store_true", help="pin the rules offline")
    args = ap.parse_args()

    if args.self_test:
        return self_test()
    if args.check_artifacts:
        return check_artifacts(args.no_network)
    if not args.brief:
        ap.error("one of --brief, --check-artifacts or --self-test is required")

    path = Path(args.brief)
    if not path.is_absolute():
        path = REPO / path
    if not path.exists():
        print(f"review gate: no such brief: {path}")
        return 2
    text = path.read_text(encoding="utf-8")
    report = gate(text, chd.fetch_source, no_network=args.no_network)
    print_report(path, report)
    if report["ok"]:
        checked_at = write_marker(path, text, report)
        print(f"  marker written at {checked_at}")
        return 0
    print("\nThe review gate is a floor, not a score: a passing brief still has to be worth "
          "reading. Fix the rows above and re-run — do not draft from a failing brief.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
