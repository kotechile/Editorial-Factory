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
meta_title: "Your Grader Adds 22 Silent Points"
meta_title_source: "derived_from_title"
meta_description: "One benchmark asked a vision-language model whether a metal part was defective. The model answered, \"The object is a nail.\" The official scorer marked that…"
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/your-grader-adds-22-points/featured.jpg"
image_style: "clay_render"
image_model: "nanobanana"
image_alt: "Two matte clay modules meet on a cracked concrete floor, a yellow connector latch hanging open between them, in a dim server room."
image_caption: "Your Grader Adds 22 Silent Points: Scores shift by up to 22 points before anyone sees them."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->

One benchmark asked a vision-language model whether a metal part was defective. The model answered, "The object is a nail." The official scorer marked that answer correct [1], because its grader ends in a closest-option snap: at a cutoff of zero, any string gets dragged to the nearest option, and the nearest option here is "Yes" by character overlap, not base rate. A rule like that adds up to 22 points to a published score on the very same outputs, and exactly zero to a model that answers in clean letters [1]. The change is silent, because nothing in the printed number records it.

The other end of the pipe is quieter. In a second pipeline reported this week, a script turned recorded agent runs into the text a judge reads. It kept tool results but left out every structured tool call, so 53 of 60 judged steps arrived blank [2]. The packets still matched their recorded hashes, both of the pipeline's own checkers passed, staging copied the files cleanly, and nothing upstream reported a fault [2].

<!-- tension -->

## Made outside the model, twice

Both papers landed on 2 November; neither set out to finish the other's half. Paper one asks what a judge is handed after an agent run. Paper two asks what a grader credits once a model has answered [1][2]. Together they describe one pipe with two joints nobody owns, and the model sits in the middle doing the only part anyone measures.

I keep returning to how small both failing pieces are. The renderer is a short script that picks which fields of a run become text. The grader is a few lines at the bottom of a scoring script, picked without argument and left unread, because reviewers judge the dataset and not the rule that turns an answer into right or wrong [1]. Neither is a model. Neither is tracked by the team that owns it, and both decide the number.

Paper two shows how much the second joint carries. Its authors reran the official scorers of eight peer-reviewed tests on five small open models, and the rule alone moved accuracy by up to 22 points on the same stored outputs [1]. Where a model answered in clean letters the swing was exactly zero. That is why the flaw never shows on a leaderboard of strong, careful models.

On the open models a small team can actually deploy, it bites. On the 110 items of one test where the model did not give a clean letter, it picked an option only 23 percent of the time, and the snap still scored 72 percent of them correct [1]. The same grader adds 22 points to one model and takes 19 from another, because the sign follows how chatty the model is, not how good it is [1].

Paper one shows the first joint failing just as quietly. Four rules define a valid judge input: the content it needs survives the render, each checker covers what it claims to check, a failed check stops later use, and the judge reads the bytes that were checked last [2]. The pipeline in the study broke all four while its hashes matched, its checkers passed and its staging worked. A matching hash says only that the bytes are unchanged. It says nothing about whether the right fields made it into the packet [2].

The details are what sting. Two checkers, written apart from each other, both missed a tool result with no call to match, and that was the one fault out of 34 shared test cases that both let through [2]. One checker's hash test hashed the same loaded text twice, so by design it could never catch a changed file [2]. A failed build's packet still reached the judge, and so did a packet edited after staging [2].

## By the numbers

- **1,670 — Items where the swing is exact:** the 22-point gap needs no human check because it is simple sums on every stored item, not a modelled guess [1].
- **29 to 37 percent — How often the fallback fires on open models:** because each measured case isolates the fallback, no gap can be wider than the rate that fires it [1].
- **0.956 — Agreement when a person checks:** the blinded human-plus-judge method that recovers what a model actually answered agrees at that Cohen's kappa, so the truth the audit measures against is itself a measurement [1].

<!-- tactical-insight -->

## Where the pipeline leaks

I will be watching whether the fix arrives as a checklist or as another model. The cheap checks in paper one are all software. Keep the structured call in the packet, test each checker against a result with no matching call, and compare the staged file with its manifest entry when the judge reads it [2]. Paper two's advice is equally plain: print the fallback rate beside accuracy, publish the score under at least two rules, and have a person check the answers when the number matters [1].

The commercial layer has moved on one half of this. Artificial Analysis, whose index gets quoted far past its own site, publishes its multiple-choice extraction as a main pattern plus seven fallbacks. It says it always takes the last match found "to account for self-correction in responses" [3]. Its methodology version 5.0, released in October, dropped four tests, added three and set the weights to 25 percent each [3]. The weights carry a date. The parser's tie-break carries none.

Test tools show the same gap from the other side. Release 0.125.0 of promptfoo adds an option to normalise text before its equals and contains checks [4]. That makes the check settable while the default stays out of sight. A team that never opens the switch runs the same unread check both papers describe, inside a harness it chose itself.

The teams closest to this seem to be heading for a manifest, and that looks like the right shape: this renderer, this packet hash at read time, this parser rule, this fallback rate. A score published without one is not a lie; it is a number nobody can trace, and the [green suite that certifies 31.08 percent wrong](/your-green-passes-hide-31-wrong/) is the same lesson from the other end of the test stack.

<!-- nuanced-takeaway -->

## The catch

The honest limit is that neither paper reorders a leaderboard. With each test's grader held fixed and only the fallback varied, paper two finds the strongest model stays on top, and its top-1 change on one test under abstention (crediting only a clean letter) is not significant at the sample size it tried [1]. The claim is that a grade is unreliable, not that a ranking is wrong. Turning that into "the leaderboard is fake" would overstate a careful result.

I could be wrong about how quickly the fix spreads. Paper one's 18-of-19 figure comes from three controls added after the faults were found, on one pipeline with 30 agent runs, and its authors call the move to other pipelines a plan rather than a finding [2]. Both papers are dated 2 November, so the findings are days old. Paper two's own control makes the point best: the test with the highest rate of unreadable answers, between 0.54 and 0.69, has a gap of exactly zero, because its grader refuses to guess [1]. A design can remove the flaw without making the model any better.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "OpenAI just made the agent loop a commodity" -> /openai-just-made-the-agent-loop-a-commodity/ [same site (aichieve.net); same category; topical overlap: model] Link "OpenAI just made the agent loop a commodity" in the section where the article touches model. -->
<!-- internal-link hint: "Your 180-day model is already wrong" -> /your-180-day-model-is-already-wrong/ [same site (aichieve.net); same category; topical overlap: model] Link "Your 180-day model is already wrong" in the section where the article touches model. -->
<!-- internal-link hint: "Your 9% Drop: Not the Model" -> /rerun-diff-measures-gpu/ [same site (aichieve.net); same category; topical overlap: model] Link "Your 9% Drop: Not the Model" in the section where the article touches model. -->
## Related reading

- [OpenAI just made the agent loop a commodity](/openai-just-made-the-agent-loop-a-commodity/)
- [Your 180-day model is already wrong](/your-180-day-model-is-already-wrong/)
- [Your 9% Drop: Not the Model](/rerun-diff-measures-gpu/)
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

**The shift:** A score is made outside the model twice: a renderer before, a grader after.

**The number:** 53 of 60 judged steps arrived blank while every hash and checker passed.

**The risk:** Better judges and stronger models still leave a number your pipeline made.

## Sources

[1] Hasan and Lwowski, "Same Outputs, Different Scores: Auditing the Unchecked Graders of Multimodal LLM Benchmarks," arXiv:2611.03377, 2 November 2026 (accepted at WACV 2027) — https://arxiv.org/abs/2611.03377
[2] Xia, Lu, Li, Sejdinovic and Zhu, "Does the Judge See What the Evaluation Requires? Input Assurance for LLM Agent Evaluation," arXiv:2611.02676, 2 November 2026 — https://arxiv.org/abs/2611.02676
[3] Artificial Analysis, "Intelligence Benchmarking" methodology, version 5.0 — https://artificialanalysis.ai/methodology/intelligence-benchmarking (read 3 November 2026)
[4] promptfoo, "Release 0.125.0," 23 October 2026 — https://github.com/promptfoo/promptfoo/releases/tag/0.125.0
