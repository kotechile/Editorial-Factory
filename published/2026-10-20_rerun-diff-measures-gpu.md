---
title: "Your 9% Drop: Not the Model"
vertical: ai_observability_qa
persona: evals_infra_eng
one_big_thing: "A score belongs to the run, not to the model: at temperature 0 with a fixed seed the same request still returns different answers when batch size, processor count or number format changes, so a two-run delta is a difference between machine setups until one is held fixed."
date: 2026-10-20
slug: rerun-diff-measures-gpu
archetype: evergreen
evergreen: true
meta_title: "Your 9% Drop: Not the Model"
meta_title_source: "derived_from_title"
meta_description: "A giant model read the exact same prompt a thousand times at a fixed zero setting, known as temperature 0, but gave 80 different answers."
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/rerun-diff-measures-gpu/featured.png"
image_style: "clay_render"
image_model: "nanobanana"
image_alt: "Hardware Noise In LLM Tests. Identical modular blocks routing into varying output stacks inside a mechanical bay."
image_caption: "Hardware Noise In LLM Tests: Why fixed models give different answers on busy chips."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->

A giant model read the exact same prompt a thousand times at a fixed zero setting, known as temperature 0, but gave 80 different answers [1]. Nothing inside the model changed between those runs, but the group of requests it ran with did. That is the hidden trap in your test scores. When an evaluation drops from 82 to 78 overnight, your new code is only one piece of that puzzle.

<!-- tension -->

## The big picture:

Computer math changes when you swap the order of the numbers. Add the same list in a new sequence, and the final total shifts. Engineers at Thinking Machines Lab proved this extreme case. They added one fixed list of numbers in ten thousand random orders and got 102 different results [1].

A graphics chip adds numbers based on its current workload. A math program, or kernel, processing 8 rows groups sums differently than one processing 32 rows. Because of this, a solo request parts ways with the exact same request running in a busy group [1].

The industry fix is batch invariance. This rule locks the math sequence so it never changes, no matter the group size [1]. With that setting turned on, all one thousand model answers came back identical [1].

Most serving setups lack this shield. The vLLM engine defaults to a zero seed and offers two ways to get repeatable text. You can fix the schedule offline, or you can turn on batch invariance online [2].

What strikes me is how much noise this adds to a normal release cycle. A team reruns 200 tests, watches the pass rate drop from 81 to 77, and blames their code. But the exact same test setup can swing that far just by running on a different number of chips.

The measured swings are huge. One study ran six models at fixed settings over eight tasks, repeating each five times. Accuracy swung by up to 10 points, and no model stayed steady across every task [3].

A second study pushed a reasoning model across 12 machine setups. Accuracy moved up to 9 points, and answer lengths shifted by 9,000 tokens, where a token is the word piece a model emits [4]. The authors state the problem clearly. Picking the most likely next word, a process called greedy decoding, does not guarantee the same text across different systems, even with a locked seed [4].

This noise bleeds into published research. One team pushed 1.2 million model calls through data tests at a fixed zero setting. Between 0.07% and 10.2% of rows changed output across five runs, and one task shifted by 24.0% [5]. In the published SemBench results, 21% of text scores changed quality between runs [5].

## By the numbers

- **80 — Distinct answers:** one fixed prompt tested 1,000 times at a zero setting produced 80 unique responses, splitting 992 to 8 at the 103rd token [1].
- **9% — Accuracy swing:** a reasoning model shifted its accuracy by 9 points across 12 machine setups using 16-bit numbers [4].
- **10% — Run spread:** six models tested at fixed settings over eight tasks showed score shifts up to 10% across five runs [3].
- **10.2% — Shifting rows:** up to 10.2% of test rows changed their output over five identical runs [5].

<!-- tactical-insight -->

## What I'd watch:

I have been reading these papers the way an engineer reads a crash log, hunting for the missing detail.

- **The setup stamp:** a score without its chip type, chip count, batch size, number format, and server version is useless. Setup alone caused a 9-point score swing [4].
- **The control run:** repeat a test suite with zero changes to find the natural spread. That spread is the floor a real code change must clear to matter.
- **The speed cost:** locking the math sequence ran about 20% slower against standard libraries in one lab test. A 1,000-answer run went from 26 seconds to 55 [1]. For a single greedy run, the second study points to 32-bit numbers instead [4].
- **The compounding errors:** four chained steps operating at 95% steadiness drop to 81.4% reliability end-to-end. This happens before counting normal errors [3].
- **The internal disagreement:** identical requests within a single run disagree just as often as requests compared across separate runs [5].

<!-- nuanced-takeaway -->

## The catch

My read: researchers measured the strongest parts of this evidence on setups much narrower than a normal release test.

The 1.2-million-call study focuses entirely on query engines over text and tables [5]. It proves the failure exists in a live setup, but it does not measure your specific test suite.

The 992-to-8 split relies on one prompt, one model, and one server build from September 2025 [1]. It is an isolated test, not a universal reliability rate.

Closed vendors keep their math methods hidden, so teams using cloud models cannot just flip a switch to lock the sequence. Repeat runs act as a backup plan, but voting only shrinks the noise without removing it completely [5].

The speed penalties are also thinner than they look. The 20% drop comes from an unoptimized research kernel, and researchers put no exact number on what 32-bit math costs in memory or overall speed [1][4].

<!-- tldr -->

## At a glance

- **The Big Shift:** A model served at a fixed zero setting still returns different answers when the group size, chip count, or number format changes.
- **Why It Matters:** A test that flags a four-point drop might actually be measuring the server instead of your code change.
- **What I'd Watch:** I am watching what teams print beside a score, because the number means nothing without it.
  - **Setup stamps:** recording the exact chip type, count, group size, and server version behind every run.
  - **Control spreads:** the score range from repeated runs of an unchanged test, setting the baseline a real code change must beat.
  - **Batch-invariant serving:** a server mode where the math sequence stays locked regardless of group size, preventing hidden changes.
- **The Catch:** Repeat runs shrink the noise without removing it, cloud vendors hide their math rules, and the biggest effects measured here stem from lab tests rather than live systems.

## Sources
[1] Horace He, "Defeating Nondeterminism in LLM Inference", Thinking Machines Lab, 10 September 2025 — the 102-order array, the 992-to-8 split at token 103, batch invariance defined, about 20% against cuBLAS, 26/55/42 seconds on 1000 sequences (https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)
[2] vLLM documentation, "Reproducibility" — seed defaulting to 0, fixed scheduling offline, batch invariance as the only route in online serving (https://docs.vllm.ai/en/latest/usage/reproducibility.html)
[3] Ouyang, Wang, Chu, Chen, Jin, Wang & Liu, "Non-Determinism of 'Deterministic' LLM Settings" (arXiv:2408.04667v2, August 2024) — six models, eight tasks, five identical runs, accuracy variations up to 10%, and the 0.95^4 = 81.4% compounding example (https://arxiv.org/html/2408.04667v2)
[4] Yang et al., "Give Me FP32 or Give Me Death? Challenges and Solutions for Reproducible Reasoning" (arXiv:2506.09501v1, June 2025) — up to 9% accuracy and 9,000 tokens of length variation under bfloat16 greedy decoding across 12 runtime setups, and the recommendation to use 32-bit numbers for a single greedy run (https://arxiv.org/html/2506.09501v1)
[5] Hassanzadeh & Subramanian, "Same Query, Different Answer: Run-to-Run Variance in Semantic Query Processing" (arXiv:2610.13823v1, 9 October 2026) — 1.2 million logged calls, 0.07% to 10.2% of rows changing over five runs, 21% of SemBench text results changing quality, 16 of 28 tests unsettled (https://arxiv.org/html/2610.13823v1)

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "$915M Illusion: Your AI Judge Moves" -> /buying-ai-quality-when-the-score-belongs-to-the-judge/ [same site (aichieve.net); same category; topical overlap: prompt] Link "$915M Illusion: Your AI Judge Moves" in the section where the article touches prompt. -->
<!-- internal-link hint: "Agentic AI Adoption Soars, But Profits Stall in 2026" -> /agentic-ai-adoption-soars-but-profits-stall-in-2026/ [same site (aichieve.net); same category; topical overlap: times] Link "Agentic AI Adoption Soars, But Profits Stall in 2026" in the section where the article touches times. -->
<!-- internal-link hint: "OpenAI just made the agent loop a commodity" -> /openai-just-made-the-agent-loop-a-commodity/ [same site (aichieve.net); same category; topical overlap: model] Link "OpenAI just made the agent loop a commodity" in the section where the article touches model. -->
## Related reading

- [$915M Illusion: Your AI Judge Moves](/buying-ai-quality-when-the-score-belongs-to-the-judge/)
- [Agentic AI Adoption Soars, But Profits Stall in 2026](/agentic-ai-adoption-soars-but-profits-stall-in-2026/)
- [OpenAI just made the agent loop a commodity](/openai-just-made-the-agent-loop-a-commodity/)
<!-- internal-links:end -->

## Gate report
lead
PASS — Delivers the core takeaway immediately in the first sentence without throat-clearing, using plain words to explain the exact problem with evaluation drops.
tension
PASS — Breaks down the floating-point math problem into short, highly readable sentences (Flesch > 60), glosses technical terms clearly, and integrates the first-person observer cue naturally.
tactical-insight
PASS — Formats actionable takeaways as declarative observations rather than imperative commands, keeping the tone analytical while adhering strictly to 1-3 sentence paragraphs.
nuanced-takeaway
PASS — Realistically evaluates the limitations of the research data, maintaining an objective and grounded perspective on the impact with simple, direct phrasing.
tldr
PASS — Strictly adheres to the 4-part Smart Brevity structure, cleanly summarizing the big shift, its importance, what to watch, and the final catch with perfect formatting.
