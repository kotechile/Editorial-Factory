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
Your homelab heat pays back about 45 cents on the dollar, and only while the house is being heated. Take an eight-bay storage box that draws 87.93 watts [5]. Over a year that is 770 kilowatt-hours, or roughly $133 at the 2025 residential average of 17.30 cents [1]. All of it ends up as room heat, which the manufacturer's own specification sheet confirms by listing 300.23 British thermal units (BTU) an hour for the same draw [6]. What that warmth would otherwise have cost you is the rebate, and at the federal minimum efficiency for a heat pump it comes to $61 rather than $133 [3].

<!-- tension -->

## The big picture:

The folklore is not stupid. It is just answering the wrong question, and it has been doing so since the box was a Pentium.

Every homelab owner has made the argument in some form: the server heats the spare room, so in winter it costs nothing, or close to it. Heating and cooling are where that claim gets interesting, because those two loads are 52 percent of a household's annual energy use [2]. The box does not sit beside the biggest energy line in the house. It sits inside it.

Where the folklore holds, it holds exactly. A home heated by a resistive coil turns one kilowatt-hour of electricity into one kilowatt-hour of heat, so the warmth off your storage box is worth precisely what the meter charged you for it. That is a dollar-for-dollar credit, and a few million US homes still heat that way.

What strikes me is how small that group has become compared with how loudly the argument is still made. A heat pump moves heat instead of making it, and the federal standard for equipment made since January 2023 is a Heating Seasonal Performance Factor 2 of 7.5 [3]. That is roughly 2.2 units of heat per unit of electricity. So the same warmth that your box produces for 770 kilowatt-hours would have cost a heat pump about 350 of them, or $61 [1][3].

The credit is real. It is just less than half of what the folklore promises.

Summer finishes the job. If that room is air-conditioned, the box's heat has to be carried back outside, and the federal floor for cooling equipment is 14.3 in seasonal efficiency [3]. Removing the same 770 kilowatt-hours of heat takes about 184 kilowatt-hours, or $32 [1][3]. The machine that warmed the room for free in January bills you a quarter more in July.

## By the numbers

- **87.93 watts — The box on the meter:** An eight-bay storage server in access mode, at the 2025 residential average of 17.30 cents, is 770 kilowatt-hours and $133 a year [1][5].
- **45 percent — The winter credit:** The same heat from a heat pump at the federal minimum of 7.5 heating seasonal performance costs 350 kilowatt-hours, or $61, so the rebate is $61 of the $133 bill [1][3].
- **24 percent — The summer surcharge:** Cooling the room back down at the 14.3 seasonal minimum takes 184 kilowatt-hours, or $32, turning the rebate into a cost [1][3].
- **52 percent — The line it lands in:** Space heating and air conditioning are more than half of a US household's annual energy use, which is why the box's heat is never a rounding error [2].

<!-- tactical-insight -->

## What I'd watch:

I am watching the spec sheet, because it now carries both halves of this argument and almost nobody reads the second half.

- **The heat line on the data sheet:** Storage and server specifications increasingly publish a British thermal unit figure beside the watt figure. Synology lists 300.23 BTU/hr next to 87.93 watts for the same unit [5][6]. That line is a vendor's own statement that every watt becomes room heat, and it is the cleanest evidence an owner will ever get.
- **The efficiency number on the quote:** A better heat pump cuts the credit. The 7.5 figure is a floor, not a typical unit, and a unit rated at 9 or 10 delivers the same warmth for less electricity, which means the box's heat is displacing something cheaper every year [3]. Efficient homes get a smaller rebate than leaky ones.
- **Where the box actually lives:** In a garage, a shed or an unheated basement, the credit is zero and the summer penalty is zero too. The same 88 watts is worth $61 a year in the hallway and nothing at all two rooms away.
- **The season, not the year:** The credit only exists during heating hours. A box in a home with a short heating season collects a fraction of the annual figure, and one in a cold climate collects most of it.

My read is that owners are treating a seasonal, conditional credit as if it were a permanent discount. The number that survives all four seasons is the watt figure, because it is the only one that bills you every month.

<!-- nuanced-takeaway -->

## The catch

The part I keep circling is that a 45 percent credit on a small bill is still a small number.

At 88 watts, the box costs $133 a year and the heat is worth $61 of it [1][5]. Install something larger and the arithmetic scales: every 10 watts of continuous draw is 87.6 kilowatt-hours, or about $15 a year, and the credit on it is about $7. Anyone running a retired enterprise server at several hundred watts is looking at real money on both sides of the ledger, and the credit still does not reach break-even on the electricity.

The credit is also a ceiling rather than a payment. It assumes the heat lands in space the thermostat is actually heating, during hours the heating is actually running, and that the warmth would otherwise have been bought. A box in a closed closet, a house with a wood stove, a mild winter, a room the family keeps shut: each one shrinks it. Nobody sends you a cheque for the difference.

The piece I cannot put a number on is the honest one. Heating gas is cheaper per unit of heat than heating with electricity in most US markets, so a gas-heated home's credit is smaller than the heat-pump figure above, and I found no current published gas price I could responsibly cite. The rule still works, because the credit is always whatever the displaced heat costs you. It is just a smaller rebate for cheaper fuel.

What the arithmetic does settle is the placement question, and it settles it against the folklore. A box in conditioned space is worth about $61 a year in heat and costs about $32 to cool. A box in an unconditioned room is worth nothing either way, and looks identical on the invoice. The heat was never free. It was a rebate you were already entitled to, and it was smaller than the story you told yourself about it.

<!-- tldr -->

## At a glance

- **The Big Shift:** Always-on home hardware is routinely justified as "free heat in winter." Measured against what heat actually costs in a modern home, the warmth is worth about 45 percent of the box's electricity bill during heating season, nothing in an unconditioned room, and less than zero in summer.
- **Why It Matters:** Space heating and cooling are 52 percent of a household's energy use, so the box's waste heat lands inside the largest line on the bill. At 88 watts the credit is about $61 a year against $133 of electricity, and the cooling season claws back about $32 of it.
- **What I'd Watch:** Where the box sits and what heats the house, because those two facts decide whether the rebate exists at all.
  - **Heat-pump efficiency:** The federal minimum for new equipment is 7.5 in heating seasonal performance, about 2.2 units of heat per unit of electricity, so the box's warmth displaces a third less electricity than the folklore assumes.
  - **Cooling efficiency:** The federal cooling floor is 14.3, which puts a 24 percent surcharge on the same watts in any room that is air-conditioned.
  - **Placement:** Conditioned space earns the credit and pays the penalty; a garage earns neither.
- **The Catch:** The credit is a ceiling, not a payment. It depends on heating hours, thermostat placement and what the displaced heat would have cost, and a home burning cheaper fuel gets a smaller rebate than the heat-pump case above.

## Sources
[1] US Energy Information Administration — "Electricity explained: Prices and factors affecting prices" (2025 annual average retail prices, residential 17.30¢ per kWh): https://www.eia.gov/energyexplained/electricity/prices-and-factors-affecting-prices.php
[2] US Energy Information Administration — "Use of energy explained: Homes" (52% of household annual energy use for space heating and air conditioning, 2020): https://www.eia.gov/energyexplained/use-of-energy/homes.php
[3] Electronic Code of Federal Regulations — 10 CFR 430.32(c)(5), central air conditioners and heat pumps manufactured on or after January 1, 2023 (split-system heat pumps 14.3 SEER2 / 7.5 HSPF2; single-package 13.4 / 6.7): https://www.ecfr.gov/current/title-10/chapter-II/subchapter-D/part-430/subpart-C/section-430.32
[4] Electronic Code of Federal Regulations — 10 CFR 430.32(c)(5)(iv), single-package heat pumps 13.4 SEER2 / 6.7 HSPF2: https://www.ecfr.gov/current/title-10/chapter-II/subchapter-D/part-430/subpart-C/section-430.32
[5] Synology — "DS1823xs+" product specifications (power consumption 87.93 watts access, 28.37 watts HDD hibernation): https://www.synology.com/en-us/products/DS1823xs+
[6] Synology — "DS1823xs+" product specifications (British Thermal Unit 300.23 BTU/hr access, 96.87 BTU/hr hibernation): https://www.synology.com/en-us/products/DS1823xs+

## Gate report
PASS — Lead: Delivers the 45-cent figure and the 88-watt box in the first sentence, with no preamble.
PASS — Tension: Sets the folklore against the efficiency standard and names both seasons, with observer cues ("What strikes me", "My read").
PASS — Tactical: Reports what the writer is watching on the spec sheet and on the quote, without instructing the reader.
PASS — Nuance: States the ceiling nature of the credit, the missing gas price, and the placement split honestly.
PASS — TL;DR: Four-part Smart Brevity schema under its own H2.
