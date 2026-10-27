---
title: "Your Green Suite Certifies 31.08% Wrong"
vertical: ai_observability_qa
persona: evals_infra_eng
one_big_thing: "A pass rate is a claim by the tests, not about the code: on the benchmark the coding-agent field is scored on, 31.08% of the patches that passed every test were wrong in ways the suite could not see and 32.67% had the answer printed in the task text, so removing both defects cut a 12.47% resolve rate to 3.97% — which is why the gate has to print a mutant kill rate, strip the answer out of the task text, and probe with cases the model has not seen."
date: 2026-10-27
slug: your-green-passes-hide-31-wrong
archetype: evergreen
evergreen: true
image_path: "context/assets/illustrations/your-green-passes-hide-31-wrong/featured.jpg"
image_style: "component_assembly"
image_model: "nanobanana"
image_alt: "False Green Checks. A brushed steel inspection gate mechanism allowing a flawed polymer module to pass through a green sensor ring."
image_caption: "False Green Checks: Why passing tests hide broken AI-generated code."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Your test suite certifies wrong code and hides it behind a green check because the tests cannot tell a real fix from a broken one. Of the 251 patches a coding agent got past every check in the software engineering (SWE) benchmark called SWE-bench, 31.08% were wrong [1]. The work was unfinished, or it edited a different file entirely, yet every check still passed.

The same hand audit found 32.67% of those passing patches had the answer sitting in the task text, because the bug report spelled out the fix [1]. The agent did not work the problem out, but read the answer. Take both faults out and the headline number collapses. A coding agent driving GPT-4, a generative pre-trained transformer (GPT) from OpenAI, resolved 12.47% of the benchmark. Scored only on the clean cases, it resolved 3.97% [1]. Nothing about the model changed between those two figures, only the credit the tests were willing to give it.

<!-- tension -->

## The big picture:

A test can only fail a change it can tell apart from a good one. That sounds small until you see how the audit ran, because it shows the gap between a strict gate and a formality. The authors pulled the logs of 286 cases the test harness marked resolved. They kept the 251 where every check passed, and read each patch against the real fix by hand [1]. Most of what passed was suspect.

Coverage is the usual answer, but coverage is the wrong tool. A study measuring fault finding directly found suites running every line of code while catching 4% of the faults planted in it [3]. The tests touched the whole file and still missed the wrong answer.

The third fault is quieter. When cases are lifted from public projects, the score carries memory as well as skill. On SWE-Bench-Verified, one model named the buggy file from the bug report alone, with no code and no project layout, up to 76% of the time, against 53% on projects outside the benchmark [2]. Across the ten models tested, that gap looks like recall more than reasoning.

What strikes me is how little of this requires anyone to cheat. The bug writer pastes a fix into the thread, and the test author writes a check the happy path already satisfies. The case is copied from a project the model has read a million times. Each step looks fine on its own, and the result is a gate reporting a number it never earned. That is the same fault the desk described in [a green check that cannot see the failure class](/agent-failures-tests-stayed-green/), and it keeps coming back for a plain reason. The pass rate is the only number anyone prints, so it is the only number anyone checks.

## By the numbers

- **31.08% — Wrong patches passed:** 78 of the 251 patches that got past every test were wrong or incomplete or touched other files, and the tests were too weak to catch it [1].
- **32.67% — Answer in text:** 82 of those same patches had the fix spelled out in the bug report or its comments, so the run measured reading rather than repair [1].
- **76% vs 53% — Known codebase recall:** o3-mini named the buggy file from the report alone up to 76% of the time on SWE-Bench-Verified, against 53% on projects outside it [2].
- **4% — Coverage without fault finding:** Some suites run every line and still catch only 4% of planted faults, which is why the study calls coverage a weak sign of fault finding [3].

<!-- tactical-insight -->

## What I'd watch:

Where this bites is the release report, not the paper. The teams closest to it have stopped arguing about the pass rate and started printing a second number beside it. What I'd want on the next release report is the pair: the pass rate, and the share of planted faults the suite caught.

- **Printing the mutant kill rate:** A mutation runner plants small faults in the code and counts how many the suite catches, which makes up the mutation score. One off-the-shelf runner ships defaults of high 80 and low 60 [4], which makes 60 the floor that tool ships rather than a rule anyone agreed.
- **Reading the task text for the answer:** Before a case counts, reviewers check whether the bug report or the comment thread already holds the fix. That is a search through text the test harness already keeps, dropping the cases that measure copying.
- **Probing with projects the model has not seen:** A held-out probe is the cheap version of the file-path test. Teams keep the same task out of the famous projects and watch what happens to the score [2]. If accuracy only holds on those projects, the score is about them.
- **Keeping the run log:** The 251-patch audit worked because the authors kept the harness logs and read them by hand [1]. Teams that throw their run records away cannot repeat this on their own suites.

<!-- nuanced-takeaway -->

## The catch

My read is that the cheapest of the three checks is the leak search, and the one that travels least is the mutation score. Mutation testing is slow, and the score does not travel. A run executes the suite once per planted fault, so a big suite pays for the number in wall-clock time. Two tools that plant different faults give scores you cannot compare.

The leak check is cheap but manual, and it needs human judgement. A comment that describes a failure is not a comment that pastes the patch, and the line between them is the one the audit drew by hand [1]. A crude script will throw out good cases and miss the clever ones.

The memory probe is the weakest evidence about your own work, because fame on a public benchmark says little about a private codebase. The 76% and 53% figures are one model on one benchmark family, and the jump to your suite is an argument, not a reading [2]. So the honest claim is narrower than it first looks. A green result says the suite could not find a fault in this change. On one well-studied benchmark, that was true of a patch that was wrong about a third of the time. The number you can act on is the one your own suite earns on faults you planted yourself, but if [the suite is too small to settle the gap you care about](/100-case-eval-925-coverage/), that pair is noise either way.

<!-- tldr -->

## At a glance

- **The Big Shift:** A hand audit of the benchmark the whole coding-agent field is scored on found that most of what passed was suspect, with answers copied straight out of the task text, and the clean subset scored far lower.
- **Why It Matters:** A release gate is only as strong as its ability to fail, so a pass rate read as proof about the code is a claim the tests made about themselves.
- **What I'd Watch:**
  - **Mutant kill rate:** The share of faults planted on purpose that a suite catches, which says what it can detect rather than what it touched.
  - **Answer leakage:** Whether the bug report, the thread or the linked discussion already holds the fix, which turns a repair task into a reading task.
  - **Held-out probe:** The same task run on projects outside the benchmark, which separates recall of a famous codebase from real skill.
- **The Catch:** Mutation runs are slow and their scores do not compare across tools, the leak check needs human judgement, and the memory figures come from one public benchmark rather than from your own codebase.

## Sources
[1] R. Aleithan, H. Xue, M. M. Mohajer, E. Nnorom, G. Uddin and S. Wang, "SWE-Bench+: Enhanced Coding Benchmark for LLMs" (arXiv:2410.06992v2, 10 October 2024) — https://arxiv.org/html/2410.06992v2
[2] S. Liang, S. Garg and R. Zilouchian Moghaddam, "The SWE-Bench Illusion: When State-of-the-Art LLMs Remember Instead of Reason" (arXiv:2506.12286v1, 14 June 2025) — https://arxiv.org/html/2506.12286v1
[3] G. Wang, Q. Xu, L. Briand and K. Liu, "Mutation-Guided Unit Test Generation with a Large Language Model" (arXiv:2506.02954v8, 15 April 2026) — https://arxiv.org/html/2506.02954v8
[4] Stryker, "StrykerJS configuration reference — thresholds" (retrieved 27 October 2026) — https://stryker-mutator.io/docs/stryker-js/configuration/

## Gate report
PASS — Lead states the stakes first, carries max one figure per sentence, and explains why the change is happening before mechanisms.
PASS — Tension clearly frames the structural problem with plain English and uses a first-person observer cue without instructing the reader.
PASS — Tactical insight focuses on what operators are doing as observations, ending on a clear metric recommendation without imperative playbook commands.
PASS — Nuanced takeaway provides realistic limitations of the metrics and closes on a direct decision linked to the desk's internal page.
PASS — TL;DR follows the exact 4-part Smart Brevity schema, summarizing the shift, impact, watch areas, and tradeoffs distinctly.
