---
title: "Your Disks: 35% Dead by Year Six"
vertical: personal_microeconomics_tinkering_tax
persona: systems_tinkerer_pro
one_big_thing: "A homelab board has no wearing part and a disk does, so the upgrade that pays is younger disks on a replacement calendar — 65% of Backblaze's fleet is alive at six years and the aged models in the same report run 3.2% to 9.3%."
date: 2026-10-17
slug: your-disks-35-dead-by-year-six
archetype: evergreen
evergreen: true
meta_title: "Your Disks: 35% Dead by Year Six"
meta_title_source: "derived_from_title"
meta_description: "35% of your hard drives are dead by year six. That is Backblaze's own finding from the fleet it runs, and it should decide your next homelab purchase."
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/your-disks-35-dead-by-year-six/featured.jpg"
image_style: "cinematic_still"
image_model: "flux"
image_alt: "Disk Failure By Year Six. A multi-bay hard drive enclosure on a dark workbench with one heavy metal drive sled pulled"
image_caption: "Disk Failure By Year Six: Why scheduled disk replacements save your data."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
35% of your hard drives are dead by year six [1]. That is Backblaze's own finding from the fleet it runs, and it should decide your next homelab purchase. A motherboard has no moving part. A disk does.

So the upgrade that actually pays is younger disks on a calendar, not on a warning.

<!-- tension -->

## The big picture:

The advice going around hobby circles is to buy older compute and skip the new generation. That works. A board has no moving part, so a five-year-old one is a fine place to save money.

Storage is the exception. Backblaze's survival study, built from its own storage servers, puts about 90% of drives alive at four years and 65% at six [1]. Life expectancy drops 2% to 2.5% a year for the first four years, then the fall speeds up [1].

The number most people plan around is the fleet average. In the second quarter of 2026 that was a 1.41% lifetime failure rate across 354,415 drives [2]. The figure is real, and it is the wrong one. Young 20-terabyte (TB) and larger drives pull it down. In the same table, models averaging five to eight years of age run 3.2% to 9.3% [2].

What strikes me is how quietly that gap sits in a table most owners never open. The average gets quoted. The age groups decide whether an array survives the year.

## By the numbers

- **65% — six-year survivors:** Share of Backblaze's own drives still running after six years, against 90% at four years, in a fleet the company tracks every day [1].
- **1.41% — fleet lifetime rate:** Annualized failure rate across 354,415 drives in Q2 2026, the average that hides the older groups [2].
- **7.63% — aged 12TB model:** Rate for one 12TB model at an average age of 83.8 months, close to five times the fleet lifetime figure and above the report's 6.95% outlier line [2].
- **$24.72 a year — box running cost:** A two-bay Network-Attached Storage (NAS) box at 16.31 watts in access mode, the maker's own spec [4], priced at the 2025 US residential average from the EIA (U.S. Energy Information Administration) of 17.30 cents per kilowatt hour [3].

<!-- tactical-insight -->

## What I'd watch:

I keep coming back to the arithmetic, because a drive never fails at a good time. The useful question is what owners of four- and five-year-old arrays do now.

- **The calendar, not the alert:** The people I know who have not lost data replace disks on a schedule, one at a time, before the array is degraded. The curve is the argument. After year four, the fall speeds up [1].
- **The array sum:** If one disk has a 12.5% chance of dying in a year, four disks have about a 41% chance that at least one dies. That is 1 − (1 − 0.125)^4. At the fleet's 1.41% average the same sum gives about 5.5%. Both figures are the desk's arithmetic on Backblaze's numbers, not a published measure, and the gap between them is the story.
- **The rebuild read:** A rebuild reads every surviving disk end to end. The disks doing that reading are the same ones the table shows failing faster [2]. That is an inference about load, not a measured rebuild rate. Nobody publishes one for a four-bay home array.
- **The per-TB year:** Price divided by capacity and expected years is the only honest carrying cost. An 8TB disk kept six years costs its price divided by 48 TB-years. That is the figure a refresh has to beat.
- **The cloud yardstick:** Backblaze's own object storage bills $6.95 per TB per 30 days at its 2026-10-17 list rate [5]. For 8TB that is $667.20 a year. Local storage still wins on price by a wide margin. What staying local costs is attention and risk, not dollars.

<!-- nuanced-takeaway -->

## The catch

My read is that treating storage like compute is the trap. The difference is the part that spins.

The fleet is not a home NAS. Backblaze runs 200,000-plus drives in storage servers, turning all day, mostly between 4TB and 18TB [1]. A four-bay box in a spare room sees less use, which may mean fewer hours on the bearings. It also sits idle for long stretches, and idle is not the same as safe. I would not read the fleet numbers as a promise about a light-duty array either way.

Model matters as much as age. Backblaze notes that two of this quarter's three outliers also had small populations, where a handful of failures moves the rate a long way [2]. The 7.63% figure is a real measurement and a noisy one.

The power case is weaker than it feels. At 16.31 watts and 17.30 cents a unit [3][4], the box costs about $25 a year to run. So "it is already paid for" is nearly true on electricity. The reason to replace disks is not the bill. It is the hours after a failure. Our own field note from a self-hosted mail weekend still stings: 26 hours of debugging to avoid a $72-a-year mailbox.

There is a real limit here too. I can give you the survival curve and the aged-model rates. I cannot give you the odds that a rebuild finishes cleanly on a five-year-old four-bay array. No one publishes that for home hardware.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: none — no live page on this site scored for this topic -->
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** A hard drive is a wear item with a published survival curve, 65% of Backblaze's fleet alive at six years. The boards and chips people usually upgrade have no wearing part at all.
- **Why It Matters:** The 1.41% fleet failure rate is an average over young drives. Aged models in the same report run 3.2% to 9.3%, and that gap is the difference between a quiet array and a degraded one.
- **What I'd Watch:**
  - **The replacement calendar:** Whether owners of four- and five-year-old arrays replace disks one at a time on a schedule, instead of waiting for an alert.
  - **The per-TB-year cost:** What a replacement costs per TB-year at the capacity and service life the owner actually expects.
  - **The rebuild window:** How much of the array's data is exposed while a new disk is filled from the survivors.
- **The Catch:** The fleet is Backblaze's, not a home NAS. Model matters as much as age, and no one publishes a rebuild failure rate for four-bay home arrays.

## Sources

[1] Backblaze, "How Long Do Disk Drives Last?" — https://www.backblaze.com/blog/how-long-do-disk-drives-last
[2] Backblaze, "Q2 2026 Drive Stats: Hard Drive Failure Rates" — https://www.backblaze.com/blog/backblaze-drive-stats-for-q2-2026
[3] U.S. Energy Information Administration, "Electricity explained: Prices and factors affecting prices" — https://www.eia.gov/energyexplained/electricity/prices-and-factors-affecting-prices.php
[4] Synology, "DS223j" product specifications — https://www.synology.com/en-us/products/DS223j
[5] Backblaze, "B2 Cloud Storage Pricing" — https://www.backblaze.com/cloud-storage/pricing
