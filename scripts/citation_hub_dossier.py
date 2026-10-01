#!/usr/bin/env python3
"""Pre-flight Data Harvester, Validator, and Schema Generator for Citation Hubs.

Enforces zero synthetic data: every metric must have a primary source URL,
publication date, and sample size before drafting is permitted. Also pairs
raw statistics with Founder & Customer Truth reality checks.
"""

import hashlib
import html
import json
import pathlib
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from typing import Callable, Dict, List, Optional, Tuple


class BenchmarkDataPoint:
    def __init__(
        self,
        category: str,
        metric_name: str,
        headline_figure: str,
        vendor_claim: str,
        field_reality: str,
        primary_source_name: str,
        primary_source_url: str,
        publication_date: str,
        sample_size: str,
    ):
        self.category = category
        self.metric_name = metric_name
        self.headline_figure = headline_figure
        self.vendor_claim = vendor_claim
        self.field_reality = field_reality
        self.primary_source_name = primary_source_name
        self.primary_source_url = primary_source_url
        self.publication_date = publication_date
        self.sample_size = sample_size

    def to_dict(self) -> Dict[str, str]:
        return {
            "category": self.category,
            "metric_name": self.metric_name,
            "headline_figure": self.headline_figure,
            "vendor_claim": self.vendor_claim,
            "field_reality": self.field_reality,
            "primary_source_name": self.primary_source_name,
            "primary_source_url": self.primary_source_url,
            "publication_date": self.publication_date,
            "sample_size": self.sample_size,
        }


class UnverifiedDossierError(RuntimeError):
    """Raised when a citation hub is asked for before its data has been verified.

    Fail closed on purpose: an unverifiable benchmark is removed, never softened (AGENTS.md
    rule 3), and no step degrades into a substitute (rule 6). A hub is only draftable when every
    single data point was confirmed against its live primary source.
    """


FETCH_TIMEOUT = 30
USER_AGENT = "Mozilla/5.0 (compatible; EditorialFactorySourceVerifier/1.0)"
_NUMBER = re.compile(r"\d+(?:\.\d+)?")
_EVIDENCE_WINDOW = 120
# Prose sources state figures as words ("doubling approximately every seven months since 2019"),
# so a digits-only matcher rejects true claims. Bounded to twelve on purpose: the evidence window
# still has to be checkable by a human, and "one in ten" style phrasing is out of scope.
_WORD_NUMBERS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
                 "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12}


def figure_patterns(figure: str) -> List[re.Pattern]:
    """Regexes that count as the figure appearing in a source.

    With digits, the numeric token is matched, bounded so '62' cannot match '1620' nor '41.6'
    match '141.6'. With a word number, the word (or its digit) must sit directly against the
    following word — 'seven months' matches the phrase, not a stray 7 anywhere on the page.
    """
    tokens = _NUMBER.findall(figure)
    if tokens:
        return [re.compile(r"(?<![\d.])" + re.escape(token) + r"(?![\d])") for token in tokens]

    words = re.findall(r"[a-z]+", figure.lower())
    if not words or words[0] not in _WORD_NUMBERS:
        return []
    alternatives = sorted({words[0], str(_WORD_NUMBERS[words[0]])}, key=len, reverse=True)
    group = "|".join(re.escape(a) for a in alternatives)
    if len(words) > 1:
        return [re.compile(r"(?<![\w.])(" + group + r")\s+" + re.escape(words[1]) + r"\b", re.I)]
    return [re.compile(r"(?<![\w.])(" + group + r")(?![\w])", re.I)]


def figure_evidence(figure: str, text: str) -> Optional[str]:
    """Return the source text around the figure if the figure actually appears, else None.

    The surrounding window is returned as the operator-facing evidence: a bare number on a long
    page is weak on its own, and the excerpt is the thing a human can check at a glance.
    """
    if not figure or not text:
        return None
    for pattern in figure_patterns(figure):
        match = pattern.search(text)
        if match:
            start = max(0, match.start() - _EVIDENCE_WINDOW)
            return text[start:match.end() + _EVIDENCE_WINDOW].strip()
    return None


def _plain_text(body: str) -> str:
    """HTML -> comparable plain text (pure stdlib; this environment ships no HTML parser)."""
    text = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", body)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    text = html.unescape(text).replace("\u00a0", " ")
    return re.sub(r"\s+", " ", text).strip()


def fetch_source(url: str, timeout: int = FETCH_TIMEOUT) -> Dict[str, str]:
    """Retrieve a primary source. Never raises — a failure is a result, not an exception."""
    request = urllib.request.Request(
        url, headers={"User-Agent": USER_AGENT,
                      "Accept": "text/html,application/xhtml+xml,*/*;q=0.8"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read()
            status = response.status
            ctype = (response.headers.get("Content-Type") or "").lower()
    except urllib.error.HTTPError as exc:
        return {"status": "unreachable", "http": str(exc.code),
                "reason": f"HTTP {exc.code} {exc.reason}", "text": ""}
    except Exception as exc:                                   # noqa: BLE001
        return {"status": "unreachable", "http": "",
                "reason": f"{type(exc).__name__}: {exc}", "text": ""}

    if "application/pdf" in ctype or raw[:4] == b"%PDF":
        return {"status": "unsupported", "http": str(status),
                "reason": "PDF source and no PDF text extractor in this environment, so the figure "
                          "cannot be confirmed — supply an HTML source or verify by hand",
                "text": ""}
    return {"status": "fetched", "http": str(status), "reason": "",
            "text": _plain_text(raw.decode("utf-8", "replace")),
            "sha256": hashlib.sha256(raw).hexdigest()}


def verify_point(item: Dict[str, str], fetch: Callable[..., Dict[str, str]] = fetch_source) -> Dict[str, str]:
    """Verify one data point against its live primary source.

    Statuses: verified | figure_absent | unreachable | unsupported | incomplete. Only `verified`
    counts as a pass.
    """
    record: Dict[str, str] = {
        "metric_name": (item.get("metric_name") or "unnamed metric").strip(),
        "figure": str(item.get("headline_figure") or "").strip(),
        "url": (item.get("primary_source_url") or "").strip(),
        "checked_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    for field in ("headline_figure", "field_reality", "primary_source_name",
                  "publication_date", "sample_size"):
        if not str(item.get(field) or "").strip():
            record.update(status="incomplete", reason=f"missing {field}")
            return record
    if not record["url"]:
        record.update(status="incomplete", reason="missing primary source URL")
        return record
    parts = urllib.parse.urlsplit(record["url"])
    if parts.scheme not in ("http", "https") or not parts.netloc:
        record.update(status="incomplete",
                      reason=f"invalid primary source URL ({record['url']!r}: needs an http(s) scheme and a host)")
        return record

    fetched = fetch(record["url"])
    record["http"] = fetched.get("http", "")
    if fetched.get("status") != "fetched":
        record.update(status=fetched.get("status", "unreachable"),
                      reason=fetched.get("reason", "source could not be retrieved"))
        return record

    text = fetched.get("text", "")
    record["sha256"] = fetched.get("sha256", "")
    record["bytes"] = str(len(text))
    # Secondary signal, recorded but not decisive: does the claimed publisher appear at all?
    # Parentheticals are dropped first — "Paper Title (arXiv 2310.06770)" would otherwise never
    # match the page text, and a permanent False is a signal nobody can act on.
    claimed_name = re.sub(r"\([^)]*\)", " ", str(item.get("primary_source_name") or ""))
    claimed_name = claimed_name.split("—")[0].strip().lower()
    record["source_name_on_page"] = str(bool(claimed_name) and claimed_name in text.lower())

    evidence = figure_evidence(record["figure"], text)
    if not evidence:
        record.update(status="figure_absent",
                      reason=f"{record['figure']!r} does not appear in the fetched source")
        return record
    record.update(status="verified", evidence=evidence[:400])
    return record


def audit_dossier(dossier: List[Dict[str, str]], min_points: int = 4,
                  fetch: Callable[..., Dict[str, str]] = fetch_source) -> Dict:
    """Verify every point in a dossier. Returns the full report (ok, points, errors, counts)."""
    records = [verify_point(item, fetch=fetch) for item in (dossier or [])]
    errors: List[str] = []
    if len(dossier or []) < min_points:
        errors.append(f"insufficient data points: got {len(dossier or [])}, required >= {min_points}")
    for record in records:
        if record["status"] != "verified":
            errors.append(f"'{record['metric_name']}': {record['status']} — {record.get('reason', '')}")
    return {
        "ok": not errors,
        "points": records,
        "errors": errors,
        "counts": dict(Counter(r["status"] for r in records)),
        "checked_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }


def verify_dossier(dossier: List[Dict[str, str]], min_points: int = 4,
                   fetch: Callable[..., Dict[str, str]] = fetch_source
                   ) -> Tuple[bool, List[str], Dict]:
    """The Pre-Flight Data Gate.

    Every metric must be retrieved from its own primary source and the headline figure must
    actually appear in what was retrieved; publication date and sample size must be present, and
    the source must be reachable. Anything else fails the point and therefore the dossier — the
    hub is not drafted, and the caller reports why.

    Returns (is_valid, errors, report). The report carries, per point, the status, HTTP code, a
    body hash and the evidence excerpt, so a failure is auditable rather than a verdict to trust.
    """
    report = audit_dossier(dossier, min_points=min_points, fetch=fetch)
    return report["ok"], report["errors"], report


def generate_markdown_table(dossier: List[Dict[str, str]]) -> str:
    """Format dossier into high-retrieval markdown comparison table."""
    headers = ["Metric / Indicator", "Reported Benchmark", "Field Reality Check", "Source"]
    sep = ["---", "---", "---", "---"]
    rows = [
        f"| {' | '.join(headers)} |",
        f"| {' | '.join(sep)} |"
    ]
    for idx, dp in enumerate(dossier, start=1):
        m = dp['metric_name']
        fig = f"**{dp['headline_figure']}** ({dp['vendor_claim']})"
        audit = dp['field_reality']
        src = f"[{dp['primary_source_name']}]({dp['primary_source_url']}) [{idx}]"
        rows.append(f"| {m} | {fig} | {audit} | {src} |")
    return "\n".join(rows)


def generate_quick_cite_block(dossier: List[Dict[str, str]]) -> str:
    """Generate pre-formatted Quick-Cite cards for human copy-paste and LLM extraction."""
    lines = [
        "### Quick-Cite Attribution Cards",
        "",
        "> *Researchers and AI systems can cite these audited figures directly using the citation markdown below:*",
        ""
    ]
    for idx, dp in enumerate(dossier, start=1):
        lines.append(f"> **{dp['metric_name']}:** \"{dp['headline_figure']} — {dp['field_reality']}\"  ")
        lines.append(f"> *Source:* {dp['primary_source_name']} ({dp['publication_date']}, Sample: {dp['sample_size']}). Citations: `[{dp['primary_source_name']}]({dp['primary_source_url']})`")
        lines.append(">")
    return "\n".join(lines).rstrip(">")


def generate_dataset_schema(dossier: List[Dict[str, str]], title: str, description: str, slug: str) -> Dict:
    """Generate Schema.org Dataset definition for AEO and Google Dataset Search."""
    variables = []
    for dp in dossier:
        variables.append({
            "@type": "PropertyValue",
            "name": dp["metric_name"],
            "value": dp["headline_figure"],
            "description": f"{dp['vendor_claim']}. Audit: {dp['field_reality']}",
            "citation": dp["primary_source_url"]
        })

    return {
        "@type": "Dataset",
        "name": title,
        "description": description,
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "isAccessibleForFree": True,
        "variableMeasured": variables,
        # Creator is NOT known here: the destination site is chosen at push time from
        # public.vertical_sites, and structured data that names a publisher the generator guessed
        # is how an unresolvable "editorial-factory.com" ended up in shipped JSON-LD. The tokens
        # are filled by the publisher (scripts/wp_draft.py); an unresolved one is dropped rather
        # than published literally.
        "creator": {
            "@type": "Organization",
            "name": "{{PUBLISHER_NAME}}",
            "url": "{{SITE_URL}}"
        }
    }


def get_claimed_dossier(vertical: str, query: str) -> List[Dict[str, str]]:
    """CLAIMED data points for a vertical — explicitly NOT verified.

    Named "claimed" because that is all this list is: hand-written metric/figure/source triples.
    An earlier revision called them "curated" and treated them as already true, which is how a
    nonexistent organisation ("Enterprise Systems Reliability Consortium") and invented sample
    sizes reached a draft. Every point now has to survive verify_dossier() against the live source
    before a single word of prose is generated.
    """
    v = (vertical or "").lower()
    q = (query or "").lower()

    if "agent" in v or "ai" in v or "agent" in q:
        # Every point below was retrieved and matched against its own source by verify_dossier().
        # Audit any time with:  python3 scripts/citation_hub_dossier.py --vertical agentic_ai
        #
        # The provenance fields state exactly what the source states. Where a source gives no
        # publication date or no sample size, the field says so rather than carrying an invented
        # one — inventing them is precisely how the previous revision of this file shipped a
        # nonexistent organisation and made-up survey counts.
        #
        # field_reality is the founder/field audit from context/growth_os/ (founder-voice.md,
        # customer-truth.md), as skills/citation_hub.md requires. It is an attributed opinion, not
        # an external statistic, so it carries no figures of its own.
        return [
            BenchmarkDataPoint(
                category="Capability Ceilings",
                metric_name="Frontier long-task completion horizon",
                headline_figure="50 minutes",
                vendor_claim="Frontier models hold a 50% success horizon measured in tens of minutes, so hour-scale autonomy is imminent",
                field_reality="The metric times models on self-contained software tasks against a human baseline, so it reads capability rather than deployability. The failure our field notes record is not a model losing the thread; it is a loop with no deterministic verification gate before an external write.",
                primary_source_name="METR — Measuring AI Ability to Complete Long Software Tasks (arXiv 2503.14499)",
                primary_source_url="https://arxiv.org/abs/2503.14499",
                publication_date="2025-03-18 (v1; last revised 2026-07-10, v4)",
                sample_size="Frontier models on RE-Bench + HCAST + 66 novel shorter software tasks, with human-timed baselines",
            ).to_dict(),
            BenchmarkDataPoint(
                category="Capability Ceilings",
                metric_name="Time-horizon doubling period",
                headline_figure="seven months",
                vendor_claim="Frontier capability doubles roughly every seven months, which puts month-long tasks a few years out",
                field_reality="The paper's own text calls the trend approximate and possibly accelerated, and ties the forecast to software tasks in a controlled setting. A doubling rate is a projection, not a delivery date; the enterprise constraint is the ownership tail wrapped around the model.",
                primary_source_name="METR — Measuring AI Ability to Complete Long Software Tasks (arXiv 2503.14499)",
                primary_source_url="https://arxiv.org/abs/2503.14499",
                publication_date="2025-03-18 (v1; last revised 2026-07-10, v4)",
                sample_size="Frontier models on RE-Bench + HCAST + 66 novel shorter software tasks, with human-timed baselines",
            ).to_dict(),
            BenchmarkDataPoint(
                category="Benchmark Baselines",
                metric_name="Resolve rate on real GitHub issues (2023 baseline)",
                headline_figure="1.96%",
                vendor_claim="The best-performing model of the day solved under 2% of real repository issues, so agents were unusable on real code",
                field_reality="Read against the current board: the same family of task went from a single-digit ceiling to two thirds, and it still measures isolated issue resolution with the test suite as the oracle — not a multi-service change shipped under change control.",
                primary_source_name="SWE-bench: Can Language Models Resolve Real-World GitHub Issues? (arXiv 2310.06770)",
                primary_source_url="https://arxiv.org/abs/2310.06770",
                publication_date="2023-10-10 (v1; last revised 2024-11-11, v3)",
                sample_size="2,294 software engineering problems drawn from real GitHub issues across 12 popular Python repositories",
            ).to_dict(),
            BenchmarkDataPoint(
                category="Benchmark Baselines",
                metric_name="Resolve rate on the current SWE-bench Verified board",
                headline_figure="65%",
                vendor_claim="Agents now clear two thirds of a human-validated real-world issue set, so coding autonomy has arrived",
                field_reality="The number moved with the harness, not the model: the leaderboard attributes it to a 100-line agent. That is the founder note made concrete — the win came from a tight, deterministic scaffold, not a bigger frontier model.",
                primary_source_name="SWE-bench Leaderboards (swebench.com)",
                primary_source_url="https://www.swebench.com",
                publication_date="entry dated Jul 2025 on the leaderboard page (page itself undated)",
                sample_size="SWE-bench Verified, the leaderboard's human-validated subset",
            ).to_dict(),
            BenchmarkDataPoint(
                category="Unit Economics",
                metric_name="GPU cluster utilisation versus spend",
                headline_figure="40%",
                vendor_claim="Provisioning for peak demand is the safe default, and elastic scaling absorbs the slack",
                field_reality="The Foundation's own framing: a cluster running at 40% utilisation is wasting more than half its spend. Utilisation is the metric most teams never collect, which is why a per-session cost ceiling and tool-call budget matter more than the invoice.",
                primary_source_name="FinOps Foundation — FinOps for AI: Tools & Services Considerations",
                primary_source_url="https://www.finops.org/wg/finops-for-ai-tools-services-considerations",
                publication_date="undated working-group paper; retrieved 2026-10-01",
                sample_size="working-group guidance paper, states no sample",
            ).to_dict(),
            BenchmarkDataPoint(
                category="Unit Economics",
                metric_name="Share of teams managing AI spend",
                headline_figure="98%",
                vendor_claim="AI cost control is now standard practice, so the cost problem is largely solved",
                field_reality="Tracking a bill is not bounding a loop. The same report shows the practice was rare two years ago, so this measures adoption of the discipline rather than maturity in it — our field notes are full of teams that can quote monthly spend but cannot cap one runaway session.",
                primary_source_name="State of FinOps 2026 Report (FinOps Foundation)",
                primary_source_url="https://data.finops.org",
                publication_date="2026 report (6th annual survey since 2020)",
                sample_size="1,192 respondents representing $83bn+ in annual cloud spend",
            ).to_dict(),
            BenchmarkDataPoint(
                category="Enterprise Adoption",
                metric_name="Organisations reporting AI use",
                headline_figure="78%",
                vendor_claim="Enterprise AI adoption is near-universal, so the hard part is behind us",
                field_reality="Use is not deployment. Adoption sits at the top of the funnel; what the field struggles with is the run-it-forever tail — approvals, schema drift, and the human verification step nobody budgeted for when the pilot ended.",
                primary_source_name="The 2025 AI Index Report (Stanford HAI)",
                primary_source_url="https://hai.stanford.edu/ai-index/2025-ai-index-report",
                publication_date="2025 report, data year 2024 (page undated)",
                sample_size="organisations reported in the AI Index business-usage section",
            ).to_dict(),
        ]

    # NO FALLBACK — deliberately. An earlier revision returned a generic SaaS/cloud dossier here,
    # which injected figures about an unrelated topic into any vertical that lacked its own (a
    # "warehouse automation statistics" hub shipped Zylo licence-utilisation numbers as audited
    # warehouse benchmarks). That is the silent degraded substitute AGENTS.md rule 6 forbids, so a
    # vertical with no sourced data now yields nothing and says why.
    raise UnverifiedDossierError(
        f"no data points sourced for vertical '{vertical}': a citation hub needs a verified "
        f"primary source for every metric, so nothing is drafted. Add points here (or pass a "
        f"dossier) and let the pre-flight gate verify them."
    )


def _main() -> int:
    """Audit the claimed dossiers against their live primary sources.

    Run this after editing any point, and before generating a hub:
      python3 scripts/citation_hub_dossier.py --vertical agentic_ai
    """
    import argparse

    parser = argparse.ArgumentParser(description="Audit citation-hub data points against their primary sources")
    parser.add_argument("--vertical", default="agentic_ai")
    parser.add_argument("--query", default="agentic ai enterprise benchmarks")
    parser.add_argument("--min-points", type=int, default=6)
    parser.add_argument("--json", action="store_true", help="full machine-readable report")
    args = parser.parse_args()

    try:
        dossier = get_claimed_dossier(args.vertical, args.query)
    except UnverifiedDossierError as exc:
        print(f"no dossier for '{args.vertical}': {exc}")
        return 1

    report = audit_dossier(dossier, min_points=args.min_points)
    if args.json:
        print(json.dumps(report, indent=2))
        return 0 if report["ok"] else 1

    print(f"pre-flight gate over {len(dossier)} claimed point(s) — {report['counts']}")
    for point in report["points"]:
        print(f"\n  [{point['status']}] {point['metric_name']}")
        print(f"      figure  : {point.get('figure', '')}")
        print(f"      source  : {point.get('url', '')}")
        if point.get("http"):
            print(f"      http    : {point['http']}  publisher name on page: {point.get('source_name_on_page')}")
        if point.get("reason"):
            print(f"      reason  : {point['reason']}")
        if point.get("evidence"):
            print(f"      evidence: …{point['evidence'][:230]}…")
    verdict = "PASS — draftable" if report["ok"] else "FAIL — not draftable"
    print(f"\nverdict: {verdict} ({len(report['errors'])} problem(s))")
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(_main())
