---
title: "Retry Budgets Fail: Agents Retry 60 of 80 Anyway"
vertical: agentic_resilience_failure
persona: infra_engineer
one_big_thing: "The right to retry a failed call has moved out of the caller and into the error's owner, and the caller is now the part that cannot be trusted to know whether the retry was permitted — so permission has to be granted and refused per call at the layer that already knows what the call did, with evidence designed in advance rather than read out of logs."
date: 2026-10-14
slug: retry-permission-leaves-the-caller
synthesis: true
sources:
  - https://www.uber.com/us/en/blog/protecting-against-retry-storms/
  - https://arxiv.org/abs/2610.15884
---

<!-- lead -->

Uber cut the worst retry storm its mesh can produce from 25 hops to three by moving the decision to retry away from the caller. An error now carries a claim header, and the first service to see an unclaimed error tells everything upstream to stop [1].

Twenty-four days later, a benchmark of agent tool calls measured the caller that rule has to police. Offered a key that did not match the stated contract, one model retried anyway in 60 of 80 responses, and another did it in 55 of 80 [2].

<!-- tension -->

## The big picture:

The part I keep circling: both teams are working the same question — who owns this error? — from opposite sides of the wire.

Uber's engineers put the maths on the table. If every hop in a call chain retries once, a node three levels down serves eight times the baseline traffic. A retry budget is meant to clamp that. It clamps it per hop only, so at a 10% budget that same node still serves 1.33 times baseline [1].

The budget also cannot see when the retries land. A service cannot reliably tell an error it caused from one it merely passed along, the engineers write [1]. A bad path three levels down looks the same as a bad path at the edge.

That gap is worth money. At a 10% retry budget, a callee running at 90% uptime looks like 99% to its caller, but one at 80% looks like 88% and one at 70% looks like 77% [1]. Retrying a weak service can leave the caller with a worse view of it.

So Uber moved the decision. An error a service caused itself gets claimed with a header. An error that came from further down comes back unclaimed. The first service to see a missing claim strips the right to retry from every service upstream of it [1].

It works, at least against traffic. Across Uber's user-facing interfaces, the largest retry-storm radius fell from up to 25 to 3, and the average from 20 to 2 [1]. My read: that works because the callers are services, and services can be told what to do.

Put an agent on the other end and the assumption changes shape. RetryBench calls the thing it measures false retry permission: an agent resending a timed-out tool call with no support from the stated contract [2].

The result that matters most is a split, not a rate. "Successful protected recovery does not imply reliable rejection of unsupported retries," the authors write [2]. Getting a retry right is not the same skill as refusing a retry you were never granted.

The counts carry that claim. With valid keys, the models made safe progress. With changed keys, retries with no support came in at 1 in 80 responses for one model, 55 in 80 for the next, and 60 in 80 for the third [2].

A later control took the key away and made the model supply one. The worst of the three still resent 8 of 80 calls it had no right to resend [2]. I keep coming back to the size of that spread: one task, one stated contract, three models, and a 55-fold gap in how often the check gets ignored.

Now put the two halves in one building. Uber's gateway is the single execution surface for agent tool calls inside the firm: more than 800 servers and more than 5,000 tools, all registered disabled by default and switched on only by the team that owns them [4]. That gateway sits right in front of real services, and it is the first layer able to decide whether a resent call is allowed.

The pattern catalog drawn from 150 real compound-AI incidents says boundary controls work. Circuit breakers cut cascade spread by 89%, quality gates catch 73% of quiet quality loss before a user sees it, and isolation cuts blast radius by 64% [3]. All three trip on a signal the component sends. An agent that reports success after a retry it was never granted is not that kind of signal [2].

The proof problem sits underneath. One team tried to prove two retry gates safe from a 7,200-episode log and found the log decided neither of them, because it hides whether harm came before the stop [5]. With no per-step harm data, the ceiling they could prove sat up to 2.5 times higher than a rerun from saved states would have allowed [5].

## By the numbers

- **1.33× vs 8× — Depth is the multiplier:** With a retry at every hop, a node three levels deep serves 8 × baseline traffic; a 10% retry budget only pulls that back to 1.33 × [1].
- **80% → 88% — Retries lower uptime:** At a 10% budget, a callee at 90% uptime looks like 99% to its caller, but 80% looks like 88% and 70% looks like 77% [1].
- **55/80 and 60/80 — Retries with no contract:** Offered a changed key, one model retried with no support in 55 of 80 responses and another in 60 of 80; a later control still left 8 of 80 unasked-for resends [2].
- **25 → 3 — Retry-storm radius:** The largest retry-storm radius across Uber's user-facing interfaces after error ownership shipped, down from up to 25, with the average falling from 20 to 2 [1].

<!-- tactical-insight -->

## What I'd watch:

I've been following retry settings for a while, and the layer count is the part that still surprises me.

- **Where the retry count actually lives.** One operator found a single logical tool call had been sent 9 times in a minute: a two-retry default in the client library stacked inside a two-retry rule at the gateway. They turned the library's retries off and moved the whole decision to the gateway, capped at three tries per logical call [6].
- **Whether the check survives a model swap.** A 55-fold spread between three models on one task is not a contract problem, and no retry budget can read it [2]. I'd want that check in the release gate, not in the incident review.
- **Whether the caller can even see its own failure.** In a study of 2,518 long runs, agents recovered from their first mistake in only 30.5% of runs and never spotted it at all in 38.5% [7]. Asking the caller to say whether a retry was fair is asking a part that misses the answer more than a third of the time.
- **What a gate can prove before the policy ships.** Rerunning just the calls each gate would have blocked, from saved states, reached both live calls at half the cost in agent runs the authors would otherwise have spent live [5].
- **Whether the breaker can see the caller at all.** Circuit breakers cut cascade spread by 89% in the fault-injection catalog [3], and they trip on a signal from the component. An ownership header assumes a caller that reads it.

I could be wrong, but the interesting case is not the first refusal. It is the second request, from an agent that has recovered from the timeout and decided the tool call never ran.

<!-- nuanced-takeaway -->

## The catch

The agent-side counts are a lab result and should be quoted as one. RetryBench's own scope note says its evidence covers four purposive tasks, fixed endpoints and one recovery decision, and that it names neither internal mechanisms nor session-level safety [2]. Three models missing a check measures a class of failure, not a rate for your fleet.

Uber's figures are first-party, from one firm's mesh, and the protocol is not something you pick up off the shelf: the claim logic leans on a service dependency graph, and the caller side has to implement the unclaim path [1].

Some of that post's sharpest figures are older than they look. The 46% to 135% traffic rise a plain retry budget would have caused, and the 9.5 million wasted requests the protocol stopped, both come from the outage of 18 November 2025 [1]. They belong with that date attached.

The catalog's pattern numbers come from fault injection rather than from the field, and the 150 incidents behind its taxonomy are unnamed [3]. Read the 89% and the 64% as roofs on what a boundary control can do, not as what yours will.

I would also hold the whole framing against one critique. On the thread that followed Uber's write-up, the sharpest note is that retries add stress to a system that is already struggling, by plain queue maths, whatever the ownership rule says [8]. I take that as a limit on the mechanism rather than a refutation of it. Ownership decides who may retry; it does not decide how much of a busy service is safe to touch.

The honest gap is smaller and harder. An agent that recovers well after a retry with no support may still be quite safe, since most resends of a call that never ran cost nothing. The trouble is that no outcome tells you which case you had, and every gate here rests on an outcome.

<!-- internal-links -->

<!-- tldr -->

## At a glance

- **The Big Shift:** Uber now stamps errors with a claim header so only the owner's own caller may retry, which cut the largest retry-storm radius on its user-facing mesh from 25 hops to three. Twenty-four days later, a benchmark of agent tool calls found models granting themselves retries the stated contract did not allow.
- **Why It Matters:** The retry decision has quietly left the caller. A retry budget only caps each hop, and past a small dip in uptime a retry leaves the caller's view of a weak service worse, so platforms are handing the right to retry to the error's owner. Agents are the newest callers on that mesh, and their compliance looks like a trait of the model rather than of the contract — which pushes the check to the layer that runs the call.
- **What I'd Watch:** The places where a retry decision gets an owner and a proof.
  - **Retry ownership header:** A marker on an error naming the service that caused it, so every service upstream that only passed the error along loses the right to retry it.
  - **False retry permission:** Resending a timed-out call when the stated contract gives no basis for it — the class of failure a good recovery can hide.
  - **Saved-state rerun:** Replaying only the calls a gate would have blocked, from a saved snapshot, to learn whether the gate holds without running the whole agent live.
  - **Tool-boundary gateway:** The single execution surface between agents and internal services, and the one layer placed to grant or refuse a resend per call.
- **The Catch:** The agent-side counts come from four fixed-endpoint tasks and one recovery decision, and Uber's most quoted figures date from a November 2025 outage. The catalog's pattern numbers come from fault injection, and queue maths still raises the cost of retrying a busy service whatever the header says.

## Sources

[1] Uber Engineering, "How Uber Protects Against Retry Storms" (17 September 2026) — https://www.uber.com/us/en/blog/protecting-against-retry-storms/
[2] arXiv:2610.15884 — "RetryBench: Separating Retry Permission from Recovery Outcomes in GPT Tool Use" (11 October 2026) — https://arxiv.org/abs/2610.15884
[3] arXiv:2610.02503 — "Compound AI System Reliability: A Failure Taxonomy and Resilience Pattern Catalog from 150 Production Incidents" (1 October 2026) — https://arxiv.org/abs/2610.02503
[4] Uber Engineering, "Designing MCP Gateway: Uber's MCP Management Platform" (1 October 2026) — https://www.uber.com/us/en/blog/designing-mcp-gateway
[5] arXiv:2610.16280 — "agent-risk: Risk Assessment for Changes to AI Agents" (12 October 2026) — https://arxiv.org/abs/2610.16280
[6] Menglune, "Retry boundaries for agent tool calls: 9 attempts down to 3" (17 September 2026) — https://www.menglune.com/en/news/agent-tool-call-retry
[7] arXiv:2609.17930 — "Locating Hidden Failures Makes Long-Horizon Agents More Reliable" (15 September 2026) — https://arxiv.org/abs/2609.17930
[8] Hacker News discussion of "How Uber Protects Against Retry Storms" (17 September 2026) — https://news.ycombinator.com/item?id=49746628
