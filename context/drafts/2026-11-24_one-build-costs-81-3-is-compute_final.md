---
title: "One Build Costs $81 — $3 Is Compute"
vertical: workstation_compute_economics
persona: infra_engineer
one_big_thing: "The waiting on a build is paid in salary, not in machine time: GitHub's own experiment measured one 92-minute build billing $81, of which $2.94 was compute and $77.94 was developer time — a 26.5x multiple — and once each wait also collects a 23-minute re-entry tax on attention, five waits a day burn about $2,600 of payroll a month, so hardware that shaves build minutes pays back in weeks, priced against $75 an hour of engineer."
date: 2026-11-24
slug: one-build-costs-81-3-is-compute
kind: evergreen
archetype: evergreen
evergreen: true
meta_title: "One Build Costs $81 — $3 Is Compute"
meta_description: "GitHub measured a single 92-minute build billing $81: $2.94 of compute, $77.94 of developer time. The wait is a payroll line, and hardware that shaves it pays back in weeks."
meta_title_source: "derived_from_title"
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/one-build-costs-81-3-is-compute/featured.jpg"
image_style: "studio_object"
image_model: "flux"
image_alt: "One Build Costs $81 — $3 Is Compute. A compact build-runner workstation box on a data-hall floor, its long shadow stretching far beyond the"
image_caption: "One Build Costs $81 — $3 Is Compute: The wait bills as salary — hardware that shaves build minutes pays back in weeks."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
GitHub ran the bill on its own build fleet, and the machine barely shows. One 92-minute build on an 8-core runner cost $2.94 of compute and $77.94 of developer time [4]. That build billed $81 in total; $3 of it was the machine, because the wait is billed as salary. The rest is payroll that no invoice shows, and it should decide whether you buy hardware or rent patience at $75 an hour of engineer [3].

<!-- tldr -->
## At a glance

This article prices a developer's build wait as a payroll line for engineering leads deciding between faster hardware and a slower queue. On GitHub's measured build, salary outruns machine time 26.5 times, so a box that cuts the wait earns its cost back in weeks.

<!-- tension -->
## Where the money actually goes

The bill splits before anyone sees it. A developer pushes code, the build runs elsewhere, and the pusher sits interrupted until it returns. Continuous integration (CI) — the automated build-and-test run after every push — is bought as compute but consumed as attention. The loaded cost of a US developer runs near $150,000 a year, or about $75 an hour, from the Stack Overflow 2022 survey [3].

GitHub's measured build table shows what that hourly rate does to each run. At 92 minutes on 8 cores, $2.94 of compute sat next to $77.94 of developer time [4]. The machine was the cheap part by 26.5 times. The engineer paid to wait is the expensive half, and no cloud dashboard prints that half.

The interruption adds a second, slower bill. Field research at the University of California, Irvine measured that interrupted work resumed the same day takes 23 minutes 15 seconds to get back to, on average [1]. Most such work — 81.9 percent — resumes the same day, so the tax lands inside a normal working day rather than on lost time [2]. A build wait is an interruption of exactly this kind: the developer switches to something else, then pays the re-entry cost when the queue turns green.

Run the monthly arithmetic on inputs you can replace with your own. Say a developer triggers five builds a day and waits 20 minutes per run — a working assumption, not a sourced figure. Five waits of 20 minutes over 21 working days is 35 hours a month, which at $75 an hour is $2,625 of payroll per developer [3]. The re-entry tax on top adds about 41 hours — another $3,052. The build fleet's own bill is single-digit dollars a day. I have never seen a budget review where anyone approved a $2,625 line item, because it never appears as a line item at all.

<!-- numbers -->
## By the numbers

- **$77.94 per build:** The developer time GitHub measured on one 92-minute build, against $2.94 of compute [4].
- **23-minute re-entry:** The measured recovery time for a task interrupted and then resumed the same day [1].
- **$2,625 a month:** The payroll five 20-minute waits a day burn at $75 an hour — arithmetic to replace with your own wait [3].

<!-- tactical-insight -->
## What teams that fixed it did

The clearest proof comes from teams that treated the wait itself as infrastructure. Elastic's Kibana pull-request pipeline ran 3 hours per change. Its team moved the pipeline to Buildkite's runners and cut that to 55 minutes — a 70% drop — and reported developers could "continue your work today" instead of hearing back the next day [5]. The fix was runner capacity, bought once and serving every push since. A workstation on a desk removes the queue the same way. If it cuts the 20-minute wait in half, the saved 17.5 hours a month is about $1,312 of payroll, which pays a $3,500 box back in roughly 2.7 months [3]. The [GPU total-cost-of-ownership calculator](/tools/gpu-compute/) runs that trade with your own minutes and watts. What strikes me when I line these up is that both fixes were priced in engineer-minutes, not in machine-dollars — and both paid for themselves inside a quarter.

<!-- nuanced-takeaway -->
## The catch

What I find hard to square is that the strongest figure here is the least verifiable on your team. The 23-minute re-entry result — the measured recovery time from the Irvine research above — comes from observations of office workers in 2004 and 2005, published through a 2006 interview, not from a study of build queues [1]. Some of your engineers may watch a second screen while a build runs and lose nothing. So measure first: record builds per day, record wait minutes, and price only the re-entry gap you can actually see. The payroll term dominates the machine term by 26.5 times in GitHub's table [4], so even a conservative reading of the re-entry tax leaves the decision unchanged. But the number that earns the purchase is your own, not the research's.

## Sources

- [1] Gallup Business Journal, "Too Many Interruptions at Work?" — Q&A with Gloria Mark (UC Irvine) — https://news.gallup.com/businessjournal/23146/too-many-interruptions-work.aspx
- [2] Gallup Business Journal, "Too Many Interruptions at Work?" — Q&A with Gloria Mark (UC Irvine) — https://news.gallup.com/businessjournal/23146/too-many-interruptions-work.aspx
- [3] GitHub Engineering Blog, "Experiment: The hidden costs of waiting on slow build times" — https://github.blog/engineering/infrastructure/experiment-the-hidden-costs-of-waiting-on-slow-build-times
- [4] GitHub Engineering Blog, "Experiment: The hidden costs of waiting on slow build times" — https://github.blog/engineering/infrastructure/experiment-the-hidden-costs-of-waiting-on-slow-build-times
- [5] Buildkite, "Elastic improves Kibana CI/CD run time by 70% after switching to Buildkite Pipelines" — https://buildkite.com/resources/case-studies/elastic
