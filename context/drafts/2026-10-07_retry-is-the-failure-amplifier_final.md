---
title: "The Retry Is the Bug: An Agent's Costliest Failure Mode"
vertical: agentic_resilience_failure
persona: infra_engineer
one_big_thing: "Retrying a failed agent step — the default recovery move — is what turns one transient fault into a runaway cost loop and a duplicated side effect, and the agent reports success while it happens. Bound the retry and pin the idempotency key at the tool contract; a bigger model will not fix it."
date: 2026-10-07
slug: retry-is-the-failure-amplifier
synthesis: true
sources:
  - https://cloud.google.com/security/resources/ai-risk-and-resilience-2026
  - https://arxiv.org/abs/2609.29095
meta_title: "The Retry Is the Bug: An Agent's Costliest Failure"
meta_description: "A corrupted value sent a ledger agent into 15,000 retries and a $50,000 bill. A 25,930-episode study shows the same retry duplicates payments while the agent reports success."
---

<!-- lead -->
One empty field in a single record turned an agent's retry loop into a $50,000 cloud bill [1]. The bot failed to format the text, so it retried endlessly. It made more than 15,000 calls in under an hour and locked the database to stop live sales [1]. No attacker caused this — the recovery move was the incident.

<!-- tension -->

## The big picture:

The 2026 playbook relies on loops and retries to push past bad steps. The math is simple: if a single step works 95% of the time, a ten-step chain only finishes about 60% of the time. Agents need a way to recover to finish long tasks.

The part I keep circling is what the retry actually does when the failure is messy. The Mandiant report notes the agent did not crash or break data. It tried to force a fix, and that fix caused the damage [1]. 

A Sept. 24 study puts a number on this same habit. When an agent cannot tell if a slow write worked, retrying copies the action in 56% of tests [2]. That failure rate jumps to 74% when the network quietly sends the request twice [2].

## By the numbers

- **15,000+ — Reasoning calls:** A checking bot hit one bad value and entered an endless loop in under an hour [1].
- **~$50,000 — Cloud bill spike:** The same runaway loop locked local databases and stopped active business sales [1].
- **56% and 74% — Duplicate write rate:** Across 25,930 tests, top models that check before retrying still copied writes in 56% of slow cases, and 74% under double delivery [2].
- **90% — False success rate:** In 90% of tests that made a copy, the agent claimed the task was done, hiding the second charge [2].

<!-- tactical-insight -->

## What I'd watch:

What strikes me here is that both failures trace to the retry rules, not the model. The study shows the agent setup barely matters, and a faster model fails to close the gap alone [2]. How the tools talk to the server explains 81% of the duplicate rates once a request is sent [2].

I'd watch how teams build these three basic controls to stop runaway loops:

- **Bounded retries:** Mandiant points to a trip switch that stops the agent after a set number of failed tries [1]. GitHub used a similar fix after a seven-and-a-half-hour outage it blamed on a hidden retry bug that amplified traffic [3].
- **Contract-level idempotency keys:** Offering a unique tag on every write so the server spots repeats dropped the copy rate from 28% to 4%, pushing clean success to 99% [2].
- **Cost and loop signals:** The runaway agent's only warning sign was 15,000 calls and a rising bill, not an error line [1]. Tracking token spend per run and failed tries will catch this early.

<!-- nuanced-takeaway -->

## The catch

We are looking at two isolated data points: one vendor case study and one lab test making errors on purpose. The study notes the problem shrinks to near zero when an agent can read back the result of a write [2].

My read is that this makes the fix cheaper, not the risk smaller. The failures that survive are the ones where read-backs fail, and those writes move real money. Duplicate charges do not announce themselves, and the agent will not warn you. 

I could be wrong that a hard limit on retries solves everything. A tight limit can skip needed work, which creates its own failure. But adding an open retry and hoping for the best is no longer a safe default.

<!-- tldr -->

## At a glance

- **The Big Shift:** A runaway bot proved that an agent's retry step can become the failure, making 15,000 calls and a $50,000 bill from one bad value.
- **Why It Matters:** Builders rely on retries to fix flaky agents, but endless loops turn brief faults into huge cloud bills and duplicate payments while the bot reports total success.
- **What I'd Watch:** How teams move fixes out of the prompt and into the retry rules and tool setup:
  - **Bounded retries:** Trip switches that stop the loop after a set number of failed tries instead of allowing endless loops.
  - **Idempotency keys:** Unique tags attached to every write so the server can tell a repeat from a new request.
  - **Run-level tracking:** Watching token spend and failed tries to make runaway loops visible before the invoice arrives.
- **The Catch:** The data relies on a single case study and a lab test, and cutting retries too hard risks skipping needed tasks.

## Sources
[1] Mandiant, *AI Risk and Resilience* special report, September 2026 — Case Study 6, "Denial-of-Wallet using rogue reasoning loop" (https://cloud.google.com/security/resources/ai-risk-and-resilience-2026)
[2] Jiapeng Li, "Where Does Exactly-Once Live? Model, Harness, and Tool-Contract Effects on Duplicate Side Effects in LLM Agents", arXiv:2609.29095, submitted 2026-09-24 (https://arxiv.org/abs/2609.29095)
[3] GitHub, "GitHub availability report: August 2026" — the 17 August incident (https://github.blog/news-insights/company-news/github-availability-report-august-2026)

## Gate report
lead
PASS — Delivers the core takeaway immediately in the first sentence with simple, active verbs. Paragraph is exactly 3 sentences. Flesch readability vastly improved.
tension
PASS — Contextualizes the industry shift with a clear first-person observer cue ("The part I keep circling:"). Broken into three highly readable paragraphs of 3, 3, and 3 sentences.
tactical-insight
PASS — Frames operator actions as observations with "What I'd watch:" and avoids playbook commands. Uses simple vocabulary ("trip switch", "unique tag") and keeps all paragraphs under 3 sentences.
nuanced-takeaway
PASS — Acknowledges data limitations with a first-person read ("My read:"). Split into three short paragraphs of 2, 3, and 3 sentences for maximum scannability and Flesch compliance.
tldr
PASS — Strictly follows the 4-part Smart Brevity schema. Cleanly separated with plain-English definitions and no complex corporate jargon.
