# SKILL: 30-Day Radar Sweep (Loop 1 — Scout)

## 1. Objective
Execute an autonomous, signal-driven intelligence sweep of one vertical, strictly constrained to
the **last 30 calendar days**, and output sourced raw signals for the Virality Judge.

## 2. Ingestion
- **Trigger:** cron (per-vertical schedule in `context/content_calendar.md`) or manual via the
  Editor-in-Chief: `Run the 30-day radar for vertical '<id>'`.
- **Inputs:** vertical definition in `context/verticals.json` (sources + primary angles).

## 3. Execution protocol

### Stage 1 — Anchor the window
- `CURRENT_DATE` = today; `SCAN_WINDOW_START` = today − 30 days.
- Every query carries a date filter (`after:`, `since:`, `past month`, `last 30 days`).
- Timestamp-check each result; drop anything older than the window.

### Stage 2 — Fan-out queries per source
Run parallel queries across the vertical's configured sources. Generic templates:
```
"<primary_angle>" after:<scan_window_start>
"<keyword>" site:news.ycombinator.com
"<keyword>" site:arxiv.org
"<keyword>" trending (GitHub)
"<keyword>" "last 30 days" OR "this month"
```
Vertical-specific sources/angles come from `context/verticals.json` — never invent a source.

> **Backend note (learned 2026-09-07):** the search backend may silently ignore `after:` / `since:`
> date filters, returning an empty result set even on a healthy source (observed: a nearshoring
> `after:<window_start>` query → 0 results; date-agnostic phrasing on the same angle → results).
> Do not treat an empty set as "no signal" — always run the date-agnostic fallback phrasing
> (`site:<source>` / `"<angle>" "last 30 days"` / `"<angle>" "this month"`) for each angle, then
> timestamp-check every hit against `SCAN_WINDOW_START` before dropping it. Never trust the operator
> alone to guarantee the window.

> **Intelligence MCP integration (`supply_chain_intel`):** For supply chain, logistics, and IT
> infrastructure verticals, query the Coolify-hosted Supply Chain Intelligence server directly via
> `scripts/supply_chain_intel_client.py --recent 30 --vertical <id> --format signals` or via MCP tools
> (`search_intelligence`, `get_latest_insights`, `get_podcast_takeaways`, `get_vendor_evaluations`).
> Primary sources, URLs, and exact figures in `key_metrics` are pre-anchored to the 30-day window.

> **Intelligence MCP integration (`home_lifestyle_intel`):** For home capital allocation, smart home,
> residential energy, and DIY/tinkering verticals, query the Coolify-hosted Home & Lifestyle Intelligence
> server directly via `scripts/home_lifestyle_intel_client.py --recent 30 --vertical <id> --format signals`
> or via MCP tools (`search_home_intelligence`, `get_latest_home_insights`, `get_market_and_mortgage_trends`,
> `get_product_recommendations`, `get_diy_and_renovation_ideas`).



### Stage 3 — Capture, score & cross-signal synthesis clustering
1. For each raw signal capture: URL, date, the concrete claim/figure, and the angle it opens.
   Assign a **Signal Intensity (0–100)** and drop anything below **60**.
2. **Cross-signal synthesis clustering**: Actively identify intersecting pairs or clusters of signals
   that collide to form a larger emergent story. Look for archetypal pairings:
   - *Cost/Driver ⨂ Operational Shift*: e.g. Frontier LLM price collapse (Signal A) + Enterprise shift
     toward local in-house software development (Signal B).
   - *Governance/Regulatory Hammer ⨂ Technical Architecture*: e.g. Compliance audit mandate (Signal A) +
     Autonomous agent tool-execution boundaries (Signal B).
   - *Infrastructure Constraint ⨂ Algorithmic Optimization*: e.g. Datacenter power bottlenecks (Signal A) +
     Model distillation & skill pruning (Signal B).

### Stage 4 — Output
Write `context/recon_proposals/YYYY-MM-DD_<vertical>_signals.md`:
```markdown
# Signals: <vertical> — YYYY-MM-DD
**Window:** <start> → <today>
**Queries run:** <n>

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|

## Candidate Synthesis Pairs
| Pair | Signals | Collision Vector / Emergent Inquiry | Estimated Emergence (1-10) |
|---|---|---|---|
| 1 | #1 ⨂ #4 | Would tumbling frontier token prices make local in-house development more reliable than SaaS? | 8.5 |
```

> **Pairing helper (advisory).** `python3 scripts/synthesize_topics.py --signals <that file>` prints a
> mechanically validated candidate table: only rows with an `https://` source, an in-window date and
> Intensity ≥ 60; word-boundary token collisions, ≥ 2 distinct tokens, different source domains, and
> archetypes scoped to the registry verticals. It reports an advisory `emergence_heuristic` — **it does
> not score the ≥ 8 gate, does not write a headline, and "no valid pair" is a legitimate answer.**
> Use it to seed the table above, then let the Judge own the collision vector and the number. The
> rows in the table above come from the Judge, not from the helper.

## 4. Failure handling
- Zero candidates ≥ 60 → log query syntax to `skills/self_improvement_eval.md`, widen to 45 days,
  re-run once. If still empty, return "no publish" — never pad.
- **Anchor-driven verticals** (configured sources that are annual/quarterly surveys or benchmarks —
  e.g. `enterprise_tech_leadership`'s `cloud_cost_reports`, `hacker_news`, `substack_tech_leads`)
  spike quarterly, not weekly. A weekly re-run whose window has advanced only ~7 days will
  legitimately find no fresh primary data between spikes. The correct outcome is "no publish" — do
  NOT widen the window past 45 days to smuggle a stale survey (e.g. an April survey into a
  September window) past the 30-day freshness gate. Anchor-driven weakness is a cadence fact, not
  a sweep defect.
