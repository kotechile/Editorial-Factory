---
title: "29 Distilled Guidelines Beat All 199 — Pick Your Memory Tier"
vertical: agentic_ai
kind: news
archetype: news
synthesis: true
persona: ai_architect
one_big_thing: "Three papers landed in one week showing agent memory is a solved engineering problem — a model does better with 29 distilled guidelines than with all 199, and a plain-text log with search beats every structured memory stack — while the MCP tool fabric those guidelines describe changed under 25% of registry hosts in the last 30 days and 11% miss a daily check in ten: the effort is pouring into the closed half while the churning half has no change feed."
date: 2026-11-23
slug: your-memory-tier-is-solved-29-of-199
meta_title: "29 Distilled Guidelines Beat All 199 — Pick Your Memory Tier"
meta_description: "A model beat itself using 29 distilled guidelines instead of all 199 — the same week a quarter of MCP registry hosts changed a tool. The memory tier is closed; the tool fabric is not."
primary_keyword: "memory tier"
sources:
  - https://arxiv.org/abs/2611.26361
  - https://nestdaddy.com/blog/state-of-remote-mcp-servers-2026
image_path: "context/assets/illustrations/your-memory-tier-is-solved-29-of-199/featured.jpg"
image_style: "cinematic_still"
image_model: "flux"
image_alt: "Agent Memory Is Solved, Tools. Printed guideline cards stacked under a desk lamp in a dark control room, a server blade half-pulled from"
image_caption: "Agent Memory Is Solved, Tools: Three papers settle agent memory the same week a quarter of MCP hosts changed a tool."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
A model given 29 distilled guidelines beat the same model given all 199 — 55.4% against 51.2% on task completion [1]. That memory system shipped to production the same week [1]. And a daily audit of the Model Context Protocol (MCP) registry — the protocol that lets agents call tools on remote hosts — reported that a quarter of its remote hosts had rewritten at least one tool in the last 30 days, and that 11% stop answering at least one day in ten [2]. The memory side of an agent's architecture just resolved into simple answers, because three teams measured it directly. The tool side those memories describe is still moving underneath them.

<!-- tldr -->

## At a glance

Three papers published in one week give architects building long-horizon agents a direct answer on memory: distill to a model's own subset, or drop the stack and search a plain log. The open problem is now the tool fabric those memories describe.

<!-- tension -->

## The week memory closed

The production paper is a deployment record [1]. Its code mines short lessons from an agent's own failed runs, folds them into guidelines, and hands the agent either all of them or a chosen subset. The result inverts the usual instinct about more. One strong model keeps improving with the full 191-guideline set, gaining 9.5 points of task completion [1]. The study's weaker model starts at 39.9%. Give it all 199 guidelines and it hits 51.2%; give it a chosen 29 and it reaches 55.4% [1]. The paper's own line is the finding: the right amount of memory is a property of the model, not the memory.

Two more papers landed in the same week. GrepMem trains an agent to keep a plain-text log of everything it has seen and recall with a text search — no embeddings, no index, no extra models — and scores 95–97% where the best lossy baseline it compares against reaches at most 21% [3]. MemFolder folds a memory store in half: 99.0% of the original performance held across three text benchmarks with 50% fewer records [4]. Three independent teams, one week, same direction: smaller, simpler, self-distilled.

| System | Where the state lives | What it drops | Measured result |
|---|---|---|---|
| Distilled guidelines [1] | Short rules mined from the agent's own failed runs | Nothing kept; only which subset is sent | 55.4% with 29 rules vs 51.2% with all 199 (mean of two runs) |
| GrepMem [3] | An append-only plain-text log, searched with regex | Nothing — lossless by design | 95–97% vs at most 21% for the best lossy baseline |
| MemFolder [4] | Fewer, folded records in a memory store | Half the records, not the evidence | 99.0% of performance kept with 50% fewer records |

I have been watching this debate since October, when the honest advice was that the memory tier — how you split state between a context window and outside stores — decided whether long tasks succeeded; this desk priced it then as [long context is not memory, why agents need tiered state](/agent-memory-tiering-l1-l4/). That advice had a shelf life, and this week dated it. The tier itself no longer loses much. A log and a search beat a retrieval stack, and half the records cost nothing to answer with.

But the guidelines the winning systems distill are snapshots. They are prose about how a given tool behaves, mined from runs against given hosts. The audit measures what happens to those hosts: 25.1% rewrote at least one tool in the last 30 days, and 86.8% answered every daily check — so 11.0% missed at least one in ten [2]. The audit's scale is the public registry itself: 322,242 tools across 22,576 hosts, median first answer 253 milliseconds [2]. The report's own framing is blunt: an agent that learned your tools last week can break when a name or an input changes silently [2].

I read the two measurements as one call. A guideline that says "call tool X to paginate" is true as of the day it was mined. With a quarter of hosts changing tools each month, a guideline is a cache entry with no expiry field. The failure does not arrive as an error — the agent calls the renamed tool, gets a plausible result, and reports done. Nothing in the memory code re-checks it, because its whole job is deciding what to keep, not whether the world still matches.

## By the numbers

- A 29-rule subset beat the same model's full set of 199, 55.4% to 51.2% on task completion [1].
- 25.1% of registry hosts changed at least one MCP tool in the last 30 days [2].
- 11.0% of remote hosts answered fewer than nine of ten daily checks [2].

<!-- tactical-insight -->

## Where this bites

The teams closest to the story have already moved. The production paper's code is live in a commercial agent and its orchestration platform, and it is open to download [1]. The GrepMem authors argue the structured-memory industry is solving a problem a log file ends [3]. What I am watching next is whether the audit turns into infrastructure: it publishes a tool-change history with a live feed per host [2], and a change feed is exactly what a distilled-guideline store needs to expire itself. The memory papers end at advice; the audit ends at a daily check. The design that wins is the one that wires the second into the first.

The audit also found that a third of hosts — 13,848 of them, 33.7% — answer but list their tools only after sign-in [2]. For an architect that is a visibility tax. Clients cannot see what a host does before connecting, and the code that mines guidelines cannot decide which tools are worth learning.

<!-- nuanced-takeaway -->

## The catch

The asymmetry is the part I keep coming back to: the memory side got papers, and the tool side got a census. The memory numbers come from benchmark runs on given models. The 29-guideline result is a mean of two runs on one weak model; a stronger model in the same study wanted every guideline it could get, so "less memory wins" is not a rule, it is a per-model calibration. The audit measures whether hosts answer, not what calls return — a host can pass every check and still give wrong results. And distillation has a documented dark side: the same paper records a guideline that backfired, and provenance that silently dropped during consolidation [1]. Both halves now have numbers attached, and only one of them has a change feed. Neither fixes the other.

## Sources

- [1] "How Much Should an Agent Remember? Deployment Lessons from Self-Distilled Memory for LLM Agents" (arXiv:2611.26361, 19 Nov 2026) — https://arxiv.org/abs/2611.26361
- [2] NestDaddy, "We graded every remote MCP server in the official registry. Here is what we found." (22 Nov 2026) — https://nestdaddy.com/blog/state-of-remote-mcp-servers-2026
- [3] "Forget Freely, Grep Later: Lossless, Index-Free Memory for Long-Horizon LLM Agents" (arXiv:2611.25123, 18 Nov 2026) — https://arxiv.org/abs/2611.25123
- [4] "MemFolder: Structure-Guided Memory Folding for Efficient Agent Memory Management" (arXiv:2611.26427, 19 Nov 2026) — https://arxiv.org/abs/2611.26427

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Agent Memory Poisoning" -> /agent-memory-poisoning-write-path/ [same site (aichieve.net); same category; topical overlap: agent, memory] Link "Agent Memory Poisoning" in the section where the article touches agent, memory. -->
<!-- internal-link hint: "Durable Execution Is Not a Transaction" -> /durable-execution-not-a-transaction/ [same site (aichieve.net); same category; topical overlap: agent, model] Link "Durable Execution Is Not a Transaction" in the section where the article touches agent, model. -->
<!-- internal-link hint: "Planner-as-Router: Fold the Model Choice Into the Plan" -> /planner-as-router-fold-the-model-choice-into-the-plan/ [same site (aichieve.net); same category; topical overlap: agent, model] Link "Planner-as-Router: Fold the Model Choice Into the Plan" in the section where the article touches agent, model. -->
## Related reading

- [Agent Memory Poisoning](/agent-memory-poisoning-write-path/) — more on Autonomous & Agentic Workflows
- [Durable Execution Is Not a Transaction](/durable-execution-not-a-transaction/) — more on Autonomous & Agentic Workflows
- [Planner-as-Router: Fold the Model Choice Into the Plan](/planner-as-router-fold-the-model-choice-into-the-plan/) — more on Autonomous & Agentic Workflows
<!-- internal-links:end -->
