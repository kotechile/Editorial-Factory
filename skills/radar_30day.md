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

> **arXiv/HN sourcing mechanics (learned 2026-10-14):** in this environment an arXiv `abs` or `html`
> page fetched through the web tools returns boilerplate with **no abstract text**, so a paper cannot
> be dated or quoted from the page itself. Query the API instead —
> `https://export.arxiv.org/api/query?search_query=<terms>&sortBy=submittedDate&sortOrder=descending`
> for a discovery sweep, and `...?id_list=2609.17930,2610.15884` for exact `published` dates plus the
> full `<summary>` (the abstract) of named papers; `http://` (not `https://`) fails there with 0
> entries. For Hacker News use Algolia rather than the site:
> `https://hn.algolia.com/api/v1/search_by_date?query=<q>&tags=story&numericFilters=created_at_i%3E<epoch>`
> returns dated stories, which is how a `site:news.ycombinator.com` angle is satisfied for a window.
> Fetched abstracts are the primary record; a publisher's own index page
> (e.g. `uber.com/us/en/blog/engineering`) is what dates a first-party post whose page carries no
> visible date in the extract.

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

> **Pairing step (required, mechanical).** Once this file is written, run
> `python3 scripts/synthesize_topics.py --seed <this file>` (the job instruction names it too). It seeds
> the `## Candidate Synthesis Pairs` block below from **this file's own rows only**: rows with an
> `https://` source, an in-window date and Intensity ≥ 60; word-boundary token collisions, ≥ 2 distinct
> tokens, different source domains, and archetypes scoped to the registry verticals. It reports an
> advisory `emergence_heuristic` — **it does not score the ≥ 8 gate, does not write a headline, and
> "no valid pair" is a legitimate answer.** Re-run it whenever you add or remove a signal row (the
> marker records the row count and `scripts/verify.sh` §8 reads a mismatched block as stale).
> Then let the Judge own the collision vector, the headline and the number.
>
> **A vertical whose every row resolves to one domain always seeds "no valid pair" — one dated first-party page
> fixes that (learned 2026-10-14).** The helper requires the two legs to sit on *different source domains*, so a
> research-only sweep (every row `arxiv.org`) returns `candidates=0` on every run, however strong the substantive
> collision is — the pattern this vertical hit on 2026-10-07 and again for `gpu_hardware`. Writing in one dated
> first-party page (a vendor docs page carrying its own `Last updated YYYY-MM-DD` footer counts, and is admissible
> at a low Intensity when it states a design rather than a measurement) gave the same sweep `rows=7 candidates=3`.
> Two consequences: the seeded candidates are *input*, not a verdict — on that run the Judge scored all three
> (each rested on the unmeasured page) and adopted a pair the token layer could not see, so answer every seeded
> candidate in the brief's runner-ups and say why; and a page with no measurement can corroborate a collision
> (as friction: what the industry ships) but can never serve as a dual-authority anchor alongside a measured leg.
>
> **A vertical that has always seeded "no valid pair" can produce candidates the moment its rows span domains (learned
> 2026-10-20).** `workstation_compute_economics` seeded `candidates=0` on 2026-10-06 and 2026-10-13 — both sweeps were
> dominated by one vendor's pricing story — and seeded `rows=9 candidates=6` on 2026-10-20 once the window carried a
> first-party model page, a launch-day retail price list, two independent price trackers (euros and dollars) and a
> hands-on write-up. The seeded pairs are then *input*: that run the Judge scored all six, adopted a pair the helper
> ranked third (the envelope needed a dollar-priced pool beside it to become one comparison) and answered the rest in
> the brief's runner-ups. So a zero-candidate sweep is evidence about the row set's domain mix, not about the vertical.

> **A sweep can legitimately rest on live status pages — date them by observation and put the event date in the claim cell (learned 2026-10-16).**
> Some verticals' strongest in-window signal is a *state of the world* rather than a dated article: a regulator's project page
> ("staff continue to work with OAL on a final review"), a county programme page ("pausing grant activities after September 1st"),
> a federal grant page ("FEMA is currently reviewing submissions"), a register entry. These carry no publication date, and a
> strict "drop anything older than the window" reading would discard the rows that make the story. The workable convention, used
> on the 2026-10-16 `resilient_home_assets` run: put the **observation date** (`2026-10-16`) in the Date column, state the
> underlying event date **inside the Figure/Claim cell** ("pause effective 2026-09-01"; "OAL action logged 2026-09-08"), add a
> `**Dating note**` paragraph under the table saying exactly which rows are event-dated and which are standing records, and keep
> the undated/just-out-of-window primaries in the `## Dated background` list so their URLs are still in the file for
> `synthesize_topics.py --check-briefs`. `parse_signal_date` reads the *leading* date token, so an observation date makes the
> row admissible to the seeder while the claim cell keeps the provenance honest. Never silently restate a status as an event.

> **A recurring report's PRIOR edition is still live on the same domain — pin the edition, not the page (learned 2026-10-16).**
> The sibling of the rule above: a report that carries the same name every year leaves last year's figure set one click away, still indexed, still ranking
> for the same query. Observed on the 2026-10-16 `career_velocity_equity_engineering` sweep — the publisher's 2026 edition page carried 47% / 88% / 26% /
> 41% / 37%, while its **2025** edition, on the same domain under the same report brand, carried a different set entirely (39% next-event tenders, plus
> the "only 5% feel very prepared to facilitate a tender offer compared to 41% for an IPO" pair) and stated its own fielding window as
> "January – February of 2025". Both pages describe themselves as the same report. Before any figure from an annual or recurring report enters the
> signals file, read that edition's own methodology or dated disclosure line and record which edition the number belongs to in the claim cell; a figure
> that cannot be pinned to the current edition is dropped, and the **verified brief names the excluded prior-edition figure explicitly** so the drafter
> cannot pick it up by accident.
>
> **Date a trade-press hit from the publisher's own date field, never from the search result (learned 2026-10-14).**
> A search hit reads as current — it ranks, it has a fresh-looking excerpt — but the story it reports can be
> weeks old, and a stale anchor silently reds the freshness gate after the Judge has already scored it.
> Most of this vertical's sources are WordPress-backed, so the publication date is one call away:
> `https://<host>/wp-json/wp/v2/posts?search=<urlencoded title>&_fields=date,modified,link,title` returns the
> canonical `date`. Observed: a "$1.8M revenue ahead of a humanoid SPAC" story was the strongest available
> unit-economics leg for this vertical, and the WP `date` field showed 2026-09-07 (its subject S-4 was filed
> 2026-09-04) — both outside a window that began 2026-09-14, so the anchor was dropped at Stage 1 instead of
> being discovered at fact-check. Probe every trade-press anchor this way before it enters the signals file;
> for a filing-backed story, date the *filing* too (SEC full-text search returns `file_date`), because a
> report is never fresher than the record it reports on.
> **The seed helper trusts the Date cell you typed, so a date lifted from the search snippet silently
> makes an out-of-window row admissible.** Observed 2026-10-22: an Eye On Housing post whose search hit
> read as current was written into the table as `2026-09-23` and seeded without complaint
> (`rows=9 candidates=0`); its WordPress `date` was **2026-09-02**, eleven days before the window opened.
> Run the publisher's own date lookup *before* the row is written, not after, and re-seed whenever a row's
> date changes — the marker records the row count, not the dates, so a corrected date is invisible in
> `verify.sh §8`.

> **Every URL a downstream artifact cites must appear as a URL in this file (learned 2026-10-08).**
> `scripts/synthesize_topics.py --check-briefs` (verify.sh §8) extracts *every* `https://` URL from a
> draft's body — including a corroborating citation in `## Sources`, not just the two synthesis
> anchors — and fails if any one of them is absent from a committed `*_signals.md` file. A draft that
> cites a record-low figure to CNBC while the signals file only mentions "CNBC" in prose (no URL)
> reds the build. Write the full `https://` URL of every corroborating source you intend to cite into
> this file (its own row or a primary-source note), not just the load-bearing anchors.
> **The file the checker reads is the `_signals.md`, not the `_verified_brief.md`** (learned 2026-10-23):
> a background URL parked only in the verified brief's table — a prior-year 10-K quoted for one computed
> comparison, say — passes every other gate and then reds `--check-briefs` on both the draft and the
> final, after the rewrite has already been paid for. Add such URLs to this file's `## Dated background`
> list before the fact-check pass, not after Loop 3.

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
- **A report's title year is not its fielding date.** A study released (or re-surfaced) *this month*
  can rest on a survey fielded a quarter earlier — date the *figure*, not the cover. Observed
  2026-10-08: an Incisiv/Anaplan "2026 Supply Chain Resilience & AI Adoption Study" resurfaced in
  the window via a Sept/Oct webinar and white paper, but its 298-executive survey was fielded in
  Q1 2026 and the release was 28 April 2026 → out of window; it was carried as dated background,
  not an anchor. Apply the same check to a "new" annual report whose underlying data predates the
  window.
