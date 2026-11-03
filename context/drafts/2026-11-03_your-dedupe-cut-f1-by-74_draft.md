---
title: "Your Dedupe Pass Costs 7.4 F1"
vertical: ai_observability_qa
kind: evergreen
archetype: evergreen
evergreen: true
persona: evals_infra_eng
one_big_thing: "A synthetic suite's breadth is set by the axes written into its prompt — asking one prompt for twenty cases lifted a security task's F1 by 43.8 points — while a similarity-based dedupe pass that improves every diversity metric can still cut the score the gate runs on, so report the effective case count and re-measure the suite's own discrimination instead of optimising the diversity number."
date: 2026-11-03
slug: your-dedupe-cut-f1-by-74
---

<!-- lead -->
A single field in the prompt decides how varied a generated case set turns out. Because the batch size sits in the instruction, a team can widen its synthetic cases this afternoon — and a 2025 study measured what that does: asked for twenty cases instead of one, a security-classification task's blended F1 score went from 0.325 to 0.763, a 43.8-point rise [1]. Stripping the most alike fifth of the same generated set — a dedupe pass — raised every diversity score it tracked and still cut F1 in nine of twelve setups, by up to 7.4 points [1]. Your synthetic cases come from the same kind of generator, so both arms turn one knob: what the instruction asked for, not what a filter took out afterwards.

<!-- tension -->

## The generator hears your sentence

A model asked for one case per prompt answers one question, then answers it again with the same nouns in the same shape. Asking a single prompt for twenty cases does not fix that by itself, and the study measured the repeat. Repeated word sequences fell 25–28% in the twenty-case arm, and the average pair-wise similarity between cases, how close two of them sit in vector space, fell 22–28% against the one-case arm [1]. Both numbers describe a set that stopped saying the same thing twice.

The study's own control is worth reading, because it shows how little the ask costs. The batch size is a single field in the prompt, set to one or twenty, and every other part of the pipeline stays fixed [1]. A team that wants broader cases can change that field this afternoon. A team that reaches for a filter is changing something else.

The easy fix is the filter. A similarity pass is cheap, it runs after generation, and it moves the number a dashboard shows. In the same study it lifted both diversity scores — repeat sequences down another 9–12%, pairwise similarity down 5–11% — and the model trained on the cleaned set did worse in nine of twelve setups [1]. The set looked wider while teaching the classifier less.

That is the part I keep circling. A release gate is a test, not a sample of prose: its job is to fail a broken build and pass a working one. Size is settled elsewhere — [a 100-case eval carries 92.5% coverage, not 95%](/100-case-eval-925-coverage/) — but size and spread are two counts, and the gate only runs one.

## By the numbers

- **5,937 — Effective cases:** a diversity score read 5937.00 on a 6,000-case set with no copies and 5936.99 after 6,000 copies were added, which its authors read as a count of effective samples [3].
- **12 times — Prompt axes:** four audiences crossed with three formats give up to 12 times the prompts from the same topic list [2].
- **Less than 1% — Duplicate text:** the bloom of 30 million prompts reports under 1% duplicates, against a high duplicate rate when only the wording of one prompt changed [2].

<!-- tactical-insight -->

## What the large sets varied

The teams that generate at scale do not ask for more of the same. Hugging Face's Cosmopedia, a 25-billion-token synthetic set built from Mixtral, started from topic prompts and found that reworded prompts were "insufficient to prevent a high rate of duplicate content" [2]. What worked was naming the audience and the format inside the instruction, with clear guidance on how the text should differ: four audiences, from young children to researchers, crossed with three formats — textbooks, blog posts, how-to articles [2]. That pass built twenty-three million prompts, and the set names its topic only half the time, so the model cannot lean on the label.

What I take from that is a change of unit. The case is not the unit of a synthetic suite; the instruction is. Two prompts that differ only in wording give one case in two labels, which is why a generated set's duplicate rate belongs to the prompt list, not to the generator.

<!-- nuanced-takeaway -->

## The catch

Two limits matter before you rebuild on this. The measured leg is requirements classification across four small data sets — the defects set holds 131 examples, and each setup ran five times — and the cut was a rough fifth of the set rather than a tuned one, so the 7.4-point drop is a warning about filters, not a law that every dedupe hurts [1]. The mechanism travels; the size of the loss in your own harness is yours to measure.

My read is that the second limit changes how you report the suite. A diversity score barely moves when copies are added, which is what you want from a measure of breadth and not from a count of cases. Report the effective count beside the row count, and re-test the suite by whether it still separates a broken build from a working one.

<!-- tldr -->

## At a glance

**The shift:** Synthetic case sets are being deduped to look diverse when their breadth is set by the prompt.
**The number:** 7.4 points of F1 lost to a pass that raised every diversity metric.
**The risk:** A diversity score stays flat under duplicates, so it cannot stand in for a case count.

## Sources

[1] Abdelkarim El-Hajjami and Camille Salinesi, "How Good Are Synthetic Requirements? Evaluating LLM-Generated Datasets for AI4RE," arXiv:2506.21138v1, 26 June 2025. https://arxiv.org/html/2506.21138v1
[2] Loubna Ben Allal, Anton Lozhkov and Daniel van Strien, "Cosmopedia: how to create large-scale synthetic data for pre-training," Hugging Face blog, 20 March 2024. https://huggingface.co/blog/cosmopedia
[3] Yuchang Zhu, Huizhe Zhang, Bingzhe Wu, Jintang Li, Zibin Zheng and Peilin Zhao, "Measuring Diversity in Synthetic Datasets," arXiv:2502.08512v3, 14 August 2025. https://arxiv.org/html/2502.08512v3
