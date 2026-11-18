---
title: "Your Timeout Is the Wrong Knob: 1 Turn in 9"
vertical: agentic_resilience_failure
kind: evergreen
archetype: evergreen
evergreen: true
persona: infra_engineer
date: 2026-11-18
slug: your-p99-is-a-product
one_big_thing: "A turn's p99 is the product of its steps' tails, not the maximum of them — at a 1% slow-call rate a twelve-step workflow makes 1 turn in 9 slow, a timeout cannot shorten that turn, and the only control that can, a duplicate request sent in flight, is permitted only for operations safe to run twice, so the latency policy is a per-tool classification decision rather than a global retry setting."
meta_title: "Your Timeout Is the Wrong Knob: 1 Turn in 9"
meta_description: "At a 1% slow-call rate a twelve-step agent turn runs slow 1 time in 9. A timeout cannot shorten it; the only fix is a duplicate request, legal only for reads."
image_path: "context/assets/illustrations/your-p99-is-a-product/featured.jpg"
image_style: "long_lens_industry"
image_model: "flux"
image_alt: "Your Timeout Is The Wrong Knob. Optical beam-splitter prism splitting one request into two duplicate paths, one dead-ending at a timeout"
image_caption: "Your Timeout Is The Wrong Knob: At a 1% slow-call rate a twelve-step agent turn runs slow 1 time in 9. A timeout cannot."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
The gRPC client does not wait for a call to fail. If a request has not answered in half a second, it sends a second copy. Then a third at one second, a fourth at 1.5 seconds, and it returns whichever answers first [1]. That is a hedge — a duplicate request sent while the original is still running — and it is the only control in the stack that shortens a slow call. A timeout just gives up on that call, which is why the knob most teams reach for is the wrong one.

An agent turn is a sequence of such calls. The p99, the latency that 99 of every 100 turns come in under, is set by the product of the steps, not by the worst step. Take a 1% slow-call rate across twelve steps, and 1 turn in 9 runs slow.

<!-- tldr -->
## At a glance
- **The shift:** A turn's tail is the product of its steps, not the maximum.
- **The number:** At 1% slow calls over 12 steps, 1 turn in 9 runs slow.
- **The risk:** A duplicate request shortens a slow turn only when the call is safe to run twice.

<!-- tension -->
## Why the multiplication happens

The chance of a slow turn follows from the chance of a slow step. Across twelve steps at a 1% slow rate, the chance that a turn holds at least one slow step is 1 − (1 − 0.01)^12, which is 11.4%. That is my arithmetic on the printed rate, not a quoted figure. At twenty steps it reaches 18.2%. The wait is worse than any single step suggests, because a turn finishes only when its slowest draw does: twelve draws from an 800-millisecond average sit near 2.5 seconds on the same arithmetic.

The knob in reach is a timeout, and it does not help with this. A timeout bounds how long a turn waits. It does not make a tool finish, so it turns a slow turn into a failed one and leaves the next run to draw again. Google's reliability engineers wrote the failure down years ago: slow responses hold a worker thread longer, the queue behind them grows, and a queue ten times the thread count turns a 100-millisecond request into a 1.1-second one [3].

Agents changed the price of the alternative, not its existence. A raced copy was cheap while the call it duplicated was a read. In an agent, the duplicated step is often a write: a ticket commented, a refund issued, a row altered. I have watched teams reach for the timeout slider because the copy felt unsafe. That instinct is right, and it moves the decision to the tool rather than the wrapper.

## By the numbers

- **0.5 seconds — the hedging delay:** The client sends a second copy after half a second without an answer [1].
- **80.4% — the error rate:** A frontend with 1,000 threads facing 5,000 queued requests errors 80.4% of them [3].
- **0 — nginx's try cap default:** Zero turns the next-upstream try limit off [4].

<!-- tactical-insight -->
## What the operators actually configure

The client that ships the control keeps it tight. gRPC stops at four attempts, and each later copy comes another 500 milliseconds after the one before it [1]. The rule for which calls may be raced sits in the spec, not in taste: hedging is "only enabled for methods that are safe to execute multiple times without adverse affect" [1]. The deadline covers the whole race, so once it passes the operation fails "regardless of in-flight RPCs" [1]. Copies buy a better draw, never more time.

The same spec shows what happens when the race stays on during an incident. Its throttle holds ten tokens, credits a tenth of a token per success and takes one per failure. It stops issuing copies once the count falls to five [1]. One failure therefore costs ten successes to repay, so the throttle goes quiet near a ten percent failure rate. That is the rate a brownout produces. Jitter of plus or minus 20% keeps the copies from marching in step [2].

Below the agent, the proxy has usually settled the same question already. nginx passes a failed request to the next upstream on error or timeout, and by default will not repeat a non-idempotent method at all, so a write request is not quietly re-sent [4]. Its try cap is the loose end: zero means no limit, and zero is the default. What I find hard to square is that the layer furthest from the model enforces the rule for which calls may be repeated, while the wrapper beside the model treats every tool alike.

<!-- nuanced-takeaway -->
## The catch

A copy is free only while the service has room. Sent into a full queue, it adds work to the same workers whose slowness caused it, and the queue math above is clear on where that ends [3]. Hedging buys a better draw and pays for it in load. A fleet that hedges a provider already at its rate limit buys the error sooner.

The other limit is the independence assumption. Slow calls cluster around one key, one provider or one incident. When they move together, a turn's real tail is worse than 1 − (1 − p)^k, so the number here is a floor. For a write, a copy is not a latency fix in any case. It is a second transaction, and the honest controls there are [a deadline picked from a false-timeout budget](/agent-timeout-false-alarm-budget/) and an idempotency check at the tool.

I would rather count the copies per tool than stretch one deadline across the turn. I would also want the queue's own depth next to that count before trusting either number. The decision belongs beside the tool's schema, not in a retry wrapper.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Your Agent's Next Step" -> /gate-the-step-not-the-model/ [same site (aichieve.net); same category; topical overlap: fail, wrong] Link "Your Agent's Next Step" in the section where the article touches fail, wrong. -->
<!-- internal-link hint: "Agent Timeouts: Pick 0.1%, Not a Round Number" -> /agent-timeout-false-alarm-budget/ [same site (aichieve.net); same category; topical overlap: timeout] Link "Agent Timeouts: Pick 0.1%, Not a Round Number" in the section where the article touches timeout. -->
<!-- internal-link hint: "Retry Budgets Fail" -> /retry-permission-leaves-the-caller/ [same site (aichieve.net); same category; topical overlap: fail] Link "Retry Budgets Fail" in the section where the article touches fail. -->
## Related reading

- [Your Agent's Next Step](/gate-the-step-not-the-model/) — more on Autonomous & Agentic Workflows
- [Agent Timeouts: Pick 0.1%, Not a Round Number](/agent-timeout-false-alarm-budget/) — more on Autonomous & Agentic Workflows
- [Retry Budgets Fail](/retry-permission-leaves-the-caller/) — more on Autonomous & Agentic Workflows
<!-- internal-links:end -->

## Sources

- [1] gRPC Authors, "gRPC Retry Design (gRFC A6)" — https://raw.githubusercontent.com/grpc/proposal/master/A6-client-retries.md
- [2] gRPC Authors, "Retry" guide — https://grpc.io/docs/guides/retry/
- [3] Google SRE, "Addressing Cascading Failures", Site Reliability Engineering — https://sre.google/sre-book/addressing-cascading-failures/
- [4] nginx, "Module ngx_http_proxy_module" — https://nginx.org/en/docs/http/ngx_http_proxy_module.html
