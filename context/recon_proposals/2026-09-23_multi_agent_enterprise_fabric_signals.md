# Signals: multi_agent_enterprise_fabric — 2026-09-23

**Window:** 2026-08-24 → 2026-09-23
**Queries run:** 12 (durable execution, saga/compensating transactions, MCP anti-corruption layer, ERP event bus, tool-schema bloat, multi-agent orchestration — arxiv + vendor + news)

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | Temporal raises $550M Series E at $12.55B valuation, led by Lightspeed | https://temporal.io/blog/temporal-raises-usd550m-series-e-at-usd12-55b-valuation-ai | 2026-09-14 | $550M at $12.55B; 1.9T actions in Aug (+350% YoY); 43M OSS installs (+134% since Dec); 4,300+ paying customers (+139% YoY); ARR run-rate +200% YoY; NDR >200% | Durable execution state persistence as the enterprise multi-agent fabric | 95 |
| 2 | Temporal Agent Harness (early look) — durable infrastructure around agent SDKs | https://temporal.io/blog/temporal-agent-harness-durable-agent-infrastructure | 2026-08-20 | Every agent = a Temporal Workflow; "seam between the model deciding to use a capability and that capability actually executing"; integrates Gemini / OpenAI Agents SDK / PydanticAI | Durable execution + control seam (anti-corruption layer) | 78 |
| 3 | Diagrid Catalyst 2.0 — agentic durable execution + cryptographic verification | https://www.diagrid.io/blog/what-is-agentic-durable-execution | 2026-09-04 | Agentic durable execution: recover from failure + tamper-proof record of every step | Durable execution + verifiable audit provenance | 65 |
| 4 | Union.ai Flyte — "Durable Execution for Any AI Agent Framework" | https://www.union.ai/blog-post/durable-execution-for-any-ai-agent-framework | 2026-08-31 | Completed model turns replay without re-calling the model; completed tools return from cache | Durable execution across agent frameworks | 62 |
| 5 | Mnemosyne: Agentic Transaction Processing (ATP) — validating/repairing AI-generated workflows | https://arxiv.org/html/2607.00269v3 | 2026-07 (v3 + GitHub artifact Aug 2026) | ATP enforces 5 semantic contracts; deterministic gate admits actions; saga compensation; compared vs LangGraph/Cadence/Temporal | Distributed saga patterns + compensating transactions | 68 |
| 6 | Agentic AI Foundation launches MCPA certification (MCP expertise) | https://aaif.io/projects/model-context-protocol | 2026-09-15 | MCPA certification to validate MCP expertise; MCP governance standardization | MCP anti-corruption layer / governance | 60 |

**Notes:** Signals 1–2 are primary (vendor announcement + press release). Signal 5 (Mnemosyne/ATP) is a strong topical match but its arXiv anchor is July 2026 (outside window); the August GitHub reproducibility artifact only partially pulls it back in — flagged as out-of-window for freshness, usable as corroboration only.
