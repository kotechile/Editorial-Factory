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

### Stage 3 — Capture & score
For each raw signal capture: URL, date, the concrete claim/figure, and the angle it opens.
Assign a **Signal Intensity (0–100)** and drop anything below **60**.

### Stage 4 — Output
Write `context/recon_proposals/YYYY-MM-DD_<vertical>_signals.md`:
```markdown
# Signals: <vertical> — YYYY-MM-DD
**Window:** <start> → <today>
**Queries run:** <n>

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
```

## 4. Failure handling
- Zero candidates ≥ 60 → log query syntax to `skills/self_improvement_eval.md`, widen to 45 days,
  re-run once. If still empty, return "no publish" — never pad.
