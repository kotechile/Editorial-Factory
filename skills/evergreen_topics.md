# SKILL: Evergreen Track (Loop 1E — Useful, Durable Topics)

## 1. Objective

Publish one **useful, durable** article for a vertical: a topic a reader would search for and act
on months from now. Not a news sweep.

The news pipeline (`skills/radar_30day.md` → `skills/virality_judge.md`) is built to find a fresh
30-day signal; its gate weights **Novelty 0.40** and drops anything whose load-bearing claim is
older than the window. That is correct for news and wrong for everything else: it is why verticals
whose beat is periodic (annual surveys, statute books, procurement cycles) returned
*"no publish"* week after week, and why the runs logged *"undated evergreen; not anchored to
window"* while discarding material readers actually want.

This track exists because those are two different products. **The news gate does not run here** —
do not score Novelty, do not run `synthesize_topics.py --seed`, do not widen a window. And the
converse holds: a topic whose value expires inside ~90 days is a news story, and belongs in the
news pipeline, not here.

## 2. What makes a topic admissible

Come to the topic from evidence, never from your own idea of what would be interesting. Any of
these is a legitimate lead; a topic with none of them is an invented topic and is refused:

| Lead | Where it lives |
|---|---|
| The vertical's own beats | `primary_angles` in `context/verticals.json` |
| What the reader is trying to decide | the persona's `wants` in `context/personas.json` |
| The founder's standing positions | `context/growth_os/founder-voice.md` §2 (content pillars) and §3 (per-vertical angles) |
| Real field friction with numbers | `context/growth_os/customer-truth.md` (per-vertical anecdotes) |
| Recurring non-news material | the intel feeds' `product_evaluations` / `market_metrics` (via `scripts/home_lifestyle_intel_client.py`, `scripts/supply_chain_intel_client.py`) |
| Demand the site is already close to winning | `scripts/gsc_analyzer.py --vertical <id> --export-md` — **bonus signal only**: impressions are thin on a young site, so low volume never vetoes a good topic |

## 3. The Evergreen Gate (hard)

Mechanical floor, enforced by `scripts/evergreen_gate.py` — a `PASS` there is required before a
single word of prose is drafted:

- **≥ 3 distinct primary sources** (`MIN_SOURCES`), on **≥ 2 distinct hosts** (`MIN_HOSTS`). Three
  pages of one vendor's site are one source wearing a costume.
- **Every cited source is fetched and must actually contain the figure it is cited for.** Not the
  URL pattern, the page. A paywalled, PDF-only or 404 source is a failure to fix, not a footnote;
  replace it.
- **A named persona decision** — the sentence the reader is trying to settle. If you cannot state
  it, there is no article.
- **A proven de-dup check** against the last **180 days** (`DEDUP_WINDOW_DAYS`) of this vertical's
  briefs and published articles: name the nearest prior artifact (a date or slug) that exists. The
  gate proves the artifact exists rather than pretending to judge similarity — a token-overlap test
  on a one-line thesis produces both false retreads and false passes.
- **An `as of` date** for any time-bound figure (a price, a rate, a cap, a standard). An undated
  figure is a news fact wearing an evergreen label, and it will be wrong within a year.

Beyond the floor, judge the topic yourself on the four axes and write the score into the brief:

| Axis | Question | Weight |
|---|---|---|
| Usefulness | Does it settle a decision the persona actually faces this year? | 0.35 |
| Durability | Is it still correct in 12 months, with the cited figures dated? | 0.25 |
| Evidence | Are the anchors primary, measured, and about this beat (not vendor claims)? | 0.25 |
| Actionability | Does it carry at least one rule with numbers — a threshold, a payback, a gotcha? | 0.15 |

Composite = round(0.35·U + 0.25·D + 0.25·E + 0.15·A, 1). **≥ 8 → proceed.** Below that, either
sharpen the evidence or return "no publish" and say why. There is no quota: a vertical that has
nothing durable to say this week says nothing.

**Refused outright (these are what "evergreen" degenerates into):**
- a listicle of unverified statistics — that is what `skills/citation_hub.md` is for, and it has its
  own stricter data gate;
- a "complete guide" whose every section restates the same three sources;
- a re-argued version of a published article (see the de-dup rule);
- anything whose honesty depends on a figure you could not fetch.

## 4. Output — the evergreen brief

Write `context/recon_proposals/YYYY-MM-DD_<vertical>_evergreen_brief.md` (the name is load-bearing:
it never collides with the news track's `_signals.md` / `_angle_brief.md`, and
`scripts/verify.sh` discovers briefs by it):

```markdown
# Evergreen Brief: <vertical> — YYYY-MM-DD
**Archetype:** evergreen
**Vertical:** <vertical_id>
**Persona:** <persona_id from context/personas.json>
**Decision the reader is facing:** <the decision + when it bites — >= 40 chars>
**Durability:** <why this is still true in 12 months; state what the figures are *as of*>
**De-dup:** <the nearest prior artifact for this vertical in the last 180 days + why this differs>
**Thesis:** <the one sentence the article must defend>

**Lead:** <which of §2's evidence sources produced this topic, and the specific material>

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | <publisher + title> | https://… | YYYY-MM-DD | <the exact figure> | measured |
| 2 | … | … | … | … | vendor claim |
| 3 | … | … | … | … | measured |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| <topic> | 9 | 8 | 9 | 7 | 8.4 | **winner** |
| <topic> | 7 | 9 | 6 | 8 | 7.4 | dropped — one anchor is a vendor claim |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->
```

Then run the gate:

```bash
python3 scripts/evergreen_gate.py --brief context/recon_proposals/YYYY-MM-DD_<vertical>_evergreen_brief.md
```

It fetches every row, prints the evidence it found for each figure, and writes the
`<!-- evergreen-gate: -->` marker on pass. **Editing a row after that makes the marker stale, and
`scripts/verify.sh` reads a stale or missing marker as a build failure** — re-run the gate.

**Writing the figure cell so the gate can read it:** the matcher looks for numeric tokens, so a row
whose figure is written in words must *begin* with the number word (`six months — …` matches "six
months" or "6 months"; `at least six months — …` generates no pattern at all and reads as
`figure_absent`). Lead the cell with the figure, then the gloss, and never bury it after prose —
the same row that fails this way will pass once the figure moves to the front.

**A multi-token figure can verify on the wrong number.** `citation_hub_dossier.figure_evidence`
returns evidence as soon as *any* numeric token in the cell appears in the fetched page, so a range
written `8% to 15%` will "verify" on a bare `8` the source never tied to the claim (observed: the
phrase was absent from both cited pages entirely, and a lone `8` elsewhere on the page passed it).
Lead the cell with the one distinctive figure the source actually states (e.g. `20% to 30%`), and
eye-check that the *phrase* — not a coincidental single digit — is on the page. A figure that
verifies this way ships a claim the source never made.

**The gate fetches with a fixed, non-browser user-agent — check fetchability before you write a
row.** `citation_hub_dossier.fetch_source` sends
`Mozilla/5.0 (compatible; EditorialFactorySourceVerifier/1.0)`, and several hosts answer it with
HTTP 403 even though the page is public in a browser. Observed: the entire Bureau of Labor
Statistics site (`bls.gov` — OEWS/CES/JOLTS/ECEC), which is otherwise the best measured anchor for
wage, turnover and benefit figures, returns 403 to the verifier and therefore cannot carry a gate
row. Probe a candidate URL through the same fetch the gate uses before committing to it:

```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); import citation_hub_dossier as c; \
print(c.fetch_source('<url>')['status'])"
```

A `verified` row needs `status == 'fetched'`; a 403/404/PDF row fails the floor no matter how good
the figure is, so build the topic around sources that actually retrieve.

**A `fetched` row can also be an error page wearing HTTP 200 — check the body, not just the status.**
EIA's `epm_table_grapher.php` URLs (Electric Power Monthly figure tables) intermittently answer 200 with
a ~260-character stub reading *"Sorry! Unexpected Error … routed to the appropriate person"* and no
numbers at all, so the same row passes on one fetch and reads `figure_absent` on the next (observed
2026-10-09: the July 2026 industrial price row verified on a manual probe, then failed inside the gate
run). Prefer a stable EIA prose page for the same figure — `eia.gov/energyexplained/electricity/…`
carries the annual average price by customer class in plain text and retrieves every time — and treat any
`fetched` body under ~400 characters as unreachable until you eyeball it.

**A `fetched` row can still fail as `figure_absent` — the page loaded and the number did not.**
Several vendor rate-card hosts render their tables client-side, so the verifier gets HTTP 200 with a
body that carries no numeric tokens at all. Observed 2026-10-08 building the supply_chain evergreen
brief: `fedex.com`, `odfl.com`, `xpo.com`, `tforcefreight.com`, `saia.com` and `ups.com` fuel-surcharge
pages either 404 or return a `fetched` page whose text is navigation only, so a row on a carrier's own
published surcharge table fails the floor even though the table is visible in a browser.
`fred.stlouisfed.org` is unreachable to the verifier outright. The source types that reliably return the
figure as text are government statistics pages (`eia.gov` works where `bls.gov` 403s), arXiv/doc sites,
and industry explainers — so check the figure, not just `status`, before committing a row:
`python3 -c "import sys; sys.path.insert(0,'scripts'); import citation_hub_dossier as c; \
print(c.figure_evidence('<figure>', c.fetch_source('<url>')['text']))"`.

## 5. Handoff

Only after `PASS`: `skills/fact_check.md` → `skills/story_draft.md` → `skills/claude_humanizer.md`
→ `scripts/publish.py`. The article keeps the house schema (section markers, `## Sources`, the
LinkedIn variant) and adds two frontmatter flags so the reader surfaces and the audit can tell it
apart from a news piece:

```yaml
archetype: evergreen
evergreen: true
```

Persistence to the site + Supabase is **not** approval-gated. Outbound distribution (LinkedIn /
Ghost / Reddit) waits for the founder's `@Simon approve` gate, exactly as the news track does.

## 6. Failure handling

- **No candidate clears ≥ 8** → return "no publish", log the axes table to
  `skills/self_improvement_eval.md`, and say what evidence was missing. Never pad.
- **A source stops resolving** (moved, paywalled, deleted) → replace the row and re-run the gate;
  never drop the figure's citation and keep the claim.
- **The de-dup names nothing** → look at `context/published_log.md` and
  `context/recon_proposals/*_<vertical>_*` for the last 180 days before re-arguing a thesis you
  already ran.
- **The topic is really news** (value expires in < 90 days) → hand it to the news track; do not
  smuggle it here, where the freshness gate cannot see it.
