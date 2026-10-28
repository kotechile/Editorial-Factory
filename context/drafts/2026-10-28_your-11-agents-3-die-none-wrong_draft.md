---
title: "Your 11 Agents: 3 Die, None Wrong"
vertical: agentic_resilience_failure
persona: infra_engineer
one_big_thing: "An agent fleet fails as a queue, not as an error: in-flight work is arrival rate times latency, the shared key is spent by the sum of every agent's calls, and the measured fix is one gate in front of that key that owns the count, the rate-limit state and the retry queue — not a retry wrapper inside each agent."
date: 2026-10-28
slug: your-11-agents-3-die-none-wrong
archetype: evergreen
evergreen: true
---

<!-- lead -->
On 15 April 2026, eleven coding agents ran at once against one shared key, and three of them died before they finished. Two lost their connections, one got a bad gateway, and about 135,000 tokens went into runs that never ended [1]. None of the 11 agents was wrong: the calls were fine, the key was valid, and the vendor had room to serve all eleven one after another [1]. They failed because they were in each other's way.

<!-- tension -->

## The big picture:

Most agent frameworks act as if capacity were endless, so each agent retries on its own schedule and nobody owns the pool they all draw on [1]. That holds at two parallel runs and breaks at twenty, because the real limit is how much work is in flight at once, not the model or the prompt. Queueing theory has a name for it. Little's Law says the calls inside a system equal the arrival rate times the average time each call takes [2].

Once latency moves, the math turns. A server handling 100 messages a second at 100 milliseconds each holds about ten threads; let each call take ten seconds and the same traffic holds a thousand, enough to fill a thread pool [2]. Nothing in that sentence throws an error. Health checks stay green, the request rate looks normal, and the pool is full.

What strikes me here is why the fleet cannot see it coming. Each run reports its own tokens, its own tool calls and its own pass or fail. The one number that decides whether that run ends is how many other runs are calling at the same moment, and no single agent holds it. A run stopped by a rate limit looks much like a run that hit a random error, so every agent does the obvious thing and asks again.

<!-- By the numbers -->

## By the numbers

- **72–100% — Unmanaged failure:** across seven scenarios at 5 to 50 parallel agents, agents retrying on their own failed 72–100% of the time under load, while a shared gate cut failures to 0–18% and removed 48–100% of wasted compute [1].
- **81.8% — The cap alone:** the test of each piece is the useful part. Limiting parallel runs with nothing else in place still failed 81.8% of the time, and dropping the shared retry left 63.6%, so a bare semaphore is not the fix [1].
- **1,000 threads — What a slow call costs:** 100 messages a second at 100 milliseconds holds ten threads on average, and the same rate at ten seconds holds 1,000, which is Little's Law in practice [2].
- **50 percent — The uptime cliff:** when the median latency equals the client timeout, half of all requests are timing out, so a slow service turns into a down service [3].

<!-- tactical-insight -->

## What I'd watch:

The teams that get this right move the limit out of the agent and put it in front of the key. HiveMind, the open-source proxy behind those figures, sits between the agents and the vendor [1]. It admits work, tracks the vendor's rate-limit state, pushes back when latency rises, caps each agent's token spend and keeps one retry queue. Agents keep their code, and the shared key gets one owner.

- **Where the count lives:** a per-cluster cap guards a pool but says nothing about who spent it. Envoy's defaults make that plain, with circuit breakers on by default at 1,024 connections per cluster, counted per upstream rather than per caller [5]. A fleet that never sets its own cap inherits one written for someone else's traffic.
- **Who retries:** ten agents retrying a rate-limit error at the same moment is a stampede that trips the limit again, which is why the proxy runs retries through the gate [1]. Google pairs a cap of three tries per request with a retry share under 10% per client, because the per-request cap alone lets attempted load reach just under three times the original rate, while the share holds it near 1.1 times [4].
- **What gets dropped:** shed early. Reject excess work at the door and serve the newest requests first, so stale ones die instead of holding a slot [3].
- **What I'm watching next:** whether gateways ship a quota-aware mode by default, and whether vendors publish a per-key limit instead of leaving teams to find it through 429s. The proxy in that study added under 3 milliseconds per call, so the cost case against a gate is thin [1].

The fleet also has a meter nobody budgets, which reads well beside this one — [the second meter in an agent fabric](/agent-fleet-two-meters/) is where the harness spend hides.

<!-- nuanced-takeaway -->

## The catch

My read is that this is the best evidence yet for a fleet-level gate, and it is still one preprint. Seven scenarios, one team's setup, self-reported figures, and a live check against two local model servers rather than a public vendor's quota [1]. The direction fits decades of queueing practice, but nobody has repeated the exact failure rates.

The paper's own test undercuts the tidy version of the story. Retry turned out to matter most, not admission control, so a team that reads "cap the workers" and stops there lands on the 81.8% arm [1]. The gate works only when it holds the retry queue, the rate-limit state and the in-flight count together. That is more work than a semaphore, and it becomes a shared point of failure unless the proxy itself is redundant.

Fairness pays too. Serving newest-first keeps uptime and starves the long job, so the shed rule is a product call, not a switch [3]. And these limits date fast: concurrency windows, per-cluster defaults and vendor headers all move, so the lasting part is the math and the placement, not the numbers.

<!-- tldr -->

## At a glance

- **The Big Shift:** Agent fleets are failing as queues rather than as errors. Eleven unmanaged agents on one key lost three runs and a large pile of tokens on a day the vendor had room to spare, because the shared key — not any single run — was the limit.
- **Why It Matters:** Each run reports on itself, so the number that decides whether it ends lives in nobody's dashboard. That turns a capacity problem into a stream of retries, and retries spend the same quota the fleet is already short of.
- **What I'd Watch:** Where the limit sits, and whether the thing enforcing it can see every agent.
  - **One gate, one owner:** A shared proxy that admits work, tracks the vendor's rate-limit state and runs retries in order — the shape measured in the fleet study.
  - **In-flight count:** Arrival rate times latency, worked out from your own logs, is the number of parallel runs the pool really needs.
  - **Shed rule:** Which requests get refused first decides who pays for the overload.
- **The Catch:** The evidence is one preprint with a promising but unrepeated result, the gate adds a hop and a shared point of failure, and its own test says retry discipline matters more than the worker cap most teams would build first.

## Sources

[1] Agyemang, Kponyo, Somuah, Amponsah, Boakye, Agyekum. "HiveMind: OS-Inspired Scheduling for Concurrent LLM Agent Workloads." arXiv:2604.17111v1, submitted 18 April 2026. https://arxiv.org/html/2604.17111v1
[2] AWS Builder Center. "Avoiding insurmountable queue backlogs." https://aws.amazon.com/builders-library/avoiding-insurmountable-queue-backlogs/
[3] AWS Builder Center. "Using load shedding to avoid overload." https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/
[4] Google. "Site Reliability Engineering," chapter 21, Handling Overload. https://sre.google/sre-book/handling-overload/
[5] Envoy documentation. "Circuit breaking" (upstream architecture overview). https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/upstream/circuit_breaking
