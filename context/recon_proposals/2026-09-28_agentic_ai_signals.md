# Signals: agentic_ai — 2026-09-28

**Window:** 2026-08-29 → 2026-09-28
**Queries run:** 21

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | OpenAI GPT-6 prompt caching for persistent agents | https://openai.com/index/better-prompt-caching-for-gpt-6 | 2026-09-22 | "GPT-6 enables persistent agents to work for hours"; discounts of up to 90% on cached input tokens; cache discounts for shared prefixes reused within a 30-minute window; new Prompt Caching Dashboard + miss diagnostics; cache breakpoints; reasoning-effort changes without breaking cache (`configuration_update`); guidance to "keep tool definitions, schemas, and ordering stable so earlier context stays reusable" | subagent cost optimization + deterministic RPC boundaries | 78 |
| 2 | GitHub Copilot: cache cut fresh-processing tokens >50% | https://techxmedia.com/en/openai-improves-prompt-caching-for-gpt-6-agents | 2026-09-22 | GitHub CPO Mario Rodriguez: caching "reduced the share of prompt tokens requiring fresh processing by more than 50% across billions of requests" | subagent cost optimization (corroboration) | 64 |
| 3 | AGNTCon + MCPCon Europe production-reality recap | https://lucaberton.com/blog/agntcon-mcpcon-europe-2026-media-partner | 2026-09-17 | Media-partner recap: "81% have agents in production, MCP hits 89% adoption, AGENTS.md at 60k repos" — shift from demos to reliability | multi-agent coordination / MCP fabric (secondary) | 58 |
| 4 | SIGARCH: multi-agent memory as a computer-architecture problem | https://www.sigarch.org/multi-agent-memory-from-a-computer-architecture-perspective-visions-and-challenges-ahead | 2026-01-20 | Agent memory framed as cache / I/O / memory hierarchy; shared vs distributed memory; consistency models (sequential, TSO, release) | memory tiering (OUT OF WINDOW) | 34 |
| 5 | Google+MIT "Towards a Science of Scaling Agent Systems" | https://arxiv.org/html/2512.08296v1 | 2025-12 | 180 configs; centralized +80.9% on parallelizable; sequential planning −39–70%; error amplification 17.2× vs 4.4× | multi-agent coordination (OUT OF WINDOW) | 32 |
| 6 | MCP 2026-07-28 stateless-first spec | https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate | 2026-07-28 | Stateless protocol layer; `initialize` handshake removed; `Mcp-Method`/`Mcp-Name` headers; Streamable HTTP | MCP fabric (OUT OF WINDOW) | 30 |

**Notes:**
- Only signal #1 clears the Intensity-60 floor AND is on-vertical, primary-source, and in-window. Signal #2 is a same-day quantitative corroboration (GitHub Copilot) of #1's cost claim, not an independent leg.
- Signal #3 is in-window but a secondary media-partner conference recap (soft figures, no named primary survey).
- Signals #4–6 are listed for de-dup transparency only — all OUT of the 30-day window and dropped per `radar_30day.md` §3 Stage 1 (SIGARCH Jan 20; Google+MIT Dec 2025; MCP stateless spec Jul 28). They are the tempting synthesis legs but fail the freshness gate.
- Window has advanced only ~4 days since the 2026-09-24 agentic_ai run (MASkills winner). Fresh acute signals are scarce by design; the vertical is event-driven, and the one fresh event is #1.
- Prior-cycle de-dup (from 09-24 brief): OpenAI Agents API (09-14), MCP Skills Extension (09-21), MASkills (09-24) are all distinct from a prompt-caching / persistent-state-cost thesis.

## Candidate Synthesis Pairs


<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=6 candidates=0 heuristic=- window=2026-08-29..2026-09-28 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->

