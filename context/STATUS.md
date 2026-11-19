# Editorial Factory — Status

**State:** pipeline live (radar → judge → verify → draft → humanize → approve gate), currently switched OFF for articles (`factory_config.generation_control.articles_enabled = false`). Model family: OpenRouter GLM 5.3 (switched 2026-11-19).
**Frontier:** `z-ai/glm-5.3` pinned to OpenRouter's `decart/fp4` endpoint (`OPENROUTER_API_KEY`); cheap tier `z-ai/glm-5.3-flash` pinned to `relace/fp4`. Transport `scripts/frontier_llm.py` (`TEXT_MODEL` / `FLASH_MODEL` / `VISION_MODEL` / `PROVIDER_PINS`). DeepSeek Pro (2026-11-02) and Gemini 3.1 Pro (2026-11-02) both retired for the editorial fleet; Claude-via-kie.ai route retired (401). See skills/claude_humanizer.md §1/§7.

## Next steps (see `docs/VPS_WIRING.md`)
1. Create the 7 bot profiles (`editor`, `radar`, `judge`, `verifier`, `drafter`, `stylist`,
   `publisher`) and mirror each `.agents/*.md` into its SOUL.
3. Register the cron jobs for the calendar cadence above.
4. Create the Coolify app for `site/` and set Supabase/Anthropic env vars.
5. Dry-run one vertical end-to-end before enabling any distribution.
