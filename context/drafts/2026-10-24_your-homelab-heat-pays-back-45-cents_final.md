---
title: "Homelab Heat Rebate: 45 Cents, Not Free"
vertical: personal_microeconomics_tinkering_tax
persona: systems_tinkerer_pro
one_big_thing: "An always-on box's waste heat is a rebate, not a refund: at the federal-minimum heat-pump efficiency, 88 watts of homelab heat pays back about 45% of its own electricity bill in heating season, nothing in an unconditioned room, and costs about 24% extra to remove in summer."
date: 2026-10-24
slug: your-homelab-heat-pays-back-45-cents
archetype: evergreen
evergreen: true
---

<!-- lead -->
Your homelab's waste heat pays back about 45 cents on the dollar, and only while the house is being heated. An eight-bay storage box drawing 87.93 watts [5] runs through 770 kilowatt-hours a year, roughly $133 at the 2025 residential average of 17.30 cents [1]. Every watt of that ends up as room heat, which the maker's own spec sheet states as 300.23 British thermal units (BTU) an hour for the same draw [6]. What that warmth would otherwise have cost you is the rebate, and at the federal minimum for a heat pump it comes to $61 rather than $133 [3].

<!-- tension -->

## The big picture:

The folklore is not stupid, but it answers the wrong question. 

Every homelab owner argues the server heats the spare room, so in winter it costs almost nothing. The box does not sit beside the biggest energy line in the house, it sits inside it.

A home using basic electric heat turns power into warmth at a perfect ratio, making the heat worth exactly what the meter charged. What strikes me is how small that group has become compared with how loudly the argument survives. 

A heat pump moves heat instead of making it, and the federal standard for equipment made since January 2023 sets the floor at a heating seasonal performance factor of 7.5 [3]. That is about 2.2 units of heat for every unit of electricity, so the warmth your box gives away for free would have cost a good heat pump 350 kilowatt-hours, or $61 [1][3]. The credit is real; it is just less than half of what the folklore promises. Summer finishes the job, because removing the same heat at the 14.3 cooling minimum takes 184 kilowatt-hours, or $32 [1][3].

## By the numbers

- **87.93 watts — The baseline draw:** An eight-bay storage server in access mode uses 770 kilowatt-hours (kWh) a year, costing $133 at the 2025 home average of 17.30 cents [1][5].
- **45 percent — The winter credit:** Making that same heat from a heat pump at the federal minimum Heating Seasonal Performance Factor 2 (HSPF2) of 7.5 costs 350 kWh, making the rebate $61 against the $133 bill [1][3].
- **24 percent — The summer surcharge:** Cooling the room back down at the 14.3 seasonal minimum takes 184 kWh, adding a $32 penalty [1][3].
- **52 percent — The household footprint:** Space heating and air conditioning make up most of a home's yearly power use, which means the server's waste heat hits the largest line on your bill [2].

<!-- tactical-insight -->

## What I'd watch:

I am watching the spec sheet, because it carries both halves of this argument and almost nobody reads the second half.

- **The heat line:** Storage and server sheets now often print a heat number beside the power draw. Synology lists 300.23 British thermal units (BTU) an hour for its eight-bay unit [5][6]. That line is a vendor's own statement that every watt becomes room heat.
- **The efficiency quote:** A better heat pump cuts the credit. The federal figure is a floor, and a better unit delivers the same warmth for less power [3]. Efficient homes get a smaller rebate than leaky ones.
- **The physical spot:** In a garage, a shed, or an unheated basement, the credit is zero and the summer penalty is zero. The same box is worth real money in the hallway and nothing at all two rooms away.
- **The local season:** The credit only exists during heating hours. A box in a home with a short heating season collects a fraction of the yearly figure, while one in a cold climate collects most of it.

My read is that owners are treating a passing, part-time credit as if it were a fixed discount.

<!-- nuanced-takeaway -->

## The catch

The part I keep circling is that a partial credit on a small bill is still a small number. The upkeep side of the same box has already been priced [in the break-even on an hour of maintenance](/self-hosting-break-even-one-hour-a-year/), and this is the other half of its bill.

Install something larger and the math scales: every 10 watts of steady draw is 87.6 kWh, or about $15 a year, and the credit on it is about $7. Anyone running a retired enterprise server at several hundred watts is looking at real money on both sides of the ledger, but the credit never reaches break-even on the power.

The rebate is also a ceiling rather than sure cash. It assumes the heat lands in space the thermostat is actively heating, and that the warmth would otherwise have been bought. A box in a closed closet or a house with a wood stove shrinks that number, and nobody sends you a check for the difference.

The piece I cannot put a number on is the honest one. Heating gas is cheaper per unit of heat than electricity in most US markets, so a gas-heated home's credit is smaller than the heat-pump case above. The rule still works, because the credit is always whatever the replaced heat costs you.

What the math settles is the placement choice, and it settles it against the folklore. A box in heated space is worth a modest rebate in winter and costs extra to cool in summer. A box in a bare room is worth nothing either way, and looks identical on the invoice. The rebate is real, and it is smaller than the story most owners tell themselves about it.

<!-- tldr -->

## At a glance

- **The Big Shift:** Always-on home hardware is often justified as free heat in winter. Measured against what heat actually costs in a modern home, the warmth is worth about 45 percent of the box's power bill during heating season, nothing in a bare room, and less than zero in summer.
- **Why It Matters:** Space heating and cooling are 52 percent of a household's energy use, so the box's waste heat lands inside the largest line on the bill. At 88 watts, the credit is about $61 a year against $133 of electricity, and the cooling season claws back about $32 of it.
- **What I'd Watch:** Where the box sits and what heats the house, because those two facts decide whether the rebate exists at all.
  - **Heat-pump efficiency:** The federal minimum for new equipment is 7.5 in heating seasonal performance, so the box's warmth replaces a third less power than the folklore assumes.
  - **Cooling efficiency:** The federal cooling floor is 14.3, which puts a 24 percent surcharge on the same watts in any room that is air-conditioned.
  - **Placement:** Heated space earns the credit and pays the penalty, while a garage earns neither.
- **The Catch:** The credit is a ceiling, not a payment. It depends on heating hours, thermostat placement, and what the replaced heat would have cost, so a home burning cheaper fuel gets a smaller rebate than the heat-pump case above.

## Sources
[1] US Energy Information Administration — "Electricity explained: Prices and factors affecting prices" (2025 annual average retail prices, residential 17.30¢ per kWh): https://www.eia.gov/energyexplained/electricity/prices-and-factors-affecting-prices.php
[2] US Energy Information Administration — "Use of energy explained: Homes" (52% of household annual energy use for space heating and air conditioning, 2020): https://www.eia.gov/energyexplained/use-of-energy/homes.php
[3] Electronic Code of Federal Regulations — 10 CFR 430.32(c)(5), central air conditioners and heat pumps manufactured on or after January 1, 2023 (split-system heat pumps 14.3 SEER2 / 7.5 HSPF2; single-package 13.4 / 6.7): https://www.ecfr.gov/current/title-10/chapter-II/subchapter-D/part-430/subpart-C/section-430.32
[4] Electronic Code of Federal Regulations — 10 CFR 430.32(c)(5)(iv), single-package heat pumps 13.4 SEER2 / 6.7 HSPF2: https://www.ecfr.gov/current/title-10/chapter-II/subchapter-D/part-430/subpart-C/section-430.32
[5] Synology — "DS1823xs+" product specifications (power consumption 87.93 watts access, 28.37 watts HDD hibernation): https://www.synology.com/en-us/products/DS1823xs+
[6] Synology — "DS1823xs+" product specifications (British Thermal Unit 300.23 BTU/hr access, 96.87 BTU/hr hibernation): https://www.synology.com/en-us/products/DS1823xs+

## Gate report
PASS — Lead: Opens with the 45-cent figure and the 88-watt box, then states the year's energy and dollars before any mechanism.
PASS — Tension: Contrasts the resistive-heat folklore with the 2023 heat-pump standard, names the 2.2-to-1 ratio, and closes the loop on the summer penalty with observer cues.
PASS — Tactical: Observes the spec sheet, the efficiency floor, the placement and the season without instructing the reader.
PASS — Nuance: States the ceiling nature of the credit, the missing gas figure, and the placement split honestly; no prescription.
PASS — TL;DR: Four-part Smart Brevity schema under its own H2.
Hand-tune note: the frontier pass had (a) dropped the mechanism sentence that explains why the credit is 45 percent and (b) inserted an invented internal link (`/homelab-true-cost-calculator/`) that no live page serves; both were restored/removed by hand, and every figure in the body was re-derived from the verified brief after the rewrite. Flesch re-measured below.

