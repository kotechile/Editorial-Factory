---
title: "Silent Leak: 68.8% Bypasses Your Filter"
vertical: agentic_resilience_failure
persona: infra_engineer
one_big_thing: "The safety number a multi-agent team reports is usually measured on the answer channel, which is the channel that leaks least — agent-to-agent messages leak at 68.8% against 27.2% on the final output, so the check belongs at each hop and the metric belongs per channel."
date: 2026-10-21
slug: silent-leak-bypasses-your-filter
archetype: evergreen
evergreen: true
---

<!-- lead -->
A silent leak sits inside most multi-agent runs. In a new test of 4,979 agent traces, 68.8% pushed private content through the messages the agents send each other. Only 27.2% let it reach the final answer [1]. The leak bypasses your output filter because it never passes through the output at all.

<!-- tension -->

## The big picture:

Multi-agent systems were sold as a way to split work. They also split the places where data can escape. Only one of those places is on screen.

A lead agent hands a task to a helper. The helper writes a note to shared memory. One of them calls a tool with a payload. Each hop is a channel. Each channel carries the same patient record, invoice or contract that the answer carries [1].

The study behind that first figure ran 1,000 cases across health care, finance, law and corporate work, on five shipped models. It recorded every channel [1]. Inside channels leaked at 57.8% on average, against 27.2% for the answer. Agent-to-agent messages ran at 2.5 times the answer rate [1].

What strikes me is the shape of the number, not its size. Multi-agent setups cut the leak rate on the answer itself, from 43.2% with one agent to 27.2% [1]. That gain is real. It also makes the answer look safer than the system is.

## By the numbers

- **68.8% — Agent-to-agent messages:** the share of 4,979 traces where private content crossed between agents, against 46.7% for shared memory and 27.2% for the final answer [1].
- **41.7% — Audit gap:** the share of breaches an answer-only audit never sees, with the same order holding across all five models and four fields tested [1].
- **2.9% vs 68.8% — The filter's blind side:** in a replay of the same traces, an answer-only filter cut the output to 2.9% and left agent-to-agent leaks exactly where they were [2].
- **19,916 — Decisions logged:** the audit events a check at each hop wrote over those traces, against 1,556 for the answer-only filter [2].

<!-- tactical-insight -->

## What I'd watch:

The replay is the part worth reading. The same team took the 4,979 traces and added a check at every hop. The check read the rule in force and cut the text before the content moved on [2].

Agent-to-agent leaks fell from 68.8% to 3.3%. Memory writes fell from 46.7% to 2.7% [2]. The answer stayed at 2.9%, which is the point. That number never told you a thing.

- **Where the check sits:** the best result came from a decision at each hop, not from a better final filter. The authors say plainly that this is a replay of old traces, not a live run [2].
- **What counts as good enough:** their policy search asks for leaks below 2%. The answer-only policy landed at 0.328, with a 0.672 pass rate and 0.718 utility. The balanced per-hop policy landed at 0.017, a 0.983 pass rate and 0.980 utility [2].
- **The bill for it:** 19,916 logged decisions against 1,556 is the real cost line. A control like this needs a budget, not a slogan [2].
- **The strict version fails too:** the cut-everything variant reached zero leaks but scored minus 0.392 utility, so the trade runs both ways [2].

A second study, with no link to the first, ran the same test on a different fault. Five memory systems, nine models, 1,620 trials, and a policy that had been revoked but was still being handed back to the agent [3].

There, a filter at the store boundary drove bad actions to zero across all 1,620 trials. An output filter left 18.1%. Prompt hardening left 37.2%. A plain rule in the system prompt still let 12.9% through, and 46.1% on one deletion case [3]. I keep coming back to that order, because it repeats across two teams that were not testing the same thing.

<!-- nuanced-takeaway -->

## The catch

Two caveats deserve more weight than the headline numbers.

The replay works over traces that were already logged. It is not a running system. It shows which breaches a per-hop check would have caught. It cannot show how agents adapt once the check starts cutting their text [2].

The revocation study was run and published by a vendor lab, on its own rig, with no outside check [3]. Its result matches the first study's order, which is why I take it seriously. A lab grading its own product type is still a weaker witness.

My read is that the lasting claim is narrow. A number measured on the answer channel cannot tell you whether a rule holds anywhere else. The first study's own authors say it: across every model and every field, the messages between agents leaked at least as much as the answer [1].

## At a glance

- **The Big Shift:** A test of 4,979 traces shows multi-agent systems pushed private data out of the final answer and into the messages, memory writes and tool calls between agents. Inside channels leak at 68.8% against 27.2% at the output [1].
- **Why It Matters:** Teams report the answer rate. So a filter that drops it from 27.2% to 2.9% reads as a fix, while agent-to-agent leaks stay at 68.8% [2].
- **What I'd Watch:** Whether the check moves to each hop, and whether the reported metric splits by channel instead of folding into one number.
  - **Per-hop check:** a decision on each message, memory write and tool call before the content goes on, which the replay measured at 3.3% agent-to-agent leaks [2].
  - **Per-channel leak rate:** the rate reported apart for the answer, the agent-to-agent messages and shared memory. It is the only form that shows the gap [1].
  - **Audit load:** the count of decisions a per-hop check writes, 19,916 over these traces, against 1,556 for the answer filter [2].
- **The Catch:** The per-hop result is a replay of old traces, not a live run, the second study is vendor-published, and the strictest form of the control scored below zero on utility [2][3].

## Sources

[1] El Yagoubi, Badu-Marfo, Al Mallah — *AgentLeak: A Full-Stack Benchmark for Privacy Leakage in Multi-Agent LLM Systems*, arXiv:2602.11510 — https://arxiv.org/html/2602.11510v2
[2] Li, Ma, Wen, Huang, Zhou, Fu, Cheng — *Safe Multi-Agent Behavior Must Be Maintained, Not Merely Asserted: Constraint Drift in LLM-Based Multi-Agent Systems*, arXiv:2605.10481 — https://arxiv.org/html/2605.10481v1
[3] Vulcan — *Revoked but Still Authoritative: An Empirical Study of Revocation Enforcement in Agent-Memory Systems* (2026-09-11) — https://vulcanlab.ai/revoked-but-still-authoritative-an-empirical-study-of-revocation-enforcement-in-agent-memory-systems
