---
title: "The Tool-List Budget: How Many Tools One Agent Can Hold"
vertical: multi_agent_enterprise_fabric
persona: ai_architect
one_big_thing: "The number of tools an agent holds is an architectural budget, not a convenience: tool selection gets less reliable as the in-context catalogue grows, so the fix is to retrieve a short list per query or split into small specialist agents — a bigger context window and a frontier model do not raise the ceiling."
date: 2026-10-07
slug: agent-tool-count-ceiling
archetype: evergreen
evergreen: true
---

<!-- lead -->
Wiring one agent to a large tool registry can cut its tool-selection accuracy to about one pick in seven. In a stress test on a big catalogue, a plain agent chose the right tool 13.62% of the time. The same setup with retrieval-augmented selection reached 43.13% and used over 50% fewer prompt tokens [1]. The tools never changed. Only the number of tool descriptions that reached the model did.

<!-- tension -->

## The big picture:

Tool choice is a pick from a list, and models get shaky as that list grows. A run of 2025 and 2026 studies on agent tools keeps hitting the same wall, and it reframes a design habit: the tool count is a budget, not a feature list.

The scale is now enormous. A snapshot of the official Model Context Protocol (MCP) registry measured 98,291 tools across its servers [4]. MCP became the common way an agent reaches enterprise systems, and the catalogue behind it is vast.

The hard limits sit far above the point where quality falls. One vendor caps a single request at 128 tools [5]. A large language model (LLM) will accept that many and still choose badly. My read: the ceiling that matters is a design choice, not the one in the vendor's interface.

**Why it matters:** a fabric agent that picks the wrong tool on a write does not fail loudly. It calls a plausible endpoint, returns a plausible result, and moves on.

## By the numbers

- **14% — Selection on a big catalogue:** A plain agent handed a large tool set chose the right tool 13.62% of the time; retrieval-scoped selection lifted that to 43.13% [1].
- **50% — Prompt-token cut:** The same retrieval approach cut prompt tokens by over 50% on an MCP stress test, so a shorter tool list also cost less to run [1].
- **7 tools — Adaptive shortlist:** A depth-aware method matched the coverage of showing 50 tools (90.3% vs 90.8%) while presenting 7 on average, across registries from 20 to 3,251 tools [2].
- **98,291 — Registry catalogue:** A full snapshot of the official MCP registry measured 98,291 tools exposed by its servers, the pool a fabric agent selects from [4].

<!-- tactical-insight -->

## What I'd watch:

What strikes me here is that every fix in the sources is a control on what the model sees, not a bid for a stronger model. The research settles on three families of control.

- **Retrieval-scoped tool lists:** Keep an index of tool descriptions, score them against the request, and pass only the top matches to the model. This is what drove the jump from 13.62% to 43.13% [1].
- **Adaptive shortlist depth:** Let the search go deeper only when a short list misses. On a 3,251-tool registry a fixed list of 5 found nothing on the hard queries, where the deeper search still found 16.7% [2].
- **Smaller specialist agents:** Split one overloaded agent into a few narrow ones with short tool sets. The desk's own field notes put a 42-tool agent at 37% task completion, against three specialists with six tools each reaching 94.8% [6].

The teams closest to this are choosing between a gateway that governs the catalogue and a split into specialists. The first is a platform build; the second is an org chart for agents. I'd watch which one the big vendors ship as the default.

<!-- nuanced-takeaway -->

## The catch

None of this is free, and the numbers have edges. A short list can omit the right tool: on the hard queries in the depth study, a fixed five found nothing at all [2]. Retrieval adds an index to build, keep fresh, and get right.

The measured rates also come from tests, not from live traffic. Read 13.62% as a floor on how bad a big catalogue can be, not as a rate every registry will hit.

My read is that the pattern holds even as the exact figures move. A model choosing among many described tools does worse than one choosing among few. I could be wrong about where the line sits for a given registry. But handing an agent a hundred tools and hoping attention sorts it out is not a design I would defend.

<!-- tldr -->

## At a glance

- **The Big Shift:** An agent's tool count is now a design budget. Tool selection gets less reliable as the in-context catalogue grows, and retrieval-scoped lists or small specialist agents are the current answers.
- **Why It Matters:** A fabric agent that picks the wrong tool on a write fails quietly. It calls a plausible endpoint, returns a plausible result, and the mistake surfaces later.
- **What I'd Watch:** Whether teams bound the catalogue the way they bound a schema. The controls in the evidence split three ways:
  - **Retrieval-scoped lists:** An index scores tools against each request and passes only the top matches to the model.
  - **Adaptive shortlist depth:** The search goes deeper only when a short list misses the right tool.
  - **Specialist agents:** One overloaded agent split into a few narrow ones, each holding a short tool set.
- **The Catch:** A short list can omit the right tool entirely, and retrieval adds an index to build and keep fresh. The rates come from tests, not live traffic.

## Sources
[1] Tiantian Gan and Qiyao Sun, "RAG-MCP: Mitigating Prompt Bloat in LLM Tool Selection via Retrieval-Augmented Generation" (arXiv:2505.03275, submitted 2025-05-06) — the MCP stress test: tool-selection accuracy 43.13% vs a 13.62% baseline, prompt tokens cut by over 50% (https://arxiv.org/abs/2505.03275)
[2] Vyzantinos Repantis, Ameya Gawde, Harshvardhan Singh and Joey Blackwell II, "How Many Tools Should an LLM Agent See? A Chance-Corrected Answer" (arXiv:2605.24660, v2 2026-06-07) — BFCL (370 tools) learned depth matches showing 50 tools (90.3% vs 90.8%) at 7 shown on average; ToolBench (3,251 tools) a fixed 5 gets 64.7% vs 61.9% coverage but nothing on hard queries, against 16.7% for the deeper search; 93.1% vs 87.1% with Claude Sonnet 4.6 (https://arxiv.org/abs/2605.24660)
[3] Dennis Thompson, "When too many tools become too much context", WRITER engineering — the RAG-MCP team's own writeup: retrieval "more than triples tool-selection accuracy and reduce prompt tokens by over 50%", inside an enterprise MCP Gateway that governs and scales the tool catalogue (https://writer.com/engineering/rag-mcp)
[4] Artem Trofimov and Boris Novikov, "When Tool Calls Succeed but Workflows Fail: Anomalies at the Agent-Tool Boundary" (arXiv:2609.15397, submitted 2026-09-14) — the official MCP registry snapshot measured 98,291 tools exposed by registered servers (https://arxiv.org/abs/2609.15397)
[5] OpenAI Developer Community, "Maximum amount of tools for the bot to use?" — the documented vendor cap: "an array of a maximum of 128 functions" per request (https://community.openai.com/t/maximum-amount-of-tools-for-the-bot-to-use/665720)
[6] Field notes — context/growth_os/founder-voice.md §`multi_agent_enterprise_fabric` ("Bound autonomous agents to lean, decoupled tool sets (≤ 8 per agent)") and context/growth_os/customer-truth.md Anecdote 2 (a dispatch agent with 42 tools: 63% parameter hallucination, 37% task completion; three specialists at ≤ 6 tools each: 94.8%)
