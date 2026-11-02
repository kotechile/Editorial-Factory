---
title: "Your Trace Store Is a User Profile and a 7.6% Alarm"
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

Two papers posted on 30 October measured the same record from opposite ends, and both conclude that the tool log you keep is not the security proof you think it is. The first ran four large language model (LLM) attackers against real tool calls from 25 servers. The test set held 1,000 made-up user profiles and 4,000 agent runs. With no chat history and only those calls to read, the attackers named the right user 26.25% of the time; a plain guess managed 17.97% [1].

The second reviewed eleven alarm tests and found a detector scoring 0.879 on AUROC, the area under the curve that trades missed attacks for false alarms. Once attacks are 2% of traffic, its hit rate drops to 7.6% [2]. At that normal attack rate, a hit rate that low is not a control anyone can lean on.

## The big picture:

The trace is the most detailed record an agent system makes, and little of it is neutral once a call leaves the system. The inputs to each call, and what came back, are the fields the profiling attack leans on. They carry what the user asked for and what the tool sent back [1]. Joining traces across sessions sharpens that picture further, so plain record keeping becomes a privacy call someone has to own. I read the privacy result as a retention warning first and a model result second, not as a benchmark score.

OpenTelemetry's Model Context Protocol (MCP) standard for tool-call spans moves the other way. It asks for a session id on each span, and it defines timers for session length on both sides of the call [4]. A standard that stamps the join key on every span makes the store richer and easier to link, and in the same week two papers show what that joining buys an observer.

## By the numbers

- **26.25% — User guessed from calls alone:** four mainstream LLM attackers named the right user from real tool calls, against 17.97% for a plain guess [1].
- **7.6% — Alarms that were real:** at a 2% attack rate, a detector scoring 0.879 on that curve raised mostly noise; swapping only the negatives moved its hit rate between 3.9% and 11.7% [2].
- **62.64% to 100% — Logging attack:** an extra attacker call worked on 18 model-server pairs, while 16 of them changed how often tasks finished by at most 6.63 points [3].
- **16% to 86% — Attack share in the tests:** the eleven reviewed tests ran at that spread; none varied it, and six never tried a second test set [2].

## What I'd watch:

The architects closest to this are splitting one question into two: what the trace can hold, and what it can prove. I am watching whether the retention policy changes before the design diagram does, because that order tells you which budget owns the trace.

- **Call inputs and results, not method names.** The profiling evidence sits in call inputs and returned values. A rule that scrubs prompts and keeps payloads has scrubbed the wrong half [1].
- **Session links as a merge decision.** Cross-session joins raise the guess rate, and the standard now asks for the id that makes those joins cheap [1][4]. The open question is whether operators treat that id as a default or as a choice.
- **Alarm checks at the operator's own rate.** The audit's sums say the hit rate depends on how rare attacks are. A test that fixes the attack share between 16% and 86% cannot say what the alarm does at 2% [2].
- **A rule for the second call.** The logging attack works by adding an attacker call after the legitimate one, the shape a host-side rule can refuse [3]. A green task does not clear the trace. What a trace must contain to count as evidence is a separate design question, and it has a longer answer than many teams expect.

## The catch

The privacy figure comes from a made-up test set, and made-up profiles are easier to tell apart than real ones. A set of 1,000 profiles and 4,000 runs shows what the channel can carry, not what a live system gives up [1]. The 2% attack rate is the audit's own case for turning a score into a hit rate, so the 7.6% shows the sums rather than any one estate. I read the 2% case as sums, not a field reading.

The same protocol page notes that a newer version drops the session id at the protocol layer, which leaves cross-session joining to whatever the operator keeps [4]. Both papers are unreviewed, and a hit rate of 7.6% still catches some attacks. The finding is that the number is never reported, not that the alarm is useless [2].

## At a glance

**The shift:** The tool-call trace is being written into standards and kept as a security asset, while two October papers measure it as a user profile and a weak alarm.
**The number:** 26.25% of users guessed from traces alone, against a 7.6% alarm hit rate at a 2% attack rate.
**The risk:** Keeping call inputs and results without a scrub and link policy leaves a personal-data store inside the logging stack.

## Sources
[1] Duan, Liu, Liu, Zou, Hu and Liu, "How Much Can Tool Calls Reveal About You? Privacy Leakage from Tool-Call Traces," arXiv:2610.41885, 30 October 2026 — https://arxiv.org/abs/2610.41885
[2] Abbasi, Núñez V. and Shahraki, "What Standard Evaluations Hide About Detectors of Hijacked LLM Agents: Rare Attacks, Unseen Tools and Benchmark Transfer," arXiv:2610.41803, 30 October 2026 — https://arxiv.org/abs/2610.41803
[3] Hu, Fan, Samyoun and Du, "Log-To-Leak: Prompt Injection Attacks on Tool-Using LLM Agents via the Model Context Protocol," arXiv:2610.36108, 26 October 2026 — https://arxiv.org/abs/2610.36108
[4] OpenTelemetry, "Semantic Conventions for Model Context Protocol (MCP)," `semantic-conventions-genai` repository, `docs/gen-ai/mcp.md`, read 2 November 2026 — https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/mcp.md
