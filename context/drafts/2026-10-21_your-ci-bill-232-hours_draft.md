---
title: "Your CI Bill: 232 Hours Before You Build"
vertical: enterprise_build_vs_buy
persona: eng_leader
one_big_thing: "Hosted build minutes and a rented server are the same compute priced two ways, so the build decision is a utilisation test: a two-core rented runner has to be busy about 50 hours a month just to cover its own bill, and about 232 hours a month once one hour of engineer upkeep is added at the 2025 median developer wage."
date: 2026-10-21
slug: your-ci-bill-232-hours
archetype: evergreen
evergreen: true
---

<!-- lead -->
The continuous integration (CI) line on the cloud bill reads as compute you could run yourself, and the published prices agree: $0.006 a minute for a two-core hosted build machine [1], $18 a month for the same two cores rented from a host [2]. What neither price states is how often the rented box has to be busy. At the 2025 median developer wage [3], your own runner needs about 232 hours a month before one hour of engineer time pays for itself.

<!-- tension -->

## The big picture:

Both sides of this call now publish a rate, which makes the decision look like multiplication. It is not.

A hosted minute is metered per job. A rented server bills whether a job runs or not. That one difference decides more of the arithmetic than the price gap does [1][2].

The gap itself is wide. Run a hosted two-core flat out for a 730-hour month and the bill is $262.80 [1]. The rented two-core is $18 for that same month [2], about 14 times less.

That number is what sells the build. What strikes me is that it leaves out the idle hours.

A rented two-core has to be busy about 6.9% of the month, roughly 50 hours, before it is the cheaper of the two [1][2]. Below that, the meter wins on hardware alone.

Then the engineer arrives. GitHub's own documentation says usage is free for self-hosted runners [1], which is true, and which is the trap: free to use is not free to run.

At $65.38 an hour, one hour of upkeep a month costs the same as 182 hosted two-core hours [1][3]. Two hours a month lifts the bar to 413 hours, or about 13.6 hours of every day [1][2][3].

## By the numbers

- **$0.006 a minute — Hosted two-core rate:** Linux two-core minutes from GitHub, against $0.062 for macOS, $0.010 for Windows and $0.002 for a single-core slim runner [1]. A macOS minute costs about 10 times a Linux one.
- **$18.00 a month — Rented two-core server:** A DigitalOcean Droplet with two processors, listed at $0.02679 an hour [2].
- **6.9% — Hardware break-even:** A hosted two-core run flat out for a 730-hour month comes to $262.80, so the rented server only wins once it is busy about 50 hours a month [1][2].
- **182 hours — One engineer-hour:** At the 2025 median wage of $65.38 [3], one hour of upkeep a month equals 182 hosted two-core hours. Two hours a month lifts the bar to 413 hours, or about 13.6 a day [1][2][3].

<!-- tactical-insight -->

## What I'd watch:

The teams I see getting this wrong are rarely wrong about the price. They compare a meter to a machine as if both were billed the same way.

- **The unit is not the minute:** GitLab bills hosted runners in cost factors of 1 for a small Linux box, 2 for medium, 3 for large, 6 for xlarge and 12 for 2xlarge, with macOS at 6 and 12 [4]. CircleCI sells credits instead [5]. One word covers three different quantities, so a per-minute comparison across vendors is unreadable.
- **The cache meter:** GitHub charges $0.07 per gigabyte a month for cache and $0.25 for shared artifact storage [1]. CircleCI adds 200 credits, about $0.12, per job run for Docker layer caching on top of compute [5]. On a rented runner, that line is a disk already paid for.
- **The parallel-lane trick:** A single-core slim runner is $0.002 a minute, so two of them cost $0.004 against $0.006 for one two-core box [1]. Splitting a job across slim lanes is 33% cheaper per minute of wall clock, and the work has to be splittable.
- **Fixed load or bursty load:** Nightly build matrices and overnight test suites run close to flat out, which is where the rented box wins. A pipeline that spikes in the afternoon and idles overnight is the case the meter was built for.

<!-- nuanced-takeaway -->

## The catch

My read is that this is a threshold, not a verdict. Nothing here argues that self-hosted runners never pay.

The bar moves. Committed spend, enterprise discounts and bundled minutes all cut the hosted rate below list, which pushes the break-even higher. The wage is a national median, not a loaded cost with benefits and overhead, so a platform team's real hour costs more than $65.38 and the bar sits further away [3].

The build still wins sometimes. A runner pool that also carries nightly regression, security scans or model training is busy far past 232 hours a month, and at that point the hardware gap is real money.

The maintenance never sits in the spreadsheet as one clean line: patching the runner image, rotating machine credentials, clearing disk, rebuilding the cache after each base-image change. That is the hour the arithmetic charges for, and it arrives in fragments.

The part I keep circling: the macOS lane runs at $0.062 a minute [1], and a rented Linux box does not reproduce it. Whatever a team decides about Linux build minutes, the Apple lane stays on the meter.

<!-- tldr -->

## At a glance

- **The Big Shift:** Hosted build minutes and rented servers are the same compute priced two ways, $0.006 a minute against $18 a month [1][2]. The real difference is that one meters per job and the other bills while idle.
- **Why It Matters:** Renting looks about 14 times cheaper on paper, but a two-core server has to be busy roughly 50 hours a month just to cover its own bill, and about 232 hours a month once one engineer-hour of upkeep is added [1][2][3].
- **What I'd Watch:** Whether the runner pool is busy enough to make the hardware gap real.
  - **Utilisation of the pool:** The share of the month the runners are actually executing jobs, because that is the only variable that decides the call.
  - **The unit each vendor bills in:** Cost factors, credits and dollars per minute are different quantities, so list prices do not compare directly [4][5].
  - **The cache and storage lines:** Meters that survive the move to a rented box, because the disk is already paid for [1][5].
- **The Catch:** Committed spend and bundled minutes push the hosted rate below list, a loaded engineer-hour costs more than the median wage, and the macOS lane stays on the meter whatever else changes [1][3].

## Sources
[1] GitHub. "GitHub Actions billing." GitHub Docs, read 2026-10-21. https://docs.github.com/en/billing/concepts/product-billing/github-actions

[2] DigitalOcean. "Droplet Pricing." Read 2026-10-21. https://www.digitalocean.com/pricing/droplets

[3] O*NET OnLine. "Software Developers (15-1252.00): Wages & Employment Trends," 2025 wage data. Read 2026-10-21. https://www.onetonline.org/link/summary/15-1252.00

[4] GitLab. "Compute minutes." GitLab Docs, read 2026-10-21. https://docs.gitlab.com/ci/pipelines/compute_minutes/

[5] CircleCI. "Pricing." Read 2026-10-21. https://circleci.com/pricing/
