# Editorial Factory — Autonomous Content Intelligence & Editorial Engine

A Hermes-native, multi-agent editorial pipeline that turns the last 30 days of signals in a
chosen vertical into **trustworthy, human-voice articles** ready for LinkedIn or a website.

It is the editorial twin of [`kotechile/factory`](https://github.com/kotechile/factory): same
agentic workforce pattern (bot fleet + skills + shared context + cron + approval gate), but the
output is published articles instead of micro-SaaS products.

> 📖 **Read [docs/USER_GUIDE.md](docs/USER_GUIDE.md)** — how it works and how to use it.

## Dual-Engine Architecture

### Engine 1: 30-Day News & Intelligence Radar
```
[Cron / Gateway / Manual trigger]
        │
        ▼
[Radar Scout]          Loop 1 — 30-day multi-source sweep per vertical
        │
        ▼
[Virality Judge]       scores ≥ 8/10 (Novelty × Authority × Shareability) or broaden seeds
        │
        ▼
[Fact Verifier]        Loop 2 — extract 3–5 claims → validate vs primary sources
        │
        ▼
[Story Drafter]        structure: incident/stat lead → systemic reason → tactical takeaway
        │
        ▼
[Claude Stylist]       Loop 3 — frontier rewrite + critic read-back until human-voice gate passes
        │
        ▼
[Publisher]            @approve gate → Supabase + LinkedIn/Ghost
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

## Agent workforce

| Role | Bot profile | Duty | Model tier |
|---|---|---|---|
| Editor-in-Chief | `editor` | orchestration, calendar, approval gate | orchestrator |
| SEO Scout | `seo_scout` | GSC query detection, DataForSEO enrichment, cannibalization audit | fast |
| Radar Scout | `radar` | 30-day sweep per vertical | fast |
| Virality Judge | `judge` | score + drop < 8 | fast |
| Fact Verifier | `verifier` | claim extraction + primary-source validation | mid |
| Story Drafter | `drafter` | structural first pass & SEO schema markup | mid |
| Claude Stylist & Critic | `stylist` | frontier human-voice rewrite | **Claude (frontier)** |
| Publisher | `publisher` | persistence + LinkedIn/Ghost | light |

## Repository layout

```
.agents/   persona contracts            skills/   SOPs (the loops)
context/   verticals.json, personas.json, calendar, published log
scripts/   cron triggers + verify gates  site/     static reader (Coolify)
published/ final approved articles       Dockerfile + docker-compose.yml
```

## Quick start (local)

```bash
# 1. Configure verticals + voice personas (already seeded with 5 verticals)
cat context/verticals.json

# 2. Manual radar sweep for 30-day industry signals
hermes -p radar chat -q "Run the 30-day radar for vertical 'agentic_ai' per skills/radar_30day.md"

# 3. Demand-Led SEO Content Machine: Scan GSC opportunities & draft article
python3 scripts/gsc_analyzer.py --min-impressions 500 --min-pos 8 --max-pos 25
python3 scripts/seo_machine.py --query "mcp server implementation python" --vertical "agentic_ai"

# 4. Full pipeline runs
scripts/cron-full-pipeline.sh   # 30-day news pipeline
scripts/cron-seo-pipeline.sh    # SEO Content Machine

# 5. Verify the quality gate
scripts/verify.sh
```

## Environment

```bash
ANTHROPIC_API_KEY=        # REQUIRED for the Claude frontier rewrite step
SUPABASE_URL=             # drafts/signals/published store
SUPABASE_SERVICE_ROLE_KEY=
LINKEDIN_AUTO_POST=       # true to auto-post via API; false (default) for copy-paste review
LINKEDIN_ACCESS_TOKEN=    # publisher (used when LINKEDIN_AUTO_POST=true)
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
(cron expression), `sources`, `primary_angles`, and `target_persona`. To add one:

1. Append an entry to `context/verticals.json`.
2. Run `python3 scripts/sync_crons.py` on the VPS — it creates the missing `Full Pipeline: <id>`
   cron job from the `cadence` field (idempotent; existing jobs are left untouched).
3. Optionally add a matching `target_persona` to `context/personas.json`.

No code changes required.

## License

MIT
