---
title: "Your Last-Mile Carbon Number Is a Rate Table, Not a Measurement"
vertical: last_mile_routing_fleet_carbon
persona: supply_chain_architect
one_big_thing: "A last-mile carbon number is activity times a published factor — 10,180 grams of CO2 per gallon of diesel, 0.81 pounds per kilowatt-hour of grid power — so a carrier's reported cut is only comparable once the factor version, the year and the boundary are pinned."
date: 2026-10-09
slug: last-mile-carbon-number-is-a-rate-table
archetype: evergreen
evergreen: true
meta_title: "Your Last-Mile Carbon Number Is a Rate Table"
meta_description: "A last-mile carbon claim is activity times a published factor, and two federal agencies publish two different grid factors for the same kilowatt-hour."
---

<!-- lead -->
A diesel van's carbon number comes from a rule, not from a route. Every gallon of diesel burned counts as 10,180 grams of carbon dioxide (CO2) [1]. The electric number is two published rates multiplied: 0.81 pounds of CO2 per kilowatt-hour of U.S. grid power [3], times the 25 to 40 kilowatt-hours a light-duty electric van uses per 100 miles [5]. Route software moves the activity. The published rates decide the total.

<!-- tension -->

## The big picture:

I keep coming back to how much of a "carbon cut" is a choice of rates, not a change on the road.

A last-mile emissions figure is activity times a published factor. The activity is yours: gallons, kilowatt-hours, miles, stops. The factor belongs to someone else. The U.S. Environmental Protection Agency (EPA) lists 10,180 grams of CO2 per gallon of diesel, a figure it agreed to in a 2010 rule with the Department of Transportation [1][2]. That rule assumes all the carbon in the diesel burns [2]. The Energy Information Administration (EIA) lists 0.81 pounds of CO2 per kilowatt-hour of U.S. power [3]. EPA's own calculator uses 823.1 pounds of CO2 equivalent per megawatt-hour instead [2].

Same kilowatt-hour, two federal numbers, two different boundaries. That decides whether two carriers can sit in one column.

The dollar side is a rate table too. In 2025 the average U.S. retail price of power was 13.63 cents per kilowatt-hour [4]. Commercial customers paid 13.41 cents, and industrial customers 8.62 cents [4]. A depot's class and zip code price the same electrons differently.

<!-- By the numbers -->

## By the numbers

- **10,180 grams — Diesel's fixed factor:** A gallon of diesel counts as 10,180 grams of CO2, and a gallon of gasoline as 8,887 [1]. The figure comes from a 2010 federal rule and has not moved since [2].
- **0.81 pounds — Grid factor per kWh:** EIA's U.S. average for 2023, drawn from 1.53 billion metric tons of CO2 over 4.18 trillion kilowatt-hours [3]. EPA's calculator instead uses 823.1 pounds of CO2 equivalent per megawatt-hour, a newer figure and a wider basket of gases [2].
- **25-40 kWh — Electric energy per 100 miles:** The range the Department of Energy gives for light-duty electric vans [5]. That range turns a grid factor into a per-mile number.
- **13.41 vs 8.62 cents — The tariff class:** The 2025 average U.S. commercial and industrial prices per kilowatt-hour [4]. They sit about 56% apart for the same power, and state averages ran from 8.20 cents in North Dakota to 35.72 cents in Hawaii [4].

<!-- tactical-insight -->

## What I'd watch:

I've been pulling these factor pages apart this week. The detail I'd want next to every quoted number is its basis.

- **The factor behind a quoted cut:** A carrier's "12% better" can be checked only if it names the factor and the year. The grid factor is updated each year. The diesel factor has not moved since 2010 [1][2][3].
- **The boundary a number claims:** EPA and the Department of Energy name three: tailpipe, well-to-wheel and cradle-to-grave [6]. An electric van has no tailpipe, but its power does come from somewhere. The three are not the same [6].
- **The depot's tariff class:** The published class averages differ by about 56% per kilowatt-hour, and the state spread is wider [4]. The same charging load lands on a different cost line by address and by meter class [4].
- **The scale being divided:** The U.S. moves over 51 million tons of freight a day, about 57 tons per person [7]. E-commerce sales grew 20-fold between 2000 and 2019 [7]. A small factor gap per parcel gets large on a network.

<!-- nuanced-takeaway -->

## The catch

My read: the math cuts both ways, and none of it argues against electric vans.

A coal-heavy grid can erase much of the electric edge, because the 0.81 figure is a national average that hides region [3]. The diesel factor assumes all the fuel burns, so it leaves out the work of getting fuel to the pump [2]. And the electric number still rides on the driver: 25 and 40 kilowatt-hours per 100 miles are the same van in a good week and a bad one [5].

I could be wrong about how much this changes a given deal. But two federal pages do give two numbers for the same kilowatt-hour [2][3]. Two honest reports can still disagree. The only way to tell is to print the basis next to the number.

<!-- internal-links -->

<!-- tldr -->

## At a glance

- **The Big Shift:** A last-mile carbon number is activity times a published factor, not a measure of a route. Diesel counts at 10,180 grams of CO2 per gallon and grid power at 0.81 pounds per kilowatt-hour, and the two share neither vintage nor boundary.
- **Why It Matters:** If a carrier's cut is a factor swap, the figures in a Scope 3 report are not the same thing. A number nobody can check is a number nobody can audit.
- **What I'd Watch:** Whether the next round of carrier scorecards prints the basis next to each number.
  - **Factor version:** Which value a fleet used — EIA's 0.81 pounds of CO2 per kilowatt-hour, or EPA's 823.1 pounds of CO2 equivalent per megawatt-hour. The two give different totals for the same power.
  - **Boundary:** Whether a number covers the tailpipe only, the fuel cycle behind it, or the whole life of the vehicle. The three answer different questions.
  - **Tariff class:** Whether the depot load is billed on the commercial or the industrial schedule. That gap was about 56% per kilowatt-hour in the 2025 averages.
- **The Catch:** Every figure here is a national average. A coal-heavy grid, a skipped fuel cycle, or a cold week of heavy loads can move the electric number more than a route change can.

## Sources
[1] U.S. Environmental Protection Agency, "Greenhouse Gas Emissions from a Typical Passenger Vehicle" — https://www.epa.gov/greenvehicles/greenhouse-gas-emissions-typical-passenger-vehicle
[2] U.S. Environmental Protection Agency, "Greenhouse Gas Equivalencies Calculator: Calculations and References" — https://www.epa.gov/energy/greenhouse-gases-equivalencies-calculator-calculations-and-references
[3] U.S. Energy Information Administration, "How much carbon dioxide is produced per kilowatthour of U.S. electricity generation?" — https://www.eia.gov/tools/faqs/faq.php?id=74&t=11
[4] U.S. Energy Information Administration, "Electricity explained: Prices and factors affecting prices" (2025 annual averages) — https://www.eia.gov/energyexplained/electricity/prices-and-factors-affecting-prices.php
[5] U.S. Department of Energy, Alternative Fuels Data Center, "Electric Vehicle Benefits and Considerations" — https://afdc.energy.gov/fuels/electricity_benefits.html
[6] U.S. Department of Energy, Alternative Fuels Data Center, "Emissions from Electric Vehicles" — https://afdc.energy.gov/vehicles/electric_emissions.html
[7] U.S. Environmental Protection Agency, "Learn about SmartWay" — https://www.epa.gov/smartway/learn-about-smartway
