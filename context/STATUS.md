# Editorial Factory — Status

**State:** pipeline live (radar → judge → verify → draft → humanize → approve gate). Frontier now DeepSeek Pro.
**Frontier:** stylist profile `provider: deepseek`, `model: deepseek-v4-pro` (`DEEPSEEK_API_KEY`); transport `scripts/frontier_llm.py`. Gemini 3.1 Pro billing retired 2026-11-02. Claude-via-kie.ai route retired (401). See skills/claude_humanizer.md §1/§7.

## Next steps (see `docs/VPS_WIRING.md`)
1. Create the 7 bot profiles (`editor`, `radar`, `judge`, `verifier`, `drafter`, `stylist`,
   `publisher`) and mirror each `.agents/*.md` into its SOUL.
3. Register the cron jobs for the calendar cadence above.
4. Create the Coolify app for `site/` and set Supabase/Anthropic env vars.
5. Dry-run one vertical end-to-end before enabling any distribution.
