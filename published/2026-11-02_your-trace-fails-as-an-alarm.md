---
title: "Your Trace Fails as an Alarm: 26.25% Profile"
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
meta_title: "Your Trace Fails as an Alarm: 26.25% Profile"
meta_title_source: "derived_from_title"
meta_description: "Two papers posted on 30 October measured the same record from opposite ends, and both say the tool log you keep is not the security proof you think it is."
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/your-trace-fails-as-an-alarm/featured.jpg"
image_style: "technical_isometric"
image_model: "nanobanana"
image_alt: "An open server rack of transparent trace cassettes sits under a beam-splitter prism in a dim server room."
image_caption: "Trace Logs Fail As Security Alarms: your trace store is a profile, and the alarm fails."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->

Two papers posted on 30 October measured the same record from opposite ends, and both say the tool log you keep is not the security proof you think it is. The first ran four large language model (LLM) attackers against real tool calls from 25 servers. The test set held 1,000 fake user profiles and 4,000 agent runs. With no chat history and only those calls to read, the attackers recovered user attributes 26.25% of the time. A plain guess managed 17.97% [1]. Your trace store is a profile of your customer, and the alarm on top of it fails.

The second paper checked eleven alarm tests. It found a detector that scores 0.879 on the AUROC (the standard curve that trades missed attacks for false alarms). Once attacks are 2% of traffic, only 7.6% of the alarms it raised were real [2]. A hit rate that low, at a base rate that ordinary, is not a control anyone can lean on.

<!-- tension -->

## The big picture:

The trace is the most detailed record an agent system makes, and almost none of it is neutral. The inputs to each call, and what came back, are the fields the profiling test leans on. They carry what the user asked for and what the tool sent back [1]. Joining traces across sessions sharpens that picture further. Plain record keeping becomes a privacy call that someone has to own.

I read the session-id line in the OpenTelemetry page twice, because it landed the same week as the two papers. The standard now recommends a session id on tool spans. The same page defines timing rules for session length on both sides of the call [4]. A standard that recommends a join key makes the store richer and easier to link. In that same week, two papers show what the linking buys an observer.

## By the numbers

- **26.25% — Guessed user:** four mainstream LLM attackers named user traits from valid tool calls alone, against 17.97% for a plain guess [1].
- **7.6% — Alarms that were real:** at a 2% attack rate, a detector scoring 0.879 on the AUROC raised mostly noise, and swapping only the negatives moved its hit rate between 3.9% and 11.7% [2].
- **62.64% to 100% — Logging attack:** an extra attacker call worked on 18 model-server pairs, while 16 of them changed how often tasks finished by at most 6.63 points [3].
- **16% to 86% — Attack share in the tests:** the eleven reviewed tests ran at that spread, none varied it, and six never tried a second test set [2].

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 172" style="background:#0f172a; border-radius:8px; font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif; margin:16px 0; max-width:100%; height:auto;">
  <text x="20" y="36" fill="#f8fafc" font-size="16" font-weight="600">Your Trace Fails as an Alarm: 26.25% Profile</text>
  <text x="20" y="52" fill="#94a3b8" font-size="12">Figures as stated in this article&#x27;s own numbers section (verified figures, %)</text>
  <!-- Row 1 -->
  <text x="20" y="84" fill="#e2e8f0" font-size="13" font-weight="500">Logging attack</text>
  <rect x="240" y="70" width="300" height="18" rx="4" fill="#1e293b"/>
  <rect x="240" y="70" width="187" height="18" rx="4" fill="#818cf8"/>
  <text x="437" y="84" fill="#f1f5f9" font-size="13" font-weight="600">62.6%</text>
  <text x="491" y="84" fill="#64748b" font-size="11">([3])</text>
  <!-- Row 2 -->
  <text x="20" y="132" fill="#e2e8f0" font-size="13" font-weight="500">Attack share in the tests</text>
  <rect x="240" y="118" width="300" height="18" rx="4" fill="#1e293b"/>
  <rect x="240" y="118" width="48" height="18" rx="4" fill="#818cf8"/>
  <text x="298" y="132" fill="#f1f5f9" font-size="13" font-weight="600">16%</text>
  <text x="352" y="132" fill="#64748b" font-size="11">([2])</text>
</svg>

<!-- tactical-insight -->

## What I'd watch:

My note from the audit is that the storage rule has to come before the detector choice. The architects closest to this are splitting one question into two: what may the trace hold, and what may it prove?

- **Keeping policy for call inputs and results:** the profiling evidence sits in call inputs and returned values, not in method names. A rule that scrubs the chat and keeps the tool payloads has scrubbed the wrong half [1].
- **Session linking as a merge decision:** cross-session joins raise the guess rate, and the standard now recommends the id that makes those joins cheap, so linking becomes a default an operator opts into [1][4].
- **Alarm checks at your own rate:** the audit's sums say the hit rate depends on how rare attacks are. A test that fixes the attack share between 16% and 86% cannot tell you what the alarm does at 2% [2].
- **A rule for the second call:** the logging attack works by adding an attacker call after the legitimate one. That is the shape a host-side rule can refuse [3]. What a trace has to contain to count as proof at all is a separate design question, and [it has a longer answer than most teams expect](/agent-audit-trail-not-evidence/).

<!-- nuanced-takeaway -->

## The catch

The privacy figure comes from a fake test set, and fake profiles are easier to tell apart than real ones. A set of 1,000 profiles and 4,000 runs shows what the channel can carry, not what a live system gives up [1]. The 2% attack rate is the audit's own way of turning a score into a hit rate, so the 7.6% shows the arithmetic rather than your estate [2].

I may be over-reading how fast the join risk arrives, because the standard itself makes the session id conditional. The page attaches it only when a request is part of a session, which leaves cross-session linking to whatever the transport and the operator keep [4]. Both papers are also unreviewed, and an alarm at 7.6% still catches some attacks. The finding is that the number is never reported, not that detection is worthless [2].

<!-- tldr -->

## At a glance

**The shift:** The tool-call trace is being written into standards and kept as a security asset, while two October papers measure it as a user profile and a weak alarm.

**The number:** 26.25% of user traits recovered from traces alone, against a 7.6% alarm hit rate at a 2% attack rate.

**The risk:** Keeping call inputs and results without a scrub and link policy leaves a personal-data store inside your logging stack.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Your Multi-Agent Failure Has a Shape" -> /agent-failure-topology-not-model/ [same site (aichieve.net); same category; topical overlap: fails, papers] Link "Your Multi-Agent Failure Has a Shape" in the section where the article touches fails, papers. -->
<!-- internal-link hint: "Answer Field First Costs 38.15 Points" -> /answer-field-first-costs-38-points/ [same site (aichieve.net); same category; topical overlap: tool] Link "Answer Field First Costs 38.15 Points" in the section where the article touches tool. -->
<!-- internal-link hint: "Durable Execution Is Not a Transaction" -> /durable-execution-not-a-transaction/ [same site (aichieve.net); same category; topical overlap: tool] Link "Durable Execution Is Not a Transaction" in the section where the article touches tool. -->
## Related reading

- [Your Multi-Agent Failure Has a Shape](/agent-failure-topology-not-model/) — more on Autonomous & Agentic Workflows
- [Answer Field First Costs 38.15 Points](/answer-field-first-costs-38-points/) — more on Autonomous & Agentic Workflows
- [Durable Execution Is Not a Transaction](/durable-execution-not-a-transaction/) — more on Autonomous & Agentic Workflows
<!-- internal-links:end -->

## Sources

[1] Duan, Liu, Liu, Zou, Hu and Liu, "How Much Can Tool Calls Reveal About You? Privacy Leakage from Tool-Call Traces," arXiv:2610.41885, 30 October 2026 — https://arxiv.org/abs/2610.41885
[2] Abbasi, Núñez V. and Shahraki, "What Standard Evaluations Hide About Detectors of Hijacked LLM Agents: Rare Attacks, Unseen Tools and Benchmark Transfer," arXiv:2610.41803, 30 October 2026 — https://arxiv.org/abs/2610.41803
[3] Hu, Fan, Samyoun and Du, "Log-To-Leak: Prompt Injection Attacks on Tool-Using LLM Agents via the Model Context Protocol," arXiv:2610.36108, 26 October 2026 — https://arxiv.org/abs/2610.36108
[4] OpenTelemetry, "Semantic Conventions for Model Context Protocol (MCP)," `semantic-conventions-genai` repository, `docs/gen-ai/mcp.md`, read 2 November 2026 — https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/mcp.md
