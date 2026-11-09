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
meta_title: "Your 413 Files Cost Four Badges"
meta_title_source: "derived_from_title"
meta_description: "Claude Sonnet 3.7 wrote 413 memory files during a single game run and earned one badge; Claude Fable 5 wrote nine and earned four."
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/your-413-files-cost-four-badges/featured.jpg"
image_style: "paper_collage"
image_model: "nanobanana"
image_alt: "Your 413 Files Cost Four Badges. Hundreds of paper file folders piled beside two slim folders with four badges on a drafting table"
image_caption: "Your 413 Files Cost Four Badges: A memory store belongs to a model version; the four badges are the cost of the mismatch."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Claude Sonnet 3.7 wrote 413 memory files during a single game run and earned one badge; Claude Fable 5 wrote nine and earned four [1]. The game and the tools were the same; the difference was what each model chose to keep. A benchmark posted four days earlier supplies the other half: written state beats re-reading only at a history length set by the reader, because a reader's hold on the log weakens as the log grows [2]. Together they describe a deal most teams signed without reading. A memory store belongs to a model version, and the four badges are what the mismatch costs.

<!-- tldr -->

## At a glance

- **The shift:** Memory is sold by size; what matters is how far the reader follows a log.
- **The number:** 1,024 events, where written state beats a 120B reader.
- **The risk:** A folder tuned on an old model bills for a horizon the new model never reaches.

<!-- tension -->

## Only the reader changed

I made myself read the three documents in the order they were published. On 2 November, a preprint set up a test of permission decisions—grants, withdrawals, reinstatements, expiries, groups and change windows—and scored pairs of histories that differ only in the order of a deciding event or in one field of it [2]. Anthropic's post followed on 6 November with the per-model memory folders [1]. Two days later, a vendor argued that the field is missing a shared data model, not another store [5].

A model that reads the whole transcript has to keep every event tied to its key, and that tie weakens as the log grows [2]. Open models of 7 to 32 billion parameters fall from 72 to 86 percent after eight or sixteen events to 48 to 55 percent after 256 [2]. Written state throws the events away and keeps the answer, so a 32-billion-parameter reasoner reading state gets 96 and 98 percent of the same pairs, about double what a model of its size manages from the log [2].

Anthropic compared one run of Claude Sonnet 3.7 with one run of Claude Fable 5, both about 10,000 steps into the game [1]. Sonnet 3.7 wrote 413 files across 225 folders and earned one badge; its notes were mostly a list of things it had met, and the game's state changes every turn, so those notes were stale by the time they were read [1]. Fable 5 wrote nine files in two folders plus a global.md file, and earned four badges [1]. Around the ten-thousandth step, Sonnet 3.7 created six files and removed nine over seventeen straight steps, and took no in-game action at all [1].

The obvious fix, telling the model what to keep, failed in the lab's own test. Told to record only failures, Opus 5 and Opus 4.7 lost much of the gain that memory had given them [1]. What separated the two folders was the model's own call about what mattered. In a separate evaluation, Sonnet 5 read its memory before answering nine times in ten unprompted; Sonnet 4.6 did so less than half the time.

## By the numbers

- **413 memory files:** What one Claude wrote in a single run, for one badge [1].
- **Nine files:** What a later model kept, in two folders, to earn four badges [1].
- **1,024 events:** The history length where written state beats a 120B reader's re-read [2].

<!-- tactical-insight -->

## Where this lands

What I find hardest to square is how little of this is about storage. The test prices state against the log at a length the reader sets: a 120B reasoner still trails written state by four points at 256 events and seven at 512, and it crosses over near 1,024 [2]. The paper calls that crossover a measured property of the reader, not a fixed size of the store [2]. The same state that rescues a 32-billion-parameter model is wasted work for a frontier model at the same history length, and swapping the reader moves both numbers.

Curation is also the security boundary. When a harmful instruction stays in memory and the document that carried it is removed, four agent setups showed attack success between 59.38 and 76.39 percent under indirect injection [3]. In 55.71 percent of those episodes the attacker's choice came inside a task that was formally finished and ran without a fault. Outside parties who never gave the agent work reached 79.58 and 64.20 percent [3]. A stored note is an instruction the moment the model reads it again.

The delivery paper is the one to put in front of a budget owner. It ran three memory systems through 8,000 coding episodes and found that adding memory moved success rates by less than 0.4 points against no memory at all [4]. Most delivered notes were beside the point, and most useful notes were never used, which is why the volume number and the value number disagree.

<!-- nuanced-takeaway -->

## The catch

What I would defend here is smaller than the headline number seems to promise. The folder comparison is one run per model, reported by the lab that built both, with no repeated trials and no token cost per session [1]. The crossover is measured on permission decisions, not coding or research, so 1,024 events belongs to that test and is not a general figure [2]. Neither paper reports a crossover for coding work, which is the number an architect needs.

A bigger store did not rescue a weaker reader in either data set, and a fixed rule about what to keep took value away from a stronger one. So the memory budget follows the reader: how far the model in front of you can follow a log on the calls you give it, measured per installation rather than copied from a vendor page. The four badges are what the mismatch costs. If the tiering argument from [last month's piece](/agent-memory-tiering-l1-l4/) still holds, it now needs a version number attached.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Agent Memory Poisoning" -> /agent-memory-poisoning-write-path/ [same site (aichieve.net); same category; topical overlap: memory] Link "Agent Memory Poisoning" in the section where the article touches memory. -->
<!-- internal-link hint: "Long Context Is Not Memory" -> /agent-memory-tiering-l1-l4/ [same site (aichieve.net); same category; topical overlap: memory] Link "Long Context Is Not Memory" in the section where the article touches memory. -->
<!-- internal-link hint: "Stop Piling Memory Onto AI Agents" -> /maskills-multi-agent-skills-optimization/ [same site (aichieve.net); same category; topical overlap: memory] Link "Stop Piling Memory Onto AI Agents" in the section where the article touches memory. -->
## Related reading

- [Agent Memory Poisoning](/agent-memory-poisoning-write-path/) — more on Autonomous & Agentic Workflows
- [Long Context Is Not Memory](/agent-memory-tiering-l1-l4/) — more on Autonomous & Agentic Workflows
- [Stop Piling Memory Onto AI Agents](/maskills-multi-agent-skills-optimization/) — more on Autonomous & Agentic Workflows
<!-- internal-links:end -->

## Sources

- [1] Anthropic, "The components of agent memory", 6 November 2026 — https://www.anthropic.com/research/components-of-agent-memory
- [2] "Agent Memory as Rate-Limited Filtering: Explicit State Outlasts Long Context Beyond a Reader-Dependent Horizon", arXiv:2611.02361, 2 November 2026 — https://arxiv.org/abs/2611.02361
- [3] "MemHarmBench: Evaluating Cross-Session Prompt Injection in Memory-Persistent AI Agents", arXiv:2611.01700, 1 November 2026 — https://arxiv.org/abs/2611.01700
- [4] "Delivered, Not Used: Evaluating Agent Memory at Its Point of Use", arXiv:2611.01718, 1 November 2026 — https://arxiv.org/abs/2611.01718
- [5] LoreKit, "Agent memory needs its OpenTelemetry moment", 8 November 2026 — https://www.lorekit.io/blog/open-agent-memory-format
