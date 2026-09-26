#!/usr/bin/env python3
"""
scripts/synthesize_topics.py — mechanical multi-signal pairing helper.

What this is
    A deterministic pre-filter that proposes *candidate* pairs of acute signals from a
    30-day signals file (`context/recon_proposals/YYYY-MM-DD_<vertical>_signals.md`), for
    the "Candidate Synthesis Pairs" section of `skills/radar_30day.md` Stage 4.

What this is NOT
    A scorer, and not an author. It never emits the Judge's composite and never clears the
    >= 8 publish gate — that gate belongs to `skills/virality_judge.md` §2.5 and is scored
    by an LLM on Emergence / Dual Authority / Tension from evidence the verifier has
    checked. It never writes a headline, tension or claim: the Judge writes those.

Design rules (each exists because an earlier revision broke it)
    1. No invented scores. Output carries `emergence_heuristic` (0.0-1.0, advisory, with its
       terms printed). The literal `Composite` never appears in any output.
    2. No invented content. A candidate is built only from rows that already carry an
       `https://` source, a parseable date inside the signals window, and Intensity >= 60.
    3. No thesis authoring. Patterns supply axis tokens, a one-line description and the
       registry verticals they apply to. Nothing else.
    4. Precision over recall. Word-boundary matching (`port` must not fire on "ports"),
       >= 2 distinct strong tokens, at least one strong token per leg, different source
       domains, and vertical scoping (an ocean `carrier` is not an insurance `carrier`).
       Generic tokens (cost, price, local, platform, ...) never form a match on their own.
       A pair this layer cannot justify is a miss, not a maybe — the Judge looks for the
       pairs this layer does not see.
    5. Refuses to overwrite the Judge's artifacts and never writes into `context/drafts/`.

Usage
    python3 scripts/synthesize_topics.py --signals context/recon_proposals/2026-09-25_resilient_home_assets_signals.md
    python3 scripts/synthesize_topics.py --signals <file> --format json --show-rejected
    python3 scripts/synthesize_topics.py --demo
    python3 scripts/synthesize_topics.py --check-fixtures     # fixtures cite only real committed sources
    python3 scripts/synthesize_topics.py --check-briefs       # synthesis briefs/drafts conform (verify.sh §8)
"""

import argparse
import datetime
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MAX_LEG_AGE_DAYS = 30
MIN_INTENSITY = 60

# Tokens so common in this corpus that a match resting on them is noise, not signal.
# Kept visible (rather than deleted from the axes) so a reader can see what was discounted.
WEAK_TOKENS = {
    "cost", "costs", "price", "prices", "pricing", "local", "platform", "platforms",
    "internal", "discount", "discounts", "cheap", "cheaper", "tco", "saas", "enterprise",
    "market", "growth", "revenue", "spend", "budget", "rate", "rates",
}

# Collision archetypes. `axis_a` is the driver leg, `axis_b` the operational-shift leg.
# `verticals` is the registry-scoped allow-list: a pattern may not fire outside it, which is
# what stops an ocean `carrier` from matching the insurance pattern in a supply-chain run.
PATTERNS = [
    {
        "pattern_id": "economics_x_architecture",
        "description": "input-cost economics colliding with build-vs-buy / architecture choices",
        "axis_a": ["token", "inference", "finops", "rate card", "price war", "unit economics",
                   "api pricing", "compute cost curve"],
        "axis_b": ["in-house", "repatriation", "build-vs-buy", "developer platform",
                   "internal platform", "bespoke", "saas renewal", "self-hosted"],
        "verticals": ["agentic_ai", "agentic_resilience_failure", "ai_observability_qa",
                      "enterprise_ai_finops", "enterprise_build_vs_buy",
                      "enterprise_tech_leadership", "multi_agent_enterprise_fabric"],
    },
    {
        "pattern_id": "governance_x_runtime",
        "description": "regulatory/liability pressure colliding with agent runtime architecture",
        "axis_a": ["regulation", "compliance", "liability", "audit", "governance",
                   "eu ai act", "ciso", "enforcement", "disclosure rule"],
        "axis_b": ["runtime", "agent loop", "tool execution", "mcp", "memory",
                   "orchestration", "circuit breaker", "trace log", "permission scope"],
        "verticals": ["agentic_ai", "agentic_resilience_failure", "ai_observability_qa",
                      "enterprise_ai_governance", "multi_agent_enterprise_fabric",
                      "control_tower_exception_orchestration"],
    },
    {
        "pattern_id": "compute_bottleneck_x_distillation",
        "description": "physical compute/power limits colliding with model-shrinking techniques",
        "axis_a": ["gpu", "cluster", "power cap", "datacenter", "capex", "blackwell",
                   "memory bandwidth", "gigawatt", "grid", "rack density", "thermal"],
        "axis_b": ["distillation", "quantization", "slm", "pruning", "small model",
                   "edge inference", "on-prem", "skill pruning", "speculative decoding"],
        "verticals": ["gpu_hardware", "workstation_compute_economics",
                      "nhil_infrastructure_ops", "agentic_ai"],
    },
    {
        "pattern_id": "freight_chokepoint_x_nearshoring",
        "description": "freight-network disruption colliding with reshoring / domestic capacity",
        "axis_a": ["tariff", "port congestion", "strike", "panama", "suez", "demurrage",
                   "chokepoint", "container", "ocean carrier", "blank sailing", "freight"],
        "axis_b": ["nearshore", "mexico", "reshoring", "domestic manufacturing",
                   "dual-sourcing", "supplier tier", "plant", "rail merger"],
        "verticals": ["supply_chain", "supplier_risk_reshoring_decision",
                      "control_tower_exception_orchestration",
                      "warehouse_automation_robotics_capex", "meio_working_capital_tco"],
    },
    {
        "pattern_id": "working_capital_x_automation_capex",
        "description": "cost-of-capital pressure colliding with warehouse/robotics capex decisions",
        "axis_a": ["interest rate", "working capital", "holding cost", "cash flow", "meio",
                   "safety stock", "cost of capital", "inventory carrying"],
        "axis_b": ["robotics", "automation", "amr", "warehouse", "wms", "asrs", "raas",
                   "dock-to-dock"],
        "verticals": ["warehouse_automation_robotics_capex", "meio_working_capital_tco",
                      "demand_sensing_advanced_sop", "supplier_risk_reshoring_decision",
                      "supply_chain"],
    },
    {
        "pattern_id": "electrification_subsidies_x_utility_rates",
        "description": "electrification incentives colliding with retail utility rate structure",
        "axis_a": ["rebate", "hear", "subsidy", "tax credit", "doe", "25c",
                   "incentive program", "electrification program"],
        "axis_b": ["rate hike", "utility", "kwh", "electric bill", "grid", "time-of-use",
                   "peak demand", "tariff schedule"],
        "verticals": ["home_equity_tco", "home_infrastructure_lifecycle_tco",
                      "resilient_home_assets", "smart_home_telemetry",
                      "personal_microeconomics_tinkering_tax"],
    },
    {
        "pattern_id": "insurance_withdrawal_x_asset_resilience",
        "description": "insurer withdrawal colliding with property-level hardening economics",
        "axis_a": ["insurance", "non-renewal", "premium", "fair plan", "wildfire", "flood",
                   "underwriting", "insurer", "reinsurance"],
        "axis_b": ["hardening", "fortified", "roof", "mitigation discount",
                   "defensible space", "building code", "resilience upgrade"],
        "verticals": ["resilient_home_assets", "home_equity_tco",
                      "home_infrastructure_lifecycle_tco"],
    },
    {
        "pattern_id": "tax_enforcement_x_cross_border_mobility",
        "description": "cross-border tax enforcement colliding with remote/mobility arrangements",
        "axis_a": ["irs", "fbar", "fatca", "permanent establishment", "withholding",
                   "double tax", "tax residency", "safe harbour"],
        "axis_b": ["nomad", "relocation", "visa", "remote work", "expat", "residency",
                   "diaspora", "global mobility"],
        "verticals": ["expat_cross_border_relocation",
                      "career_velocity_equity_engineering",
                      "personal_microeconomics_tinkering_tax"],
    },
]

STOPWORDS = {
    "with", "from", "that", "this", "into", "their", "there", "which", "while", "after",
    "before", "above", "below", "about", "would", "could", "should", "these", "those",
    "under", "over", "more", "most", "than", "then", "when", "what", "have", "has", "had",
    "will", "been", "being", "and", "the", "for", "are", "was", "were", "not", "but", "its",
    "year", "years", "month", "months", "week", "weeks", "first", "market", "record",
}

# A URL only counts as a citation when a host follows immediately — "https://`" in prose is not one.
URL_RE = r"https://[A-Za-z0-9][^\s)>\]]*"


# --------------------------------------------------------------------------- inputs

def load_vertical_registry():
    """Return {vertical_id: registry entry} from context/verticals.json (empty dict if absent)."""
    path = REPO_ROOT / "context" / "verticals.json"
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"WARN: could not read {path}: {exc}", file=sys.stderr)
        return {}
    entries = data.get("verticals", [])
    if not isinstance(entries, list):
        print(f"WARN: unexpected shape in {path}: 'verticals' is not a list", file=sys.stderr)
        return {}
    return {v["id"]: v for v in entries if isinstance(v, dict) and "id" in v}


def parse_signals_markdown(content):
    """Extract table rows from a signals markdown file.

    Columns: # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity [| extra...]
    """
    signals, headers = [], None
    for raw in content.splitlines():
        line = raw.strip()
        if line.startswith("|") and "Source URL" in line:
            headers = [h.strip() for h in line.split("|")[1:-1]]
            continue
        if not line.startswith("|"):
            headers = None
            continue
        cols = [c.strip() for c in line.split("|")[1:-1]]
        if len(cols) < 5 or not cols[0].isdigit():
            continue
        signals.append({
            "id": cols[0],
            "title": cols[1],
            "url": cols[2],
            "date": cols[3],
            "claim": cols[4],
            "angle": cols[5] if len(cols) > 5 else "",
            "intensity": cols[6] if len(cols) > 6 else "",
            "columns": headers or [],
        })
    return signals


def parse_window(content, fallback_end=None):
    """Parse `**Window:** YYYY-MM-DD → YYYY-MM-DD`; fall back to 30 days ending at the file date."""
    m = re.search(r"\*\*Window:\*\*\s*(\d{4}-\d{2}-\d{2})\s*(?:→|->|to|—|-)\s*(\d{4}-\d{2}-\d{2})", content)
    if m:
        return m.group(1), m.group(2)
    m = re.search(r"^#\s*Signals:.*?(\d{4}-\d{2}-\d{2})\s*$", content, re.MULTILINE)
    end = m.group(1) if m else (fallback_end or datetime.date.today().isoformat())
    end_d = datetime.date.fromisoformat(end)
    return (end_d - datetime.timedelta(days=MAX_LEG_AGE_DAYS)).isoformat(), end


def parse_signal_date(cell):
    """Signal date from a Date cell.

    Prefers the *leading* date token (that is the event being reported — "2026-09 (CDI-approved;
    effective 2026-10-15)" is a September signal, not an October one), then falls back to the first
    full date anywhere in the cell, then to a bare YYYY-MM expanded to the 1st.
    """
    cell = cell or ""
    m = re.match(r"\s*(\d{4})-(\d{2})-(\d{2})", cell)
    if m:
        try:
            return datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        except ValueError:
            return None
    m = re.match(r"\s*(\d{4})-(\d{2})", cell)
    if m:
        try:
            return datetime.date(int(m.group(1)), int(m.group(2)), 1)
        except ValueError:
            return None
    m = re.search(r"(\d{4}-\d{2}-\d{2})", cell)
    if m:
        try:
            return datetime.date.fromisoformat(m.group(1))
        except ValueError:
            return None
    m = re.search(r"(\d{4})-(\d{2})", cell)
    if m:
        try:
            return datetime.date(int(m.group(1)), int(m.group(2)), 1)
        except ValueError:
            return None
    return None


def parse_intensity(cell):
    m = re.search(r"(\d{1,3})", cell or "")
    return int(m.group(1)) if m else None


def domain_of(url):
    m = re.search(r"https?://([^/\s]+)", url or "")
    if not m:
        return ""
    host = m.group(1).lower().lstrip("www.")
    return ".".join(host.split(".")[-2:]) if host.count(".") >= 1 else host


def is_https(url):
    return bool(re.match(r"https://[^\s|]+", url or ""))


# --------------------------------------------------------------------------- matching

def _token_pattern(token):
    return re.compile(r"(?<![a-z0-9])" + re.escape(token.lower()) + r"(?![a-z0-9])")


def find_tokens(text, tokens):
    """Word-boundary token hits. 'port congestion' never fires on 'ports'."""
    low = (text or "").lower()
    return sorted({t for t in tokens if _token_pattern(t).search(low)})


def leg_text(sig):
    return f"{sig['title']} {sig['claim']} {sig['angle']}"


def match_pattern(leg_a, leg_b, vertical=None):
    """Best (pattern, hits_a, hits_b) for an ordered leg pair, or None.

    Requires at least one strong token on each leg and >= 2 distinct strong tokens overall.
    """
    text_a, text_b = leg_text(leg_a), leg_text(leg_b)
    best = None
    for pattern in PATTERNS:
        allowed = pattern.get("verticals") or []
        if vertical and allowed and vertical not in allowed:
            continue
        axis_a = [t for t in pattern["axis_a"] if t not in WEAK_TOKENS]
        axis_b = [t for t in pattern["axis_b"] if t not in WEAK_TOKENS]
        hits_a = find_tokens(text_a, axis_a)
        hits_b = find_tokens(text_b, axis_b)
        if not hits_a or not hits_b:
            continue
        if len(set(hits_a) | set(hits_b)) < 2:
            continue
        if best is None or len(set(hits_a) | set(hits_b)) > len(set(best[1]) | set(best[2])):
            best = (pattern, hits_a, hits_b)
    return best


def weak_hits(leg_a, leg_b, pattern=None):
    """Weak tokens present in either leg — reported for context, never used to match."""
    text = f"{leg_text(leg_a)} {leg_text(leg_b)}".lower()
    found = {t for t in WEAK_TOKENS if _token_pattern(t).search(text)}
    return sorted(found)


def validate_legs(leg_a, leg_b, window_start, window_end):
    """Return a list of hard-rejection reasons ([] = both legs are usable anchors)."""
    reasons = []
    for label, sig in (("A", leg_a), ("B", leg_b)):
        if not is_https(sig["url"]):
            reasons.append(f"leg{label}:no_https_source")
        date = parse_signal_date(sig["date"])
        if date is None:
            reasons.append(f"leg{label}:no_parseable_date")
        elif not (datetime.date.fromisoformat(window_start) <= date <= datetime.date.fromisoformat(window_end)):
            reasons.append(f"leg{label}:out_of_window({date.isoformat()})")
        intensity = parse_intensity(sig["intensity"])
        if intensity is None:
            reasons.append(f"leg{label}:no_intensity")
        elif intensity < MIN_INTENSITY:
            reasons.append(f"leg{label}:intensity<{MIN_INTENSITY}({intensity})")
    if leg_a["url"] and leg_a["url"] == leg_b["url"]:
        reasons.append("same_source_url")
    elif domain_of(leg_a["url"]) and domain_of(leg_a["url"]) == domain_of(leg_b["url"]):
        reasons.append("same_source_domain")
    return reasons


# --------------------------------------------------------------------------- scoring (advisory)

def _content_tokens(text):
    return {w for w in re.findall(r"[a-z][a-z0-9-]{4,}", (text or "").lower())
            if w not in STOPWORDS}


def _jaccard(a, b):
    if not a and not b:
        return 0.5
    if not a or not b:
        return 0.5
    return len(a & b) / len(a | b)


def emergence_heuristic(leg_a, leg_b, hits_a, hits_b, vertical, registry):
    """Advisory 0.0-1.0 hint with its terms. Deliberately NOT the publish gate."""
    vert = registry.get(vertical, {})
    vert_terms = _content_tokens(" ".join(vert.get("primary_angles", [])) + " " + str(vert.get("label", "")))
    pair_terms = _content_tokens(" ".join(hits_a + hits_b)) | _content_tokens(
        leg_a["angle"] + " " + leg_b["angle"])
    fit_denom = min(4, len(vert_terms)) or 1
    terms = {
        "token_coverage": round(min(1.0, len(set(hits_a) | set(hits_b)) / 4.0), 2),
        "intensity": round(((parse_intensity(leg_a["intensity"]) or 0)
                            + (parse_intensity(leg_b["intensity"]) or 0)) / 200.0, 2),
        "angle_fit": round(min(1.0, len(pair_terms & vert_terms) / fit_denom), 2),
        "contrast": round(1.0 - _jaccard(_content_tokens(leg_a["angle"]), _content_tokens(leg_b["angle"])), 2),
    }
    score = (0.35 * terms["token_coverage"] + 0.25 * terms["intensity"]
             + 0.20 * terms["angle_fit"] + 0.20 * terms["contrast"])
    return round(min(1.0, score), 2), terms


def retread_flags(leg_a, leg_b):
    """Advisory prior-cycle overlap against published articles and the calendar."""
    flags, corpus = [], ""
    sources = [REPO_ROOT / "context" / "published_log.md", REPO_ROOT / "context" / "content_calendar.md"]
    published_dir = REPO_ROOT / "published"
    if published_dir.exists():
        sources.extend(sorted(published_dir.glob("*.md")))
    for path in sources:
        if path.exists():
            corpus += path.read_text(encoding="utf-8", errors="replace")
    for label, sig in (("A", leg_a), ("B", leg_b)):
        if sig["url"] and sig["url"] in corpus:
            flags.append(f"leg{label}:url_already_cited")
    overlap = sorted(_content_tokens(leg_a["title"]) & _content_tokens(leg_b["title"]) & _content_tokens(corpus))
    if overlap:
        flags.append("prior_cycle_token_overlap:" + "|".join(overlap[:4]))
    return flags


# --------------------------------------------------------------------------- pairing

def find_pairs(signals, vertical, window_start, window_end, registry):
    """Return (pairs, rejected). Rejected carries the reason for pairs that had token signal."""
    pairs, rejected = [], []
    for i in range(len(signals)):
        for j in range(i + 1, len(signals)):
            leg_a, leg_b = signals[i], signals[j]
            match = match_pattern(leg_a, leg_b, vertical)
            if match:
                pattern, hits_a, hits_b = match
            else:
                reversed_match = match_pattern(leg_b, leg_a, vertical)
                if not reversed_match:
                    continue
                pattern, hits_b, hits_a = reversed_match   # axis order, not row order
            reasons = validate_legs(leg_a, leg_b, window_start, window_end)
            if reasons:
                rejected.append({
                    "signals": [leg_a["id"], leg_b["id"]],
                    "pattern_id": pattern["pattern_id"],
                    "reason": ";".join(reasons),
                })
                continue
            score, terms = emergence_heuristic(leg_a, leg_b, hits_a, hits_b, vertical, registry)
            pairs.append({
                "vertical": vertical,
                "pattern_id": pattern["pattern_id"],
                "description": pattern["description"],
                "signals": [leg_a["id"], leg_b["id"]],
                "shared_axis": f"{pattern['description']} (tokens: {', '.join(hits_a)} ⨂ {', '.join(hits_b)})",
                "contrasting_axis": f"A: {leg_a['angle'] or '-'} | B: {leg_b['angle'] or '-'}",
                "anchor_urls": [leg_a["url"], leg_b["url"]],
                "anchor_titles": [leg_a["title"], leg_b["title"]],
                "anchor_dates": [leg_a["date"], leg_b["date"]],
                "intensities": [parse_intensity(leg_a["intensity"]), parse_intensity(leg_b["intensity"])],
                "emergence_heuristic": score,
                "heuristic_terms": terms,
                "weak_tokens_present": weak_hits(leg_a, leg_b, pattern),
                "flags": retread_flags(leg_a, leg_b),
            })
    pairs.sort(key=lambda p: (-p["emergence_heuristic"], p["signals"][0]))
    return pairs, rejected


# --------------------------------------------------------------------------- rendering

ADVISORY = ("> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) "
            "owns the collision vector\n> and the >= 8 publish gate. `emergence_heuristic` is a hint, "
            "not a score; it cannot clear any gate.")


def render_table(vertical, window_start, window_end, signals, pairs, registry):
    vert = registry.get(vertical, {})
    out = [f"# Candidate Synthesis Pairs — {vertical} — {datetime.date.today().isoformat()}",
           "", ADVISORY,
           f"> Window: {window_start} → {window_end} | persona: {vert.get('target_persona', 'UNKNOWN')} "
           f"| signals rows: {len(signals)} | validated pairs: {len(pairs)}", ""]
    if not pairs:
        out.append("_No mechanically valid pair. That is a legitimate answer, not a failure: the "
                   "Judge may still find a synthesis this token layer cannot see._")
        return "\n".join(out)
    out += ["| Pair | Signals | Shared axis | Contrasting axis | Anchor URLs | Heuristic | Flags |",
            "|---|---|---|---|---|---|---|"]
    for idx, p in enumerate(pairs, 1):
        urls = " ".join(p["anchor_urls"])
        flags = "; ".join(p["flags"]) or "-"
        out.append(f"| {idx} | #{p['signals'][0]} ⨂ #{p['signals'][1]} | {p['pattern_id']} | "
                   f"{p['contrasting_axis']} | {urls} | {p['emergence_heuristic']} | {flags} |")
    out += ["", "**Heuristic terms (advisory):**"]
    for idx, p in enumerate(pairs, 1):
        t = p["heuristic_terms"]
        out.append(f"- #{idx}: token_coverage={t['token_coverage']} intensity={t['intensity']} "
                   f"angle_fit={t['angle_fit']} contrast={t['contrast']} → "
                   f"{p['emergence_heuristic']} ({p['pattern_id']})")
    return "\n".join(out)


# --------------------------------------------------------------------------- checks

def _recon_dir():
    return REPO_ROOT / "context" / "recon_proposals"


def check_briefs():
    """verify.sh §8 — synthesis artifacts must carry two real anchors, and no invented sources."""
    problems = []
    recon = _recon_dir()
    signals_by_prefix = {p.name[: -len("_signals.md")]: p for p in recon.glob("*_signals.md")}
    committed_sources = "\n".join(p.read_text(encoding="utf-8", errors="replace")
                                  for p in signals_by_prefix.values())

    for path in sorted(recon.glob("*_angle_brief.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        prefix = path.name[: -len("_angle_brief.md")]
        signals_text = signals_by_prefix[prefix].read_text(encoding="utf-8", errors="replace") \
            if prefix in signals_by_prefix else ""
        urls = sorted(set(re.findall(URL_RE, text)))
        for url in urls:
            if signals_text and url.rstrip("/") not in signals_text.replace(")", ""):
                problems.append(f"{path.name}: url not present in its signals file: {url}")
        if re.search(r"Angle Type:\*\*\s*Synthesis", text):
            if len(urls) < 2:
                problems.append(f"{path.name}: synthesis brief needs 2 distinct https anchors, found {len(urls)}")
            if not signals_text:
                problems.append(f"{path.name}: synthesis brief has no matching _signals.md")
            verified = recon / f"{prefix}_verified_brief.md"
            if not verified.exists():
                problems.append(f"{path.name}: synthesis brief has no {verified.name}")
            else:
                vtext = verified.read_text(encoding="utf-8", errors="replace")
                for url in urls:
                    if url.rstrip("/") not in vtext.replace(")", ""):
                        problems.append(f"{path.name}: anchor {url} absent from {verified.name}")

    for draft in sorted((REPO_ROOT / "context" / "drafts").glob("*.md")):
        text = draft.read_text(encoding="utf-8", errors="replace")
        if not re.search(r"^synthesis:\s*true", text, re.MULTILINE):
            continue
        urls = sorted(set(re.findall(URL_RE, text)))
        if len(urls) < 2:
            problems.append(f"drafts/{draft.name}: synthesis: true needs >= 2 https anchors in sources:")
        for url in urls:
            if url.rstrip("/") not in committed_sources.replace(")", ""):
                problems.append(f"drafts/{draft.name}: anchor not traceable to any committed signals file: {url}")
    return problems


def check_fixtures():
    """Every URL in scripts/fixtures/*.md must cite a row that exists in a committed signals file."""
    problems = []
    committed = "\n".join(p.read_text(encoding="utf-8", errors="replace") for p in _recon_dir().glob("*_signals.md"))
    for path in sorted((REPO_ROOT / "scripts" / "fixtures").glob("*.md")):
        for url in sorted(set(re.findall(URL_RE, path.read_text(encoding="utf-8")))):
            if url.rstrip("/,") not in committed:
                problems.append(f"{path.name}: fixture URL not present in any committed signals file: {url}")
    return problems


# --------------------------------------------------------------------------- cli

def _resolve_vertical(path, explicit, content):
    if explicit:
        return explicit
    m = re.match(r"(\d{4}-\d{2}-\d{2})_(.+?)_signals\.md$", Path(path).name)
    if m:
        return m.group(2)
    m = re.search(r"\*\*Vertical:\*\*\s*(.+)", content)
    if m:
        return m.group(1).strip()
    return ""


def run_signals(args):
    path = Path(args.signals)
    if not path.exists():
        print(f"Error: file not found: {args.signals}", file=sys.stderr)
        return 2
    content = path.read_text(encoding="utf-8")
    signals = parse_signals_markdown(content)
    if not signals:
        print(f"Error: no structured signals rows found in {args.signals}", file=sys.stderr)
        return 2
    vertical = _resolve_vertical(path, args.vertical, content)
    registry = load_vertical_registry()
    if vertical and vertical not in registry:
        print(f"WARN: vertical '{vertical}' is not in context/verticals.json — pattern scoping "
              f"and angle_fit are degraded", file=sys.stderr)
    window_start, window_end = (args.window_start, args.window_end) if args.window_start and args.window_end \
        else parse_window(content)
    if args.window_start:
        window_start = args.window_start
    if args.window_end:
        window_end = args.window_end

    pairs, rejected = find_pairs(signals, vertical, window_start, window_end, registry)

    if args.format == "json":
        payload = {
            "vertical": vertical,
            "persona": registry.get(vertical, {}).get("target_persona"),
            "window": [window_start, window_end],
            "rows": len(signals),
            "pairs": pairs,
            "rejected": rejected if args.show_rejected else [],
            "note": "emergence_heuristic is advisory and cannot clear the >=8 publish gate; "
                    "the Judge owns the collision vector, the headline and the score.",
        }
        text = json.dumps(payload, indent=2)
    else:
        text = render_table(vertical, window_start, window_end, signals, pairs, registry)
        if args.show_rejected:
            text += "\n\n**Pairs rejected by validation (advisory):**\n" + (
                "\n".join(f"- #{r['signals'][0]} ⨂ #{r['signals'][1]} ({r['pattern_id']}): {r['reason']}"
                          for r in rejected) or "- none")

    if "Composite" in text:
        print("Error: internal guard tripped — output must never carry a gate score", file=sys.stderr)
        return 2

    if args.out:
        target = Path(args.out)
        guard = validate_out_path(target, force=args.force)
        if guard:
            print(f"Error: {guard}", file=sys.stderr)
            return 2
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        print(f"Written to {target}")
        return 0
    print(text)
    return 0


def validate_out_path(target, force=False):
    """Refuse to clobber the Judge's artifacts or write drafts."""
    name = target.name
    if name.endswith(("_angle_brief.md", "_verified_brief.md")):
        return (f"refusing to write {name}: that is the Judge's/verifier's artifact. Write the "
                f"helper output beside it (e.g. <date>_<vertical>_pairs.md).")
    try:
        target.resolve().relative_to((REPO_ROOT / "context" / "drafts").resolve())
        return "refusing to write into context/drafts/ — drafts come from the drafter, not this helper."
    except ValueError:
        pass
    if target.exists() and not force:
        return f"{target} already exists — pass --force to overwrite."
    return None


def run_demo():
    fixture = REPO_ROOT / "scripts" / "fixtures" / "synthesis_positive_home_signals.md"
    if not fixture.exists():
        print(f"Error: fixture missing: {fixture}", file=sys.stderr)
        return 2
    print(f"=== DEMO: pairing helper over a pinned, source-verified fixture ({fixture.name}) ===\n")
    args = argparse.Namespace(signals=str(fixture), vertical="resilient_home_assets",
                              window_start=None, window_end=None, format="table",
                              show_rejected=False, out=None, force=False)
    return run_signals(args)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Multi-signal pairing helper (advisory pre-filter)")
    parser.add_argument("--signals", help="Path to a 30-day signals markdown file")
    parser.add_argument("--vertical", help="Vertical id (default: inferred from the filename)")
    parser.add_argument("--window-start", help="Override the window start (YYYY-MM-DD)")
    parser.add_argument("--window-end", help="Override the window end (YYYY-MM-DD)")
    parser.add_argument("--format", choices=("table", "json"), default="table")
    parser.add_argument("--show-rejected", action="store_true", help="List pairs rejected by validation")
    parser.add_argument("--out", help="Write output to this path (guarded)")
    parser.add_argument("--force", action="store_true", help="Allow overwriting an existing file")
    parser.add_argument("--demo", action="store_true", help="Run over the pinned fixture")
    parser.add_argument("--check-fixtures", action="store_true",
                        help="Fail if any fixture cites a source absent from the committed signals files")
    parser.add_argument("--check-briefs", action="store_true",
                        help="Fail if synthesis briefs/drafts are under-anchored or cite invented sources")
    args = parser.parse_args(argv)

    if args.demo:
        return run_demo()
    if args.check_fixtures:
        problems = check_fixtures()
    elif args.check_briefs:
        problems = check_briefs()
    elif args.signals:
        return run_signals(args)
    else:
        parser.print_help()
        return 2

    for problem in problems:
        print(f"FAIL: {problem}")
    if problems:
        print(f"--check: {len(problems)} problem(s)")
        return 1
    print("--check: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
