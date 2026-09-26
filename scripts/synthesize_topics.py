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
    python3 scripts/synthesize_topics.py --seed <signals file>   # pipeline step: seeds the pair block
    python3 scripts/synthesize_topics.py --signals <file> --format json --show-rejected
    python3 scripts/synthesize_topics.py --demo
    python3 scripts/synthesize_topics.py --check-seed         # every new signals file is seeded, and fresh
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

# The synthesis flag contract (verify.sh §8): a brief that declares `Angle Type: Synthesis` must be
# carried through to the draft/published artifact it produced as `synthesis: true`, matched on the
# artifact's date prefix + `vertical:` field, or the build fails. Same-day verticals therefore
# cannot borrow each other's flag.
ANGLE_BRIEF_SUFFIX = "_angle_brief.md"
DATED_ARTIFACT_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})_")
SYNTHESIS_FLAG_RE = re.compile(r"^synthesis:\s*true\s*$", re.MULTILINE)
VERTICAL_FIELD_RE = re.compile(r"^vertical:\s*(\S+)\s*$", re.MULTILINE)
FRONTMATTER_RE = re.compile(r"\A---\s*\r?\n(.*?)\r?\n---\s*(?:\r?\n|\Z)", re.DOTALL)
INLINE_SOURCES_RE = re.compile(r"^sources:\s*\[(.*)\]\s*$", re.MULTILINE)
SOURCES_ITEM_RE = re.compile(r"^\s+-\s*(https://\S+)\s*$", re.MULTILINE)


def frontmatter_sources(text):
    """URLs declared under the frontmatter `sources:` key — block-list or inline-array form.

    Both shapes are in the wild (`sources:\\n  - <url>` from the drafting step, `sources: [<url>, …]`
    as documented in skills/story_draft.md §3), and this is the list the reader-facing surfaces
    publish as the article's checkable anchors.
    """
    front = FRONTMATTER_RE.match(text or "")
    if not front:
        return []
    body = front.group(1)
    raw = []
    inline = INLINE_SOURCES_RE.search(body)
    if inline:
        raw += [u.strip().strip("\"'") for u in inline.group(1).split(",")]
    block = re.search(r"^sources:\s*$(.*?)(?=^\S|\Z)", body, re.MULTILINE | re.DOTALL)
    if block:
        raw += [m.group(1) for m in SOURCES_ITEM_RE.finditer(block.group(1))]
    urls, seen = [], set()
    for url in raw:
        url = url.rstrip(",.;")
        if not url.startswith("https://") or url in seen:
            continue
        seen.add(url)
        urls.append(url)
    return urls


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

    Rows are only collected while a table declaring a `Source URL` column is open, so a sibling table
    (e.g. the seeded `## Candidate Synthesis Pairs` block, or the radar's own pair table) can never be
    mistaken for signal rows.
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
        if headers is None:
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
    """Return (pairs, rejected). Rejected carries the reason for pairs that had token signal.

    Fail-closed on the vertical: archetypes are scoped to registry verticals, so an unresolvable or
    unregistered vertical yields no candidates rather than unscoped (cross-domain) ones.
    """
    pairs, rejected = [], []
    if vertical not in registry:
        print(f"WARN: vertical {vertical!r} is not in context/verticals.json — no archetype can be "
              f"scoped, so no candidates are emitted (fail-closed)", file=sys.stderr)
        return pairs, rejected
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
    out.append(render_table_body(pairs))
    return "\n".join(out)


def render_table_body(pairs):
    """The table + its advisory terms. Used by the stdout view and the in-file seed block."""
    if not pairs:
        return ("_No mechanically valid pair. That is a legitimate answer, not a failure: the "
                "Judge may still find a synthesis this token layer cannot see._")
    out = ["| Pair | Signals | Shared axis | Contrasting axis | Anchor URLs | Heuristic | Flags |",
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


# --------------------------------------------------------------------------- autonomous seeding

SEED_HEADING = "## Candidate Synthesis Pairs"
SEED_START = "<!-- synthesis-seed:start -->"
SEED_END = "<!-- synthesis-seed:end -->"
SEED_ENFORCED_FROM = "2026-09-26"  # signals files dated on/after this must carry a seed block
SEED_MARKER_RE = re.compile(
    r"<!--\s*pair-seeding:\s*helper=(?P<helper>\S+)\s+rows=(?P<rows>\d+)\s+"
    r"candidates=(?P<candidates>\d+)\s+heuristic=(?P<heuristic>\S+)\s+"
    r"window=(?P<window_start>\d{4}-\d{2}-\d{2})\.\.(?P<window_end>\d{4}-\d{2}-\d{2})\s*-->"
)


def seed_block(pairs, rows, window_start, window_end):
    """Deterministic seed block: marks that the step ran and what it found. No scores, no theses."""
    heuristic = "-" if not pairs else f"{pairs[-1]['emergence_heuristic']:.2f}-{pairs[0]['emergence_heuristic']:.2f}"
    marker = (f"<!-- pair-seeding: helper=synthesize_topics.py rows={rows} "
              f"candidates={len(pairs)} heuristic={heuristic} "
              f"window={window_start}..{window_end} -->")
    block = [SEED_START, marker, ADVISORY,
             ("> Seeded mechanically from this file's own rows by "
              "`python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or "
              "removing a signal row. The Judge scores the rows and writes the collision vector per "
              "`skills/virality_judge.md` §2.5."), "",
             render_table_body(pairs), SEED_END]
    return "\n".join(block)


def apply_seed(text, block):
    """Insert or replace the seeded block, idempotently. Returns (new_text, action)."""
    if SEED_START in text and SEED_END in text:
        head, rest = text.split(SEED_START, 1)
        _old, tail = rest.split(SEED_END, 1)
        return f"{head}{block}{tail}", "replaced"
    heading_re = re.compile(r"^" + re.escape(SEED_HEADING) + r"\s*$", re.MULTILINE)
    m = heading_re.search(text)
    if m:
        nxt = re.compile(r"^##\s", re.MULTILINE).search(text, m.end())
        end = nxt.start() if nxt else len(text)
        return f"{text[:m.end()]}\n\n{block}\n\n{text[end:].lstrip(chr(10))}", "seeded"
    sep = "" if text.endswith("\n") else "\n"
    return f"{text}{sep}\n{SEED_HEADING}\n\n{block}\n", "appended"


def seed_signals_file(path, vertical=None):
    """Seed (or re-seed) the candidate-pair block inside a signals file. Idempotent."""
    path = Path(path)
    if not path.exists():
        return {"ok": False, "error": f"file not found: {path}"}
    content = path.read_text(encoding="utf-8")
    signals = parse_signals_markdown(content)
    if not signals:
        return {"ok": False, "error": f"no structured signals rows in {path}"}
    vertical = vertical or _resolve_vertical(path, None, content)
    registry = load_vertical_registry()
    window_start, window_end = parse_window(content)
    pairs, _rejected = find_pairs(signals, vertical, window_start, window_end, registry)
    block = seed_block(pairs, len(signals), window_start, window_end)
    if "Composite" in block:
        return {"ok": False, "error": "internal guard tripped — the seed block must never carry a gate score"}
    new_text, action = apply_seed(content, block)
    path.write_text(new_text, encoding="utf-8")
    return {"ok": True, "action": action, "rows": len(signals), "candidates": len(pairs),
            "window": [window_start, window_end], "vertical": vertical}


def _signals_file_date(path):
    m = re.match(r"(\d{4}-\d{2}-\d{2})_", Path(path).name)
    return m.group(1) if m else None


def check_seed(enforce_from=SEED_ENFORCED_FROM, directory=None):
    """verify.sh §8 — signals files written since the step became autonomous must carry its proof.

    The check is on the marker's `rows=` count against the file's own table, so a signals file whose
    rows changed after seeding cannot pass as seeded; the Judge's edits to the pair table are ignored.
    """
    problems = []
    for path in sorted((Path(directory) if directory else _recon_dir()).glob("*_signals.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        rows = len(parse_signals_markdown(text))
        date = _signals_file_date(path)
        enforced = bool(date and date >= enforce_from)
        marker = SEED_MARKER_RE.search(text)
        if not marker:
            if enforced:
                problems.append(f"{path.name}: no pair-seeding marker — run "
                                f"`python3 scripts/synthesize_topics.py --seed {path.name}`")
            continue
        if marker.group("helper") != "synthesize_topics.py":
            problems.append(f"{path.name}: seed marker names an unknown helper "
                            f"{marker.group('helper')!r}")
        if int(marker.group("rows")) != rows:
            problems.append(f"{path.name}: seed is stale — marker says rows={marker.group('rows')}, "
                            f"file has {rows} signal rows; re-run the --seed step")
        if SEED_START not in text or SEED_END not in text:
            problems.append(f"{path.name}: seed marker present without the seeded block delimiters")
        if "Composite" in text.split(SEED_START)[-1].split(SEED_END)[0]:
            problems.append(f"{path.name}: the seeded block carries a gate score")
    return problems



# --------------------------------------------------------------------------- checks

def _recon_dir():
    return REPO_ROOT / "context" / "recon_proposals"


def _drafts_dir():
    return REPO_ROOT / "context" / "drafts"


def _published_dir():
    return REPO_ROOT / "published"


def brief_vertical(name):
    """`2026-09-26_supply_chain_angle_brief.md` -> `('2026-09-26', 'supply_chain')`.

    None when the name is not a dated angle brief. The vertical is read from the filename because
    that is the only place the brief names it without parsing prose.
    """
    if not name.endswith(ANGLE_BRIEF_SUFFIX):
        return None
    match = DATED_ARTIFACT_RE.match(name)
    if not match:
        return None
    return match.group(1), name[match.end():-len(ANGLE_BRIEF_SUFFIX)]


def declared_syntheses(directories):
    """`{(date, vertical)}` for every draft/published article declaring `synthesis: true`.

    The flag is the only machine-readable statement that an article's thesis is the *fusion* of two
    independent signals rather than a single-signal story with corroborating sources; §8 uses this
    set to prove a Synthesis brief actually reached the artifact it was written for. Published
    copies count as well, so a run whose drafts were cleaned up after publishing still passes.
    """
    declared = set()
    for directory in directories:
        for path in sorted(Path(directory).glob("*.md")):
            text = path.read_text(encoding="utf-8", errors="replace")
            if not SYNTHESIS_FLAG_RE.search(text):
                continue
            match = DATED_ARTIFACT_RE.match(path.name)
            if not match:
                continue
            vertical = VERTICAL_FIELD_RE.search(text)
            declared.add((match.group(1), vertical.group(1).strip("\"'") if vertical else ""))
    return declared


def check_briefs(recon_dir=None, drafts_dir=None, published_dir=None):
    """verify.sh §8 — synthesis artifacts must carry two real anchors, and no invented sources.

    A brief that declares `Angle Type: Synthesis` must also be *carried through*: the matching
    draft or published article has to declare `synthesis: true` (matched on date + vertical), so a
    fusion thesis can never ship indistinguishable from a single-signal story.
    """
    problems = []
    recon = Path(recon_dir) if recon_dir else _recon_dir()
    drafts_dir = Path(drafts_dir) if drafts_dir else _drafts_dir()
    declared = declared_syntheses([drafts_dir, Path(published_dir) if published_dir else _published_dir()])
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
            # Carry-through: the fusion must be visible on the artifact, not only in the brief.
            key = brief_vertical(path.name)
            if key and key not in declared:
                problems.append(
                    f"{path.name}: synthesis brief has no artifact declaring `synthesis: true` for "
                    f"{key[0]}/{key[1]} — add `synthesis: true` plus the two anchors to "
                    f"`sources:` in the frontmatter of the matching "
                    f"context/drafts/{key[0]}_<slug>_final.md (or the published copy), so a fused "
                    f"thesis is not readable as a single-signal story"
                )

    for draft in sorted(drafts_dir.glob("*.md")):
        text = draft.read_text(encoding="utf-8", errors="replace")
        if not SYNTHESIS_FLAG_RE.search(text):
            continue
        anchors = frontmatter_sources(text)
        if len(anchors) < 2:
            problems.append(f"drafts/{draft.name}: synthesis: true needs >= 2 https anchors in the "
                            f"frontmatter `sources:` list, found {len(anchors)}")
        for url in sorted(set(re.findall(URL_RE, text))):
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
    parser.add_argument("--seed", metavar="SIGNALS_FILE",
                        help="Seed/re-seed the Candidate Synthesis Pairs block inside a signals file "
                             "(the pipeline step; idempotent)")
    parser.add_argument("--check-seed", action="store_true",
                        help="Fail if a signals file written since the step became autonomous has no "
                             "seed block, or its block is stale")
    parser.add_argument("--enforce-from", help=f"Date from which --check-seed enforces "
                                               f"(default {SEED_ENFORCED_FROM})")
    parser.add_argument("--check-fixtures", action="store_true",
                        help="Fail if any fixture cites a source absent from the committed signals files")
    parser.add_argument("--check-briefs", action="store_true",
                        help="Fail if synthesis briefs/drafts are under-anchored, cite invented sources, "
                             "or a Synthesis brief was not carried through as `synthesis: true`")
    args = parser.parse_args(argv)

    if args.demo:
        return run_demo()
    if args.seed:
        result = seed_signals_file(args.seed, args.vertical)
        if not result["ok"]:
            print(f"Error: {result['error']}", file=sys.stderr)
            return 2
        print(f"seeded {Path(args.seed).name}: {result['action']} | rows={result['rows']} "
              f"candidates={result['candidates']} | window={result['window'][0]}..{result['window'][1]} "
              f"(advisory — the Judge scores it)")
        return 0
    if args.check_seed:
        problems = check_seed(args.enforce_from or SEED_ENFORCED_FROM)
    elif args.check_fixtures:
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
