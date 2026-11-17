---
title: "Your Judge's 80% Overpays 39 Points"
vertical: ai_observability_qa
kind: evergreen
archetype: evergreen
evergreen: true
persona: evals_infra_eng
one_big_thing: "Raw agreement between a judge model and human labels is inflated by luck, so the number a release gate prints has to be a luck-adjusted score beside the raw match, measured against what people reach with each other rather than against 1.0."
date: 2026-11-17
slug: your-judges-80-overpays-39-points
meta_title: "Your Judge's 80% Overpays 39 Points"
meta_description: "Across 21 judge models and 541,000 judgments, raw match ran about 39 points above a luck-adjusted score. Why a release gate should print kappa, not match."
---

<!-- lead -->
A judge model that matches human labels 80% of the time overpays by about 39 points, because it gets much of that match by guessing. Across 21 judge models from nine providers, raw exact match sat 33.8 to 41.3 points above a score that removes luck, over roughly 541,000 judgments [1]. That gap is why a raw match rate cannot block a release on its own.

<!-- tldr -->
## At a glance
- **The shift:** raw match rates look strong and are puffed up by luck.
- **The number:** 0.82 kappa, the parity a task judge reached with people.
- **The risk:** a stable judge can carry a stable bias.

<!-- tension -->
## Why a match rate overpays

The judge era opened with a clean number. In 2023 the team behind the Multi-turn Benchmark (MT-Bench) reported that a strong model acting as judge matched human experts 85% of the time with ties removed, above the 81% two people reached with each other [4]. The NeurIPS record of that work says the same thing in one line: agreement above 80%, the same level people reach [3]. That line is why a judge got a seat at the release table. It was measured, it was careful, and it is still the sentence most teams quote when a judge is proposed for a gate.

The audit that landed on 2026-06-17 tested what the line measures. Three researchers ran 21 judges from nine providers over three test sets (fixed lists of items with known answers) and three scoring modes, and logged about 541,000 verdicts in 118 runs [1]. On MT-Bench, every judge showed the same gap between raw match and kappa, the score that removes the agreement two raters would reach by guessing. The gap held across model sizes, including the frontier models out through April 2026 [1]. The finding is not a small-model artifact: the deflation runs across capability tiers, frontier models included [1].

The cause is a simple sum. If nine items in ten carry one label, a judge that always returns that label agrees with people 90% of the time, and knows nothing about the tenth item. Kappa asks how much better than that flat guess the judge does. A lopsided set therefore drags the same judge's kappa down, and live traffic is lopsided on purpose, because most outputs are fine and failures are rare [1].

What I find hard to square is the second finding. Teams treat repeatability as the cheap stand-in for a good judge, yet two judges in live use held test–retest scores above 0.95 while their verdicts moved with the order the answers were shown in, at a bias above 0.10 [1]. A judge can repeat its own bias almost perfectly. Rank order moved too, by as much as 14 places, depending on which test set did the ranking [1]. Read that way, repeatability measures a judge's habits rather than its accuracy.

<!-- tactical-insight -->
## Where this bites

The teams closest to this problem are not dropping judges. They are changing what the gate prints and what it compares against. The calibration set gets labelled twice, by people, so the human-to-human kappa lands on the same items as the human-to-judge kappa, and the second is read against the first rather than against a perfect score [1]. A judge that clears what people reach on those items is evidence. A judge that clears a round number picked in a meeting is not, and the difference only shows up in the labelling work nobody wants to budget. That human cost is the only part of the pipeline that buys a number anyone can defend.

Answer order is the cheapest control to add. Swap the two answers in each pairwise call, then report how far each slot's win rate sits from even [1]. A narrow rubric leaves a judge fewer ways to look right for the wrong reason. One team has already shown what a cleared bar looks like. On a cancer-progression task drawn from radiology reports, a prompted group of models reached a mean kappa of 0.82 against human labels, with a 95% confidence interval of 0.74 to 0.89, while two people reached 0.79 with each other [2]. That judge had a narrow task, a written rubric and a set built for it, and it removed 72% of the manual review [2].

What I'm watching next is whether the same parity holds outside a task built on a bench. Rank order moves by up to 14 places when the test set changes. A judge cleared on one set is not cleared on the next, and the paper offers no shortcut around measuring each one [1]. Parity is a property of a task, and not a property of a model.

## By the numbers

- **0.82 kappa:** the agreement a task-specific judge reached with human labels, above the 0.79 two people reached [2].
- **541,000 verdicts:** the volume behind the 21-judge audit, spread over 118 runs and three test sets [1].
- **14 places:** how far a judge's rank moved when the test set doing the ranking changed [1].

<!-- nuanced-takeaway -->
## The catch

Kappa is not a badge you carry between tasks. It is computed from the label mix of the set it was measured on, so the same judge scores lower on live traffic where failures are rare than on a balanced set built to include them [1]. A gate that clears on the first set can still miss the rare failure it exists to catch, and the 14-place drift says the same thing another way: a judge has a standing on one test set, not a standing. Carrying a score between tasks is what teams assume and what the metric does not offer.

Where I've landed is that the score is still worth printing, because the other option is a percent that counts guessing as skill. What changes is the claim it backs. A luck-adjusted score measured on your own labels, against the people who wrote them, is a statement about one task. The same figure quoted without that set is the puffed-up version the field has published since 2023 [3]. The claim has to travel with its label set, its rubric and the people who wrote the labels. A kappa without them is a number about a set, and only a guess about a system.

The sampling question under all of this has its own arithmetic, and [what a small case set can really support](/100-case-eval-925-coverage/) is worth settling before the judge's number is trusted.

## Sources

- [1] Justin Norman, Michael Rivera and Alex Hughes, "Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge Models Across Agreement, Consistency, and Bias" (arXiv:2606.19544v1, submitted 2026-06-17) — https://arxiv.org/html/2606.19544v1
- [2] ESMO Real World Data and Digital Oncology, "Prompting large language models and evaluating inter- and intra-rater agreement for cancer progression assessment from radiology reports" (2026 Mar 10;11:100689) — https://pmc.ncbi.nlm.nih.gov/articles/PMC12993880
- [3] Lianmin Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena", NeurIPS 2023 Datasets and Benchmarks Track — https://papers.nips.cc/paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract-Datasets_and_Benchmarks.html
- [4] Lianmin Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" (arXiv:2306.05685v4, full text) — https://arxiv.org/html/2306.05685v4
