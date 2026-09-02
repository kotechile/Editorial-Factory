# VPS Wiring — Editorial Factory (next-phase handoff)

The Editorial Factory engine is Hermes-native. This repo is the **shared brain** the fleet reads
and writes. The following wiring happens on the VPS (`72.61.72.70`, Ubuntu 24.04) where the
Hermes gateway and bot fleet already run the software factory. The software factory is left
running untouched.

## 1. Frontier key (blocking prerequisite)

The Claude Stylist & Critic step requires a frontier model. Add **one** of the following to the
gateway env (`~/.hermes/.env` on the VPS), then `hermes doctor` to confirm:

```bash
ANTHROPIC_API_KEY=sk-ant-...        # preferred
# or an OpenRouter route:
OPENROUTER_API_KEY=...
```

Until this key exists, the pipeline halts at the frontier gate (by design — no non-frontier
substitution). Verify the Claude model is selectable before the first end-to-end run.

## 2. Bot fleet (7 profiles)

Create each profile and mirror its persona contract into the bot's SOUL/instructions:

| Profile | Persona source | Model tier |
|---|---|---|
| `editor` | `.agents/editor_in_chief.md` | orchestrator (deepseek-v4-pro) |
| `radar` | `.agents/radar_scout.md` | fast |
| `judge` | `.agents/virality_judge.md` | fast |
| `verifier` | `.agents/fact_verifier.md` | mid |
| `drafter` | `.agents/story_drafter.md` | mid |
| `stylist` | `.agents/claude_stylist.md` | **Claude frontier** |
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
