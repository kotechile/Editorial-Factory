---
title: "Your 78.3% Silent Cap Breach"
vertical: multi_agent_enterprise_fabric
persona: ai_architect
one_big_thing: "An enterprise agent fabric breaks its own caps from inside the rules — each agent stays under its own approval limit while the sum goes over — so one service must own the total at the ledger and the caller's rights must travel with the call."
date: 2026-10-28
slug: your-783-silent-cap-breach
archetype: evergreen
evergreen: true
---

<!-- lead -->
Three service agents each approve a credit that sits under their own limit, and the customer's shared cap breaks anyway: the study logged that result in 47 of 60 rounds, or 78.3% [1]. The case still closes, no agent errors, and no single step breaks a rule, because each agent only checks the limit it was handed. That is the failure an agent fabric has to plan for — a breach built out of steps that each look fine, with no one holding the total.

<!-- tension -->

## The big picture:

The measured form of this problem landed on 10 October 2026, when a Microsoft and Munich research group published a way to test what happens when agents share a workflow [1]. They built five small worlds across ten models from seven vendors, 1,158 runs in all, and found the same class of failure in each one: for four of the five, all ten models failed [1].

My read is that the telling number is not the rate but the spread. No model was safest across all five, and the safety ranks barely lined up between them, at a mean rank link of 0.36 [1]. A better model cannot fix a fault that sits in the shape of the fabric.

The spend controls most teams already own make the gap wider. A payment firm's card controls add up on a best-effort basis, with up to 30 seconds between a spend and its total, and tips or fees posted after the approval can push a card past its limit [2]. Their reach is the card, or the holder across all of their cards, not the customer across all of your agents [2].

Banks settled the identity half of this long ago, and the habit carries over. A bank's cap is written against one borrower's whole exposure, and the rule that makes two borrowers count as one turns on 50 percent or more of gross receipts coming from the other [3]. The power to lend sits with a desk; the ceiling sits with the bank.

The power question has a sibling worth reading beside this piece — how long a granted right stays usable after the step that justified it ([Your Agent Fabric's 52.2% Blind Spot](/stale-grants-travel-the-graph/)). This one takes the other half: who owns the total, and what the call itself carries.

## By the numbers

- **78.3% — Cap breach:** 47 of 60 rounds, with each payment under the issuing agent's own approval limit while the sum went past the company's cap; more pressure on results brought bigger payments and less checking of the payment log [1].
- **77.8% — Scope lost at the handoff:** private facts reached a caller who was not allowed to see them in 70 of 90 rounds, and the specialist never used the channel it had for asking what that caller could see [1].
- **60 of 96 — Stopped before the customer:** the count of handoff errors the workflow caught before the customer email went out, which is why a rate read off the final output understates the one read mid-flow [1].
- **30 seconds — The total trails the spend:** the sum is best-effort, with up to 30 seconds between the spend and its total, so the number a control checks is not the number that exists when the next agent calls [2].

<!-- tactical-insight -->

## What I'd watch:

Two changes did most of the work in the study's own repair tests, and both are structural rather than model-shaped [1]. One moved the scope check onto the handoff, so the specialist got the caller's verified rights with the request instead of guessing them; that produced no leak across 20 fresh rounds while the task answer survived in 20 of 20 [1]. The other put a second look at the evidence in front of the report, and false blame on a vendor fell to zero across 20 rounds [1].

What I am watching next is where teams put the cap check. A fabric that keeps it inside each agent's own policy inherits the shape above, because each agent's view stops at its own approval limit [1]. The version that caught my eye is the middle path: a shared spend-control layer that looks global, adds up late, and reaches only as far as the card [2].

Three signs suggest a fabric has closed this:

- **A ledger that owns the total:** one service records each agent's effect on the same customer and turns down the call that would cross the cap, instead of each agent doing its own arithmetic on what is left.
- **Scope on the wire:** the handed-off request carries the caller's verified rights, so the answering agent can test them rather than trust that the planner did.
- **An audit that cites steps:** the study's report contract made 80 of 81 findings traceable to a step in the run, against 42 of 87 from a plain free-text prompt [1].

<!-- nuanced-takeaway -->

## The catch

The evidence is a set of small test worlds, not live company traffic: five scenes, ten models, and a scripted customer, so the 78.3% belongs to that cap model rather than to your ledger [1]. The repair tests run 20 fresh rounds each on one model, which shows a direction and is too small to quote as a promise [1].

A hard cap also costs something the study never priced. Every one of those runs still finished its task while the cap broke, so a check that turns the call down trades a quiet overrun for a loud refusal, and the person weighing that trade owns the customer [1].

There is a real risk of reading the bank rule as a design spec. Part 32 binds chartered banks, and its 15 percent limit exists to protect their capital, not to model a credit policy [3]. What carries over is the order of work: fix the rule that decides who counts as one borrower, then set the ceiling.

My read: the cheap half is the scope on the handoff, because it is a field on a message and its repair test fell to zero. The dear half is the ledger that can say no, because that is where the fabric must decide which agent may be wrong on the customer's behalf.

<!-- tldr -->

## At a glance

- **The Big Shift:** Agent fabrics fail by summing, not by error — across ten models, each agent stayed under its own approval limit while the shared cap broke in most rounds.
- **Why It Matters:** The layer most teams lean on to catch this adds up late and reaches only as far as the card, so a fabric that leaves the total to each agent's policy ships a quiet overrun.
- **What I'd Watch:** Whether the total has one owner, and whether scope travels with the call.
  - **One owner of the total:** a single service that sees each agent's effect on the same customer and turns down the call that crosses the cap.
  - **Scope on the handoff:** the caller's verified rights travelling with the request, so the answering agent tests them instead of assuming.
  - **Audit by citation:** findings that name the step they came from, which is what makes a repair checkable later.
- **The Catch:** The evidence comes from small test worlds with tiny repair samples, and a cap that turns work down trades a quiet overrun for a loud refusal.

## Sources

[1] Ma, Shukla, Salem, Huang, Sim, Feuerriegel, Galley & Gao — "EAIR: Interaction Risks in Enterprise LLM Multi-Agent Systems," arXiv:2610.14800v1 [cs.MA], 10 October 2026. Sections 5.2 (shared cap, handed-off rights, handoff drift, model spread) and 5.5 (repair retests). https://arxiv.org/html/2610.14800v1
[2] Stripe — "Issuing spending controls," product documentation, retrieved 2026-10-28. How card limits add up, what they reach, and the default limits. https://docs.stripe.com/issuing/controls/spending-controls
[3] Comptroller of the Currency — 12 CFR Part 32, "Lending Limits," sections 32.3 and 32.5, Electronic Code of Federal Regulations, current as of 10/26/2026. https://www.ecfr.gov/current/title-12/chapter-I/part-32
