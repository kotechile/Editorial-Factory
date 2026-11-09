---
title: "Your 413 Files Cost Four Badges"
vertical: agentic_ai
kind: news
persona: ai_architect
one_big_thing: "A memory store belongs to a model version: the history length at which written state beats re-reading is set by the reader, so a folder and a write rule tuned on one model are mispriced after an upgrade."
date: 2026-11-09
slug: your-413-files-cost-four-badges
synthesis: true
sources:
  - https://www.anthropic.com/research/components-of-agent-memory
  - https://arxiv.org/abs/2611.02361
---

<!-- lead -->
One Claude wrote 413 memory files during a single game run and earned one badge; a later model wrote nine and earned four. The game and the tools were the same, so the gap was not room, and Anthropic's own write-up says the difference was the call about what deserved keeping, because notes outlived their use [1]. That is the half of a memory budget nobody prices, and a test posted four days earlier supplies the other half: notes you write down only start to pay once the history is long, and how long depends on who is reading [2]. Together they describe a deal most teams signed without reading it. A memory store belongs to a model version, and the four badges in that first sentence are what the mismatch costs.

<!-- tldr -->

## At a glance

- **The shift:** Memory is sold by size; the measured variable is how far the reader follows a log.
- **The number:** 1,024 events, where state beats a 120B reader.
- **The risk:** A folder tuned on the old model bills for a horizon the new one no longer needs.
<!-- -->

<!-- tension -->

## Only the reader changed

My read starts with the order these three documents landed in. The test came first, on 2 November: permission decisions such as grants, withdrawals, restorations, expiries and change windows, scored on pairs of histories that differ only in the order or one field of a deciding event [2]. Anthropic's post followed on 6 November with the per-model memory folders [1]. Two days later a vendor noted that the four memory formats on a typical laptop cannot read one another, and argued that the field is missing a shared data model, not another store [5].

A model that reads the whole transcript has to keep every event tied to its key, and that tie weakens as the log grows. Open models of 7 to 32 billion parameters fall from 72 to 86 percent after eight or sixteen events to 48 to 55 percent after 256 [2]. Written state throws the events away and keeps the answer, so a 32B reasoner reading state gets 96 and 98 percent of the same pairs, about double what a model of its size manages from the log.

Anthropic's logs show the same trade from the other end. Sonnet 3.7's 413 files were mostly a list of things it had met, and the game's state changes every turn, so those notes were stale by the time they were read. Around its ten-thousandth step it made six files and removed nine over seventeen steps, and never moved in the game at all [1]. The model with nine files kept a dashboard, a plan and a book of rules, and it earned four badges to the other's one.

The obvious fix, telling the model what to write down, failed in the lab's own test. Told to record only failures, Opus 5 and Opus 4.7 lost much of the gain that memory had given them [1]. What separated the two folders was the model's own call about what mattered. The newer model made that call without being asked nine times in ten, and the older made it less than half the time.

## By the numbers

- **413 memory files:** What one Claude wrote in a single run, for one badge [1].
- **Nine files:** What a later model kept, in two folders, to earn four badges [1].
- **1,024 events:** The history length where written state beats a 120B reader's re-read [2].

<!-- tactical-insight -->

## Where this lands

What I find hardest to square is how little of this is about storage. The test prices state against the log at a length the reader sets: a 120B reasoner still trails written state by four points at 256 events and seven at 512, and it crosses over near 1,024 [2]. A smaller reader crosses much sooner. The same state that rescues a 32B model is wasted work for a frontier one at the same history length, and swapping the reader moves both numbers.

Curation is also the security boundary. When a harmful instruction stays in memory and the document that carried it is removed, four agent setups showed attack success between 59.38 and 76.39 percent under indirect injection [3]. In 55.71 percent of those episodes the attacker's choice came inside a task that was formally finished and ran without a fault. Outside parties who never gave the agent work reached 79.58 and 64.20 percent. A note is a standing order the moment something reads it again.

Delivery numbers are the ones I would put in front of a budget owner. On 8,000 coding episodes, three memory systems changed success rates by less than 0.4 points against no memory at all [4]. Most delivered notes were beside the point, and most useful notes were never used. Volume is easy to count and says little about the work.

<!-- nuanced-takeaway -->

## The catch

The comparison of 413 files against nine is one run per model, reported by the lab that built both, with no repeated trials and no token cost per session [1]. The crossover is measured on permission decisions rather than coding or research, so 1,024 events belongs to that test and is not a general figure [2]. Neither paper reports a crossover for coding work, which is the number an architect actually needs.

The pair still settles something narrower. What I would defend here is smaller than the headline number seems to promise: a bigger store did not rescue a weaker reader in either data set, and a fixed rule about what to keep took value away from a stronger one. What decides a memory budget is how far the model in front of you can follow a log on the calls you give it, and that figure is measured for each installation rather than copied from a vendor page. If the tiering argument from [last month's piece](/agent-memory-tiering-l1-l4/) still holds, it now needs a version number attached.

## Sources

- [1] Anthropic, "The components of agent memory", 6 November 2026 — https://www.anthropic.com/research/components-of-agent-memory
- [2] "Agent Memory as Rate-Limited Filtering: Explicit State Outlasts Long Context Beyond a Reader-Dependent Horizon", arXiv:2611.02361, 2 November 2026 — https://arxiv.org/abs/2611.02361
- [3] "MemHarmBench: Evaluating Cross-Session Prompt Injection in Memory-Persistent AI Agents", arXiv:2611.01700, 1 November 2026 — https://arxiv.org/abs/2611.01700
- [4] "Delivered, Not Used: Evaluating Agent Memory at Its Point of Use", arXiv:2611.01718, 1 November 2026 — https://arxiv.org/abs/2611.01718
- [5] LoreKit, "Agent memory needs its OpenTelemetry moment", 8 November 2026 — https://www.lorekit.io/blog/open-agent-memory-format
