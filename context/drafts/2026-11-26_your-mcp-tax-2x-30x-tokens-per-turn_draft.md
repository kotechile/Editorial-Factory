---
title: Your MCP Bill Grows 2x–30x Per Server
vertical: agentic_ai
kind: evergreen
archetype: evergreen
evergreen: true
persona: ai_architect
one_big_thing: "Mounting MCP servers the default way re-bills their full tool schemas on every turn, measured at 2x–30x prompt inflation. Retrieving the few tools a query needs cuts that payload by 99.6%."
date: 2026-11-26
slug: your-mcp-tax-2x-30x-tokens-per-turn
---

<!-- lead -->
Every MCP server an agent mounts adds to the bill. Model Context Protocol (MCP) is the hub-and-spoke layer that connects a model's tool calls to outside services, and measured agents show its calls inflate prompt tokens by 2x–30x over plain chat [1]. That wiring is a choice, not a fee anyone has to accept. One measured fix cut tool tokens by 99.6% and still found the right tool 97.1% of the time [2].

<!-- tldr -->
## At a glance

For teams running agents against several MCP servers, the full tool list sitting in the model's context is the runtime's biggest hidden cost. New studies price that tax and show that fetching only the tools a query needs clears almost all of it.

<!-- tension -->
## Why Every Turn Re-bills

MCP sets one way for a host to find and call tools. It says nothing about where their definitions live during a run. The chat APIs underneath keep no memory of earlier requests.

So the host client — Claude Code, Cursor, or your own runtime — copies the whole tool catalog into every request [4]. One measured study traced OpenRouter traffic and ran Cline (an open-source coding agent host) against live servers. It found prompt size grows with each tool you enable. Both Cursor and Cline now cap active tools at 40 [1]. Long multi-step runs pay it hardest, and so does code work already close to the model's size limit. What I find hard to square is that the protocol's own strength — many servers, easy to mount — is what multiplies the payload it carries.

## By the numbers

- **2x–30x prompt inflation.** MCP interactions versus plain chat, across nine frontier LLMs [1].
- **54.6k tokens per turn.** A 106-tool enterprise database catalogue's schema payload [4].
- **99.6% fewer schema tokens.** With the right tool still retrieved 97.1% of the time [2].

<!-- tactical-insight -->
## How Teams Move the Payload

What I find striking is how production teams decouple this in two directions, and both now have numbers behind them. The first is retrieval over the catalog instead of mounting it. A vector index (a similarity search) over tool text fetches only the tools a query needs.

One study pulled 10 tools from a set of 121. At a K of 3 (how many tools the retriever returns), this cut tool-related tokens by 99.6% [2]. The right tool ranked first 97.1% of the time, and retrieval stayed under 91ms at every setting tested [2]. My read is that the two paths compound: retrieval trims what enters the window, and a sandbox trims what comes back.

The second direction is a sandbox. The agent writes one small program that calls the tools. Schemas and intermediate output run inside that program, and only the final result returns to the model [4].

The schema text also needs curation, because sloppy wording steers the model wrong. A scan of 856 tool texts across 103 servers found 97.1% with at least one defect, and 56% never stating their purpose [3]. Fully rewriting that text bought a median 5.85 points of task success, but it cost 67.46% more execution steps [3]. Targeted fixes beat full rewrites for that reason. The [tool surface release practices](/your-tool-surface-is-a-release-surface/) teams already run for security apply here too: version them, review them, and stop letting them drift per mount.

<!-- nuanced-takeaway -->
## The Catch

Each fix gives something back, though. Retrieval's hit rate, measured across all its test queries, still falls short of perfect. A missed tool on a critical path means a failed run, not just a smaller bill. A sandbox moves untrusted tool output into runnable code, so an injected response gains power and needs guardrails of its own [4]. And description rewrites cost steps: the 5.85 points of task success arrived with 67.46% more steps, which is why the rewrite must stay narrow [3].

My read is that mounting the full list should become a planned exception, priced against the 10k–60k tokens per turn that field reports compile [4], rather than the default each new server inherits without a word.

## Sources

- [1] Hu et al., "Network and Systems Performance Characterization of MCP-Enabled LLM Agents" (arXiv:2511.07426v1) — https://arxiv.org/html/2511.07426v1
- [2] "Semantic Tool Discovery for Large Language Models: A Vector-Based Approach to MCP Tool Selection" (arXiv:2603.20313v1) — https://arxiv.org/html/2603.20313v1
- [3] "Model Context Protocol (MCP) Tool Descriptions Are Smelly! Towards Improving AI Agent Efficiency with Augmented MCP Tool Descriptions" (arXiv:2602.14878v1) — https://huggingface.co/papers/2602.14878
- [4] "Tool Attention Is All You Need: Dynamic Tool Gating and Lazy Schema Loading for Eliminating the MCP/Tools Tax in Scalable Agentic Workflows" (arXiv:2604.21816v1) — https://arxiv.org/html/2604.21816v1
