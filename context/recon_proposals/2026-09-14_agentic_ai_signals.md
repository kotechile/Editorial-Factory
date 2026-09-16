# Signals: agentic_ai — 2026-09-14

**Window:** 2026-08-15 → 2026-09-14
**Queries run:** 12

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | OpenAI launched the Agents API in public beta: the Codex harness (model-and-tool loop) becomes a managed runtime — orchestration, long-running sessions, context management, crash recovery — with no extra fee beyond tokens/tools | https://community.openai.com/t/introducing-the-agents-api-and-hosted-sandboxes/1396481 | 2026-09-10 | "We handle orchestration, long-running sessions, and context management. You focus on what makes your agent unique."; "no additional fees"; "OpenAI runs the agent loop on its infrastructure" | distributed runtime / deterministic RPC boundaries / subagent cost | 94 |
| 2 | The API abstracts an agent into four concepts — Agent (model, instructions, tools, MCP servers), Environment (optional sandbox), Session (durable instance), Events and items (inputs/outputs) | https://developers.openai.com/api/docs/guides/agents-api/overview | 2026-09-10 | four named primitives; session "retains session state so you can continue work across turns" | runtime architecture / protocol fabric | 88 |
| 3 | Sub-agent coordination is a config flag, not a framework: `multi_agent: {enabled: true, max_concurrent_subagents: N}` plus automatic context compaction | https://developers.openai.com/api/docs/guides/agents-api/overview | 2026-09-10 | `max_concurrent_subagents`; compaction/context handling managed by the runtime | multi-agent coordination modes / subagent cost | 82 |
| 4 | Sandbox is a per-task choice: OpenAI-hosted sandboxes or self-hosted (bring-your-own VPC), with first-class integrations to Blaxel AI, Cloudflare Dev, Daytona, DigitalOcean, E2B, Modal, Oracle Cloud, Runloop AI, Vercel | https://community.openai.com/t/introducing-the-agents-api-and-hosted-sandboxes/1396481 | 2026-09-10 | nine named partner integrations; "CPU, GPU, and memory options"; "deployments within your VPC" | distributed microservices architecture | 76 |
| 5 | OpenAI reported its research org now runs 3.1 agent-workdays of coding-agent effort per human workday, but more than half of successful 4–8 hour agent tasks still need human intervention | https://www.explainx.ai/blog/openai-research-acceleration-coding-agents-september-2026 | 2026-09-06 | 3.1 agent-workdays : 1 human workday; >50% of long tasks need human intervention | subagent cost / human-in-the-loop | 72 |
| 6 | Anthropic's Claude Developer Platform added auto permission policies for Managed Agents (server evaluates each agent/MCP tool call: run, deny, or pause for approval) and beta sessions-connect terminal attach | https://releasebot.io/updates/anthropic | 2026-09-10 | per-call auto permission policy; deny/pause/approve | deterministic RPC boundaries / permission gate | 74 |
| 7 | Adversa flagged malicious MCP tool servers inducing cyclic "overthinking loops" that amplify token consumption up to 142.4× (denial-of-wallet) | https://adversa.ai/blog/top-mcp-security-resources-march-2026 | 2026-09-07 | 142.4× token amplification; denial-of-wallet | tool use / cost attack surface | 78 |

**Dropped — outside 30-day window (freshness rule):**
- MemTier tiered-memory / retrieval-bottleneck paper (arXiv:2605.03675) — May 2026.
- MCP 2026-07-28 "stateless core" spec revision — July 28, precedes window start.
- NSA MCP "Security Design Considerations" CSI — May 20, 2026.
- LLM Agent Failure Taxonomy synthesis (arXiv:2607.05775) — July 2026.
- Salesforce UK Connectivity Report — vendor survey, thin primary authority; intensity < gate.

**Dropped — intensity < 60:** none.
