---
title: "Silent Leak: 68.8% Bypasses Your Filter"
vertical: agentic_resilience_failure
persona: infra_engineer
one_big_thing: "The safety number a multi-agent team reports is usually measured on the answer channel, which is the channel that leaks least — agent-to-agent messages leak at 68.8% against 27.2% on the final output, so the check belongs at each hop and the metric belongs per channel."
date: 2026-10-21
slug: silent-leak-bypasses-your-filter
archetype: evergreen
evergreen: true
image_path: "context/assets/illustrations/silent-leak-bypasses-your-filter/featured.png"
image_style: "technical_isometric"
image_model: "nanobanana"
image_alt: "Multi-Agent Data Leaks. Isometric cutaway of optical processing modules showing an internal light ray diverging before the"
image_caption: "Multi-Agent Data Leaks: Internal messages bypass output filters to leak data."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Most multi-agent runs hide a silent data leak. In a new test of 4,979 agent traces, 68.8% pushed private content through the messages the agents sent to each other [1]. Only 27.2% let that data reach the final user answer [1]. The leak bypasses your output filter because the data never passes through the output channel at all.

<!-- tension -->

## The big picture:

Multi-agent setups split up work, but they also split the places where data can escape.

A lead agent hands a task to a helper. The helper writes a note to shared memory. One of them calls a tool with a data payload. Each hop acts as a channel. Each channel carries the same patient records, invoices or contracts as the final answer [1].

The study behind that first figure ran 1,000 test cases on five shipped models. The cases covered health care, finance, law and company work [1]. It recorded every channel. Inside channels leaked at 57.8% on average. The answer leaked at 27.2% [1]. Agent-to-agent messages ran at 2.5 times the answer rate [1].

What strikes me is the shape of the number, not just its size. Multi-agent setups cut the leak rate on the final answer itself, from 43.2% with a single agent to 27.2% [1]. That gain is real. It also makes the answer look safer than the system is.

## By the numbers

- **68.8% — Agent-to-agent leaks:** The share of 4,979 traces where private content crossed between agents, compared to 46.7% for shared memory and 27.2% for the final answer [1].
- **41.7% — Audit gap:** The share of breaches an answer-only audit completely missed [1].
- **2.9% vs 68.8% — Filter blind spot:** In a replay of the same traces, an answer-only filter cut the output leaks to 2.9% but left agent-to-agent leaks untouched [2].
- **19,916 — Decisions logged:** The audit events a per-hop check recorded over those traces, compared to just 1,556 for the answer-only filter [2].

<!-- tactical-insight -->

## What I'd watch:

I keep circling back to the replay work. The same team added a check at every hop on those 4,979 traces [2]. The check read the active rule. Then it cut the text before the content moved on.

Agent-to-agent leaks fell from 68.8% to 3.3% [2]. Memory writes fell from 46.7% to 2.7% [2]. The answer stayed at 2.9%. That metric never told the whole story.

- **Where the check sits:** The best result came from making a decision at each hop, not from building a stronger final filter [2].
- **What counts as good enough:** The researchers aimed for leaks below 2%. The balanced per-hop policy landed at a 0.017 leak score, a 0.983 pass rate, and 0.980 utility [2].
- **The audit bill:** Logging 19,916 decisions instead of 1,556 is the real computing cost. A per-hop control needs a serious budget [2].
- **The strict version fails:** A variant that cut all text reached zero leaks but scored minus 0.392 on utility. The trade-off runs both ways [2].

A second study ran a similar test on a different fault. Researchers tested five memory systems and nine models across 1,620 trials using a revoked policy that the system still handed back to the agent [3].

There, a filter at the memory store drove bad actions to zero across all 1,620 trials [3]. An output filter left 18.1% of them [3]. A plain rule in the system prompt still let 12.9% through [3]. That same order repeats across two teams testing different things.

<!-- nuanced-takeaway -->

## The catch

Two caveats matter more than the headline numbers.

The replay ran over traces the system had already logged. It is not a live system. It shows which breaches a per-hop check would have caught [2]. It cannot show how agents adapt once the check starts cutting their text.

A vendor lab ran and published the revoked-rule study on its own hardware, with no outside check [3]. The result matches the first study's order. A lab grading its own product type is still a weaker witness.

My read is that the lasting claim is narrow. A number measured on the answer channel cannot tell you whether a rule holds anywhere else. In every model and field tested, the messages between agents leaked at least as much as the answer [1].

<!-- tldr -->

## At a glance

- **The Big Shift:** A test of 4,979 traces shows multi-agent systems pushed private data out of the final answer and into the messages, memory writes, and tool calls between agents. Inside channels leak at 68.8% against 27.2% at the output [1].
- **Why It Matters:** Teams report the answer rate. A filter that drops the final output leak from 27.2% to 2.9% reads as a fix, while agent-to-agent leaks secretly stay at 68.8% [2].
- **What I'd Watch:** Whether the check moves to each hop, and whether the reported metric splits by channel instead of folding into one number.
  - **Per-hop check:** A decision on each message, memory write, and tool call before the content goes on, which the replay measured at 3.3% agent-to-agent leaks [2].
  - **Per-channel leak rate:** The rate reported apart for the answer, the agent-to-agent messages, and shared memory. It is the only form that shows the gap [1].
  - **Audit load:** The count of decisions a per-hop check writes, 19,916 over these traces, against 1,556 for the answer filter [2].
- **The Catch:** The per-hop result is a replay of old traces, not a live run. The second study is vendor-published, and the strictest form of the control scored below zero on utility [2][3].

## Sources

[1] El Yagoubi, Badu-Marfo, Al Mallah — *AgentLeak: A Full-Stack Benchmark for Privacy Leakage in Multi-Agent LLM Systems*, arXiv:2602.11510 — https://arxiv.org/html/2602.11510v2
[2] Li, Ma, Wen, Huang, Zhou, Fu, Cheng — *Safe Multi-Agent Behavior Must Be Maintained, Not Merely Asserted: Constraint Drift in LLM-Based Multi-Agent Systems*, arXiv:2605.10481 — https://arxiv.org/html/2605.10481v1
[3] Vulcan — *Revoked but Still Authoritative: An Empirical Study of Revocation Enforcement in Agent-Memory Systems* (2026-09-11) — https://vulcanlab.ai/revoked-but-still-authoritative-an-empirical-study-of-revocation-enforcement-in-agent-memory-systems

## Gate report
lead — PASS — Opens immediately with the core takeaway and stats, no throat-clearing.
tension — PASS — Uses correct H2s with blank lines, includes a first-person observer cue, and contains the mandatory By the numbers section perfectly formatted.
tactical-insight — PASS — Uses correct H2, features a first-person cue, bullets are observations rather than commands.
nuanced-takeaway — PASS — Uses correct H2, includes a first-person cue, keeps paragraphs short and plain.
tldr — PASS — Matches the strict 4-part Smart Brevity structure under 'At a glance' H2.
