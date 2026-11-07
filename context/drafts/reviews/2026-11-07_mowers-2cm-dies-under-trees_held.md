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
A wire-free mower's 2 cm accuracy dies under tree canopy. The centimetres are not built into the machine: they arrive as real-time kinematic (RTK) correction data, a steady stream of position fixes sent while it cuts [3]. That stream comes either from a cellular service that covers the whole lawn or from a station bolted onto your property. Husqvarna sells both, and it rates the cell route weaker — 1–6 cm against 1–2 cm for its own station [2]. The better figure needs a station with a clear 135-degree view of sky and a power outlet beside it. The choice lands before you order on how much sky the grass can see and whether a phone signal reaches the back fence.

<!-- tldr -->

## At a glance

- **The shift:** Wire-free mowing traded a wire you own for a fix sold as a service.
- **The number:** 2.03 m — survey-grade RTK's error under closed conifer canopy [5].
- **The risk:** Outside coverage, a lot needs a mast, open sky and power.

<!-- tension -->

## Accuracy is a correction service

A mower that steers by RTK correction is subtracting two position readings. It counts radio waves between a satellite and its own antenna; a second receiver at a known spot does the same sum. The gap between the two counts is the correction, and that correction shrinks a metre-wide error to a centimetre-wide one. A receiver that holds this position has what surveyors call a fix. Lose the correction, and the mower falls back to rough positioning with no promise of a straight line [5].

I read the accuracy table twice before I believed which path was the weaker one. The maker publishes three paths, not one number [4].

| Setup | What goes in | Stated accuracy | What the lot needs |
|---|---|---|---|
| Cloud fixes | nothing at the mower | 1–6 cm | cell coverage across the lawn [3] |
| Long-range station | one station, up to 25 km | 1–2 cm within 10 km | cell coverage and a mast site [4] |
| Short-range station | one per 500 m of radio, repeatable | 1–2 cm | a mast 2 m up, a 135-degree sky cone and power [2] |

The cloud route looks free: the fix arrives over the mobile network and nothing goes into the ground. Whether that service exists at your address is another question. The maker's own coverage note lists the United States as limited availability by region [2]. Outside that map, only a station steers the mower. If you move the station after the map is drawn, the map is wiped, so its spot is a lasting choice [1].

Segway's Navimow, a wire-free mower, sells the same arrangement from the other side. Its network service costs nothing extra and the cell data is free. The page carries a postcode box plus a form for buyers not covered yet [9]. A postcode box on a product page concedes what the sales copy does not: coverage sets the limit, not hardware.

<!-- by-the-numbers -->

## By the numbers

- **84 points:** The sample behind the 2.03 m horizontal error under closed conifer canopy [5].
- **93%:** The fix rate in comparatively favourable forest conditions, the fair picture for a lightly treed yard [6].
- **$899.99 for the station:** What a US dealer lists for the unit a lot outside coverage needs [7].

<!-- tactical-insight -->

## What the sellers already concede

I keep noticing that the sellers concede the failure in their own feature lists. Kress lists dead reckoning among the key features of its KR172 robotic mower [8]. The term means position guessed from wheel turns and heading when the satellite signal weakens. The page words it "for mowing even undershade (weak satellite signal)". Husqvarna's station rule reads like a site survey: two metres up, a 135-degree cone of open sky, a power outlet nearby [1]. Navimow offers to email a buyer when its network reaches their area, which is a queue no purchase can jump [9].

None of that is a scandal. Each maker draws the same boundary from its own side, and the failure arrives quietly. A fix wants at least five satellites held steadily. Leafy cover blunts the signal instead of removing it, so the position estimate worsens with no alarm [6]. On this site's [yard robot pages](/categories/yard-robotics/), steering type sits beside the acreage figure that gets quoted first.

<!-- nuanced-takeaway -->

## The catch

I would put the risk this way: real on some lots, overstated on most. The 2.03 m result came from a conifer forest trial that accepted any position the receiver could log, without a signal filter [5]. It describes the leftovers once canopy closes, rather than a lawn with three maples. The same explainer that sets the five-satellite threshold describes the favourable forest condition as the fair picture for a lightly treed yard [6].

Continuous canopy over the cutting area is where the promise fails. A north-facing tree line or a back garden with no cell signal puts a lot in the same place. The buyer's risk sits in the corner of the property nobody photographs for the dealer. The coverage list and the dealer price are the two figures that date fastest, both were read on 7 November 2026.

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
