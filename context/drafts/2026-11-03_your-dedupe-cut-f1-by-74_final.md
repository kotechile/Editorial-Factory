---
title: "Your Dedupe Pass Costs 7.4 F1"
vertical: ai_observability_qa
kind: evergreen
archetype: evergreen
evergreen: true
persona: evals_infra_eng
one_big_thing: "A synthetic suite's breadth is set by the axes written into its prompt — not by how many cases you request or how hard you dedupe — because asking one prompt for twenty cases lifted F1 by 43.8 points in one task, while a similarity filter that improved every diversity score still cut F1 in nine of twelve setups."
date: 2026-11-03
slug: your-dedupe-cut-f1-by-74
---

<!-- lead -->

One line in the prompt decides how varied your test set turns out. Because the batch size sits in the prompt, a team can widen its cases this afternoon. A 2025 study asked one prompt for twenty cases instead of one, and watched a security-versus-non-security classification task's blended F1 climb from 0.325 to 0.763, a 43.8-point rise [1]. Then it stripped the most alike fifth of the same set, a dedupe pass: every diversity score it tracked rose, yet F1 fell in nine of twelve setups, by up to 7.4 points [1]. Both levers turn the same knob — what the prompt asked for, not what a filter took out later.

<!-- tension -->

## The generator hears the ask

Generated cases repeat. A model asked for one case per prompt answers one question, then answers it again with the same nouns in the same shape. Asking a single prompt for twenty cases does not fix that by itself, and the study measured the repeat. Repeated word sequences fell 25–28% in the twenty-case arm, and average closeness, how near two cases sit in vector space, fell 22–28% against the one-case arm [1]. Both counts describe a set that stopped saying the same thing twice.

The study's design shows how cheap the ask is. The batch size is one field in the prompt, set to one or twenty, and every other part of the pipeline stays fixed [1]. A team that wants broader cases can change that field this afternoon. A team that reaches for a filter is changing something else.

The easy fix is the filter. A pass that strips near-copies is cheap, runs after the build, and moves the number a dashboard shows. In the same study it lifted both diversity scores — repeat sequences down another 9–12%, closeness down 5–11%. The model trained on the cleaned set still did worse in nine of twelve setups, so the set looked wider while teaching the classifier less.

That is the part I keep returning to: a release gate is a test, not a sample of prose, and its job is to fail a broken build and pass a working one. Size is settled elsewhere — [a 100-case eval carries 92.5% coverage, not 95%](/100-case-eval-925-coverage/) — but size and diversity are two counts, and the gate only runs one.

## By the numbers

- **5,937 — Effective cases:** a diversity score read 5937.00 on a 6,000-case set with no copies and 5936.99 after 6,000 copies were added, which its authors read as a count of effective samples [3].
- **12 times — Prompt axes:** four audiences crossed with three formats give up to 12 times the prompts from the same topic list [2].
- **Less than 1% — Duplicate text:** a build of 30 million prompts reports under 1% duplicates, against a high copy rate when only the wording of one prompt changed [2].

<!-- tactical-insight -->

## What the large sets varied

Scale does not fix this. The teams that build at scale do not ask for more of the same. Hugging Face's Cosmopedia, a 25-billion-token set built from Mixtral, started from topic prompts and found that reworded prompts were "insufficient to prevent a high rate of duplicate content" [2]. Naming the audience and the format in the prompt worked: four audiences, from young children to researchers, crossed with three formats — textbooks, blog posts, how-to articles [2]. That pass built twenty-three million prompts, and the set names its topic only half the time, so the model cannot lean on the label [2].

Here is what I take from that: the case is not the unit of a generated set, the prompt is. Two prompts that differ only in wording give one case in two labels, so a set's duplicate rate belongs to the prompt list, not to the generator. The open question is whether naming two or three of those axes inside a small prompt list does the same work before a cleanup pass.

<!-- nuanced-takeaway -->

## The catch

Two limits matter. The measured leg is sorting requirement text across four small data sets, and the defects set holds 131 examples with each setup run five times. The cut was a rough fifth of the set rather than a tuned one, so the 7.4-point drop is a warning about filters, not a law that every dedupe hurts [1]. The effect travels; the size of the loss in your own setup is yours to measure.

The second limit changes how you report the suite, because a diversity score barely moves when copies are added — what you want from a measure of breadth, not from a count of cases. I keep wanting the report to show the effective count beside the row count, and to re-test the setup by whether it still separates a broken build from a working one.

<!-- tldr -->

## At a glance

**The shift:** Synthetic test sets are being deduped to look varied when their breadth is set by the prompt.
**The number:** 7.4 points of F1 lost to a pass that raised every diversity score.
**The risk:** A diversity score stays flat under copies, so it cannot stand in for a case count.

## Sources

[1] Abdelkarim El-Hajjami and Camille Salinesi, "How Good Are Synthetic Requirements? Evaluating LLM-Generated Datasets for AI4RE," arXiv:2506.21138v1, 26 June 2025. https://arxiv.org/html/2506.21138v1
[2] Loubna Ben Allal, Anton Lozhkov and Daniel van Strien, "Cosmopedia: how to create large-scale synthetic data for pre-training," Hugging Face blog, 20 March 2024. https://huggingface.co/blog/cosmopedia
[3] Yuchang Zhu, Huizhe Zhang, Bingzhe Wu, Jintang Li, Zibin Zheng and Peilin Zhao, "Measuring Diversity in Synthetic Datasets," arXiv:2502.08512v3, 14 August 2025. https://arxiv.org/html/2502.08512v3
