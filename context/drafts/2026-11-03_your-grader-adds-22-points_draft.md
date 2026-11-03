---
title: "Your Grader Adds 22 Silent Points"
vertical: ai_observability_qa
kind: news
persona: evals_infra_eng
one_big_thing: "An eval score is made twice outside the model — once when a renderer turns the run into the text a judge reads, and once when a parser turns the reply into a verdict — and because both fail quietly at exactly the inputs where the model is weakest, a score is only worth trusting when the pipeline reports what it rendered, what it parsed and how often the fallback fired."
date: 2026-11-03
slug: your-grader-adds-22-points
synthesis: true
sources:
  - https://arxiv.org/abs/2611.02676
  - https://arxiv.org/abs/2611.03377
---

<!-- lead -->

A vision-language model asked whether a metal part was defective answered "The object is a nail." One published benchmark scores that reply correct, because its grader ends in a closest-option snap: it drags any string to the nearest option, and with no cut-off the nearest option is "Yes" [1]. A grader like yours adds up to 22 points to a model's published score on the very same outputs, and not one point to a model that answers in clean letters. It does that silently, because nothing in the number records the change [1].

The other end of the pipe is quieter. In a second pipeline studied this week, the script that turns recorded agent runs into the text a judge reads left out every structured tool call, so 53 of 60 judged steps arrived blank [2]. The packets still matched their hashes, both of the pipeline's own checkers passed, staging copied the files cleanly, and nothing reported a problem [2].

<!-- tension -->

## Made before and after the model

Both papers landed on 2 November, and neither set out to write the other's half. The first asks what a judge is handed; the second asks what a grader credits once a model has answered [1][2]. Read together they describe one pipe with two joints that nobody owns, and the model sits in the middle doing the only part anyone measures.

The part I keep circling is how small both failing pieces are. The renderer is a short script that picks which fields of a run go into a text file. The grader is a few lines at the bottom of a scoring script, picked without argument and left unread, because reviewers judged the dataset and not the rule that turns an answer into right or wrong [1]. Neither piece is a model. Neither is versioned by the team that owns it, and both decide the number.

Paper two shows how much the second piece carries. Its authors reran the official graders of eight peer-reviewed tests on five open vision-language models, and the rule alone moved accuracy by up to 22 points on the same stored outputs [1]. Where a model answers in clean letters the swing is exactly zero, which is why the flaw never shows on a leaderboard of strong, careful models.

On the models a small team can actually run, it bites. On the 110 items of one benchmark where the model did not give a clean letter, it committed to an option only 23 percent of the time, and the snap still scored 72 percent of them correct [1]. The same grader adds 22 points to one model and takes 19 from another, because the sign follows how chatty the model is rather than how good it is [1].

Paper one shows the first piece failing just as quietly. Four rules say what a judge's input has to meet: the content it needs survives the render, each checker covers what it claims to check, a failed check stops later use, and the judge reads the bytes that were checked last [2]. The pipeline in the study broke all four while its hashes matched, its checkers passed and its staging worked.

The details are what sting. Two checkers, written apart from each other, both missed a tool result with no call to match, and that was the one fault out of 34 shared test cases that both let through [2]. One checker's hash test hashed the same loaded text twice, so by design it could never spot a changed file [2]. A failed build's packet still reached the judge, and so did a packet edited after staging [2].

## By the numbers

- **1,670 — Items where the swing is exact:** the 22-point gap needs no human check, because it is worked out on every stored item, so it is arithmetic on the same outputs rather than a modelled guess [1].
- **29 to 37 percent — Times the fallback fires:** that is the share of items where the deployed open models reach the fallback, and since each case is built around the fallback alone, no gap can be wider than the rate that fires it [1].
- **0.956 — Agreement when a person checks:** the blinded human-plus-judge method that recovers what a model actually answered agrees at that Cohen's kappa, so the truth the audit measures against is itself a measurement [1].

<!-- tactical-insight -->

## Where the pipeline leaks

What I'm watching is whether the fix comes as a checklist or as one more model. The cheap checks in paper one are all software. Keep the structured call in the packet, test each checker against a result with no matching call, and compare the staged file with its manifest entry when the judge reads it [2]. Paper two's advice is just as plain: print the rate at which the fallback fires beside accuracy, publish the score under at least two rules, and have a person check the answers when the number matters [1].

The commercial layer has moved on one half of this. Artificial Analysis, whose index gets quoted far past its own site, prints its multiple-choice extraction as a main pattern plus seven fallbacks, and says it always takes the last match found "to account for self-correction in responses" [3]. Its version history treats the index itself as a chosen thing: version 5.0 in October dropped four tests, added three and set the weights to 25 percent each [3]. The weights are written down with a date. The tie-break in the parser is written down with no date.

Eval tools show the same gap from the other side. Release 0.125.0 of promptfoo adds an option to normalise text before its equals and contains checks, which makes the comparison settable and leaves the default out of sight [4]. A team that never opens that switch runs the same unread comparison both papers describe, inside a harness it picked itself.

The teams closest to this seem to be heading for a manifest, and that looks like the right shape: this renderer, this packet hash at read time, this parser rule, this fallback rate. A score published without one is not a lie. It is a number nobody can trace, and the [green suite that certifies 31.08 percent wrong](/your-green-passes-hide-31-wrong/) is the same lesson from the other end of the test stack.

<!-- nuanced-takeaway -->

## The catch

The honest limit is that neither paper reorders a leaderboard. With each benchmark's grader held fixed and only the fallback varied, paper two finds the strongest model stays on top, and its top-1 change on one benchmark under abstention (crediting only a clean letter) is not significant at the sample size it tested [1]. The claim is that a grade is unreliable, not that a ranking is wrong, and turning this into "the leaderboard is fake" would overstate a careful result.

I could be wrong about how fast the fix spreads. Paper one's 18-of-19 figure comes from three controls added after the faults were found, on one pipeline with 30 agent runs, and its authors call the move to other pipelines a plan rather than a finding [2]. Both papers are days old and have not been through public review. Paper two's own control makes the point best: the benchmark with the highest rate of unreadable answers, between 0.54 and 0.69, has a gap of exactly zero, because its grader refuses to guess [1]. A design can remove the flaw without making the model any better.

<!-- tldr -->

## At a glance

**The shift:** Two papers show a score is set by a renderer before the model and a grader after it.

**The number:** 53 of 60 judged steps arrived blank while every hash and checker passed.

**The risk:** Better judges and models still leave a number your own pipeline made.

## Sources

[1] Hasan and Lwowski, "Same Outputs, Different Scores: Auditing the Unchecked Graders of Multimodal LLM Benchmarks," arXiv:2611.03377, 2 November 2026 (accepted at WACV 2027) — https://arxiv.org/abs/2611.03377
[2] Xia, Lu, Li, Sejdinovic and Zhu, "Does the Judge See What the Evaluation Requires? Input Assurance for LLM Agent Evaluation," arXiv:2611.02676, 2 November 2026 — https://arxiv.org/abs/2611.02676
[3] Artificial Analysis, "Intelligence Benchmarking" methodology, version 5.0 — https://artificialanalysis.ai/methodology/intelligence-benchmarking (read 3 November 2026)
[4] promptfoo, "Release 0.125.0," 23 October 2026 — https://github.com/promptfoo/promptfoo/releases/tag/0.125.0
