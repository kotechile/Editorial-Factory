# Signals: agentic_ai — 2026-09-17

**Window:** 2026-08-18 → 2026-09-17
**Queries run:** 21 (web_search + web_extract across arxiv, hacker_news, vendor newsrooms, protocol/spec sources)

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | Salesforce researchers (arXiv preprint) found evolving the agent "harness" around a smaller Qwen model lifted mean task success from 29.2% to 78.0% across seven enterprise-agent benchmarks without changing model weights; imitation fine-tuning to a stronger model DROPPED it to 63.1%; on-policy correction recovered 79.7% | https://arxiv.org/abs/2609.09134 | 2026-09 (v1) | 29.2%→78.0% (+48.8 pts); 78.0%→63.1% regression; →79.7% recovery | deterministic RPC boundaries / distributed microservices architecture | 95 |
| 2 | Salesforce Enterprise AI Harness (announced Sep 11) productizes the finding: "six capabilities spanning context, agency, action, governance, security, and models, delivered through a common, composable architecture" + an AI Control Plane | https://www.salesforce.com/ap/news/press-releases/2026/09/11/salesforce-introduces-the-trusted-enterprise-ai-harness | 2026-09-11 | six capabilities; "AI reasoning can be open-ended, but enterprise execution often cannot" | deterministic RPC boundaries / multi-agent coordination | 92 |
| 3 | Headless 360 MCP Server (Aug 19) lets "agents running in Agentforce, Claude, ChatGPT, Cursor, and other AI platforms to dynamically discover, understand, and invoke Salesforce capabilities in real time" | https://www.salesforce.com/news/stories/expanding-headless-360-enterprise-capabilities | 2026-08-19 | MCP server; cross-platform dynamic discovery | tool use / MCP protocol fabric | 88 |
| 4 | Salesforce + Google Cloud (Sep 15): Salesforce's headless architecture connects to Gemini Enterprise "built on MCP open standard" — "agents on either platform can reason and act upon the same data without custom integrations" | https://www.salesforce.com/news/stories/salesforce-google-cloud-unify-infrastructure-and-agents | 2026-09-15 | native MCP interoperability | tool use / MCP protocol fabric | 88 |
| 5 | Salesforce + AWS (Sep 15): Informatica MCP servers accessible from Bedrock AgentCore + Amazon Quick; agent-to-agent handoff between Amazon Connect and Agentforce Voice | https://www.salesforce.com/news/stories/aws-salesforce-enterprise-ai-expansion/ | 2026-09-15 | cross-vendor agent-to-agent + MCP | multi-agent coordination / MCP fabric | 80 |
| 6 | Koa: Salesforce's first CRM reasoning model on NVIDIA Nemotron — "matches or exceeds leading model performance on CRM actions with 3x fewer errors"; no customer data used to train | https://www.salesforce.com/news/press-releases/2026/09/15/koa-reasoning-model/ | 2026-09-15 | 3x fewer errors; synthetic-only training corpus | subagent cost / model economics | 78 |
| 7 | AIforce (Sep 15) — "AI Replaces the UI": a live interface layer (Claudeforce, Slackforce, Agentforce Coworker) over the Headless Toolkit (MCPs, APIs, skills) | https://www.salesforceben.com/salesforce-launches-aiforce-at-dreamforce-26-ai-replaces-the-ui | 2026-09-15 | permission model = security boundary | distributed microservices architecture | 76 |
| 8 | Enterprise AI Harness caveat: not GA; "new capabilities and the unified experience" expected Q1 FY 2028 | https://thelettertwo.com/2026/09/10/salesforce-trusted-enterprise-ai-harness-dreamforce-2026 | 2026-09-10 | Q1 FY2028 GA | (caveat) | 65 |

**Dropped — outside 30-day window (freshness rule):**
- MCP 2026-07-28 "stateless core" spec (Cloudflare MCP v2) — July 28, precedes window start.
- Google A2A → Agentic AI Foundation (AAIF) governance transfer (Aug 17–20) — near-window-edge governance story; already scored N=7 S=6 as a runner-up on 2026-09-10 (retread per virality_judge §3.5).
- Princeton HAL "scaffold gap" (scaffold +30 pts on GAIA) — load-bearing leaderboard data April/May 2026, out of window.
- Camunda 2026 State of Agentic Orchestration report — January 2026, out of window.
- Memory-tiering papers (arXiv:2607.21503 Jul 23; 2606.24775 Jun; 2603.07670 Mar) — out of window.
- Rubrik MCP (Sep 15) — single-vendor MCP support, "table stakes" (same class as Nutanix MCP, rejected N=5 on 09-03).
- Cloudflare "agentic internet" content rules (Sep 15) — publisher-crawler governance, off-angle for ai_architect.

**Dropped — intensity < 60:** none.
