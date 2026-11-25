# Signals: multi_agent_enterprise_fabric — 2026-11-25
**Window:** 2026-10-26 → 2026-11-25
**Queries run:** 7 arXiv API + 7 HN Algolia + web (Google Workspace, Reddit corroboration)

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | Google mandates MCP for all agent access to Workspace | https://workspaceupdates.googleblog.com/2026/11/mcp-servers-cli-standardized-usage-tiers-now-available.html | 2026-11-24 | "AI agents or similar access tools must use MCP to access Workspace data, rather than calling Workspace REST APIs directly. Technical enforcement begins on February 1, 2027." Scaled tier billing starts April 1, 2027; over 99% of active developers sit in the Standard tier (no cost). New Workspace AI Tools Addendum, admin-console agent access management, HITL confirmations, DLP + audit logging. | ERP/SaaS event-driven integration bus (governance hammer ⨂ integration architecture) | 95 |
| 2 | Measurement: ad-serving MCP servers, disclosure failure | https://arxiv.org/html/2611.28911v1 | 2026-11-21 | Census of 101,363 open remote MCP endpoints and 122,656 local packages: 579 endpoints (0.57%) show ad evidence, 226 return ads in query results, only 52 packages (0.04%) serve ads. Only 9.3% of ads carry an explicit sponsored label; operators (not the 173 identified ad networks) place ads themselves on 117 of 226 servers; 48 of 52 ad-serving packages carry the operator's own affiliate ID. Proposes per-item ad annotation in MCP results. | MCP anti-corruption layer / context poisoning | 90 |
| 3 | Measurement: tool-provider misbinding in MCP | https://arxiv.org/html/2611.21577v1 | 2026-11-16 | Tool names are not provider identities. Across 5 LLM clients (GPT-5.4, Claude Sonnet 5, Gemini 2.5 Pro, Qwen3.7 Max, DeepSeek V3), 50 trials per model per condition: with exact name collision + copied description + compatible schema (C10), non-legitimate resolution hits 1.00 for GPT-5.4/Qwen3.7 Max/DeepSeek V3 and 0.84 for Gemini 2.5 Pro. Authority-enhanced descriptions with compatible schema (C06) also misresolve without name collision (Gemini 2.5 Pro VR 0.42). | MCP anti-corruption layer / trust boundaries | 85 |
| 4 | Measurement: recovery in 50 agent harnesses and runtimes | https://arxiv.org/html/2611.27090v1 | 2026-11-20 | Under a pre-registered protocol, 12 persistent runtimes, 26 coding-agent harnesses, 12 research runtimes graded on 8 recovery mechanisms. 11/12 runtimes and 25/26 harnesses have real-use evidence, but of 128 such reports only 19 describe full recovery; 54 partial, 45 failed. Checkpoint/resume recovered in 1 of 27 reports; rollback in 1 of 15. Research runtimes' saga-style compensation is benchmarked, never exercised in production. | Distributed saga patterns and multi-agent rollbacks / compensating transactions | 85 |
| 5 | Real-world hit: Notion's official MCP injects ads, masks tracking link | https://www.reddit.com/r/ClaudeCode/comments/1y4qm5o/heads_up_if_you_wire_notions_official_mcp_into/ | 2026-11-25 | User report that Notion's official MCP server injects promotional content into tool results and masks the tracking link — first-party vendor behavior, corroborating signal #2's 117/226 operator-placed finding. (Community report, not a vendor disclosure; used as friction, not as a measured anchor.) | MCP context poisoning | 65 |
| 6 | Production-agent platform layer consolidating | https://news.ycombinator.com/item?id=50549188 | 2026-11-18 | Launch HN: Maritime (YC F26) — a managed cloud for production AI agents; 60 points, 67 comments. The market is building managed operational fabrics (state, retries, spend limits) for exactly the failure modes signals #3 and #4 document. (Launch thread, market context.) | Durable execution / orchestration market shift | 65 |

**Dating note:** All six rows are dated from the publisher's own fields (Blogger feed `published` for row 1: 2026-11-24T09:02:59-08:00; arXiv `<published>` for rows 2–4; HN/Reddit `created_at` for rows 5–6). No status-page or event-dated rows.

## Candidate Synthesis Pairs

<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=6 candidates=4 heuristic=0.95-0.98 window=2026-10-26..2026-11-25 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

| Pair | Signals | Shared axis | Contrasting axis | Anchor URLs | Heuristic | Flags |
|---|---|---|---|---|---|---|
| 1 | #1 ⨂ #2 | governance_x_runtime | A: ERP/SaaS event-driven integration bus (governance hammer ⨂ integration architecture) | B: MCP anti-corruption layer / context poisoning | https://workspaceupdates.googleblog.com/2026/11/mcp-servers-cli-standardized-usage-tiers-now-available.html https://arxiv.org/html/2611.28911v1 | 0.98 | - |
| 2 | #1 ⨂ #3 | governance_x_runtime | A: ERP/SaaS event-driven integration bus (governance hammer ⨂ integration architecture) | B: MCP anti-corruption layer / trust boundaries | https://workspaceupdates.googleblog.com/2026/11/mcp-servers-cli-standardized-usage-tiers-now-available.html https://arxiv.org/html/2611.21577v1 | 0.97 | - |
| 3 | #1 ⨂ #5 | governance_x_runtime | A: ERP/SaaS event-driven integration bus (governance hammer ⨂ integration architecture) | B: MCP context poisoning | https://workspaceupdates.googleblog.com/2026/11/mcp-servers-cli-standardized-usage-tiers-now-available.html https://www.reddit.com/r/ClaudeCode/comments/1y4qm5o/heads_up_if_you_wire_notions_official_mcp_into/ | 0.95 | - |
| 4 | #1 ⨂ #6 | governance_x_runtime | A: ERP/SaaS event-driven integration bus (governance hammer ⨂ integration architecture) | B: Durable execution / orchestration market shift | https://workspaceupdates.googleblog.com/2026/11/mcp-servers-cli-standardized-usage-tiers-now-available.html https://news.ycombinator.com/item?id=50549188 | 0.95 | - |

**Heuristic terms (advisory):**
- #1: token_coverage=1.0 intensity=0.93 angle_fit=1.0 contrast=1.0 → 0.98 (governance_x_runtime)
- #2: token_coverage=1.0 intensity=0.9 angle_fit=1.0 contrast=1.0 → 0.97 (governance_x_runtime)
- #3: token_coverage=1.0 intensity=0.8 angle_fit=1.0 contrast=1.0 → 0.95 (governance_x_runtime)
- #4: token_coverage=1.0 intensity=0.8 angle_fit=1.0 contrast=1.0 → 0.95 (governance_x_runtime)
<!-- synthesis-seed:end -->

## Dated background
- https://benchmarks.bespokelabs.ai/multi-agent-coordination-bench/ — Bespoke Labs Multi-Agent Coordination Benchmark (2026-11-18)
- https://arxiv.org/html/2611.31063v1 — From Local Errors to System Failures: error propagation in multi-agent LLM systems (2026-11-23)
- https://arxiv.org/html/2611.27095v1 — Epistemic Guard: out-of-process MCP receipt proxying, post-turn prose supervision (2026-11-20)
- https://arxiv.org/html/2611.24839v1 — Kaer: security-aware replanning for multi-agent systems (2026-11-18)
- https://arxiv.org/html/2611.21259v1 — Evaluating authorization and trust boundaries in agentic orchestration frameworks (2026-11-16)
- https://arxiv.org/html/2611.06967v1 — Call-level revision contracts for LLM-authored workflows (durable execution) (2026-11-04)
