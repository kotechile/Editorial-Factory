---
title: "Agent Timeouts: Pick 0.1%, Not a Round Number"
vertical: agentic_ai
persona: ai_architect
one_big_thing: "An agent tool call is an at-least-once call whose retry sits inside a loop the model drives, so the deadline has to be derived from a stated false-timeout budget and the downstream latency it implies, not copied as a round number into every wrapper."
date: 2026-10-12
slug: agent-timeout-false-alarm-budget
archetype: evergreen
evergreen: true
meta_title: "Agent Timeouts: Pick 0.1%, Not a Round Number"
meta_description: "Amazon sets a call timeout from an accepted false-timeout rate of 0.1%, then reads the downstream p99.9. Most agent stacks pick one round number instead."
---

<!-- lead -->
Amazon sets a call timeout by first deciding how often it is willing to be wrong. Its practice, written up in the company's own engineering library, is to pick an acceptable rate of false timeouts — 0.1% is the figure it prints — and then read the matching latency point off the service being called, the 99.9th percentile in that example [1]. In an agent, that number is set in code, and the model that picks the tool never sees it.

<!-- tension -->

## The big picture:

An agent tool call is an at-least-once call with a planner sitting on the retry button.

That mix is new. Its failure modes are not.

A call that times out has an outcome nobody knows: it may have run, or it may not have [1]. The common fix is to try again, and the common cost is load.

Amazon's own numbers make that cost plain. A five-deep stack of calls, with three tries at each layer, multiplies the load on the shared database by 243 — three tries, then nine, then 27, then 81, then 243 [1].

Agents do that retrying on their own. The τ-bench study put tool-using agents on retail and airline tasks and found the best of them finishing under half, with repeated runs agreeing only about a quarter of the time [5]. An agent that fails half its tasks is an agent that retries a lot.

What I keep circling: the model has no view of the clock. It picks a tool and reads what comes back. The deadline lives in the harness, beside the retry count and the rate limit. Most stacks I look at set one round number there for every call, because a round number is what everyone else copied.

So the interesting question is not which model. It is who sets the deadline, and what they set it from.

## By the numbers

- **0.1% — The false-timeout budget:** Amazon's rule is to choose how often a call may be wrongly declared dead (0.1%), then read that latency point off the downstream service (the 99.9th percentile). The timeout falls out of an error budget rather than being picked by hand [1].
- **243x — Retry load:** On a five-deep call stack with three tries at each layer, independent retries multiply the load on the shared database 243 times over, which is how a slow query becomes an outage [1].
- **under 50% — Agent success:** The τ-bench study found leading tool-calling agents finishing fewer than 50% of their tasks, with only about a quarter of repeated runs landing the same way. Inconsistency is what drives the retry [5].
- **100 seconds — Retry ceiling:** Temporal's default policy doubles the gap between tries, from a 1-second first attempt to a 100-second cap, and leaves the attempt count unlimited unless a team sets it [3].

<!-- tactical-insight -->

## What I'd watch:

I have been watching how harnesses expose the deadline, because it is the one setting the model cannot reach.

- **The per-tool budget:** Reading a small record and calling a model do not deserve the same timer. Amazon's write-up treats 20 milliseconds as too tight for a fresh connection, and a timer below the cost of connecting starts the retries by itself [1]. I would want that budget published per tool, not per runtime.
- **Who retries:** Amazon has built retries into its own client libraries since 2016, so the first try again often happens under the model's feet [1]. Counting attempts at one layer hides the other four.
- **The key window:** Stripe answers a repeated request from a saved response, keeps the idempotency key (a label that makes a repeat safe) for at least 24 hours, and accepts keys up to 255 characters [4]. A retry that outlives that window is a second charge waiting for a quiet release.
- **Contention, not just delay:** In the backoff simulation, adding jitter at 100 competing clients cut the call count by more than half, while the total work still grew with the square of the crowd [2]. An agent fleet is a crowd.

My read: the deadline is a budget decision, and in most stacks I see it is being made by default.

<!-- nuanced-takeaway -->

## The catch

The honest limit is that most of this evidence is about service calls and payment requests, not agents.

Amazon, Stripe and Temporal are describing deterministic systems doing what they were told. The agent side rests on one benchmark of made-up retail and airline tasks [5]. Joining the two is the argument of this piece, not a finding in any of those sources.

A longer timer is not free either. A call that waits holds a worker and a slot, so padding every deadline buys a slower failure and a fuller queue.

I could be wrong about how quickly harnesses move here. The test I would apply: whether a run's own logs print the deadline and the retry count beside each tool call. Until they do, the 99.9th percentile that should set the number stays unmeasured.

<!-- internal-links -->

<!-- tldr -->

## At a glance

- **The Big Shift:** Agent runtimes retry tool calls the way distributed systems have always retried requests, except the retry now sits inside a loop the model drives. Amazon sets a call timeout from an accepted false-timeout rate (0.1%) and the latency point that goes with it (the 99.9th percentile); agent stacks rarely derive either number.
- **Why It Matters:** A loose deadline pushes its cost onto the shared service, where independent retries at each layer multiply load 243 times over. A tight one is worse, because a timer below connection time turns slow success into a retry, and Stripe's 24-hour key window is what stands between a retry and a duplicate charge.
- **What I'd Watch:** Whether the deadline becomes a per-tool setting a team can read, rather than one round number copied between stacks.
  - **Per-tool budgets:** A separate timeout for each tool, set from that service's own latency, so a slow model call and a fast record read stop sharing one number.
  - **Retry ownership:** A single place that counts attempts, since client libraries already retry without asking.
  - **Key lifespan:** Whether the idempotency key window is checked against the longest a retry can run.
- **The Catch:** The service-side evidence is strong and the agent-side evidence is one benchmark on made-up tasks. A longer timer also holds a worker, so a loose deadline is a real trade rather than a free fix.

## Sources
[1] Marc Brooker, "Timeouts, retries, and backoff with jitter," AWS Builders' Library, published 2026-06-12, modified 2026-06-15. https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
[2] Marc Brooker, "Exponential Backoff And Jitter," AWS Architecture Blog. https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/
[3] Temporal documentation, "Retry Policies." https://docs.temporal.io/encyclopedia/retry-policies
[4] Stripe API documentation, "Idempotent requests." https://docs.stripe.com/api/idempotent_requests
[5] Yao et al., "τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains," arXiv:2406.12045 (2024-06-17). https://arxiv.org/abs/2406.12045
