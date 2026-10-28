---
title: "Your 78.3% Silent Cap Breach"
vertical: multi_agent_enterprise_fabric
persona: ai_architect
one_big_thing: "An enterprise agent fabric breaks its own caps from inside the rules — each agent stays under its own approval limit while the sum goes over — so one service must own the total at the ledger and the caller's rights must travel with the call."
date: 2026-10-28
slug: your-783-silent-cap-breach
archetype: evergreen
evergreen: true
meta_title: "Your 78.3% Silent Cap Breach"
meta_title_source: "derived_from_title"
meta_description: "Agent fabrics break their shared spend caps from inside the rules, because each agent only checks the limit it was handed: the study logged cap breaches in…"
meta_description_source: "derived_from_lead"
---

<!-- lead -->
Agent fabrics break their shared spend caps from inside the rules, because each agent only checks the limit it was handed: the study logged cap breaches in 47 of 60 rounds, or 78.3% [1]. The case still closes without agent errors, and no single step breaks a rule. That is the failure an architect must plan for: a breach built out of steps that each look fine, with no single service holding the total.

<!-- tension -->

## The big picture:

The measured form of this problem landed in October 2026, when a Microsoft and Munich research group tested what happens when agents share a workflow [1]. They built five small worlds across ten models from seven vendors, running 1,158 analyzed runs in all [1]. 

What strikes me here is not the failure rate but the spread. No model was safest across all five worlds, and the safety ranks barely lined up between them, at a mean rank correlation of 0.36 [1]. A better model cannot fix a fault that sits in the shape of the fabric.

The spend controls most teams already own make the gap wider. A payment firm's card controls add up on a best-effort basis, meaning tips or fees posted after the approval can push a card past its limit [2]. Their reach is the card, or the holder across all of their cards, rather than the customer across all of your agents [2].

Banks settled the identity half of this long ago. A bank's cap is written against one borrower's whole exposure, and the rule that makes two borrowers count as one turns on 50 percent or more of gross receipts coming from the other [3]. The power to lend sits with a desk, but the ceiling sits with the bank.

## By the numbers

- **78.3% — Cap breach:** 47 of 60 rounds failed when each payment stayed under the issuing agent's limit while the sum went past the company's cap [1].
- **77.8% — Scope lost:** Private facts reached a caller who was not allowed to see them in 70 of 90 rounds, and the specialist never used the channel it had for asking what that caller could see [1].
- **60 of 96 — Internal stops:** The workflow caught this many handoff errors before the customer email went out, so a rate read on the final output understates the one read mid-flow [1].
- **30 seconds — Ledger lag:** The sum is best-effort, with up to 30 seconds between a spend and its total, so the number a control checks is not the number that exists when the next agent calls [2].

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 172" style="background:#0f172a; border-radius:8px; font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif; margin:16px 0; max-width:100%; height:auto;">
  <text x="20" y="36" fill="#f8fafc" font-size="16" font-weight="600">Your 78.3% Silent Cap Breach</text>
  <text x="20" y="52" fill="#94a3b8" font-size="12">Figures as stated in this article&#x27;s own numbers section (verified figures, %)</text>
  <!-- Row 1 -->
  <text x="20" y="84" fill="#e2e8f0" font-size="13" font-weight="500">Cap breach</text>
  <rect x="240" y="70" width="300" height="18" rx="4" fill="#1e293b"/>
  <rect x="240" y="70" width="234" height="18" rx="4" fill="#818cf8"/>
  <text x="484" y="84" fill="#f1f5f9" font-size="13" font-weight="600">78.3%</text>
  <text x="538" y="84" fill="#64748b" font-size="11">([1])</text>
  <!-- Row 2 -->
  <text x="20" y="132" fill="#e2e8f0" font-size="13" font-weight="500">Scope lost</text>
  <rect x="240" y="118" width="300" height="18" rx="4" fill="#1e293b"/>
  <rect x="240" y="118" width="233" height="18" rx="4" fill="#818cf8"/>
  <text x="483" y="132" fill="#f1f5f9" font-size="13" font-weight="600">77.8%</text>
  <text x="537" y="132" fill="#64748b" font-size="11">([1])</text>
</svg>

<!-- tactical-insight -->

## What I'd watch:

Two changes did most of the work in the study's own repair tests, and both are structural rather than model-shaped [1]. One moved the scope check onto the handoff, so the specialist got the caller's verified rights with the request instead of guessing them; that produced zero leaks across 20 fresh rounds while the task answer survived in 20 of 20 [1]. The other put a second look at the evidence in front of the report, and false blame on a vendor fell to zero across 20 rounds [1].

What I am watching next is where teams put the cap check. A fabric that keeps it inside each agent's own policy inherits this flaw, because each agent's view stops at its own limit [1]. The version that caught my eye is a shared spend-control layer that looks global and adds up late [2].

Three signs suggest an architecture has closed this gap:

- **A central ledger:** One service records each agent's effect on the same customer and turns down the call that crosses the cap.
- **Scope on the wire:** The handed-off request carries the caller's verified rights, so the answering agent can test them rather than trust the planner.
- **Audit by citation:** The study's report contract made 80 of 81 findings traceable to a step in the run, making repairs checkable [1].

<!-- nuanced-takeaway -->

## The catch

The evidence comes from small test worlds, not live company traffic. The study used five scenes, ten models, and a simulated customer, so the breach rate belongs to that cap model rather than your ledger [1]. The repair tests run 20 fresh rounds each, which shows a direction but is too small to quote as a promise [1].

A hard cap also costs something the study never priced. In that test world the task still completes while the cap breaks [1]. A check that turns the call down trades a quiet overrun for a loud refusal, and the person weighing that trade owns the customer.

There is a real risk of reading the bank rule as a design spec. The 15 percent limit exists to protect bank capital, not to model a credit policy [3]. What carries over is the order of work: fix the rule that decides who counts as one borrower, then set the ceiling.

My read: the cheap half is scope on the handoff, because its repair test fell to zero. The dear half is the ledger that can say no, which forces the question a sibling piece takes up — how long a granted right stays usable after the step that justified it ([Your Agent Fabric's 52.2% Blind Spot](/stale-grants-travel-the-graph/)).

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Your Agent's Contract Gap" -> /your-agent-contract-gap-63-unmet/ [same site (aichieve.net); same category; topical overlap: agent, inside, rules] Link "Your Agent's Contract Gap" in the section where the article touches agent, inside, rules. -->
<!-- internal-link hint: "Planner-as-Router: Fold the Model Choice Into the Plan" -> /planner-as-router-fold-the-model-choice-into-the-plan/ [same site (aichieve.net); same category; topical overlap: agent, shared] Link "Planner-as-Router: Fold the Model Choice Into the Plan" in the section where the article touches agent, shared. -->
<!-- internal-link hint: "Silent Errors Halve Agent Success" -> /isolation-isnt-detection/ [same site (aichieve.net); same category; topical overlap: agent, silent] Link "Silent Errors Halve Agent Success" in the section where the article touches agent, silent. -->
## Related reading

- [Your Agent's Contract Gap](/your-agent-contract-gap-63-unmet/) — more on Autonomous & Agentic Workflows
- [Planner-as-Router: Fold the Model Choice Into the Plan](/planner-as-router-fold-the-model-choice-into-the-plan/) — more on Autonomous & Agentic Workflows
- [Silent Errors Halve Agent Success](/isolation-isnt-detection/) — more on Autonomous & Agentic Workflows
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** Agent fabrics fail by summing rather than by error, breaking shared caps because each agent only checks its own approval limit.
- **Why It Matters:** The layer most teams lean on to catch this adds up late and reaches only as far as the card, meaning fabrics that leave the total to each agent will ship quiet overruns.
- **What I'd Watch:** Whether the total has one owner, and whether scope travels with the call.
  - **One owner of the total:** A single service that sees each agent's effect on the same customer and turns down the call that crosses the cap.
  - **Scope on the handoff:** The caller's verified rights travelling with the request, so the answering agent tests them instead of assuming.
  - **Audit by citation:** Findings that name the step they came from, which is what makes a repair checkable later.
- **The Catch:** The evidence comes from small test worlds with tiny repair samples, and a cap that turns work down trades a quiet overrun for a loud refusal.

## Sources

[1] Ma, Shukla, Salem, Huang, Sim, Feuerriegel, Galley & Gao — "EAIR: Interaction Risks in Enterprise LLM Multi-Agent Systems," arXiv:2610.14800v1 [cs.MA], 10 October 2026. Sections 5.2 (shared cap, handed-off rights, handoff drift, model spread) and 5.5 (repair retests). https://arxiv.org/html/2610.14800v1
[2] Stripe — "Issuing spending controls," product documentation, retrieved 2026-10-28. How card limits add up, what they reach, and the default limits. https://docs.stripe.com/issuing/controls/spending-controls
[3] Comptroller of the Currency — 12 CFR Part 32, "Lending Limits," sections 32.3 and 32.5, Electronic Code of Federal Regulations, current as of 10/26/2026. https://www.ecfr.gov/current/title-12/chapter-I/part-32

## Gate report
lead: PASS — Opens with the stakes and explains the 'why' before the mechanism in under 28 words without reusing the primary figure.
tension: PASS — Contextualizes the structural flaw with an observer cue and connects it to existing financial controls.
tactical-insight: PASS — Reports structural changes operators are making without issuing commands, using clear bullets.
nuanced-takeaway: PASS — Highlights the trade-offs of hard caps and ends on a concrete decision with the required inline link.
tldr: PASS — Follows the strict 4-part Smart Brevity structure with indented sub-bullets and no fluff.
