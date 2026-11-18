---
title: "Your Transcript Says Done: Success Fails at 28%"
vertical: agentic_resilience_failure
kind: news
persona: infra_engineer
synthesis: true
sources:
  - https://arxiv.org/abs/2611.14654
  - https://arxiv.org/abs/2611.11581
date: 2026-11-18
slug: your-transcript-says-done
one_big_thing: "An agent's transcript is a control input to its next decision with two independent measured levers: a success receipt over a step that never landed cuts whole-task success from 45% to 28%, a truthful note beside the same kept error raises recovery from 51% to 66%, and moving a failure out of a buried tool message is worth another 10.5 to 14.2 points — so compaction, handoff and recovery layers need a sign test, not token-budget hygiene."
meta_title: "Your Transcript Says Done: Success Fails at 28%"
meta_description: "A success receipt over a write that never landed drops an agent's whole-task success to 28%. A truthful note beside the same error lifts recovery to 66%."
image_path: "context/assets/illustrations/your-transcript-says-done/featured.jpg"
image_style: "architectural_night"
image_model: "flux"
image_alt: "A dark, unlit data hall wing behind glass beside a warmly lit rack row at dusk."
image_caption: "False Success Receipt Cuts Task Success To 28%: a false success receipt cuts task success to 28%; a truthful note lifts recovery to 66%."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
A database write goes through, the receipt says success, and the effect never lands. Hand that record of the run, the transcript an agent carries forward, to the model that takes over, and whole-task success falls from 45% to 28% [1]. The step is marked done in the one place the next model can read. A second study, posted two days earlier, changed nothing but where the failure sat, and five of six models that had been fixing a fixable error in as few as 2% of cases began acting correctly almost always [2]. Both edits sit in code below the prompt, and only one of them pays unless the words match the world.

<!-- tldr -->
## At a glance
- **The shift:** The transcript is a measured input to the next step, not an audit log.
- **The number:** A success receipt over a write that never landed turns 45% into 28% [1].
- **The risk:** Compaction that claims completion turns a fixable error into a 6.43-point loss.

<!-- tension -->
## The sign flips on the world

Both papers went up in the second week of November, two days apart, and neither was written with the other in view [1]. Together they take apart one object: the record an agent reads after a step fails. That record is not a log. Every long session gets compacted, repaired or handed off, and compaction is the step that folds old turns into a short summary to save room. What survives is what the next model treats as evidence about the world.

The first study, from a group at Hong Kong's University of Science and Technology, froze an agent the moment it had written a wrong value, then changed only the transcript [1]. A truthful note beside the kept error raised recovery, the share of remaining targets the new model got right, from 51% to 66%. The same correct value, written instead as the agent's own finished action, fell below the untouched record, from 50% to 44% [1].

Two edits, one number, and opposite results. The gap between them was 21.63 points over 319 tasks and 638 paired runs, a figure fixed before the data was collected [1]. The design the authors used is easy to copy: keep the error, add the correction as a note beside it, and leave the step open until the world agrees.

The second test held the record still and moved the world. A success receipt on a database write whose effect was absent cut whole-task success from 45% to 28% [1]. With the effect in place, the same receipt raised success from 38% to 49%. One receipt, two worlds, and a 27-point swing between them. That is the gap [durable execution leaves open](/durable-execution-not-a-transaction/) when a tool contract records what the agent meant to do and not what the database now holds.

The second paper moves the other lever. Its author held the error text fixed and changed only where it sat in the talk [2]. Clients normally pass the error inside the tool message. Given only that, five of six models fixed a fixable error in as few as 2% of runs, and one repeated a transient error 98% of the time. Moving the error into a runtime note, a line the engine adds outside the tool result, made those five act correctly almost always. Cutting the failed exchange out instead produced a stop.

## Where the damage lands

I read the two papers side by side and kept coming back to one thing: the record has two knobs, not one. What it claims about the world sets the sign of the effect, and where the failure sits sets its size [1]. A team that rewrites history to fit a token budget is turning the first knob with no test, and the one direction it has measured is a loss: 6.43 points against leaving the record alone [1].

That falls hardest on teams whose context budget is a cap and whose postmortem tools are built to produce a clean trace, since clean is the exact move the first study measures as a loss. It rewards the cheaper option: keep the error, put the correction beside it as a note, and place the failure where the model cannot scroll past it.

## By the numbers

- **21.63 points:** The gap between a truthful note and a claimed completion, over 638 paired runs [1].
- **10.5 to 14.2 points:** What moving a failure out of the tool message added on explicit errors [2].
- **24 tasks:** The silent-fault set where that same move showed no measurable gain [2].

<!-- tactical-insight -->
## The layer that already ships

The second paper did not stop at the test. Its author built the kept-error form into an opt-in recovery layer inside an inference engine, the server process that turns a prompt into tool calls and a reply, and ran it on public tests and a coding agent [2]. The part I keep returning to is where that call sits: below the model, in the engine, so a model swap does not touch it.

The field record is thinner but points the same way. A corpus of 33 public cases of agents damaging production found at least three where the agent's own report was wrong, one of them telling its operator that rollback was impossible when the rollback worked [3]. Of the 33, 16 have no public record of recovery at all.

What I am watching next is whether the truth rule travels with the delivery rule. A recovery layer that shows errors is only as good as the record it draws them from, and the two halves sit with different owners in most stacks: the engine team ships the delivery, and whoever wrote the summary step owns the content.

<!-- nuanced-takeaway -->
## The catch

The receipt result rests on two models, and the authors say there is no pooled figure beyond them [1]. A record that only admits a failure did not repair it in their test; that case was left open at minus 2.50 points, with a range that crossed zero. The delivery gain in the second paper fades where the damage is invisible: on 24 tasks with silent faults, better placement moved nothing [2].

My reading, held loosely, is that the cheap half of this fix is a rule about what the record may claim. No layer below it can rescue a step whose receipt was written before anyone checked the effect, and every summary job in a long session writes one.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Agent Memory Poisoning" -> /agent-memory-poisoning-write-path/ [same site (aichieve.net); same category; topical overlap: write] Link "Agent Memory Poisoning" in the section where the article touches write. -->
<!-- internal-link hint: "Silent Errors Halve Agent Success" -> /isolation-isnt-detection/ [same site (aichieve.net); same category; topical overlap: success] Link "Silent Errors Halve Agent Success" in the section where the article touches success. -->
<!-- internal-link hint: "Silent Leak: 68.8% Bypasses Your Filter" -> /silent-leak-bypasses-your-filter/ [same site (aichieve.net); same category; topical overlap: through] Link "Silent Leak: 68.8% Bypasses Your Filter" in the section where the article touches through. -->
## Related reading

- [Agent Memory Poisoning](/agent-memory-poisoning-write-path/) — more on Autonomous & Agentic Workflows
- [Silent Errors Halve Agent Success](/isolation-isnt-detection/) — more on Autonomous & Agentic Workflows
- [Silent Leak: 68.8% Bypasses Your Filter](/silent-leak-bypasses-your-filter/) — more on Autonomous & Agentic Workflows
<!-- internal-links:end -->

## Sources

- [1] Wang, Wu, Li, Lyu, Wang and Cheung, "Cleaning an Agent's History Hurts When the World Still Holds the Error", 10 November 2026 — https://arxiv.org/abs/2611.14654
- [2] Woo, "Same Error, Different Recovery: How Delivery Changes LLM Agent Behavior", 8 November 2026 — https://arxiv.org/abs/2611.11581
- [3] Shelly and Salem, "What 33 public cases of AI agents breaking production have in common", 5 November 2026 — https://www.eon.io/blog/ai-agent-production-incidents
