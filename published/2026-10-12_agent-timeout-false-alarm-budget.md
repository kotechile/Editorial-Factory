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
image_path: "context/assets/illustrations/agent-timeout-false-alarm-budget/featured.jpg"
image_style: "studio_object"
image_model: "flux"
image_alt: "Agent Timeout Budgets. An intricate brass mechanical timer and steel calipers on a slate surface."
image_caption: "Agent Timeout Budgets: Why lazy timeout settings break agent retry loops."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Amazon sets a call timer by deciding how often it can be wrong. The cloud giant picks a budget for false alarms; its published standard is 0.1%. It then traces that back to the speed of the service it calls, reading the 99.9th percentile [1].

In an AI agent, that number is written into the wrapper by hand, and the model never sees the clock.

<!-- tension -->

## The big picture:

An agent tool call is a request made at least once, with a planner hitting the retry button.

That mix is new, but the ways it breaks are old. A timed-out call leaves a mystery: it might have run, or it might have dropped [1]. The normal fix is to try again, and the normal cost is system load.

Amazon shows how fast that cost grows. A stack five layers deep, with three tries at each step, multiplies the load on the shared database 243 times over. The tries stack up: three, nine, 27, 81, 243 [1].

Agents create that retry loop on their own. The τ-bench study tracked tool-using agents on retail and airline tasks; the best models finished fewer than half, and repeat runs agreed under a quarter of the time [5].

An agent that fails half its tasks is an agent trying over and over.

What I keep circling: the model has no sense of time. It picks a tool and waits for an answer. The deadline lives in the outside code next to the rate limit, usually set as a lazy round number copied from someone else.

## By the numbers

- **0.1% — False-timeout budget:** Amazon chooses how often a call can wrongly be marked dead (0.1%), then reads that speed off the service it calls (the 99.9th percentile) [1].
- **243x — Retry load:** Independent retries on a five-deep call stack multiply the load on a shared database 243 times over [1].
- **Under 50% — Agent success:** Top tool-calling agents finish fewer than half of their tasks, and that mixed success drives heavy retry loops [5].
- **100 seconds — Retry ceiling:** Temporal's default rule doubles the wait between tries, scaling from a 1-second first try to a 100-second cap [3].

<!-- tactical-insight -->

## What I'd watch:

I have been watching how agent code exposes the deadline. It is the one critical setting the model cannot reach.

- **The per-tool budget:** Reading a small record and calling a heavy model do not deserve the same timer. Amazon treats 20 milliseconds as too tight for a fresh connection. A timer below the connection cost starts retries on its own [1].
- **Who retries:** Amazon builds retries directly into its client libraries, and has since 2016. The first try often happens under the model's feet [1]. Counting tries at just the agent layer hides the other four layers.
- **The key window:** Stripe answers a repeated request from a saved response. It keeps the idempotency key (a label that makes a repeat safe) for at least 24 hours [4]. A retry that outlives that window is treated as a new request, so the side effect can land twice.
- **Contention, not just delay:** Adding random wait times across 100 competing clients cuts the call count by more than half, while the total work still grows with the square of the crowd [2]. An agent fleet acts exactly like one.

My read: the deadline is a strict budget choice, yet in most stacks I see, it happens purely by default.

<!-- nuanced-takeaway -->

## The catch

The honest limit is that most of this proof covers basic service calls and payment requests, not agents.

Amazon, Stripe, and Temporal are describing deterministic systems doing what they were told. The agent side rests on a single test of made-up retail and airline tasks [5]. Joining the two is my read of the setup, not a finding in any of them.

A longer timer is not a free pass, either. A call that waits holds a server worker and a queue slot. Padding every deadline just buys a slower failure.

I could be wrong about how quickly agent builders will adapt. The test I look for next: whether a run's own logs print the exact deadline and retry count beside each tool call.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Tool-List Budget: How Many Tools One Agent Can Hold" -> https://giniloh.com/agent-tool-count-ceiling/ [same site (giniloh.com); same category; topical overlap: agent, pick] Link "Tool-List Budget: How Many Tools One Agent Can Hold" in the section where the article touches agent, pick. -->
<!-- internal-link hint: "Agent Memory Poisoning" -> https://giniloh.com/agent-memory-poisoning-write-path/ [same site (giniloh.com); same category; topical overlap: agent] Link "Agent Memory Poisoning" in the section where the article touches agent. -->
<!-- internal-link hint: "Durable Execution Is Not a Transaction" -> https://giniloh.com/durable-execution-not-a-transaction/ [same site (giniloh.com); same category; topical overlap: agent] Link "Durable Execution Is Not a Transaction" in the section where the article touches agent. -->
## Related reading

- [Tool-List Budget: How Many Tools One Agent Can Hold](https://giniloh.com/agent-tool-count-ceiling/) — more on Autonomous & Agentic Workflows
- [Agent Memory Poisoning](https://giniloh.com/agent-memory-poisoning-write-path/) — more on Autonomous & Agentic Workflows
- [Durable Execution Is Not a Transaction](https://giniloh.com/durable-execution-not-a-transaction/) — more on Autonomous & Agentic Workflows
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** Agent code retries tool calls just like older systems, but the retry now sits inside a blind loop driven by the model. Amazon sets a call timer from an accepted false-alarm rate (0.1%) and its matching speed; agent stacks rarely calculate either number.
- **Why It Matters:** A loose deadline pushes its cost onto the shared service, where retries at each layer multiply load 243 times over. A tight deadline is worse, because a timer shorter than the connection time turns a slow success into a forced retry.
- **What I'd Watch:** Whether the deadline becomes a per-tool setting a team can read, rather than one round number copied between stacks.
  - **Per-tool budgets:** A separate timer for each tool, set from that service's own speed, so a slow model call and a fast record read stop sharing one number.
  - **Retry ownership:** A single place that counts attempts, since client tools already retry without asking.
  - **Key lifespan:** Whether the idempotency key window is checked against the longest a retry can run.
- **The Catch:** The service-side proof is strong, but the agent-side proof relies on one test of simulated tasks. A longer timer also holds a worker, making a loose deadline a real trade rather than a free fix.

## Sources
[1] Marc Brooker, "Timeouts, retries, and backoff with jitter," AWS Builders' Library, published 2026-06-12, modified 2026-06-15. https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
[2] Marc Brooker, "Exponential Backoff And Jitter," AWS Architecture Blog. https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/
[3] Temporal documentation, "Retry Policies." https://docs.temporal.io/encyclopedia/retry-policies
[4] Stripe API documentation, "Idempotent requests." https://docs.stripe.com/api/idempotent_requests
[5] Yao et al., "τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains," arXiv:2406.12045 (2024-06-17). https://arxiv.org/abs/2406.12045

## Gate report
lead: PASS — Direct, punchy opening that states the core news immediately. Uses plain English to explain the false-timeout concept.
tension: PASS — Clean structural H2. Plain English explanation of retry mechanics, simplified vocabulary to boost Flesch score, and clear first-person observer cue.
tactical-insight: PASS — Clear "What I'd watch:" H2. Bulleted observations of operator moves rather than imperative commands. Includes clear observer cue.
nuanced-takeaway: PASS — Honest limitation cleanly stated under "The catch". Includes observer cue ("my read", "I could be wrong"). Sentences shortened for readability.
tldr: PASS — Strict 4-part Smart Brevity format. Distinct H2 header, formatted exactly to spec, distinctly summarizing the article with simplified vocabulary.
