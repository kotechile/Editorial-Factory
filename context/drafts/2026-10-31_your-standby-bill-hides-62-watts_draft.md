---
title: "Your Standby Bill Hides 62 Watts"
vertical: personal_microeconomics_tinkering_tax
persona: systems_tinkerer_pro
one_big_thing: "The 5 to 10 percent of household electricity that standby draws works out to 62 to 123 watts of continuous load, which forty compliant half-watt adapters cannot account for, so a device-by-device vampire hunt with a sub-$50 meter collects about a dollar fifty a watt a year while costing an hour that bills at $47.66."
date: 2026-10-31
slug: your-standby-bill-hides-62-watts
kind: evergreen
archetype: evergreen
evergreen: true
---

<!-- lead -->
Your standby bill hides about 62 watts of continuous draw, and the adapters you would go unplug are not where it lives. Berkeley Lab puts standby at 5 to 10 percent of residential electricity use [1], and because the average United States residential customer bought 10,791 kilowatt-hours in 2022 [6], the low end of that share is 540 kilowatt-hours a year. One watt held for a year is 8.76 kilowatt-hours, so 540 divided by 8.76 is about 62 watts.

Forty power supplies sitting at the federal no-load ceiling of 0.5 watts [5] draw 20 watts between them. That is a third of the low end, and the ceiling is a maximum rather than an average. The watts did not disappear when the bricks got better. They moved.

<!-- tension -->

## The big picture:

The folklore is less wrong than out of date, and the regulation explains why. A power supply sold in the United States has carried a federal limit on its no-load draw since 2008, when the standard for a class A supply up to 250 watts settled at half a watt [5]. Berkeley Lab's own history of the field says typical products drew 1 to 3 watts two decades ago and sit near a fraction of a watt now [2].

What changed is the count. The same lab notes that products with standby multiplied faster than their draw fell, leaving roughly the same standby energy spread over far more devices [2]. So the share of the bill barely moved while its address did: out of the bricks on the floor and into the boxes that never really turn off.

What strikes me is how faithfully the advice kept pointing at the bricks. Every guide to cutting standby tells you to unplug chargers, and every charger made since 2008 is capped at a level that cannot pay for the effort. The share the lab measures is real, and it is now carried by a small number of devices drawing watts rather than milliwatts.

## By the numbers

- **123 watts — The top of the band:** Ten percent of that household purchase is 1,079 kilowatt-hours and a continuous average of 123 watts, which is the range a set-top box, a receiver and an older appliance occupy [1][6].
- **$93 to $187 — The bill behind the share:** At the 2025 residential average of 17.30 cents a kilowatt-hour, the band is $93 to $187 a year of electricity nobody switched on [1][7].
- **$1.56 — A watt-year at today's rate:** The lab's rule of thumb is 9 kilowatt-hours and about $1.20 at a tariff of 13 cents; at the 2025 average the same watt is $1.56, so the worked example now understates itself [2][7].

<!-- tactical-insight -->

## What I'd watch:

I keep coming back to three numbers, because they decide whether the afternoon is worth spending.

- **The hour — $47.66.** The 2025 median wage for network and computer systems administrators is $47.66 [8], and the entire first-year recovery of about a fifth of the band is $18.67 to $37.34 [1][3][7]. That is the same division that priced the self-hosting maintenance hour in [Self-Hosting Break-Even: 1.26 Hours a Year](/self-hosting-break-even-one-hour-a-year/), with the audit on the wrong side of it.
- **The meter — under $50.** The lab sells the audit and then undercuts its instrument: meters cost less than $50, and their errors grow relatively larger when standby is below about a watt [4]. The target and the blind spot are in the same place.
- **The loads worth chasing — above 10 watts.** A 10-watt load held all year is 87.6 kilowatt-hours and about $15.15 [7], so a dozen of those outweigh every brick in the house, and they are visible on a whole-home meter in one evening.
- **The payback on the instrument — 1.3 to 2.7 years.** That is what a $50 meter returns at the lab's own 20 percent [3][4], and it assumes the reader captures all of the 20 percent rather than the two or three devices that are easy to reach.

My read is that the ordering is backwards in almost every guide: the devices that are cheap to unplug are the ones that stopped mattering, and the devices that matter are the ones a person forgets are on.

<!-- nuanced-takeaway -->

## The catch

The share is an estimate rather than a survey, and the lab says so: both the portion of the bill it attributes to standby and the portion of that an aggressive audit can recover rest on limited research, not on a national metered sample [1][3]. Treat the band as a scale, not a reading.

What I find more limiting is the instrument. A meter that is honest above a watt and approximate below it cannot tell a reader whether the thing in the guest room is drawing four watts or none, and the difference between those two answers is the difference between a dollar and four dollars a year.

The audit is not worthless. It pays from the second year if the reader skips the per-device hunt and starts from the whole-home baseline, where a receiver, a set-top box or a retired server shows up as a step rather than a trickle. A house can carry most of its own share in two devices, and both are found in minutes. The error is spending an hour to find a fifth of a watt, then calling the hour free.

<!-- tldr -->

## At a glance

- **The shift:** Standby is 5 to 10 percent of household electricity, and the adapters are no longer where it sits.
- **The number:** The band implies 62 to 123 watts; a 20 percent cut returns $19 to $37 a year against an hour billed at $47.66.
- **The risk:** The share is a lab estimate, and the meter cannot resolve the loads below a watt.

## Sources
[1] Lawrence Berkeley National Laboratory — "Standby Power" (standby is 5-10% of residential electricity use): https://standby.lbl.gov/
[2] Lawrence Berkeley National Laboratory — "Frequently Asked Questions About Standby Power" (one watt for a year is 9 kWh, about $1.20 at 13 cents; typical products were 1-3 W two decades ago and are near 0.5 W now): https://standby.lbl.gov/frequently-asked-questions
[3] Lawrence Berkeley National Laboratory — "Frequently Asked Questions About Standby Power", reduction section (an informed and aggressive approach cuts standby about 20%; "there are more productive ways to save energy with an investment of an hour"): https://standby.lbl.gov/frequently-asked-questions
[4] Lawrence Berkeley National Laboratory — "Frequently Asked Questions About Standby Power", measuring section (meters cost less than $50; errors grow relatively larger below about 1 W): https://standby.lbl.gov/frequently-asked-questions
[5] Electronic Code of Federal Regulations — 10 CFR 430.32(w)(1), no-load mode ceiling of 0.5 watts for class A external power supplies up to 250 watts: https://www.ecfr.gov/current/title-10/chapter-II/subchapter-D/part-430/subpart-C/section-430.32
[6] US Energy Information Administration — "How much electricity does an American home use?" (10,791 kWh a year, about 899 kWh a month, 2022): https://www.eia.gov/tools/faqs/faq.php?id=97&t=3
[7] US Energy Information Administration — "Electricity explained: Prices and factors affecting prices" (2025 annual average residential price 17.30 cents per kWh): https://www.eia.gov/energyexplained/electricity/prices-and-factors-affecting-prices.php
[8] O*NET OnLine, US Department of Labor — "15-1244.00 Network and Computer Systems Administrators" (median wage 2025: $47.66 hourly, $99,130 annual): https://www.onetonline.org/link/summary/15-1244.00
