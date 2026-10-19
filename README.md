# Editorial Factory — Autonomous Content Intelligence & Editorial Engine

A Hermes-native, multi-agent editorial pipeline that turns the last 30 days of signals in a
chosen vertical into **trustworthy, human-voice articles** ready for its reader sites.

It is the editorial twin of [`kotechile/factory`](https://github.com/kotechile/factory): same
agentic workforce pattern (bot fleet + skills + shared context + cron + approval gate), but the
output is published articles instead of micro-SaaS products.

> 📖 **Read [docs/USER_GUIDE.md](docs/USER_GUIDE.md)** — how it works and how to use it.

## Triple-Engine Architecture

### Engine 1: 30-Day News & Intelligence Radar (with Cross-Topic Synthesis)
```
[Cron / Gateway / Manual trigger]
        │
        ▼
[Radar Scout]          Loop 1 — 30-day multi-source sweep + synthesis pair clustering
        │
        ▼
[Virality Judge]       evaluates single signals & cross-pollination pairs (Signal A ⨂ Signal B)
                       scores ≥ 8/10 (Emergence × Dual Authority × Tension/Shareability)
        │
        ▼
[Fact Verifier]        Loop 2 — dual-anchor extraction → validate both vs primary sources
        │
        ▼
[Story Drafter]        structure: collision lead → systemic tension → dual-anchor stats → tactics
        │
        ▼
[Claude Stylist]       Loop 3 — frontier rewrite + critic read-back until human-voice gate passes
        │
        ▼
[Publisher]            persist → published/ + Supabase + sitemap + CMS draft (no gate)
                       (no social distribution — the LinkedIn/Reddit channel was removed 2026-10-06)
```

### Engine 2: SEO Content Machine (Growth OS)
```
[Google Search Console] ──> High-impression / emerging query detected (Pos 8-25, Impr > 500, WoW > 50%)
           │
           ▼
     [DataForSEO]        ──> Enrich with search volume, SERP intent, keyword clusters, top 10 URLs
           │
           ▼
 [Growth OS Knowledge]   ──> Cross-reference founder-voice.md & customer-truth.md (Moat & Taste)
           │
           ▼
[Cannibalization Shield] ──> Audit sitemap.json + generate contextual internal link map
           │
           ▼
     [LLM / Agent]       ──> Drafts post + meta title/description + JSON-LD schema (@Article/@FAQPage)
           │
           ▼
 [Frontier Humanizer]    ──> Loop 3 human-voice rewrite preserving SEO schema & internal links
           │
           ▼
    [Approval Gate]      ──> Human checks voice, adds contrarian founder take, hits publish
           │
           ▼
   [Performance Loop]    ──> Post-publish rank tracking in GSC feeds learnings back to Growth OS
```

### Engine 3: Evergreen Track (useful, durable topics)
```
[Cron: Evergreen Pipeline: <vertical>] ──> same weekday as the news run, 17:30-20:00 UTC band
           │
           ▼
 [Evergreen Scout]      ──> topic from EVIDENCE, never invention: the vertical's primary_angles,
           │                the persona's `wants`, founder-voice §2/§3 pillars, customer-truth
           │                field notes, the intel feeds, GSC striking-distance queries
           ▼
 [Evidence floor]       ──> scripts/evergreen_gate.py: >= 3 primary sources on >= 2 hosts, each
           │                FETCHED and shown to contain the figure cited, a named persona
           │                decision, a proven 180-day de-dup, an `as of` date on time-bound figures
           ▼
   [fact_check] ──> [story_draft] ──> [claude_humanizer] ──> publish.py (published/ + Supabase)
```
Engine 1 answers *what happened this month* and is gated on freshness (Novelty carries 0.40), so it
correctly refuses a durable topic. Engine 3 publishes the topics Engine 1 must refuse — a decision
the reader faces for years — with a different gate (`skills/evergreen_topics.md`), its own schedule,
and the same persistence/approval rules. Both fleets are reconciled from `context/verticals.json`
and each mode can be switched off per vertical (`news_enabled` / `evergreen_enabled`), which removes
its cron job rather than leaving a half-configured pipeline behind.

## Agent workforce

| Role | Bot profile | Duty | Model tier |
|---|---|---|---|
| Editor-in-Chief | `editor` | orchestration, calendar, run-log | orchestrator |
| SEO Scout | `seo_scout` | GSC query detection, DataForSEO enrichment, cannibalization audit | fast |
| Radar Scout | `radar` | 30-day sweep per vertical | fast |
| Virality Judge | `judge` | score single signals + cross-pollination pairs; drop < 8 | fast |
| Fact Verifier | `verifier` | claim extraction + primary-source validation | mid |
| Story Drafter | `drafter` | structural first pass & SEO schema markup | mid |
| Claude Stylist & Critic | `stylist` | frontier human-voice rewrite | **Claude (frontier)** |
| Publisher | `publisher` | persistence + CMS draft | light |

## Repository layout

```
.agents/   persona contracts            skills/   SOPs (the loops)
context/   verticals.json, personas.json, calendar, published log
scripts/   cron triggers + verify gates  site/     static reader (Coolify)
published/ final approved articles       Dockerfile + docker-compose.yml
```

## Quick start (local)

```bash
# 1. Configure verticals + voice personas (already seeded with 26 verticals)
cat context/verticals.json

# 2. Manual radar sweep for 30-day industry signals
hermes -p radar chat -q "Run the 30-day radar for vertical 'agentic_ai' per skills/radar_30day.md"

# 2b. Multi-topic signal synthesis — pair seeding (advisory pre-filter, no scoring)
python3 scripts/synthesize_topics.py --seed context/recon_proposals/2026-09-26_<vertical>_signals.md
python3 scripts/synthesize_topics.py --demo
python3 scripts/synthesize_topics.py --check-seed    # does every new signals file carry a fresh seed block?
python3 scripts/test_synthesize_topics.py            # regression suite for the helper
python3 scripts/test_sync_crons.py                   # cron fleet contract tests (cadence + prompt)

# 3. Demand-Led SEO Content Machine: Scan GSC opportunities & draft article
python3 scripts/gsc_analyzer.py --min-impressions 500 --min-pos 8 --max-pos 25
python3 scripts/seo_machine.py --query "mcp server implementation python" --vertical "agentic_ai"

# 4. Full pipeline runs
scripts/cron-full-pipeline.sh   # 30-day news pipeline
scripts/cron-seo-pipeline.sh    # SEO Content Machine

# 5. Verify the quality gate (also runs daily via the `Editorial Verify Gate` cron job)
scripts/verify.sh
```

## The PressFlow dashboard

`site/` is the operations dashboard (internal, behind `PRESSFLOW_AUTH_SECRET`). It deliberately
**does not list, preview or edit articles** any more (owner, 2026-10-18): a finished article is
pushed to the CMS and read on the reader fronts, so a second copy in the dashboard had no
destination. What it does hold:

| Tab | What it is |
|---|---|
| ⚙️ **Verticals** | the registry that drives both cron fleets, with the full Supabase round-trip on the same tab (`↥ Push`, `↧ Pull`, `⚡ Sync Crons`) and a status strip saying which copy you are looking at |
| ✅ **Approvals** | Simon's open asks as one row each — what it is, what he needs, and the exact reply to copy — plus the app inventory, where each product carries its own `@Simon retire <app>` reply. The queue is read from `kotechile/factory` (`context/approval_queue.json`) with `context/approvals.json` as the committed fallback, and the tab says which copy is showing |
| 📅 **What's Next** | the forward calendar in UTC: the next article runs computed from each vertical's `cadence` / `evergreen_cadence`, and the next app-harvest sweeps from `context/app_harvest_queue.json` (two verticals per Monday recon, never-scanned first) |
| 📣 **App Promotion To-Do** | the software-factory apps' promotion queue (below) |
| ⚡ **SEO Machine** | GSC demand, DataForSEO, Growth OS, cannibalization and ranking loop |
| 👥 **Personas** | the reader archetypes the verticals point at |
| 🛰️ **Fleet & Crons** | cron reconciliation and the operations log |

## App Promotion To-Do Queue (Applications only) & Removed Article Distribution

The PressFlow dashboard provides an **📣 App Promotion To-Do** list strictly for the software factory's live applications (catalog: `context/promoted_apps.json`). Each app card features recommended subreddits, ready-to-paste Reddit/LinkedIn copy, and a direct web-intent submit link for manual posting.

In contrast, **article-level** social distribution remains removed (as of 2026-10-06):

- The pipeline generates **no** social media copy for published articles.
- `scripts/publish.py` persists articles to the reader sites (`published/`, Supabase, and WordPress CMS) without creating article social cards.
- The article's legacy `<!-- linkedin -->` block is not required, produced or shipped.
- The to-do list in PressFlow is populated exclusively from `context/promoted_apps.json` via `POST /api/distribution/seed` and manual curation.

## Environment

```bash
ANTHROPIC_API_KEY=        # REQUIRED for the Claude frontier rewrite step
SUPABASE_URL=             # drafts/signals/published store
SUPABASE_SERVICE_ROLE_KEY=
GHOST_ADMIN_API_KEY=      # publisher (optional)
GHOST_API_URL=

# SEO Content Machine & Growth OS (Optional Live APIs; Built-in Sandbox fallback)
GSC_PROPERTY_URL=         # e.g. sc-domain:editorialfactory.io
GSC_CREDENTIALS_JSON=     # Path to service-account.json
DATAFORSEO_LOGIN=         # DataForSEO basic auth login
DATAFORSEO_PASSWORD=      # DataForSEO basic auth password or API key
```

See `docs/VPS_WIRING.md` for the VPS-side bot fleet, cron jobs, and Coolify deploy steps.

## Adding a vertical (config-as-data)

Verticals live entirely in `context/verticals.json` — each entry carries `id`, `label`, `cadence`
(cron expression), `news_enabled`, `evergreen_cadence`, `evergreen_enabled`, `sources`,
`primary_angles`, and `target_persona`. To add one:

1. Append an entry to `context/verticals.json`, giving it a `cadence` slot that is **free on every
   weekday it uses** (slots are 30 minutes apart, 10:30–13:00 UTC — pipelines cannot share a slot).
   Keep it out of DeepSeek's peak windows (Mon–Fri 01:00–04:00 and 06:00–10:00 UTC, where tokens cost
   2x): `scripts/sync_crons.py` refuses to apply such a cadence, `--check` fails on it, and
   `scripts/check_offpeak_crons.py` audits the whole live fleet (watchdogs included) the same way.
2. Add an `evergreen_cadence` if the vertical should also run the evergreen track — a free slot in
   the **17:30–20:00 UTC** band (the news fleet's slots and the daily watchdogs are taken), on the
   same weekday as its news run. `--check` fails on a collision between the two fleets. Leave it
   out (or set `evergreen_enabled: false`) for a news-only vertical.
3. Run `python3 scripts/sync_crons.py` on the VPS — it creates the missing
   `Full Pipeline: <id>` / `Evergreen Pipeline: <id>` cron jobs and fixes any job whose schedule or
   instruction drifted from the registry. Add `--dry-run` to see the plan first; `--check` exits
   non-zero if the registry and the live fleets disagree (this is what `scripts/verify.sh` runs,
   together with the off-peak gate). A mode switched off (`news_enabled: false` /
   `evergreen_enabled: false`) has its job **removed** by the same run.
4. Optionally add a matching `target_persona` to `context/personas.json`.

No code changes required.

## License

MIT
