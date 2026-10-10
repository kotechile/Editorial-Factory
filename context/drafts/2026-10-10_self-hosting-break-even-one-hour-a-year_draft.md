---
title: "Self-Hosting Break-Even: 1.26 Hours a Year"
vertical: personal_microeconomics_tinkering_tax
persona: systems_tinkerer_pro
one_big_thing: "Self-hosting trades a small visible bill for a large invisible one: on 2025 medians, 1.26 hours of maintenance a year is enough to cancel a $60 mailbox bill, so cost is a bad reason to run your own services and a good reason to decide once."
date: 2026-10-10
slug: self-hosting-break-even-one-hour-a-year
archetype: evergreen
evergreen: true
---

<!-- lead -->
An hour of network-admin work was worth $47.66 at the 2025 median wage [1]. A year of managed email costs $60 [4]. Divide one by the other and the "free" self-hosted stack gets a break-even a reader can check: about an hour and a quarter of upkeep a year, after which the $5-a-month plan is the cheaper way to keep the same mailbox.

<!-- tension -->

## The big picture:

Self-hosting swaps a small bill you can see for a large one you cannot.

The pitch is always the same. Cancel the subscription, run the open-source version, keep the data. The visible price is the hardware and the electricity.

The real price is the hours.

What strikes me is that this price is not secret. It is simply never divided. Managed replacements publish their fees — $7 per user per month for mail and documents [5], $4 a month for a small rented server [6], $9.99 a month for two terabytes of storage [7] — and the wage side of the division is public as well [1]. Two published numbers settle most of these decisions before anyone opens a terminal.

The desk's own field file holds one case. A systems administrator spent 26 weekend hours chasing a self-hosted mail server that Gmail and Outlook were quietly blacklisting, and missed a real-estate deadline doing it. At a $150-an-hour engineering rate, that weekend was about $3,900 of unpaid labour set against a $72-a-year mailbox.

Repeat that across a home rack and the shape stays the same, service after service. The cash out is tiny. The time out is the cost.

## By the numbers

- **$47.66 per hour — Median admin wage:** The Labor Department's 2025 median pay for network and computer systems administrators, the benchmark that prices an hour of upkeep [1].
- **1.26 hours — Mail break-even:** One year of Fastmail is $60, so at the median rate 1.26 hours of maintenance erases the saving; Google Workspace at $7.00 per user per month crosses over at 1.76 hours [1][4][5].
- **16.31 watts — Storage box draw:** A two-bay home storage box pulls 16.31 watts with its disks spinning, about $25 a year at the 2025 residential average of 17.30 cents per kilowatt-hour [2][3].
- **$4.00 per month — Rented small server:** A basic cloud box that someone else patches and reboots [6].

<!-- tactical-insight -->

## What I'd watch:

I am watching the price side, because the managed fees keep getting cheaper and more public.

- **The published fees:** Fastmail at $60 for 12 months, Workspace at $7.00 per user per month, two terabytes at Apple for $9.99 a month, a small cloud server at $4.00 a month, and Tailscale free for up to 6 users — the remote access layer usually rebuilt by hand [4][5][6][7][8].
- **The chore clock:** fifteen minutes a month is three hours a year, which is $143 at the median rate — more than two years of the mailbox it replaced.
- **The failure modes:** the update that lands at 2 a.m., the certificate that expires quietly, the disk that dies on a Sunday. Each turns an hour meant for something else into an hour of firefighting.

What I take from that list is that the managed side stopped being the expensive one. The self-hosted side stopped being free in the way the pitch implies.

<!-- nuanced-takeaway -->

## The catch

The part I keep circling is that cost was never the real reason most people self-host.

Control is. So are privacy, no lock-in, and the plain fact that some jobs have no $7-a-month substitute — a media server, a two-disk backup, a rack you learn on. Those are real returns, and none of them show up in the division above.

The wage figure is also a benchmark, not a personal rate. A hobby hour on a Saturday is not a billed hour, and a national median hides a wide spread by region and by role. Someone who enjoys the work is paying in a currency they like.

My read: cost is a poor reason to self-host, and a good reason to decide once instead of drifting into it. Two numbers and one division settle the money question. Everything after that is preference, and preference gets to win — as long as nobody calls the server free.

<!-- tldr -->

## At a glance

- **The Big Shift:** Self-hosted services are still sold as "free," but the honest comparison is a division: the annual managed fee against the hourly value of the upkeep it replaces. On 2025 medians, an hour and a quarter of maintenance a year is enough to erase a $60 mailbox bill.
- **Why It Matters:** Managed mail, storage and small servers now list between $4 and $10 a month, while the hours they replace are priced at a median $47.66 an hour. The tinkering tax is not a metaphor; it has a number, and a fifteen-minute monthly chore costs more than two years of the plan it replaced.
- **What I'd Watch:** Whether the published fees keep falling and the upkeep clock keeps ticking, because both move the break-even.
  - **Break-even hours:** the annual fee divided by the hourly rate — 1.26 hours for a $60 mailbox, 2.52 hours for two terabytes at $9.99 a month.
  - **Always-on power:** a small storage box draws 16.31 watts, roughly $25 a year on the 2025 residential average.
  - **Free tiers:** the remote access layer now has a free plan for small setups [8], so rebuilding it by hand buys less than it used to.
- **The Catch:** Cost is not the only axis, and often not the real one. Control, privacy and the build itself are genuine returns, and a national wage median is not an individual rate.

## Sources
[1] US Department of Labor, O*NET OnLine — "15-1244.00 Network and Computer Systems Administrators," median wages (2025): https://www.onetonline.org/link/summary/15-1244.00
[2] US Energy Information Administration — "Electricity explained: Prices and factors affecting prices" (2025 annual average retail prices): https://www.eia.gov/energyexplained/electricity/prices-and-factors-affecting-prices.php
[3] Synology — "DS223j" specifications (power consumption 16.31 watts access, 4 watts hibernation): https://www.synology.com/en-us/products/DS223j
[4] Fastmail — pricing, Individual billed yearly ($5 per month, $60 for 12 months): https://www.fastmail.com/pricing/
[5] Google Workspace — pricing, Business Starter ($7.00 per user per month): https://workspace.google.com/pricing.html
[6] DigitalOcean — Droplet pricing ($4.00 per month, 512 MiB): https://www.digitalocean.com/pricing/droplets
[7] Apple — iCloud+ storage plan prices (2 TB at $9.99 per month, USD): https://support.apple.com/en-us/108047
[8] Tailscale — pricing (free plan up to 6 users): https://tailscale.com/pricing
