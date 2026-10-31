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
meta_title: "Your Standby Bill Hides 62 Watts"
meta_title_source: "derived_from_title"
meta_description: "Your standby bill hides about 62 watts of constant draw because the energy moved out of your wall chargers and into larger appliances."
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/your-standby-bill-hides-62-watts/featured.jpg"
image_style: "clay_render"
image_model: "nanobanana"
image_alt: "The 62 Watt Standby Load. A heavy-duty power meter block and a tiny standard wall adapter rendered in matte clay on a concrete surface."
image_caption: "The 62 Watt Standby Load: The hidden appliances driving your idle electricity bill."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Your standby bill hides about 62 watts of constant draw because the energy moved out of your wall chargers and into larger appliances. Berkeley Lab says standby power makes up 5 to 10 percent of home electricity use [1]. The average United States residential customer bought 10,791 kilowatt-hours in 2022 [6], so the low end of that chunk is 540 kilowatt-hours a year. Holding one watt for a full year takes 8.76 kilowatt-hours, which means 540 divided by 8.76 yields about 62 watts. Forty chargers sitting at the strict federal limit of 0.5 watts [5] only draw 20 watts total. That is barely a third of the low end, and the legal cap is a maximum rather than a daily average.

<!-- tension -->

## The big picture:

The old advice to unplug chargers is less wrong than out of date.

A power supply sold in the United States has faced a hard limit on its idle draw since 2008, setting the cap for a standard brick at half a watt [5]. The lab notes that typical products drew 1 to 3 watts two decades ago, yet they sit near a fraction of a watt now [2]. Devices with standby functions multiplied faster than their single draw fell, leaving roughly the same idle energy spread over far more boxes [2]. The total share of the bill barely moved, but the source shifted off the floor and into the gear that never actually turns off.

What strikes me is how faithfully energy guides keep pointing at those power bricks. Every guide tells you to unplug chargers, yet every charger made since 2008 is capped at a level that cannot pay for the effort. The share the lab measures is real, but a small number of devices drawing whole watts now carry that load.

## By the numbers

- **123 watts — Upper band limit:** Ten percent of that average home purchase equals 1,079 kilowatt-hours and a steady draw of 123 watts, which fits a set-top box, a receiver, and an older appliance [1][6].
- **$93 to $187 — Annual standby bill:** At the 2025 average rate of 17.30 cents a kilowatt-hour, this band costs $93 to $187 a year for electricity nobody switched on [1][7].
- **$1.56 — Single watt cost:** The lab assumes 9 kilowatt-hours and about $1.20 at a rate of 13 cents, but at the 2025 average, that same watt costs $1.56 [2][7].

<!-- tactical-insight -->

## What I'd watch:

I keep coming back to these numbers, because they decide whether a weekend power audit is worth your afternoon.

- **$47.66 — The hourly wage:** The 2025 median wage for network admins is $47.66 [8], and recovering a fifth of the standby band only saves $18.67 to $37.34 [1][3][7].
- **Under $50 — The meter cost:** The lab suggests an audit and then undercuts its own tool, noting plug meters cost less than $50 and their errors grow larger when standby drops below a watt [4].
- **Above 10 watts — The real targets:** A 10-watt load held all year consumes 87.6 kilowatt-hours and costs roughly $15.15 [7], so a dozen of those outweigh every brick in the house.
- **1.3 to 2.7 years — Tool payback:** A $50 meter pays for itself in a few years at the lab's 20 percent reduction rate [3][4], assuming the reader unplugs enough devices to hit that full mark.

My read is that the standard ordering is backwards in almost every energy guide. The devices that are cheap to unplug stopped mattering years ago, and the loads that actually matter are the ones a person forgets are even plugged in.

<!-- nuanced-takeaway -->

## The catch

The total share is a rough estimate rather than a strict survey, and the lab's own verdict is blunter: "Frankly, there are more productive ways to save energy with an investment of an hour." Both the portion of the bill it links to standby and the chunk an aggressive audit can recover rest on narrow research, not on a national metered sample [1][3]. Treat the band as a loose scale rather than a precise reading.

What I find more limiting is the tool you use to measure the draw. A meter that is honest above a watt and fuzzy below it cannot tell a reader whether the thing in the guest room is drawing four watts or none. The difference between those two answers is about six dollars a year.

The audit pays off from the second year if you skip the per-device hunt and check the whole-home baseline, where a retired server shows up as a large step rather than a slow trickle. A house can carry most of its own idle share in just two devices, and both are usually found in minutes. The error is spending an hour to find a fraction of a watt, then calling that hour free — the same division that priced the self-hosting maintenance hour in [Self-Hosting Break-Even: 1.26 Hours a Year](/self-hosting-break-even-one-hour-a-year/), with the audit landing on the wrong side of it.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Your $125 Exam Costs 122 Hours" -> /your-125-exam-costs-122-hours/ [same site (giniloh.com); topical overlap: because, bill] Link "Your $125 Exam Costs 122 Hours" in the section where the article touches because, bill. -->
## Related reading

- [Your $125 Exam Costs 122 Hours](/your-125-exam-costs-122-hours/)
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The shift:** Standby is 5 to 10 percent of home electricity, and adapters are not where it lives.
- **The number:** The band implies 62 to 123 watts; a 20 percent cut returns $19 to $37 against a $47.66 hour.
- **The risk:** The share is an estimate, and meters cannot read below a watt.

## Sources
[1] Lawrence Berkeley National Laboratory — "Standby Power" (standby is 5-10% of residential electricity use): https://standby.lbl.gov/
[2] Lawrence Berkeley National Laboratory — "Frequently Asked Questions About Standby Power" (one watt for a year is 9 kWh, about $1.20 at 13 cents; typical products were 1-3 W two decades ago and are near 0.5 W now): https://standby.lbl.gov/frequently-asked-questions
[3] Lawrence Berkeley National Laboratory — "Frequently Asked Questions About Standby Power", reduction section (an informed and aggressive approach cuts standby about 20%; "there are more productive ways to save energy with an investment of an hour"): https://standby.lbl.gov/frequently-asked-questions
[4] Lawrence Berkeley National Laboratory — "Frequently Asked Questions About Standby Power", measuring section (meters cost less than $50; errors grow relatively larger below about 1 W): https://standby.lbl.gov/frequently-asked-questions
[5] Electronic Code of Federal Regulations — 10 CFR 430.32(w)(1), no-load mode ceiling of 0.5 watts for class A external power supplies up to 250 watts: https://www.ecfr.gov/current/title-10/chapter-II/subchapter-D/part-430/subpart-C/section-430.32
[6] US Energy Information Administration — "How much electricity does an American home use?" (10,791 kWh a year, about 899 kWh a month, 2022): https://www.eia.gov/tools/faqs/faq.php?id=97&t=3
[7] US Energy Information Administration — "Electricity explained: Prices and factors affecting prices" (2025 annual average residential price 17.30 cents per kWh): https://www.eia.gov/energyexplained/electricity/prices-and-factors-affecting-prices.php
[8] O*NET OnLine, US Department of Labor — "15-1244.00 Network and Computer Systems Administrators" (median wage 2025: $47.66 hourly, $99,130 annual): https://www.onetonline.org/link/summary/15-1244.00

## Gate report
PASS — lead (states stakes first, bounds to one figure per opening sentence, strictly avoids jargon)
PASS — tension (features isolated H2, opens with a single direct sentence, maintains short connected sentences)
PASS — tactical-insight (incorporates observer cue, uses bold bullet points with exact metric titles, avoids commands)
PASS — nuanced-takeaway (includes observer cue, concludes on a concrete decision carrying a single internal link)
PASS — tldr (three-line shift / number / risk box under 50 words, separated with an isolated H2 header; the retired four-part recap is not used)
