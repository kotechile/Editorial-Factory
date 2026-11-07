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
image_path: "context/assets/illustrations/mowers-2cm-dies-under-trees/featured.jpg"
image_style: "cinematic_still"
image_model: "flux"
image_alt: "Mower'S 2 Cm Dies Under Trees. Wire-free robotic mower on a residential driveway under conifer canopy and open sky, split-screen contrast"
image_caption: "Mower'S 2 Cm Dies Under Trees: The 2 cm claim is correction data, not hardware — under trees it falls to metres."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
A wire-free mower's 2 cm accuracy dies under trees, because the centimetres are not built into the machine. They arrive as real-time kinematic (RTK) correction data, a steady stream of position fixes sent while it cuts [3]. That stream comes either from a cell service that covers the whole lawn or from a station bolted onto your property. Husqvarna sells both, and it rates the cell route weaker: 1–6 cm against 1–2 cm for its own station [3]. The better figure needs a station with a clear 135-degree view of sky and a power outlet beside it [1]. So the choice lands before you order, on how much sky the grass can see and whether a phone signal reaches the back fence.

<!-- tldr -->

## At a glance

- **The shift:** Wire-free mowing traded a wire you own for a fix sold as a service.
- **The number:** 2.03 m — survey-grade RTK's error under closed conifer canopy [5].
- **The risk:** Outside coverage, a lot needs a mast, open sky and power.

<!-- tension -->

## Accuracy is a correction service

A mower that steers by RTK correction is subtracting two readings. It counts radio waves between a satellite and its own antenna, while a second unit in a known spot does the same sum [5]. The gap between the two counts is the correction, and it turns a metre-wide error into a centimetre-wide one. A receiver holding that has what surveyors call a fix. Lose it, and the mower falls back to a rough guess with no promise of a straight line [5].

I read the accuracy table twice before I believed which path was the weaker one. The maker publishes three paths, not one number [4].

| Setup | What goes in | Stated accuracy | What the lot needs |
|---|---|---|---|
| Cloud fixes | nothing at the mower | 1–6 cm | cell coverage across the lawn [3] |
| Long-range station | one station, up to 25 km | 1–2 cm within 10 km | cell coverage and a mast site [4] |
| Short-range station | one per 500 m of radio, repeatable | 1–2 cm | a mast 2 m up, a 135-degree sky cone and power [2] |

The cloud route looks free, because the fix arrives over the mobile network and nothing goes in the ground. Whether that service exists at your address is another question. The maker's own coverage note lists the United States as limited availability by region [2]. Outside that map, only a station steers the mower. Move the station after the map is drawn and the map is wiped, so its spot is a lasting choice [1].

Segway's Navimow sells the same setup from the other side. Its network service costs nothing extra, the cell data is free, and the page carries a postcode box plus a form for buyers not covered yet [9]. A postcode box on a product page admits what the sales copy does not: coverage sets the limit, not hardware.

## By the numbers

- **2.03 m of error:** The mean a survey-grade receiver logged at 84 points under closed conifer canopy [5].
- **93%:** The fix rate in fairly good forest, the honest picture for a lightly treed yard [6].
- **$899.99 for the station:** What a US dealer lists for the unit a lot outside coverage needs [7].

<!-- tactical-insight -->

## What the sellers already concede

I keep noticing that the sellers admit the failure in their own feature lists. Kress lists dead reckoning — position guessed from wheel turns and heading when the signal weakens — in the key features of its KR172 mower, and words it "for mowing even undershade (weak satellite signal)" [8]. Husqvarna's station rule reads like a site survey: two metres up, a 135-degree cone of open sky, a power outlet nearby [1]. Navimow offers to email a buyer when its network reaches their area, a queue no purchase can jump [9].

None of that is a scandal: each maker draws the same boundary from its own side. What strikes me is how quietly the failure arrives. A fix wants at least five satellites held steadily, and leafy cover blunts the signal instead of removing it, so the position worsens with no alarm at all [6]. On this site's [yard robot pages](/categories/yard-robotics/), steering type sits beside the acreage figure that gets quoted first.

<!-- nuanced-takeaway -->

## The catch

Where I've landed is that the risk is real on some lots and overstated on most. The 2.03 m came from a conifer forest trial that accepted any position the receiver could log, with no signal filter [5]. It describes what is left once canopy closes, not a lawn with three maples. The same explainer that sets the five-satellite rule treats good forest as the fair test for a lightly treed yard [6].

Continuous canopy over the cutting area is where the promise fails. A north-facing tree line or a back garden with no cell signal puts a lot in the same place. The buyer's risk sits in the corner of the property nobody shows the dealer. Most yards will never meet that test, which is the part the sales copy gets right. The coverage list and the dealer price are the two figures that age fastest; both were read on 7 November 2026.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Your Mower's 2.4-Year Payback Trap" -> /your-mower-pays-back-in-24-years-or-09/ [same site (wellroost.com); topical overlap: machine, mower's] Link "Your Mower's 2.4-Year Payback Trap" in the section where the article touches machine, mower's. -->
## Related reading

- [Your Mower's 2.4-Year Payback Trap](/your-mower-pays-back-in-24-years-or-09/) — more on Yard Robots & Automation
<!-- internal-links:end -->

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
