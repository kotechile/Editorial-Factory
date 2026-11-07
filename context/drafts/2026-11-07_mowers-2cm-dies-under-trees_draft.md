---
title: Mower's 2 cm Dies Under Trees
vertical: yard_robotics
kind: evergreen
archetype: evergreen
evergreen: true
persona: homeowner_pro
one_big_thing: "A wire-free mower's centimetre accuracy is correction data, not hardware — the cloud route is rated 1–6 cm and needs cell coverage across the lawn, a reference station is rated 1–2 cm and needs a mast with a 135-degree sky cone and power, and under closed canopy the fix collapses to metres."
date: 2026-11-07
slug: mowers-2cm-dies-under-trees
meta_title: "Mower's 2 cm Dies Under Trees"
meta_description: "A robot mower's 2 cm claim is correction data, not hardware: the cloud route needs cell coverage, a station needs a 135-degree sky cone, and canopy takes the rest."
---

<!-- lead -->
A wire-free mower's 2 cm accuracy dies under trees. The centimetres are not built into the machine: they arrive as correction data, a steady stream of fixes sent to it while it cuts [3]. That stream comes from a cell service that has to cover the whole lawn, or from a station you bolt to your own property. Husqvarna sells both setups, and the cell route is the weaker one: 1–6 cm against 1–2 cm [2]. The better figure needs a station with a clear 135-degree view of sky and a power outlet beside it. So the choice lands before you order, and it hinges on two things no spec sheet measures: how much sky the grass can see, and whether a phone signal reaches the back fence.

<!-- tldr -->

## At a glance

- **The shift:** Wire-free mowing traded a wire you own for a fix sold as a service.
- **The number:** 2.03 m — survey-grade RTK's error under closed conifer canopy [5].
- **The risk:** Outside coverage, a lot needs a mast, open sky and power.

<!-- tension -->

## Accuracy Is a Correction Service

It helps to know what real-time kinematic (RTK) steering does. The mower counts the waves between a satellite and its antenna, and a second receiver in a known spot does the same sum [5]. The gap between the two counts is the correction, and it shrinks a metre-wide error to a centimetre-wide one. A receiver holding it has what surveyors call a fix. Lose the sum, and the mower drops to a rough position with no promise of a straight line [5].

What I find telling is that the maker publishes a ladder, not a single number, and the ladder has three rungs [4].

| Setup | What goes in | Stated accuracy | What the lot needs |
|---|---|---|---|
| Cloud fixes | nothing at the mower | 1–6 cm | cell coverage across the lawn [3] |
| Long-range station | one station, up to 25 km | 1–2 cm within 10 km | cell coverage and a mast site [4] |
| Short-range station | one per 500 m of radio, repeatable | 1–2 cm | a mast 2 m up, a 135-degree sky cone and power [2] |

The cloud rung looks free: the fix arrives over the mobile network and nothing goes in the ground. Whether it exists at your address is another question. The maker's own coverage list answers it in one line, easy to skim past, and the United States is listed as limited availability by region [2]. Outside that map, only a station steers the mower. Move the station after the map is drawn and the map is wiped, so its spot is a lasting choice [1].

Segway's Navimow sells the same deal from the other side. Its network service costs nothing extra and the cell data is free. The page carries a postcode box, plus a form for buyers in areas not covered yet [9]. A postcode box on a product page admits what the sales copy does not: coverage sets the limit, not hardware.

## By the numbers

- **2.03 m of horizontal error:** What a survey-grade receiver averaged across 84 points under closed conifer canopy [5].
- **1–6 cm against 1–2 cm:** The maker's published accuracy for cloud fixes, against its own station [3].
- **$899.99 for the station:** What a US dealer lists for the unit a lot outside coverage needs [7].

<!-- tactical-insight -->

## What the Sellers Already Concede

What I keep circling is how much of this the sellers print themselves. Kress lists dead reckoning — position guessed from wheel turns and heading when the signal weakens — among the key features of its KR172, worded "for mowing even undershade (weak satellite signal)" [8]. Husqvarna's station rule reads like a site survey: two metres up, a 135-degree cone of open sky, a socket nearby [1]. Navimow offers to email a buyer when its network reaches their area, which is a queue no purchase can jump [9].

None of that is a scandal. Each maker draws the same boundary from its own side. The feature list on the Kress page also frames the whole product as "no perimeter wire installation", which names the older way to keep a mower on the grass: a buried cable that needs no corrections at all [8]. The part I find harder to square is how quietly the failure arrives. A fix wants at least five satellites held steadily, and leaves a signal blunt instead of removing it, so position quality bleeds away with no alarm [6]. Mowers are sorted by this same split on this site's [yard robot pages](/categories/yard-robotics/), where steering type sits beside the acreage figure that gets quoted first.

<!-- nuanced-takeaway -->

## The catch

Where I've landed: this is a real risk on some lots and an overstated one on most. The 2.03 m came from a conifer forest trial that accepted any position the receiver could log, with no signal filter, so it describes what is left once the canopy closes rather than what a lawn with three maples will see [5]. The same explainer that sets the five-satellite rule puts the fix rate near 93% in comparatively favourable forest conditions, which is the fair picture for a lightly treed yard [6].

Continuous canopy over the cutting area is where the promise actually fails, and a north-facing tree line or a back garden with no cell signal puts a lot in the same place. My read is that a buyer's risk sits there, in the corner of the property nobody photographs for the dealer. The two figures that date fastest are the coverage list and the dealer price, both read on 7 November 2026.

## Sources

- [1] Husqvarna, "EPOS: Virtual boundaries" (product page and answers) — https://www.husqvarna.com/us/discover/epos
- [2] Husqvarna, "EPOS wire free installation: Husqvarna Cloud vs reference station" (support article) — https://www.husqvarna.com/uk/support/install-virtual-boundaries-with-husqvarna-epos-two-installation-options-ka-70323
- [3] Husqvarna, "Husqvarna EPOS" (three correction paths) — https://www.husqvarna.com/id/learn-and-discover/husqvarna-epos
- [4] Husqvarna, "Husqvarna EPOS" (long-range and short-range station comparison) — https://www.husqvarna.com/id/learn-and-discover/husqvarna-epos
- [5] Cățeanu et al., "Performance Evaluation of Real-Time Kinematic GNSS with Survey-Grade Receivers and Short Observation Times in Forested Areas" (NIH full text) — https://pmc.ncbi.nlm.nih.gov/articles/PMC11479190
- [6] LRTK (Lefixea), "RTK Surveying Under Trees: How to Handle Canopy and Multipath Errors" — https://www.lefixea.com/article/rtk112
- [7] SmartYard, "Husqvarna EPOS Reference Station" (US dealer listing) — https://smartyardnw.com/product/husqvarna-epos-reference-station-2-4
- [8] Kress, "Kress RTKⁿ ½-acre robotic lawn mower KR172" (key features) — https://www.kress.com/en-us/kress-rtk%E2%81%BF-%C2%BD-acre-robotic-lawn-mower-kr172
- [9] Segway, "Navimow" (network RTK and coverage checker) — https://navimow.segway.com/
