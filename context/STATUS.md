# Editorial Factory — Status

**State:** scaffolded; frontier key wired (Claude via kie.ai). Fleet + cron not yet created.
**Frontier key:** `ANTHROPIC_API_KEY=Bearer <kie.ai key>` set in both `~/.hermes/.env` (laptop) and `/root/.hermes/.env` (VPS). Routes Claude via `https://api.kie.ai/claude` (model `claude-fable-5`).

## Next steps (see `docs/VPS_WIRING.md`)
1. Create the 7 bot profiles (`editor`, `radar`, `judge`, `verifier`, `drafter`, `stylist`,
   `publisher`) and mirror each `.agents/*.md` into its SOUL.
3. Register the cron jobs for the calendar cadence above.
4. Create the Coolify app for `site/` and set Supabase/Anthropic env vars.
5. Dry-run one vertical end-to-end before enabling any distribution.
