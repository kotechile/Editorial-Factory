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

## 3. Cron jobs (config-driven, reconciled)

Two fleets, both generated from `context/verticals.json` (**26 + 26 today**) by
`scripts/sync_crons.py`: one `Full Pipeline: <vertical>` job per registry `cadence` (the 30-day news
radar) and one `Evergreen Pipeline: <vertical>` job per registry `evergreen_cadence` (the useful,
durable track, `skills/evergreen_topics.md`). A vertical whose `news_enabled` / `evergreen_enabled`
is false has **no job for that mode** — see the drift classes below.

```
python3 scripts/sync_crons.py --dry-run   # show the plan
python3 scripts/sync_crons.py             # create missing, fix drifted, remove disabled
python3 scripts/sync_crons.py --check     # exit 1 if drifted (wired into scripts/verify.sh)
python3 scripts/sync_crons.py --retire-orphans   # also drop jobs for retired verticals
```

The script reconciles six drift classes, and `--check` fails closed on every one of them:

- **missing** — a registry vertical with no job for an enabled mode (this is how 22 verticals sat
  unscheduled: the earlier create-only version skipped any job whose *name* already existed, so the
  09-19/09-20 registry expansion never reached the live fleet)
- **drifted** — a job whose schedule differs from the registry `cadence` / `evergreen_cadence`
  (a create-only sync can never apply a cadence change)
- **stale prompt** — a job whose instruction differs from `prompt_for(vertical)` /
  `evergreen_prompt_for(vertical)`. The registry owns the step *sequence* too, so a step added to
  the template (e.g. `synthesize_topics.py --seed`, which seeds each signals file's candidate-pair
  block, or the evergreen gate step) cannot silently fail to reach the fleet.
- **disabled** — the settings say the mode is off for the vertical but a live job still exists. The
  registry owns the job's *existence*, so apply **removes** it (re-enabling recreates it). Reusing
  `pause()` here would be ambiguous with an operator's deliberate pause, which the tool leaves alone.
- **orphan** — a job for a vertical no longer in the registry (e.g. `home_systems_reno`, retired in
  `b927ea6` and replaced by the Home & Lifestyle set)
- **collision** — two registry cadences sharing a `(weekday, hour, minute)` slot, across both
  fleets. Slots were a manual discipline ("verify per-weekday uniqueness from the live store, not by
  eye") until the evergreen fleet doubled the number of slots to check; it is a gate now, because
  concurrent pipelines stampede the shared deepseek API and the pinned frontier stylist.

**Staggering.** Slots are 30 minutes apart — news 10:30–13:00 UTC, evergreen 17:30–20:00 UTC — and
unique within each weekday, so no two jobs fire together. Six concurrent 06:00 runs is what we saw
before: they share the deepseek API and the pinned frontier stylist (`kie.ai`), whose 400/5xx
responses halt Loop 3.

**Off-peak.** DeepSeek bills weekday tokens at 2x inside **01:00–04:00 and 06:00–10:00 UTC**
(weekends are off-peak all day), and the scheduler reads cadence hours on the host clock, which is
UTC on this VPS. So every weekday cadence sits at/after 10:30 UTC — the first slot after the
morning window — and the evergreen band starts at 17:30. The watchdogs sit with the fleet:
`Weekly Market Recon` Mon 14:30, `Editorial Verify Gate` 14:00, `WordPress Draft Sweep` 14:15,
`Daily Proactive Sweep` 15:30, `Build Watchdog` 16:30, `Growth Watchdog` Fri 17:00 (which is why the
Friday evergreen band starts at 18:00). Two gates enforce it: `scripts/sync_crons.py --check`
(registry cadences — it refuses to *apply* a peak cadence) and `scripts/check_offpeak_crons.py`
(every enabled job in the live store that makes a model call; run by `verify.sh` §7.2, so the daily
gate reports a drift back into the 2x band). `--no_agent` script jobs are exempt: they make no model
call.

Current weekday slot map: **Mon** news 10:30, 11:00, 11:30, 12:00, 12:30 + evergreen 17:30 … 19:30 ·
**Tue** news 10:30 … 13:00 (6) + evergreen 17:30 … 20:00 (6) · **Wed** news 10:30 … 12:30 (5) +
evergreen 17:30 … 19:30 · **Thu** news 10:30 … 13:00 (6, incl. `agentic_ai`) + evergreen 17:30 … 20:00 ·
**Fri** news 10:30, 11:00, 11:30 + evergreen 18:00, 18:30, 19:00 · **Sat** news 06:00, 06:30 +
evergreen 17:30, 18:00 (all off-peak). Full table: `docs/USER_GUIDE.md` §3, or `hermes cron list`.

Each job is self-contained and runs its track's complete pipeline. News:
`radar_30day → synthesize_topics --seed → virality_judge → fact_check → story_draft →
claude_humanizer`. Evergreen: `evergreen_topics → evergreen_gate --brief → fact_check → story_draft →
claude_humanizer` — note the news gate (`virality_judge`) deliberately does **not** run there: its
Novelty axis (0.40) is what dead-ends a durable topic, and the evergreen evidence floor is enforced
in code instead. Both fleets run with `--workdir /root/editorial-factory` (loads `AGENTS.md` +
`skills/`), `--model deepseek-v4-pro` and `--deliver slack` — the live fleet delivers to the Slack
home channel (`#loop-ai`), which is where the `@Simon approve` gate is read. The `editor` bot
orchestrates: it runs Loops 1–2 on deepseek, then dispatches `stylist`
(`hermes -p stylist chat -q "…"`) for the Claude rewrite (Loop 3). Publishing is not approval-gated
(site + Supabase + the CMS draft persist in the run) and there is no social distribution step: the
LinkedIn/Reddit channel was removed by the owner on 2026-10-06.
`EDITORIAL_CRON_DELIVER` / `EDITORIAL_CRON_MODEL` override the delivery target and model if you
re-wire the fleet onto Bot Chats.

### The seed step, and the gate that proves it ran

`radar` writes `context/recon_proposals/YYYY-MM-DD_<vertical>_signals.md`; the job instruction then
requires `python3 scripts/synthesize_topics.py --seed <that file>`, which writes the file's
`## Candidate Synthesis Pairs` block from its own rows (mechanically validated: `https://` source,
in-window date, Intensity ≥ 60, word-boundary token collisions, archetypes scoped to the registry
vertical) plus a machine-readable `<!-- pair-seeding: … rows=N … -->` marker. The helper never scores
the ≥ 8 gate, and `"no valid pair"` is a legitimate outcome.

Two things keep that step honest without a human:

- `scripts/verify.sh` §8 re-derives that marker's row count against the file itself, so a signals file
  that gained or lost a row after seeding is reported as stale (files written before 2026-09-26 are
  grandfathered). It also runs the regression suites for the helper and this reconciler.
- The **Editorial Verify Gate** cron job (`0 14 * * *`, `--no-agent --script`,
  `~/.hermes/scripts/editorial_verify_gate.sh` → `scripts/cron-verify-gate.sh`) runs `verify.sh` and
  checks that the pressflow image is on HEAD, printing **nothing** when green and a short, actionable
  report to `#loop-ai` when not. A gate nobody runs is documentation; this is the thing that runs it.

> The registry is the source of truth. Adding a vertical there and re-running the script is the
> only supported way to add coverage — hand-created jobs are invisible to `--check` and are the
> drift this section exists to prevent.

> To split the radar sweep into its own cheaper job later, add a `Radar Sweep: <vertical>` cron
> delivering to `bot-chat:radar` and have the pipeline consume `context/recon_proposals/*`.

## 4. Coolify deploy (the site)

1. New application → GitHub repo `kotechile/editorial-factory`, Dockerfile build.
2. Env vars: `PORT=3000` **and `PRESSFLOW_AUTH_SECRET=<long random value>`**.
   `PRESSFLOW_AUTH_SECRET` is not optional: without it `site/server.mjs` answers 503 on every
   non-public route (fail closed). With it, the dashboard requires HTTP Basic auth — any username,
   the value as the password — and **only `/healthz` and a disallow-all `/robots.txt` are reachable
   without it**. PressFlow is an internal dashboard: the articles it holds are exported to the reader
   sites (`giniloh.com` / `wellroost.com`), so serving them here would publish a second, competing
   copy of every article — including the ones still sitting as CMS drafts — on a domain that is not a
   reader surface. `scripts/test_public_surface.mjs` (run by `verify.sh` §10) spawns the real server
   and asserts exactly that surface, including the fail-closed path. Set `SUPABASE_URL` +
   `SUPABASE_SERVICE_ROLE_KEY` **as well**: they are what makes the deployed dashboard's
   persistence work — without them the container runs filesystem-only (`"mocked"` responses on the
   Supabase routes) and nothing it writes survives a redeploy.
3. Domain: e.g. `editorial.<your-domain>` (products ship at subpaths in the factory; this is a
   separate app and can get its own subdomain).
4. Optionally add a production CMS app and point the Publisher at it (`GHOST_API_URL`,
   `GHOST_ADMIN_API_KEY`).
   Publishing is executed via `python3 scripts/publish.py <draft_path>`. There is no LinkedIn /
   Reddit / social configuration — that channel was removed on 2026-10-06.

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
-- Settings & Verticals persistence for PressFlow
create table editorial_verticals (
  id text primary key,
  label text not null,
  cadence text not null,
  target_persona text not null,
  sources jsonb default '[]'::jsonb,
  primary_angles jsonb default '[]'::jsonb,
  is_active boolean default true,
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);
create table editorial_personas (
  id text primary key,
  label text not null,
  reader_level text,
  tone text,
  wants text,
  updated_at timestamptz default now()
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
