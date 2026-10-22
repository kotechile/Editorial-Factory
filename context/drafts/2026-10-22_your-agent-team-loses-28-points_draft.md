---
title: "Your Agent Team Loses 28 Points: The 188x Bill"
vertical: agentic_ai
persona: ai_architect
one_big_thing: "A second agent is not a capability purchase: measured against the same model alone it costs 1.8 to 5.1 times as much for a gain inside the noise, and up to 188 times as much in code review where it doubles the unverified claims."
date: 2026-10-22
slug: your-agent-team-loses-28-points
synthesis: true
sources:
  - https://arxiv.org/abs/2610.27655
  - https://www.vals.ai/blogs/multi-agent-vibe-code-bench
---

<!-- lead -->
An agent team loses 28 points against a single agent on the same job. The same week produced a 188-fold bill for one. The first figure is the weighted mean from a pre-registered study of about 7,950 simulated customer chats, across six models from three families [1]. The second comes from twenty pull requests run through one shipped review command [3]. A third test, fifty app builds released on 9 October, sits between them at 1.8 to 5.1 times the cost [2]. None of the three is about the model. All three are about the second agent.

<!-- tension -->

## The big picture:

The field had a rule for this. Teams help while the single agent is weak. They hurt once it is strong, and the crossing sits near 45% single-agent accuracy. The new paper calls that the most systematic finding to date, and notes it came from tests where no user takes part [1].

The new study tests the rule where agents now work: in chat with a person, under a written policy. On the airline, retail and telecom tasks, the team is worse in 12 of the 13 valid cells and tied in the thirteenth [1]. My read is that the setting broke the rule, not the model.

That matters because the team is being sold as an architecture. A lead agent splits a job, hands each slice to a helper, and glues the results back together. Both big labs ship the primitive. The pitch is speed: split the work and finish sooner.

What I keep circling is that the cost and the failure land in different places. The team burns tokens re-reading context it already had. It then fails by running out of budget, not by writing something wrong. The paper finds no clear drop in bad database writes, and it finds that other failures turn into budget exhaustion and inaction [1]. A single agent that writes the wrong row is a bug you can trace. A team that never finishes is an argument.

## By the numbers

- **12 of 13 — Cells where the team lost:** a team built from the same model, run against the plain single agent under a fixed simulated user. Worse in 12 cells, tied in one, with a fitted gain of -28 points and a 95% range of -44 to -12 [1].
- **1.8x to 5.1x — Team cost premium:** fifty app builds, one run per setup. Only one of four score gaps cleared significance: a 7.3-point gain for the cheapest team in the study. The rest ran from -0.3 to +3.4 points [2].
- **23.9 vs 11.9 — Unmatched claims per pull request:** the review fan-out found 23 of 27 serious issues against 21 for one agent. It found the same 47 of 65 issues overall. The extra claims doubled. The findings did not [3].
- **224 million — Cached tokens read per app:** the slowest team's helpers, against 17 million for their lead and 55 million for the single agent. Most of the team's extra spend is its own context, sent again on every call [2].

<!-- tactical-insight -->

## What I'd watch:

One setup did pay, and it is the useful one. The medium-effort team of OpenAI's Sol gained 7.3 points at p = 0.005 [2]. The write-up shows where that came from. On the nine apps where it gained 20 points or more, the lone agents had said their tests passed when some features were never built. The team built them, and its lead checked the parts against each other [2].

That is not parallel work buying skill. That is one agent doing the check the other skipped. The review numbers show the same thing from the far side. There the team doubled the claims at 188 times the recorded subtotal, and the found-issue count moved by two, which its author calls scoring noise [3].

- **The check is the thing you buy.** What the team added was a second reader of seams: a form that did not match the schema, a rule that blocked a step. An integration test catches those too, and it does not re-read 224 million cached tokens.
- **More effort competes with more agents.** Sol's top-effort single agent cost $4.82 an app and scored 89.0%. Its medium-effort team cost $3.07 and scored 84.9% [2]. That is effort against agents, not team against single agent, and it is the pair I would put beside any plan to add a supervisor.
- **Claims need a judge that cannot see them.** A study published on 21 October found that hiding an agent's own success note lifted trace-only detection of false claims by 43.4 points on one model and 13.3 on another [4]. A claim-blind reader reached an F1 of 0.75 to 0.78 [4]. If teams mainly add claims, that reader is where the next bill lands.
- **What I'm watching next:** whether a vendor prints a paired, compute-matched test from the setting it sells into. The dual-control result came from a pre-registered study with a public change log, and that is rare.

<!-- nuanced-takeaway -->

## The catch

All three tests are narrow. Each was run by someone with a stake in its setting. The dual-control paper names a bar it did not meet: the team's planner never saw the tool schemas [1]. It also calls the trend in capability unresolved, with a slope of -0.41 and a range from -1.51 to +0.68 [1]. It cannot tell you that teams get worse as models improve.

The app-build study covers one kind of work, full-stack web apps, with one run per setup. Its author says so and warns the result may not hold elsewhere [2]. The review test compares two shipped settings that differ in more than agent count. It ran once per setup on twenty hard pull requests, and its author sells a rival tool [3].

I could be wrong about where this goes. A team whose lead already knows how to test seams may be a fair buy at 1.8 times the cost. None of these studies ran on your workload.

<!-- tldr -->

## At a glance

- **The Big Shift:** Three separate tests, published inside thirteen days, found the agent team costs 1.8 to 188 times as much as one agent. The shift in verified score sat inside the noise. The one team that won was also the cheapest in its study.
- **Why It Matters:** The team payoff was measured on tests with no user in the loop. On user-facing work the team turns failures into spent budget, and its extra output is claims, not findings. So the check is what has to be bought, not the agent.
- **What I'd Watch:** Three signals decide if a team earns its premium in a given shop.
  - **A paired test in your own setting:** the only real win came from a same-task comparison, not from a public average, and the paper that tested the field's rule used a pre-registered design.
  - **Cached input per helper:** each helper sends its own copy of the spec and its working state on every call, which is where 224 million tokens an app went.
  - **Claim counts beside finding counts:** the review team doubled unmatched claims while the found issues moved by two, so a team should be scored on confirmed finds.
- **The Catch:** One test family with a stated gap, one 50-app study with a single run per cell, one vendor test on twenty pull requests. All three are real evidence for their own setting. None of them is your workload.

## Sources
[1] https://arxiv.org/abs/2610.27655
[2] https://www.vals.ai/blogs/multi-agent-vibe-code-bench
[3] https://quickchat.ai/post/claude-code-multi-agent-code-review
[4] https://arxiv.org/abs/2610.29609
