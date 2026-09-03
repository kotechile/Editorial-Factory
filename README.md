# Editorial Factory — Autonomous Content Intelligence & Editorial Engine

A Hermes-native, multi-agent editorial pipeline that turns the last 30 days of signals in a
chosen vertical into **trustworthy, human-voice articles** ready for LinkedIn or a website.

It is the editorial twin of [`kotechile/factory`](https://github.com/kotechile/factory): same
agentic workforce pattern (bot fleet + skills + shared context + cron + approval gate), but the
output is published articles instead of micro-SaaS products.

> 📖 **Read [docs/USER_GUIDE.md](docs/USER_GUIDE.md)** — how it works and how to use it.

## The pipeline (3 loops)

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

## Agent workforce

| Role | Bot profile | Duty | Model tier |
|---|---|---|---|
| Editor-in-Chief | `editor` | orchestration, calendar, approval gate | orchestrator |
| Radar Scout | `radar` | 30-day sweep per vertical | fast |
| Virality Judge | `judge` | score + drop < 8 | fast |
| Fact Verifier | `verifier` | claim extraction + primary-source validation | mid |
| Story Drafter | `drafter` | structural first pass | mid |
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

# 2. Manual radar sweep for one vertical
hermes -p radar chat -q "Run the 30-day radar for vertical 'agentic_ai' per skills/radar_30day.md"

# 3. Full pipeline (radar → judge → verify → draft → Claude rewrite)
scripts/cron-full-pipeline.sh

# 4. Verify the quality gate
scripts/verify.sh
```

## Environment

```bash
ANTHROPIC_API_KEY=        # REQUIRED for the Claude frontier rewrite step
SUPABASE_URL=             # drafts/signals/published store
SUPABASE_SERVICE_ROLE_KEY=
LINKEDIN_ACCESS_TOKEN=    # publisher (optional, v1 = manual review)
GHOST_ADMIN_API_KEY=      # publisher (optional)
GHOST_API_URL=
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
