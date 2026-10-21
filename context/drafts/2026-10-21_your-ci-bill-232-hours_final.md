---
title: "Your CI Bill: 232 Hours Before You Build"
vertical: enterprise_build_vs_buy
persona: eng_leader
one_big_thing: "Hosted build minutes and a rented server are the same compute priced two ways, so the build decision is a utilisation test: a two-core rented runner has to be busy about 50 hours a month just to cover its own bill, and about 232 hours a month once one hour of engineer upkeep is added at the 2025 median developer wage."
date: 2026-10-21
slug: your-ci-bill-232-hours
archetype: evergreen
evergreen: true
image_path: "context/assets/illustrations/your-ci-bill-232-hours/featured.png"
image_style: "clay_render"
image_model: "nanobanana"
image_alt: "The Math Of Self-Hosted CI. Split-screen mechanical assembly showing a metered server module alongside a dedicated hardware"
image_caption: "The Math Of Self-Hosted CI: Why engineer upkeep breaks the self-hosted build math."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
The continuous integration (CI) line on your cloud bill looks like compute you could run yourself. The list prices say so: $0.006 a minute for a two-core hosted build machine [1], against $18 a month for the same two cores rented from a host [2]. At the 2025 median developer wage, that rented runner needs about 232 hours a month of busy time before one hour of engineer upkeep pays for itself [3].

<!-- tension -->

## The big picture:

Both sides publish a rate, making the build-versus-buy decision look like simple multiplication.

It is not. A hosted minute meters per job, while a rented server bills whether a job runs or not [1][2].

The price gap itself is wide. Run a hosted two-core flat out for a 730-hour month and the bill hits $262.80 [1]. A rented two-core costs $18 for that same month [2].

That 14-fold difference is what sells teams on hosting their own builds. What strikes me is how often this math ignores the idle hours.

A rented two-core must stay busy about 6.9% of the month, or roughly 50 hours, before it beats the hosted meter on hardware alone [1][2].

Then the engineer arrives. GitHub's docs say self-hosted runners are free to use [1]. But free to use is not free to run.

At $65.38 an hour, one hour of upkeep a month costs the same as 182 hosted two-core hours [1][3]. Two hours of maintenance a month push the bar to 413 hours. The box has to run jobs for about 13.6 hours of every day [1][2][3].

## By the numbers

- **$0.006 a minute — Hosted two-core rate:** Linux two-core minutes from GitHub, against $0.062 for macOS, $0.010 for Windows and $0.002 for a single-core slim runner [1]. A macOS minute costs about 10 times a Linux one.
- **$18.00 a month — Rented two-core server:** A DigitalOcean Droplet with two processors, listed at $0.02679 an hour [2].
- **6.9% — Hardware break-even:** A hosted two-core running flat out for a 730-hour month costs $262.80, so the rented server only wins once it stays busy about 50 hours a month [1][2].
- **182 hours — One engineer-hour:** At the 2025 median wage of $65.38 [3], a single hour of upkeep equals 182 hosted two-core hours. Two hours a month lift the bar to 413 hours, or about 13.6 a day [1][2][3].

<!-- tactical-insight -->

## What I'd watch:

The teams I see getting this wrong rarely miss the price. They compare a meter to a machine as if both bill the same way.

- **The billing units:** GitLab bills hosted runners in cost factors, 1 for a small Linux box and 2, 3 and 6 as the sizes climb, up to 12 for its largest. macOS sits at 6 and 12 [4]. CircleCI sells credits instead [5]. Comparing per-minute rates across vendors rarely works.
- **The cache meter:** GitHub charges $0.07 per gigabyte a month for cache and $0.25 for shared artifact storage [1]. CircleCI adds 200 credits, about $0.12, per job run for Docker layer caching [5]. On a rented runner, that disk is already paid for.
- **The parallel-lane trick:** A single-core slim runner costs $0.002 a minute, meaning two cost $0.004 against $0.006 for one two-core box [1]. Splitting a job across slim lanes saves 33% per minute of wall clock.
- **The load shape:** Nightly build matrices and overnight test suites run close to flat out, which favors the rented box. A pipeline that spikes in the afternoon and idles overnight is exactly what the meter was built for.

<!-- nuanced-takeaway -->

## The catch

My read is that this 232-hour mark is a threshold, not a verdict. Self-hosted runners still pay off in the right setup.

The bar moves. Committed spend, enterprise discounts and bundled minutes all cut the hosted rate below list price [1].

The wage is also a national median. A platform team's loaded cost, with benefits and overhead, runs higher than $65.38 an hour, which pushes that line further away [3].

The rented build still wins sometimes. A runner pool that handles nightly regression tests, security scans or model training stays busy far past 232 hours a month. At that volume, the hardware gap is real money.

The upkeep never shows up as one clean line. Patching the runner image, rotating machine keys and rebuilding the cache arrive in fragments.

The part I keep circling: the macOS lane runs at $0.062 a minute [1]. A rented Linux box cannot replace it, so the Apple lane stays on the meter no matter what.

<!-- tldr -->

## At a glance

- **The Big Shift:** Hosted minutes and rented servers are the same cores sold two ways [1][2]. One meters per job, while the other bills whether it runs or sits idle.
- **Why It Matters:** Renting looks 14 times cheaper on paper, but a two-core server must run jobs for about 50 hours a month just to cover its own bill. Add one hour of engineer upkeep, and that break-even jumps to 232 hours a month [1][2][3].
- **What I'd Watch:** Whether the runner pool stays busy enough to make the hardware savings real.
  - **Pool utilization:** The share of the month the runners actually execute jobs, since idle time destroys the rented margin.
  - **Vendor billing units:** Cost factors, credits and dollars a minute are different units, so list prices do not compare [4][5].
  - **Cache and storage:** Meters that survive the move to a rented box, because the disk is already paid for [1][5].
- **The Catch:** Committed spend cuts the hosted rate below list price, a loaded engineer-hour costs more than the median wage, and the pricey macOS lane stays on the meter regardless [1][3].

## Sources
[1] GitHub. "GitHub Actions billing." GitHub Docs, read 2026-10-21. https://docs.github.com/en/billing/concepts/product-billing/github-actions

[2] DigitalOcean. "Droplet Pricing." Read 2026-10-21. https://www.digitalocean.com/pricing/droplets

[3] O*NET OnLine. "Software Developers (15-1252.00): Wages & Employment Trends," 2025 wage data. Read 2026-10-21. https://www.onetonline.org/link/summary/15-1252.00

[4] GitLab. "Compute minutes." GitLab Docs, read 2026-10-21. https://docs.gitlab.com/ci/pipelines/compute_minutes/

[5] CircleCI. "Pricing." Read 2026-10-21. https://circleci.com/pricing/

## Gate report
lead: PASS — Delivers the two list prices and the 232-hour takeaway in the first paragraph, with CI expanded on first use and no preamble.
tension: PASS — States the metering difference, the 14-fold gap and the utilisation floor in short paragraphs, with a first-person cue ("What strikes me").
tactical-insight: PASS — Four bullets on billing units, cache metering, lane splitting and load shape, reported as observation rather than instruction.
nuanced-takeaway: PASS — Names what moves the bar (discounts, loaded wage, busy pools, macOS) with the first-person cue ("The part I keep circling").
tldr: PASS — The four-slot schema with indented sub-bullets; both sides of the comparison and the caveats are present.
