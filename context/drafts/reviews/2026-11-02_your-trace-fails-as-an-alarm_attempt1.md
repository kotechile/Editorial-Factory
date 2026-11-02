---
title: "Your Tool-Call Trace Is a 26.25% Profile and a 7.6% Alarm"
vertical: agentic_ai
kind: news
persona: ai_architect
one_big_thing: "The tool-call trace an agent fleet keeps is a personal-data store that identifies its user and a security control that fails at production base rates, so it has to be governed as evidence rather than trusted as a detector."
date: 2026-11-02
slug: your-trace-fails-as-an-alarm
synthesis: true
sources:
  - https://arxiv.org/abs/2610.41885
  - https://arxiv.org/abs/2610.41803
---

<!-- lead -->

Two papers posted on 30 October measured the same trace from opposite ends. The first sent four large language model (LLM) attackers against real tool calls from 25 servers. The test set held 1,000 made-up user profiles and 4,000 agent runs. With no chat history and only those calls to read, the attackers named the right user 26.25% of the time; a plain guess managed 17.97% [1]. The second reviewed eleven alarm tests and found a detector that scores 0.879 on the standard curve that trades missed attacks for false alarms. Once attacks were 2% of traffic, its hit rate dropped to 7.6% [2]. A third paper posted four days earlier showed why the trace cannot vouch for clean task outcomes. An extra attacker call worked on 18 model-server pairs, while 16 of them changed how often tasks finished by at most 6.63 points [3]. The trace you keep is a profile of your customer, a weak alarm, and an evidence trail that can be beaten without breaking the task.

## The big picture:

A tool-call trace is the most detailed record an agent system keeps, and almost none of it is neutral. Call inputs and returned values are the fields the profiling attack leans on. They carry what the user asked for and what the tool sent back [1]. Joining traces across sessions sharpens that picture further. Plain record keeping becomes a privacy decision, and someone has to own it.

The platform is moving the other way. OpenTelemetry's Model Context Protocol (MCP) standard recommends a session identifier on every tool-call record, and the same page defines session-length timers for both sides of the call [4]. A standard that stamps the session identifier on every trace entry makes the store richer and easier to link. I read the OpenTelemetry page twice because the field that makes profiling stronger is the field the standard treats as ordinary metadata.

## By the numbers

- **26.25% — Guessed user:** four mainstream LLM attackers named user traits from valid tool calls alone, against 17.97% for a plain guess [1].
- **7.6% — Alarms that were real:** at a 2% attack rate, a detector scoring 0.879 on the standard detection curve raised mostly noise, and swapping only the negatives moved its hit rate between 3.9% and 11.7% [2].
- **62.64% to 100% — Logging attack:** an extra attacker call worked on 18 model-server pairs, while 16 of them changed how often tasks finished by at most 6.63 points [3].
- **16% to 86% — Attack share in the tests:** the eleven reviewed tests ran at that spread, none varied it, and six never tried a second test set [2].

## What I'd watch:

The architects closest to this are splitting one question into two: what may the trace hold, and what may it prove? I would put the keeping decision before the detector decision, because most diagrams are drawn after the store has already filled.

- **Keeping policy for call inputs and returned values:** the profiling evidence sits in inputs and returned values, not in method names. A rule that scrubs prompts and keeps payloads has scrubbed the wrong half [1].
- **Session linking as a merge decision:** cross-session joins raise the guess rate. The MCP standard recommends the identifier that makes those joins cheap, so linking becomes an operator choice rather than a default [1][4].
- **Alarm checks at your own rate:** the audit's arithmetic says hit rate depends on how rare attacks are. A test that fixes the attack share between 16% and 86% cannot show what the alarm does at 2% [2].
- **A rule for the second call:** the logging attack adds an attacker call after the legitimate one, which is the shape a host-side rule can refuse [3]. What a trace must contain to count as evidence is a separate design question, and [it has a longer answer than most teams expect](/agent-audit-trail-not-evidence/).

## The catch

The privacy figure comes from a made-up test set, and made-up profiles are easier to tell apart than real ones. A set of 1,000 profiles and 4,000 runs shows what the channel can carry, not what a live system gives up [1]. The 2% attack rate is the audit's own scenario for turning a score into a hit rate, so the 7.6% figure shows the sums, not a forecast for a given fleet [2].

I could be wrong about how fast the join risk arrives. The same OpenTelemetry page notes that a newer protocol version drops the session identifier at the protocol layer, leaving cross-session linking to whatever the operator keeps [4]. The two 30 October papers are also unreviewed, and a hit rate of 7.6% still catches some attacks. The finding is that the number is rarely reported, not that detection is worthless [2].

## At a glance

**The shift:** The tool-call trace is being written into standards and kept as a security asset, while two 30 October papers measure it as a user profile and a weak alarm.

**The number:** 26.25% of users guessed from traces alone, against a 7.6% alarm hit rate at a 2% attack rate.

**The risk:** Keeping call inputs and returned values without a scrub and link policy leaves a personal-data store inside your logging stack.

## Sources
[1] Duan, Liu, Liu, Zou, Hu and Liu, "How Much Can Tool Calls Reveal About You? Privacy Leakage from Tool-Call Traces," arXiv:2610.41885, 30 October 2026 — https://arxiv.org/abs/2610.41885
[2] Abbasi, Núñez V. and Shahraki, "What Standard Evaluations Hide About Detectors of Hijacked LLM Agents: Rare Attacks, Unseen Tools and Benchmark Transfer," arXiv:2610.41803, 30 October 2026 — https://arxiv.org/abs/2610.41803
[3] Hu, Fan, Samyoun and Du, "Log-To-Leak: Prompt Injection Attacks on Tool-Using LLM Agents via the Model Context Protocol," arXiv:2610.36108, 26 October 2026 — https://arxiv.org/abs/2610.36108
[4] OpenTelemetry, "Semantic Conventions for Model Context Protocol (MCP)," `semantic-conventions-genai` repository, `docs/gen-ai/mcp.md`, read 2 November 2026 — https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/mcp.md
