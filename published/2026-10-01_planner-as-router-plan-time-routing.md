---
title: "Planner-as-Router: Fold the Model Choice Into the Plan"
vertical: agentic_ai
persona: ai_architect
one_big_thing: "Planner-as-Router cuts multi-agent cost 44% by assigning each subtask a model tier at plan time — no router model, no training data — and its own pilot warns cheap routing may quietly compound errors."
date: 2026-10-01
slug: planner-as-router-plan-time-routing
meta_title: "Planner-as-Router: Fold the Model Choice Into the Plan"
meta_title_source: "derived_from_title"
meta_description: "On Sept. 26, three researchers shared a new system called Planner-as-Router (PaR) that cuts AI agent costs by 44 percent."
meta_description_source: "derived_from_lead"
---

<!-- lead -->
On Sept. 26, three researchers shared a new system called Planner-as-Router (PaR) that cuts AI agent costs by 44 percent [1]. Instead of building a separate tool to pick models, PaR assigns a cheap or smart model to each step while making the initial plan [1]. Top frontier models cost 25 times more per word than small ones, and that price gap piles up fast when tools link many steps together [1].

<!-- tension -->
## The Router Moves Upfront

I have watched agent builders fight high cloud bills all month, and the real shift here is exactly where the routing choice happens. Most teams build a separate router that checks one step at a time to pick a model [1]. PaR flips this by assigning each small job a model tier — small, mid, or frontier — before any agent starts working [1]. 

**Why it matters:** Picking the right model is now a core design choice, not just a quick fix to save money later. Teams do not need to train a separate router model or gather data to teach it [1]. This lets the system see how tasks link together right from the start [1].

**By the numbers:**
- **25×:** The cost jump from a small model to a top-tier frontier model for the exact same amount of text [1].
- **44%:** The total cost drop PaR hits compared to using the biggest model for every step [1].
- **1,157:** The total number of tests run across eight routers and 54 business tasks [1].
- **3:** The number of test seeds used to grade tasks by running code against live Structured Query Language (SQL) and MongoDB databases [1].

<!-- tactical-insight -->
## A Fixed Backup Plan

What strikes me here is how this open-source system looks like classic software design, rather than a complex machine learning trick [1]. The main planner gives a tier to every small job right away, and the dispatcher runs them in the exact order they need to happen [1]. If a job fails, the dispatcher simply bumps it up to a smarter model and tries again [1].

**What I'd watch:**
- **Plan-time sorting:** Whether picking models before the work starts holds up well on messy, real-world jobs [1].
- **The escalating dispatcher:** How this fixed backup plan — bumping a failed job to a smarter model — compares to messy, custom retry loops [1].
- **The compounding penalty:** The paper warns that using cheap models early on might quietly multiply errors across long chains of tasks [1]. I want to see builders test this at scale before they trust the 44 percent savings [1].

<!-- nuanced-takeaway -->
**The catch:** The 44 percent cost cut acts as a ceiling, not a floor, because it comes with a 2.9-point drop in accuracy [1]. The paper honestly notes that several of these gaps sit inside a wide ±6-point range of doubt [1]. My read: The real win is moving the model choice upfront to see how tasks link together, while finally naming the risk of piled-up errors that most cheap-router pitches ignore [1].

**Go deeper:**
<!-- internal-links -->

<!-- tldr -->
- **The Big Shift:** A new paper called Planner-as-Router (PaR) cuts AI agent costs by 44 percent by assigning a small, mid, or frontier model to each step during the planning phase.
- **Why It Matters:** Moving this choice upfront removes the need to train and keep a separate router model, making cost control a core design choice instead of a late fix.
- **What I'd Watch:** Whether the cost savings hold up in the real world without causing a chain of hidden errors.
  - **Plan-time tiering:** Giving a model tier to each small job before the work starts so the system sees how tasks link together.
  - **Escalating dispatcher:** Running tasks in order and automatically bumping failed jobs to a smarter model tier.
  - **Compounding penalty:** The risk that using cheap models for early jobs quietly multiplies errors across long chains of tasks.
- **The Catch:** The 44 percent savings cost 2.9 accuracy points, and several test results sit within a wide ±6-point range of doubt.

## Sources
[1] Planner-as-Router: Joint Plan-Time Model Routing for Cost-Efficient Multi-Agent Workflows — arXiv:2609.32917 (submitted Sept 26, 2026) — https://arxiv.org/abs/2609.32917

<!-- linkedin -->
I have been reading agent-routing papers all month, and one from Sept. 26 stopped me. Planner-as-Router (PaR) tries something different. Instead of a separate router model picking a tier for each call, it folds the choice right into the plan. 

Each small job gets assigned a small, mid, or frontier model before any of them run. 

The result: a 44 percent cost cut against running the top model everywhere, at a 2.9-point accuracy cost, across 1,157 tests. No router model to train, no training data to collect.

My read: the real contribution isn't the number. It is moving the routing choice into the plan, where task links are visible, instead of bolting a classifier on later.

The part I keep circling: the paper quietly flags that cheap routing might carry a hidden compounding penalty on long task chains. Every cheaper-router pitch leaves that risk unsaid. This one names it.

The catch: the 44 percent is a ceiling, not a floor. Several accuracy gaps fall inside the study's ±6-point range of doubt.

I am curious how routing teams are handling this: is the compounding penalty real at scale, or just a small-pilot blip?

## Gate report
lead: PASS — Delivers the core news directly in sentence 1 with no throat-clearing, using plain English and adhering to the 3-sentence limit.
tension: PASS — Features the required observer cue, context signpost ("Why it matters:"), and a mandatory By the numbers section with 4 verified stats. Paragraphs are strictly 1-3 sentences.
tactical-insight: PASS — Uses an observer cue, the "What I'd watch:" signpost, and 3 bolded bullets phrased as observations. Merged sentences to stay within the 3-sentence maximum.
nuanced-takeaway: PASS — Includes an observer cue and "The catch:" signpost to present limitations clearly. Condenses the text to fit the 3-sentence rule.
tldr: PASS — Strictly adheres to the 4-part schema, including indented sub-bullets for definitions. Fixes applied for acronym definition (SQL) and paragraph length limits.
