---
title: Your Truck Mile Costs 2.2 Driver-Minutes
vertical: last_mile_routing_fleet_carbon
persona: supply_chain_architect
one_big_thing: "A delivery truck's mile costs about 79 cents of diesel at the October 26, 2026 national print — 2.6 times a light van's mile — which is the same money as 2.2 minutes of a driver's wage at the federal median, so a routing change that adds more than two minutes to save a mile loses money and the optimizer's return lives in stops per paid hour rather than in miles saved."
date: 2026-10-30
slug: your-truck-mile-costs-2-2-driver-minutes
archetype: evergreen
evergreen: true
meta_title: "Your Truck Mile Costs 2.2 Driver-Minutes"
meta_title_source: "derived_from_title"
meta_description: "A delivery truck's mile costs $0.79 of diesel at this week's national price, because the stop-and-go duty rather than the engine sets what a route burns, and…"
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/your-truck-mile-costs-2-2-driver-minutes/featured.jpg"
image_style: "architectural_night"
image_model: "flux"
image_alt: "The Cost Of A Truck Mile. A modern delivery truck parked at a commercial loading bay illuminated by warm light at twilight."
image_caption: "The Cost Of A Truck Mile: The trade-off between driver wages and diesel fuel costs."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
A delivery truck's mile costs $0.79 of diesel at this week's national price, because the stop-and-go duty rather than the engine sets what a route burns, and that is where a business case is usually built on the wrong number [1][3][4]. The same $0.79 is what 2.2 driver-minutes of wage comes to at the federal median of $21.57 an hour [6]. Those two lines are most of what a plan can move, and they convert into each other at that rate. A route change that adds three minutes to save a mile spends more on pay than it saves at the pump [3][4][6].

<!-- tension -->

## The big picture:

My read starts with where these numbers come from, because neither is a software sales pitch.

The U.S. Department of Transportation publishes a yearly table of average fuel economy by vehicle class, and its 2024 edition measures them in gasoline gallon equivalents (GGE) [1][2]. The unit needs one adjustment, because a gallon of low-sulfur diesel holds 1.12 of those gallons, so every figure rises by 12% before it describes diesel [2][3].

| Vehicle class | Miles per GGE | Miles per diesel gallon (x1.12) |
| :--- | :--- | :--- |
| Light truck or van | 18.5000 | 20.72 |
| Delivery truck | 7.1928 | 8.06 |
| Class 8 highway tractor | 6.3048 | 7.06 |

Local delivery is where the mileage goes. Only 12% to 30% of the energy in a gallon reaches the road in the government's stop-and-go test cycle [7]. Every stop restarts that loss, which is why a truck halting hundreds of times a day gets less than half the miles of the van beside it [1][7]. Pulling away from neighborhood kerbs, it burns diesel at nearly the pace of the highway tractor in the same table.

Put the two tables together and a route decision turns into arithmetic. A plan that saves a mile but spends two minutes is close to a wash, one that spends four is a loss, and a stop carries more than a mile because it spends pay and fuel at the same time.

## By the numbers

- **12% to 30% — Energy to the road:** the share of a gallon's energy that moves a conventional vehicle in stop-and-go city driving [7].
- **$6.352 — Diesel print:** U.S. on-highway diesel per gallon the week of October 26, 2026, against $2.634 a year earlier [4].
- **$21.57 — Driver's hour:** median wage for light truck drivers in the 2025 survey, or $44,860 a year [6].

<!-- tactical-insight -->

## What I'd watch:

I've been watching how supply-chain teams test route claims against fuel tables rather than against a vendor's slide.

None of this prices a software licence, but these lines decide whether an upgrade pays for itself [3][4][6].

- **The money claim:** a ten-mile cut on a hundred-mile route saves about $7.90 of diesel, the same money as 22 driver-minutes [3][4][6].
- **The stop rate:** at 22 stops in a paid hour the median wage puts $0.98 of pay on each stop, and at 18 stops it puts $1.20 on each, the one line a planner can shorten without buying fuel [6].
- **The false baseline:** a case built on the van's 18.5 rather than the truck's 7.1928 hides fuel cost by a factor of 2.6 [1][2].
- **The hidden work:** the order of stops matters less than the density of the map it is drawn on, which sets the day's pace before the router sees an address [1].

<!-- nuanced-takeaway -->

## The catch

My sense is that these federal numbers are averages, not readings of one route.

A fleet running long country legs between stops will beat the highway figure, and a truck working tight city blocks will burn well past it [1][2]. The pump price moves the rate as well: at the diesel print of a year ago the same mile was worth nine-tenths of a driver-minute, so a case written then priced a mile at about 41% of today's level [4][6].

The wage line is a median too, and health benefits, overtime and route incentives sit on top of it, which lifts the driver-minute and helps the case for time over miles [6]. A truck burning gasoline changes the arithmetic again: at this week's $4.269 a gallon the same mile comes to about $0.59 [5].

What the rate cannot say is whether the minutes freed are spent well. A plan that saves miles without shortening the paid day saves nothing but the pump, and [the district's own density](/your-routes-5x-stop-gap/) does more to the paid day than the sequence does.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Same-Day Delivery Race Is Undoing a Decade of Route Optimization" -> /same-day-race-undoes-route-optimization/ [same site (aichieve.net); same category; topical overlap: delivery, route] Link "Same-Day Delivery Race Is Undoing a Decade of Route Optimization" in the section where the article touches delivery, route. -->
<!-- internal-link hint: "Sticker Price Lies" -> /the-sticker-price-lies-why-mexico-beats-china-on-total-landed-cost/ [same site (aichieve.net); same category; topical overlap: costs, price] Link "Sticker Price Lies" in the section where the article touches costs, price. -->
<!-- internal-link hint: "Your Fuel Surcharge Hides Three Negotiated Numbers" -> /fuel-surcharge-peg-mpg-audit/ [same site (aichieve.net); same category; topical overlap: diesel, price] Link "Your Fuel Surcharge Hides Three Negotiated Numbers" in the section where the article touches diesel, price. -->
## Related reading

- [Same-Day Delivery Race Is Undoing a Decade of Route Optimization](/same-day-race-undoes-route-optimization/) — more on Supply Chain & Operations
- [Sticker Price Lies](/the-sticker-price-lies-why-mexico-beats-china-on-total-landed-cost/) — more on Supply Chain & Operations
- [Your Fuel Surcharge Hides Three Negotiated Numbers](/fuel-surcharge-peg-mpg-audit/) — more on Supply Chain & Operations
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

**The shift:** Federal tables let a route's miles be priced against a driver's minutes.
**The number:** 2.2 driver-minutes buys the diesel in one truck-mile.
**The risk:** Both are averages, and a plan that saves miles without shortening the paid day saves only fuel.

## Sources
[1] U.S. Department of Energy, Alternative Fuels Data Center — "Average Fuel Economy by Major Vehicle Category" (delivery truck 7.1928 miles per gasoline gallon equivalent; light truck/van 18.5; Class 8 truck 6.3048; refuse truck 5.2392; source line: Federal Highway Administration, Highway Statistics 2024, Table VM-1) — https://afdc.energy.gov/data/10310
[2] Same source — the chart's unit note, "The metric used is gasoline gallon equivalents (GGEs), representing a quantity of fuel with the same amount of energy contained in a gallon of gasoline" — https://afdc.energy.gov/data/10310
[3] U.S. Department of Energy, Alternative Fuels Data Center — "Fuel Properties Comparison" (low sulfur diesel: 1 gal = 1.12 GGE, 1 gal = 1.00 DGE) — https://afdc.energy.gov/fuels/properties
[4] U.S. Energy Information Administration — "Gasoline and Diesel Fuel Update" (U.S. on-highway diesel 6.352 dollars per gallon the week of 10/26/2026, against 2.634 a year earlier; release date October 27, 2026) — https://www.eia.gov/petroleum/gasdiesel/
[5] Same source — U.S. regular gasoline 4.269 dollars per gallon the week of 10/26/2026 — https://www.eia.gov/petroleum/gasdiesel/
[6] O*NET OnLine, U.S. Department of Labor — 53-3033.00 Light Truck Drivers (median wages 2025: $21.57 hourly, $44,860 annual) — https://onetonline.org/link/summary/53-3033.00
[7] U.S. Department of Energy and Environmental Protection Agency — FuelEconomy.gov, "Where the Energy Goes: Gasoline Vehicles" (only about 12%–30% of the fuel's energy moves a conventional vehicle down the road; diagram estimated for stop-and-go city driving under the EPA FTP-75 procedure) — https://www.fueleconomy.gov/feg/atv.shtml
