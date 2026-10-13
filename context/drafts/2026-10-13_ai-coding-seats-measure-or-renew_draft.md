---
title: "AI Coding Seats: The 75-Point Gap"
vertical: enterprise_tech_leadership
persona: eng_leader
one_big_thing: "The published randomized trials of AI coding tools span 55.8% faster to 19% slower, so a seat count has to rest on a trial of your own code, not on a vendor's headline number."
date: 2026-10-13
slug: ai-coding-seats-measure-or-renew
archetype: evergreen
evergreen: true
---

<!-- lead -->
Two randomized trials of AI coding seats sit about 75 points apart. In one, GitHub measured a group finishing a task 55.8% faster with its Copilot assistant [3]. In the other, METR (a nonprofit that studies AI risks) clocked veteran engineers at 19% slower with the tools switched on [1]. Both tests were controlled. The gap is the story, because neither number is the one a leader signs for.

<!-- tension -->

## The big picture:

The gap tracks one thing: how well the engineer already knows the code.

METR's trial put 16 veteran maintainers on 246 real tasks. The work came from code bases they had helped build for five years on average [1]. With AI allowed, they took 19% longer than they did without it [1]. Before they started, they had forecast a 24% speedup. After they finished, they still put the saving at 20% [1]. Two expert panels, economists and machine-learning researchers, expected 38% to 39% [1].

Adoption is already so wide that a team can learn little from its own split. In the 2025 Stack Overflow developer survey, 84% of respondents use or plan to use AI tools [4]. Among full-time developers there, 50.6% use them every day [4]. There is no clean holdout group left.

What strikes me is how hard the follow-up shows the measuring to be. The same group ran the trial again on later tools: 57 developers, 143 code bases, more than 800 tasks. It now puts the saving for returning developers at 18%, inside a range that runs from a 38% saving to a 9% slowdown [2]. Their own label for it: "only very weak evidence" [2]. The sample skewed too, because developers who refuse to work without AI dropped out and the study cut its pay to $50 an hour from $150 [2].

My read: the shift here is in buying, not in the models. When the published trials span 55.8% faster to 19% slower, a vendor's headline number says nothing about your team.

## By the numbers

- **55.8% — Greenfield speedup:** The Copilot trial's group finished one task, an HTTP (web) server in JavaScript, that much faster than the control group [3].
- **19% — Slower on known code:** Veteran maintainers took that much longer with AI tools on their own code, against their own forecast of a 24% speedup [1].
- **18% — Follow-up estimate:** The same group's later trial, inside a range from a 38% saving to a 9% slowdown [2].
- **84% — Already using AI:** Share of surveyed developers using or planning to use AI tools, with 46% distrusting the output against 33% who trust it [4].

<!-- tactical-insight -->

## What I'd watch:

The teams closest to this treat it as a measuring problem first and a licence problem second. Their attention sits in three places.

- **A trial on their own code:** The design behind the 19% result is easy to copy. They split each task into AI-allowed or AI-disallowed, draw the work from their own backlog, keep it near two hours, and read the result from the code that shipped rather than from the engineer's own guess [1]. The original tasks ran 2.0 hours on average [1].
- **Where the gains concentrate:** The positive result is one brand-new task in an unfamiliar setting [3]. The negative one is maintainers on code they wrote [1]. Seats look likelier to earn out on onboarding, migrations and services nobody owns.
- **The upkeep line:** GitClear's look at 211 million changed code lines found cloned lines rising from 8.3% to 12.3%, while clean-up work fell from 25% of changed lines to under 10% [5]. That is the vendor's own dataset, so I read it as a line to track, not as proof.
- **What the best shops look like:** LinearB's benchmark puts the top 10% of 253 companies at 54% of pull requests getting AI help, 45% of merged lines written by AI, and under 5% of pull requests coming from self-running agents (also called agentic pull requests). Those merge at 79%, against 92% for human-only work [6]. Also vendor data, and the clearest case for splitting the assistant budget from the agent budget.

What I'm watching next is the second trial's range, not its single number. A spread from a 38% saving to a 9% slowdown is the honest shape of this data. A deck that quotes one number is quoting the part that moves easiest.

<!-- nuanced-takeaway -->

## The catch

The 19% result is narrow by design: 16 developers, early-2025 tools, familiar code [1]. METR's own later work now points toward a speedup on newer models, while still calling its data weak [2].

The high end is narrow too. The 55.8% figure comes from one task with a known finish line, closer to a fresh exercise than to a Tuesday inside a legacy service [3]. Numbers from a single task travel badly between code bases.

The two supporting datasets, the clone drift and the use benchmark, are both vendor-owned [5][6]. Neither is neutral, and both count their own customers' code.

My read: none of this argues that the tools fail. It argues that the number you renew against has to come from inside your own code, using the same random split the two trials used. Without it, the licence case is a feeling with a decimal point.

<!-- tldr -->

## At a glance

- **The Big Shift:** Random trials of AI coding tools disagree by about 75 points. GitHub's Copilot study found 55.8% faster on one brand-new task [3], while METR's trial found veteran maintainers 19% slower on code they knew [1]. Use is already near-total, at 84% of surveyed developers [4].
- **Why It Matters:** A fleet licence usually gets signed on a vendor's headline speedup, yet the published data spans a 38% saving to a 9% slowdown in one follow-up range [2]. The seat count turns on a measurement the buyer has not run.
- **What I'd Watch:** How engineering leaders produce their own number before a renewal.
  - **A random task trial:** Backlog items split into AI-allowed and AI-disallowed, with the result read from the merged code rather than from developer estimates [1].
  - **Where the seats earn out:** Unfamiliar work, such as onboarding, migrations and unowned services, is where the published gains sit [1][3].
  - **The upkeep line:** Cloned code rising while clean-up falls, in a vendor dataset of 211 million changed lines [5]. This is where a speedup can come back as rework.
- **The Catch:** The 19% figure rests on 16 developers using early-2025 tools [1]. The 55.8% figure rests on one task with a known finish line [3], and the two supporting datasets are vendor-owned [5][6]. METR's later trial still spans a saving to a slowdown [2].

## Sources
[1] METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity" (arXiv:2507.09089) — https://arxiv.org/html/2507.09089v1
[2] METR, "We are Changing our Developer Productivity Experiment Design" (24 February 2026) — https://metr.org/blog/2026-02-24-uplift-update
[3] Sida Peng, Eirini Kalliamvakou, Peter Cihon, Mert Demirer, "The Impact of AI on Developer Productivity: Evidence from GitHub Copilot" (arXiv:2302.06590) — https://arxiv.org/abs/2302.06590
[4] Stack Overflow, "2025 Developer Survey — AI" — https://survey.stackoverflow.co/2025/ai
[5] GitClear, "AI Copilot Code Quality: 2025 Look Back at 12 Months of Data" — https://www.gitclear.com/ai_assistant_code_quality_2025_research
[6] LinearB, "The AI engineering productivity gap: 2026 benchmarks" — https://linearb.io/resources/ai-engineering-productivity-gap
