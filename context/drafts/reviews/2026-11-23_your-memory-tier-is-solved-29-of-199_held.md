---
title: "Agent Memory Management: Your Memory Tier Is Solved: 29 of 199"
vertical: agentic_ai
kind: news
archetype: news
synthesis: true
persona: ai_architect
one_big_thing: "Three papers landed in one week showing agent memory is a solved engineering problem — a model does better with 29 distilled guidelines than with all 199, and a plain-text log with search beats every structured memory stack — while the MCP tool fabric those guidelines describe changed under 25% of registry hosts in the last 30 days and 11% miss a daily check in ten: the effort is pouring into the closed half while the churning half has no change feed."
date: 2026-11-23
slug: your-memory-tier-is-solved-29-of-199
meta_title: "Your Memory Tier Is Solved: 29 of 199"
meta_description: "A model beat itself using 29 distilled guidelines instead of all 199 — the same week a quarter of MCP registry hosts changed a tool. The memory tier is closed; the tool fabric is not."
primary_keyword: "agent memory management"
sources:
  - https://arxiv.org/abs/2611.26361
  - https://nestdaddy.com/blog/state-of-remote-mcp-servers-2026
---

<!-- lead -->
A model given 29 distilled guidelines beat the same model given all 199 — 55.4% against 51.2% on task completion [1]. That memory system shipped to production the same week [1]. And a daily audit of the Model Context Protocol (MCP) registry — the open standard agents use to call outside tools — reported that a quarter of its remote hosts had rewritten at least one tool in the last 30 days, and that 11% stop answering at least one day in ten [2]. The memory half of an agent's architecture just resolved into simple answers. The tool half those memories describe is still moving underneath them.

<!-- tldr -->

## At a glance

Three papers landed in one week telling teams building long-horizon agents how to handle agent memory management: distill to your model's own subset, or drop the stack and search a plain log. The open problem is now the tool fabric those memories describe — which changes under a quarter of registry hosts each month.

<!-- tension -->

## The week memory closed

The production paper is a deployment record, not a lab sketch [1]. Its pipeline mines short lessons from an agent's own failed runs, folds them into guidelines, and hands the agent either all of them or a chosen subset. The result inverts the usual instinct about more. One strong model keeps improving with its full 191-guideline set, gaining 9.5 points of task completion [1]. The weaker model in the study starts at 39.9%, climbs to 51.2% with all 199 of its guidelines — and reaches 55.4% with a chosen subset of about 29 [1]. The paper's own line is the finding: the right amount of memory is a property of the model, not the memory.

Two more papers landed the same week. GrepMem trains an agent to keep a plain-text log of everything it has seen and recall with a text search — no embeddings, no index, no extra models — and scores 95–97% where the best lossy baseline it compares against reaches at most 21% [3]. MemFolder folds a memory store in half: 99.0% of the original performance held across three text benchmarks with 50% fewer records [4]. Three independent teams, same direction: smaller, simpler, self-distilled.

I have been giving the same advice since October — that the memory tier, how you split state between a context window and outside stores, was the call that decided long tasks. This week dated that advice. The tier no longer loses much: a log and a search beats a retrieval stack, and half the records cost almost nothing in accuracy.

But the guidelines the winning systems distill are snapshots. They are prose about how a given tool behaves, mined from runs against given hosts. The audit measures what happens to those hosts: 25.1% rewrote at least one tool in the last 30 days, and 86.8% answered every daily check — so 11.0% missed at least one in ten [2]. The audit's scale is the public registry itself: 322,242 tools across 22,576 hosts, median first answer 253 milliseconds [2]. The report's own framing is blunt: an agent that learned your tools last week can break when a name or an input changes silently [2].

My reading, held loosely: these are one problem, not two. A guideline that says "call tool X to paginate" is true as of the day it was mined. With a quarter of hosts changing tools each month, a guideline is a cache entry with no expiry field. The failure does not arrive as an error. The agent calls the renamed tool, gets a plausible result, and reports done. Nothing in the memory code re-checks it, because its whole job is deciding what to keep, not whether the world still matches.

## By the numbers

- A weak model scored 55.4% with a 29-guideline subset, beating 51.2% with all 199 [1].
- 25.1% of remote MCP hosts rewrote at least one tool in the last 30 days [2].
- 11.0% of hosts answered fewer than nine daily checks in ten [2].

<!-- tactical-insight -->

## Where this bites

The teams closest to the story have already moved. The production pipeline ships in IBM's CUGA agent and the watsonx Orchestrate platform, and its code is open to download [1]. The GrepMem authors argue the structured-memory industry is solving a problem a log file ends [3]. What I am watching next is whether the audit becomes infrastructure rather than a report: a per-host history of tool changes is exactly what a distilled-guideline store needs to expire its own entries, and nothing on the memory side currently asks for it. The memory papers end at advice. The audit ends at a daily check. The design that wins is the one that wires the second into the first.

The audit also found that a third of hosts — 13,848 of them, 33.7% — answer but list their tools only after sign-in [2]. For an architect that is a visibility tax. A client cannot see what a host does before connecting, and the code that mines guidelines cannot decide which tools are worth learning from a surface it is not allowed to read.

<!-- nuanced-takeaway -->

## The catch

The memory numbers come from benchmark runs on given models. The 29-guideline result is a mean of two runs on one weak model, and a stronger model in the same study wanted every guideline it could get — so "less memory wins" is a per-model calibration, not a rule. The audit measures whether hosts answer, not what they return: a host can pass every daily check and still hand back wrong results. And distillation has a documented dark side — the same paper records a guideline that backfired, and provenance that silently dropped during consolidation [1]. My honest position after reading all four documents: both halves now have numbers attached, and only one of them has anyone checking it daily. Neither fixes the other.

## Sources

- [1] "How Much Should an Agent Remember? Deployment Lessons from Self-Distilled Memory for LLM Agents" (arXiv:2611.26361, 19 Nov 2026) — https://arxiv.org/abs/2611.26361
- [2] NestDaddy, "We graded every remote MCP server in the official registry. Here is what we found." (22 Nov 2026) — https://nestdaddy.com/blog/state-of-remote-mcp-servers-2026
- [3] "Forget Freely, Grep Later: Lossless, Index-Free Memory for Long-Horizon LLM Agents" (arXiv:2611.25123, 18 Nov 2026) — https://arxiv.org/abs/2611.25123
- [4] "MemFolder: Structure-Guided Memory Folding for Efficient Agent Memory Management" (arXiv:2611.26427, 19 Nov 2026) — https://arxiv.org/abs/2611.26427

<!-- internal-links -->
