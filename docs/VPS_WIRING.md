# VPS Wiring — Editorial Factory (next-phase handoff)

The Editorial Factory engine is Hermes-native. This repo is the **shared brain** the fleet reads
and writes. The following wiring happens on the VPS (`72.61.72.70`, Ubuntu 24.04) where the
Hermes gateway and bot fleet already run the software factory. The software factory is left
running untouched.

## 1. Frontier key — Claude via kie.ai (already wired)

The Claude Stylist & Critic step routes Anthropic models through **kie.ai**, not `api.anthropic.com`.

- **Endpoint:** `https://api.kie.ai/claude` (Anthropic Messages API)
- **Key:** `ANTHROPIC_API_KEY=Bearer <kie.ai key>` — the literal `Bearer ` prefix is **required** by kie.ai (already set in `/root/.hermes/.env` and `~/.hermes/.env`).
- **Key source:** Supabase project "StoryTeller", table `api_keys`, row `provider='kie.ai'`, column `key_value`.
- **Model IDs (from Supabase `llm_models`):** request with the **alias** `claude-sonnet-5` — kie.ai resolves it to the real dated model `claude-opus-4-5-20251101` (visible in the response). `Claude-Opus-4-8` is also available. Do NOT send dated Anthropic IDs as the request model — kie.ai returns "page does not exist".
- **Auth header:** `Authorization: Bearer <kie.ai key>` (kie.ai's official convention). `x-api-key: Bearer <kie.ai key>` is also accepted. Hermes's anthropic provider sends `x-api-key`, so keep the `Bearer ` prefix in `ANTHROPIC_API_KEY`.
- **kie.ai-specific fields:** `thinkingFlag: true` and `stream: false` (kie.ai extensions — safe to omit, harmless when present).
- **Routing:** set the stylist profile's model config to:
  ```yaml
  model:
    default: claude-sonnet-5
    provider: anthropic
    base_url: https://api.kie.ai/claude
  ```
  (`model.base_url` is what redirects Hermes's Anthropic provider off `api.anthropic.com`.)

Verify before the first end-to-end run:
```bash
# credits (key valid?)
curl -s https://api.kie.ai/api/v1/chat/credit -H "Authorization: Bearer <key>"
# a real completion
curl -s https://api.kie.ai/claude/v1/messages -H "x-api-key: Bearer <key>" \
  -H "anthropic-version: 2023-06-01" -H "content-type: application/json" \
  -d '{"model":"claude-sonnet-5","max_tokens":64,"messages":[{"role":"user","content":"ping"}]}'
```

> Note: kie.ai's Claude upstream intermittently returns 502/503 `Internal error` (their documented stability caveat) — retry if you hit it. The credit endpoint returning 200 confirms the key itself is valid.

## 2. Bot fleet (7 profiles)

Create each profile and mirror its persona contract into the bot's SOUL/instructions:

| Profile | Persona source | Model tier |
|---|---|---|
| `editor` | `.agents/editor_in_chief.md` | orchestrator (deepseek-v4-pro) |
| `radar` | `.agents/radar_scout.md` | fast |
| `judge` | `.agents/virality_judge.md` | fast |
| `verifier` | `.agents/fact_verifier.md` | mid |
| `drafter` | `.agents/story_drafter.md` | mid |
| `stylist` | `.agents/claude_stylist.md` | **Claude via kie.ai** (`claude-sonnet-5`) |
| `publisher` | `.agents/publisher.md` | light |

Each bot's working directory must be this repo (so `skills/`, `context/`, and `scripts/` resolve).

## 3. Cron jobs

Register via `hermes cron` (mirroring the factory's "[bot:simon] Weekly Market Recon" pattern):

| Job | Schedule | Prompt (self-contained) |
|---|---|---|
| `Radar Sweep: <vertical>` | per `context/content_calendar.md` | "Run the 30-day radar for vertical '<id>' per skills/radar_30day.md, write to context/recon_proposals/" |
| `Full Editorial Pipeline: <vertical>` | after radar (offset) | "Run full pipeline for '<id>': virality_judge -> fact_check -> story_draft -> claude_humanizer per the matching skills; halt at the approval gate for @Simon approve." |

One `Radar Sweep` + one `Full Editorial Pipeline` pair per active vertical (start with
`agentic_ai`, add the rest once the first vertical passes end-to-end).

## 4. Coolify deploy (the site)

1. New application → GitHub repo `kotechile/editorial-factory`, Dockerfile build.
2. Env vars: `PORT=3000` (no secrets needed for the static reader — the site serves `published/`).
3. Domain: e.g. `editorial.<your-domain>` (products ship at subpaths in the factory; this is a
   separate app and can get its own subdomain).
4. Optionally add a production Ghost CMS app and point the Publisher at it
   (`GHOST_API_URL`, `GHOST_ADMIN_API_KEY`) when auto-publish is approved.

## 5. Supabase (persistence)

Reuse the factory's Supabase project or create a new one. Minimal tables:

```sql
create table articles (
  id uuid primary key default gen_random_uuid(),
  slug text unique not null,
  vertical text not null,
  headline text not null,
  body_md text not null,
  linkedin_post text,
  sources jsonb,
  status text default 'draft', -- draft | approved | published
  live_urls jsonb,
  created_at timestamptz default now()
);
create table signals (
  id uuid primary key default gen_random_uuid(),
  vertical text not null,
  source_url text not null,
  claim text,
  angle text,
  intensity int,
  swept_at timestamptz default now()
);
```

## 6. First end-to-end dry run

```bash
hermes -p editor chat -q "Run the full editorial pipeline for vertical 'agentic_ai' \
  per skills/radar_30day.md, virality_judge.md, fact_check.md, story_draft.md, claude_humanizer.md. \
  Stop at the approval gate — do not publish."
```

Confirm: a `_signals.md`, `_angle_brief.md`, `_verified_brief.md`, `_draft.md`, and `_final.md`
all land in `context/recon_proposals/` and `context/drafts/`, and `scripts/verify.sh` passes.
Then enable distribution vertical-by-vertical.
