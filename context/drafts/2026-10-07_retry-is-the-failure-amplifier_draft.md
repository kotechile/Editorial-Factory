---
title: "The Retry Is the Bug: An Agent's Recovery Is Its Costliest Failure Mode"
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
A corrupted null value in a single ledger entry was all it took. The accounting agent could not format the record, so it retried — and retried — and in under an hour it had made more than 15,000 reasoning calls, run up a roughly $50,000 cloud bill, and locked the billing database hard enough to halt live transactions [1]. No attacker touched the system and no prompt injection was involved. The recovery action was the incident.

<!-- tension -->

## The big picture:

The whole 2026 agent-reliability playbook says the same thing: give the agent a loop, a retry, and a recovery path, and let it work past a bad step. The math behind it is real — if a single step succeeds 95% of the time, a ten-step chain lands about 60% of the time, so recovery is the only way to finish long tasks. But I keep coming back to what the retry actually does when the failure is not clean. The Mandiant report on the ledger agent is blunt that the loop did not crash or corrupt anything; it "brute force[d] a fix" and the fix was the damage [1]. A separate study published Sept. 24 puts a number on the same primitive at the call level: when an agent cannot tell whether a timed-out write already landed, retrying it duplicates the write in 56% of episodes, and in 74% when the network quietly delivered the request twice [2].

## By the numbers

- **15,000+ — Reasoning calls in one hour:** A ledger-reconciliation agent with read/write access to its billing databases hit one corrupted null value and entered what Mandiant calls "an unconstrained, recursive reasoning loop" [1].
- **~$50,000 — Cloud-billing spike:** The same under-an-hour run also caused "severe local database locking that halted active business transactions" — cost and outage from one fault [1].
- **56% and 74% — Duplicate-write rate:** Across 25,930 graded episodes spanning nine models and three production agent harnesses, frontier models that verify before retrying still duplicated a write in 56% of in-flight cases and 74% under redelivery [2].
- **90% — Agents that reported success anyway:** "In 90% of episodes that produced a duplicate, the agent reported the task as completed" — so the run's own success signal hides the second charge [2].

<!-- tactical-insight -->

## What I'd watch:

What strikes me is that both failures trace to the recovery policy, not to the model. The study is explicit: the harness barely matters, and a faster model does not close the gap on its own — the tool contract explains 81% of the duplicate variance once a request is in flight [2]. So the controls worth watching are the unglamorous ones the two sources agree on.

- **A bounded retry, not an open one:** Mandiant's own remedy is a circuit breaker that halts the agent "after a set threshold of consecutive task failures," plus bounded recursion limits and rate limits [1]. GitHub reached for the same lever after a 7-hour-35-minute outage it blamed on "a latent client retry bug [that] sharply amplified traffic" [3].
- **The idempotency key at the contract, not the prompt:** offer a key on every write and the duplicate rate in the study fell from 28% to 4%, and exactly-once success reached 99% [2].
- **A cost and loop signal in the trace:** the doomed run's tell was not an error line — it was 15,000 calls and a rising bill [1]. Token spend per run, and consecutive-failure count, are the two series that would have caught it.

I'd want to know whether the teams shipping these agents treat retry count as a monitored metric or as a framework default nobody set.

<!-- nuanced-takeaway -->

## The catch

The obvious counter-read is that this is two isolated data points. One is a vendor's case study of a single incident; the other is a sandbox, not production, and the sandbox faults are injected on purpose. The study also shows the problem shrinks to near zero when a write's outcome can be read back — frontier models told to act once duplicated on only 0.5% of those episodes [2]. My read is that this makes the fix cheaper, not the risk smaller: the failures that survive are exactly the ones where read-back cannot help, and those are the writes that move money. Duplicate charges and double deployments do not announce themselves, and the agent will not tell you. I could be wrong that a bounded retry is the whole answer — a tight retry bound can also skip required work, which is its own failure. But "add a retry and hope" is no longer a defensible default.

<!-- tldr -->

## At a glance

- **The Big Shift:** A runaway ledger agent showed that an agent's retry can be the failure, not the fix — more than 15,000 calls and a $50,000 bill from one bad value — and a new 25,930-episode study shows the same retry silently duplicating writes the agent believes it made once.
- **Why It Matters:** Retry-and-recover is the standard prescription for flaky agents, but an unbounded retry turns one transient fault into a five-figure bill or a duplicate payment, and the agent reports success while it happens, so nothing in the run looks wrong until the invoice arrives.
- **What I'd Watch:** Whether teams move the fix out of the prompt and into the retry policy and the tool contract:
  - **Bounded retry and circuit breakers:** stop the loop after a set number of consecutive failures instead of letting it self-correct indefinitely.
  - **Idempotency keys on every write:** a unique tag the client attaches so the server can tell a repeat from a new request, which cut duplicates from 28% to 4% in the study.
  - **Per-run spend and failure-count telemetry:** the two series that make a runaway loop visible before the bill does.
- **The Catch:** Two data points, one a single-incident case study and one a lab sandbox; and cutting retries too hard starts skipping required work instead.

## Sources
[1] Mandiant, *AI Risk and Resilience* special report, September 2026 — Case Study 6, "Denial-of-Wallet using rogue reasoning loop" (https://cloud.google.com/security/resources/ai-risk-and-resilience-2026)
[2] Jiapeng Li, "Where Does Exactly-Once Live? Model, Harness, and Tool-Contract Effects on Duplicate Side Effects in LLM Agents", arXiv:2609.29095, submitted 2026-09-24 (https://arxiv.org/abs/2609.29095)
[3] GitHub, "GitHub availability report: August 2026" — the 17 August incident (https://github.blog/news-insights/company-news/github-availability-report-august-2026)
