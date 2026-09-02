# Editorial Factory — Status

**State:** scaffolded, not yet wired to the VPS fleet.
**Frontier key:** `ANTHROPIC_API_KEY` **missing** — the Claude rewrite gate will halt until added.

## Next steps (see `docs/VPS_WIRING.md`)
1. Add `ANTHROPIC_API_KEY` (or an OpenRouter route) to the gateway env.
2. Create the 7 bot profiles (`editor`, `radar`, `judge`, `verifier`, `drafter`, `stylist`,
   `publisher`) and mirror each `.agents/*.md` into its SOUL.
3. Register the cron jobs for the calendar cadence above.
4. Create the Coolify app for `site/` and set Supabase/Anthropic env vars.
5. Dry-run one vertical end-to-end before enabling any distribution.
