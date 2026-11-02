---
title: "Your Tool-Call Trace Is a User Profile and a 7.6% Alarm"
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

Two papers posted on 30 October measured the same record from opposite ends, and both conclude that the tool log an agent fleet keeps is not the security proof the team assumes. The first ran four large language model (LLM) attackers against real tool calls from 25 servers. The test set contained 1,000 synthetic user profiles and 4,000 agent runs. With no chat history and only those calls to read, the attackers named the correct user 26.25 percent of the time. A plain guess managed 17.97 percent [1]. The same record also produced a weak alarm.

The second paper reviewed eleven evaluations of hijack detectors. One detector scored 0.879 on the area under the receiver operating characteristic curve (AUROC), the standard trade-off between missed attacks and false alarms. When attacks fell to 2 percent of traffic, its precision dropped to 7.6 percent [2]. A precision that low at a 2 percent attack rate is not much of a control.

<!-- tension -->

## The big picture:

The tool-call trace is the most detailed record an agent system makes, and very little of it is neutral. The fields that do the identifying are the arguments sent to each tool and the results the tool returns. Those fields carry what the user asked for and what the service handed back [1]. Joining traces across sessions sharpens the picture further. Record keeping stops being routine and becomes a privacy decision someone has to own.

I read the OpenTelemetry Model Context Protocol (MCP) page last, and the session identifier struck me as the quiet part being made standard. The conventions mark `mcp.session.id` as a recommended field on every span and define duration metrics for both client and server sessions [4]. A standard that stamps a stable join key on each span makes the store richer for defenders and easier to link for everyone else. The same two papers show what that linking buys an observer.

## By the numbers

- **26.25 percent — Guessed user:** four mainstream LLM attackers named the right user from valid tool calls alone, against 17.97 percent for a plain guess [1].
- **7.6 percent — Alarms that were real:** at a 2 percent attack rate, a detector with a 0.879 AUROC reached 7.6 percent precision; replacing only the negative samples moved it between 3.9 percent and 11.7 percent [2].
- **62.64 percent to 100 percent — Logging attack:** across 18 model-server pairs with valid tool execution, an extra attacker call succeeded at that rate, and 16 of those pairs changed task completion by at most 6.63 points [3].
- **16 percent to 86 percent — Attack share in the tests:** the eleven reviewed evaluations set attacks at that spread; none varied the share, and six never tried a second benchmark [2].
- **85.53 percent — Benign descriptions flagged:** an instruction detector in the logging-attack study raised an alarm on most harmless descriptions [3].

<!-- tactical-insight -->

## What I'd watch:

The architects closest to this are splitting one question into two: what may the trace hold, and what may it prove. That split is showing up in retention policy before it appears in a design diagram. Call arguments and returned values are the fields they are debating.

- **Keeping call arguments and results:** the profiling evidence sits in those fields, not in method names. Teams are checking whether a rule that scrubs prompts while keeping payloads removes the wrong half [1].
- **Session linking as a merge decision:** cross-session joins drive the higher inference rate, and the OpenTelemetry conventions now recommend the identifier that makes those joins cheap [1][4]. Operators are deciding whether linking becomes a default they must opt out of.
- **Alarm checks at an estate's own rate:** the evaluation audit shows that precision depends on how rare attacks are. A test that fixes the attack share between 16 percent and 86 percent cannot say what the alarm does at 2 percent [2].
- **The second call as evidence:** the logging attack adds an attacker call after the legitimate one [3]. The people closest to it are watching whether host-side rules can refuse that shape and what a trace must contain before it counts as evidence.

My reading of the audit tables is that the denominator matters more than the detector score, because a 0.879 AUROC becomes a 7.6 percent precision at a realistic base rate.

<!-- nuanced-takeaway -->

## The catch

The 26.25 percent figure comes from a synthetic test set, and synthetic profiles tend to separate more cleanly than real ones. The 1,000 profiles and 4,000 runs show what the channel can carry, not what any live system gives up [1]. The 2 percent attack rate is the audit's own scenario for turning a score into a hit rate, so the 7.6 percent illustrates the arithmetic more than a specific estate [2]. Both papers are preprints, and a detector at 7.6 percent still catches some attacks.

I would not build a governance case on the 26.25 percent alone, because the test set is made up, but the direction of the result is not easy to ignore. The protocol discussion also notes that a newer version drops the session identifier at the protocol level, which leaves cross-session linking to whatever the operator keeps [4]. That may delay the join risk, but it does not remove it.

<!-- tldr -->

## At a glance

**The shift:** Tool-call traces are being written into standards and kept as a security asset. Two October papers measure the same record as a user profile and a weak alarm.

**The number:** Attackers guessed the right user from traces alone 26.25 percent of the time; a detector with a 0.879 AUROC reached 7.6 percent precision at a 2 percent attack rate.

**The risk:** Keeping call arguments and returned results without a scrub and link policy leaves a personal-data store inside the logging stack.

## Sources
[1] Duan, Liu, Liu, Zou, Hu and Liu, "How Much Can Tool Calls Reveal About You? Privacy Leakage from Tool-Call Traces," arXiv:2610.41885, 30 October 2026 — https://arxiv.org/abs/2610.41885
[2] Abbasi, Núñez V. and Shahraki, "What Standard Evaluations Hide About Detectors of Hijacked LLM Agents: Rare Attacks, Unseen Tools and Benchmark Transfer," arXiv:2610.41803, 30 October 2026 — https://arxiv.org/abs/2610.41803
[3] Hu, Fan, Samyoun and Du, "Log-To-Leak: Prompt Injection Attacks on Tool-Using LLM Agents via the Model Context Protocol," arXiv:2610.36108, 26 October 2026 — https://arxiv.org/abs/2610.36108
[4] OpenTelemetry, "Semantic Conventions for Model Context Protocol (MCP)," `semantic-conventions-genai` repository, `docs/gen-ai/mcp.md`, read 2 November 2026 — https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/mcp.md
