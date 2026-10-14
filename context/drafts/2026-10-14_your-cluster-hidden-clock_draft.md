---
title: "Your Cluster's Hidden Clock: 3 Minor Versions, 1 Year"
vertical: enterprise_build_vs_buy
persona: eng_leader
one_big_thing: "What a managed platform layer actually sells is the upgrade calendar: every self-hosted component inherits an upstream support clock — Kubernetes patches only its three newest minor versions for about a year, PostgreSQL holds a major version for five years — and the bought side now publishes a price for taking that clock off a team's hands, from $0.10 per cluster-hour at Google Cloud to a free control plane at DigitalOcean."
date: 2026-10-14
slug: your-cluster-hidden-clock
archetype: evergreen
evergreen: true
---

<!-- lead -->
Kubernetes patches only its three newest minor versions, then drops each one about a year after it ships [1]. PostgreSQL holds a major version for five years and ships a fix at least every three months [2]. Those two clocks are the hidden part of a platform's bill, and the bought side now publishes what it charges to take your cluster's clock off your hands: $0.10 per cluster-hour at Google Cloud, or a free control plane at DigitalOcean with $40 a month for high availability [4][5].

<!-- tension -->

## The big picture:

Every layer a team runs itself inherits a clock that the upstream project publishes. The clock says how long a version stays patched, and how often the project expects anyone to move.

The licence is the visible part of self-hosting. The calendar is the part that rarely reaches the spreadsheet.

What strikes me is how narrow some of those windows turn out to be.

I have watched this shape of cost land. One platform team built its own deployment dashboard to avoid a $20,000-a-year enterprise licence.

Over 24 months, three senior engineers sank about 1,200 hours into it, mostly on upgrades that kept pace with the cluster software and on single sign-on work. The tool was scrapped in the end.

The published clocks say the same thing in plainer numbers. Kubernetes supports only its newest three minor versions, and each gets roughly a year of patches; before version 1.19 that window was nine months [1]. PostgreSQL keeps a major version alive for five years, with fixes at least every three months [2].

Ubuntu's long-term support (LTS) line carries five years of standard security fixes, ten under an extended window and fifteen on a paid plan [3]. Node.js promises 30 months of fixes on its LTS releases and moves to an annual cycle from version 27 [7].

## By the numbers

- **Three minor versions, about a year — Kubernetes' window:** Release branches are maintained for the most recent three minor versions only, and versions from 1.19 on receive roughly one year of patches [1].
- **5 years, and a fix every 3 months — PostgreSQL's clock:** A major version is supported for five years from its release, and minor releases ship at least once every three months [2].
- **$0.10 per cluster-hour — the managed control plane:** Google's flat fee for a managed control plane, the same whatever the cluster's size or mode, with $74.40 in monthly free credit and a 99.95% uptime commitment on its regional control planes [4].
- **$65.38 an hour — the price of an hour not spent:** The 2025 median hourly wage for software developers [6]. Google's fee works out to $73 for a 730-hour month, about 1.1 hours of engineer time.

<!-- tactical-insight -->

## What I'd watch:

The buying side has started pricing the clock in the open, and the shapes are worth comparing.

- **The per-cluster fee:** Google charges $0.10 per cluster-hour whatever the cluster's size, then hands back $74.40 a month in credit, which covers a small cluster's whole management fee [4].
- **The free control plane:** DigitalOcean gives the managed control plane away and charges $40 a month only for the high-availability version [5]. One product class, two price shapes.
- **The clock sold by the year:** Canonical's ladder runs five years of standard maintenance, ten under an extended window and fifteen with a subscription [3].
- **The window that moved:** Kubernetes stretched its patch window to about a year at version 1.19, up from nine months [1]. A window that moved once can move again.

My read is that the teams handling this well keep a list of clocks rather than a list of licences, with one row per layer and a name beside each upgrade.

<!-- nuanced-takeaway -->

## The catch:

The honest limit is that a clock is not the whole bill. Buying a control plane retires one treadmill; it does not touch a workload's own upgrades, the data moves or the apps sitting on top [4][5].

Free cuts both ways as well. DigitalOcean's control plane costs nothing, and Google's credit covers a small cluster, so the fee on its own rarely settles the call. A low fee is a weak reason to move a workload that the managed tier cannot run.

The wage figure is a national median, not a team's own rate [6], and that median hides a wide spread by role and region.

What I keep circling is that these clocks are policy, not physics. Kubernetes changed its window once already [1]. The numbers above are as of October 2026, and the release calendar is the part I would re-check before committing to anything longer than a year.

<!-- tldr -->

## At a glance

- **The Big Shift:** Every platform layer a team runs in-house arrives with an upstream support clock. Kubernetes patches only its three newest minor versions, for about a year each; PostgreSQL holds a major version for five years; Node.js promises 30 months of fixes on its long-term support releases.
- **Why It Matters:** The licence fee is the visible cost of self-hosting, and the upgrade calendar is the hidden one. The bought side now prices that calendar openly: $0.10 per cluster-hour at Google Cloud, or a free control plane at DigitalOcean with $40 a month for high availability.
- **What I'd Watch:** Whether vendors keep pricing the clock in the open, and whether the projects shorten or stretch their windows.
  - **The per-cluster fee:** A flat hourly charge for a managed control plane, the same whatever the cluster's size.
  - **The free tier:** Monthly credit that covers one small cluster's management fee, which is what makes the effective price near zero for a single cluster.
  - **The subscription ladder:** Paid support that extends a free project's security window from five years to ten, and to fifteen on the paid tier.
- **The Catch:** A clock is not the whole bill. Buying one component leaves the workload's upgrades, the data migration and the wage on the operator's side of the ledger.

## Sources
[1] Kubernetes — "Releases" (release history and support policy): https://kubernetes.io/releases/
[2] PostgreSQL Global Development Group — "Versioning Policy": https://www.postgresql.org/support/versioning/
[3] Canonical — "Ubuntu release cycle" (security and support coverage): https://ubuntu.com/about/release-cycle
[4] Google Cloud — "Google Kubernetes Engine pricing" (cluster management fee, free tier, SLA): https://cloud.google.com/kubernetes-engine/pricing
[5] DigitalOcean — "Kubernetes pricing" (free control plane, high-availability option): https://www.digitalocean.com/pricing/kubernetes
[6] O*NET OnLine — Software Developers (15-1252.00), median wages 2025: https://www.onetonline.org/link/summary/15-1252.00
[7] Node.js — "Releases" (previous releases and long-term support policy): https://nodejs.org/en/about/previous-releases
