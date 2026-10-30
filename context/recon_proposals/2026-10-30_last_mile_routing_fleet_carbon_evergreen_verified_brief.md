# Verified Brief: last_mile_routing_fleet_carbon — 2026-10-30

Companion to `2026-10-30_last_mile_routing_fleet_carbon_evergreen_brief.md` (evergreen gate PASS, 6 rows, 4 hosts).
Every figure below was fetched live on 2026-10-30 through `citation_hub_dossier.fetch_source` and its
evidence window read by eye. Derived arithmetic is marked DERIVED and shows its inputs.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|---|---|---|---|---|
| 1 | Vocational fuel economy | A delivery truck averages 7.1928 miles per gasoline gallon equivalent in the federal table; the same table gives a light truck/van 18.5, a Class 8 truck 6.3048 and a refuse truck 5.2392 | VERIFIED | https://afdc.energy.gov/data/10310 | "Transit Bus Refuse Truck Class 8 Truck School Bus Delivery Truck Demand Response Light Truck/Van Transit Vanpool Car Motorcycle mpg Gasoline 3.6408 5.2392 6.3048 6.5712 7.1928 7.7 18.5 19.8 25.6 44" |
| 2 | Table provenance and unit | The chart's source line is FHWA Highway Statistics 2024, Table VM-1, and its values are in gasoline gallon equivalents, not gallons of the fuel burned | VERIFIED | https://afdc.energy.gov/data/10310 | "Source: Federal Highway Administration. Highway Statistics 2024, Table VM-1." / "The metric used is gasoline gallon equivalents (GGEs), representing a quantity of fuel with the same amount of energy contained in a gallon of gasoline." |
| 3 | Diesel's energy content | One gallon of low sulfur diesel equals 1.12 gasoline gallon equivalents (1.00 diesel gallon equivalent) | VERIFIED | https://afdc.energy.gov/fuels/properties | "Gasoline or Diesel Gallon Equivalent (GGE or DGE) 1 gal = 1.00 GGE 1 gal = 0.88 DGE 1 gal = 1.12 GGE 1 gal = 1.00 DGE" |
| 4 | Diesel price, dated | U.S. on-highway diesel was $6.352 a gallon the week of 10/26/2026 (release date October 27, 2026); the same row carries $2.634 a year earlier and $6.276 the week before | VERIFIED | https://www.eia.gov/petroleum/gasdiesel/ | "U.S. On-Highway Diesel Fuel Prices*(dollars per gallon) full history XLS Change from 10/12/26 10/19/26 10/26/26 2 year ago year ago week ago U.S. 6.179 6.276 6.352 2.779 2.634 0.076" |
| 5 | Gasoline price, same release | U.S. regular gasoline was $4.269 a gallon the week of 10/26/2026 (release date October 27, 2026), against $1.234 a year earlier | VERIFIED | https://www.eia.gov/petroleum/gasdiesel/ | "U.S. Regular Gasoline Prices*(dollars per gallon) full history XLS Change from 10/12/26 10/19/26 10/26/26 2 year ago year ago week ago U.S. 4.331 4.284 4.269 1.172 1.234 -0.015" |
| 6 | Driver wage, dated | The median wage for light truck drivers is $21.57 hourly and $44,860 annual, 2025 vintage | VERIFIED | https://onetonline.org/link/summary/53-3033.00 | "Median wages (2025) $21.57 hourly, $44,860 annual" |
| 7 | Why the duty cycle costs fuel | Only about 12% to 30% of the fuel's energy moves a conventional vehicle down the road, and the page's own diagram is estimated for stop-and-go city driving under the EPA FTP-75 test procedure | VERIFIED | https://www.fueleconomy.gov/feg/atv.shtml | "Only about 12%–30% of the energy from the fuel you put in a conventional vehicle is used to move it down the road, depending on the drive cycle." / "Combined City Highway Energy requirements in this diagram are estimated for stop-and-go city driving using the EPA FTP-75 Test procedure." |
| 8 | Cost per mile, diesel truck | $0.7885 a mile: 7.1928 miles per GGE × 1.12 GGE per diesel gallon = 8.0559 miles per diesel gallon; 1 ÷ 8.0559 = 0.12413 gallons a mile; × $6.352 | DERIVED (from rows 1, 3, 4) | — | 0.12413 × 6.352 = 0.7885 |
| 9 | Cost per mile, light van | $0.3066 a mile: 18.5 × 1.12 = 20.72 miles per diesel gallon; 1 ÷ 20.72 = 0.04826 gallons a mile; × $6.352 | DERIVED (from rows 1, 3, 4) | — | 0.04826 × 6.352 = 0.3066 |
| 10 | Thirst ratio | The delivery truck's mile costs 2.572 times the light van's (0.7885 ÷ 0.3066) | DERIVED (rows 8, 9) | — | 0.7885 ÷ 0.3066 = 2.572 |
| 11 | The exchange rate | One driver-minute is worth $0.3595 ($21.57 ÷ 60), so a $0.7885 mile equals 2.193 driver-minutes | DERIVED (rows 6, 8) | — | 0.7885 ÷ 0.3595 = 2.193 |
| 12 | The same rate a year ago | At the year-earlier diesel print the mile was $0.3270, or 0.909 driver-minutes | DERIVED (rows 4, 6) | — | 1 ÷ 8.0559 × 2.634 = 0.3270; ÷ 0.3595 = 0.909 |
| 13 | Ten miles on a hundred-mile day | $7.885 of diesel (10 × 0.7885), equal to 21.9 driver-minutes | DERIVED (rows 8, 11) | — | 10 × 0.7885 = 7.885; ÷ 0.3595 = 21.9 |
| 14 | Cost per mile, gasoline truck | $0.5935 a mile on gasoline: 7.1928 miles a gallon (1.00 GGE per gallon), 0.13903 gallons a mile, × $4.269 | DERIVED (rows 1, 5) | — | 0.13903 × 4.269 = 0.5935 |
| 15 | Stop cost at an illustrated rate | At 22 stops a paid hour the median wage spreads $0.98 of driver pay across each stop ($21.57 ÷ 22); at 18 stops it is $1.20 | DERIVED — illustrated rate, not a measured stop count (rows 6) | — | 21.57 ÷ 22 = 0.9805; 21.57 ÷ 18 = 1.198 |

## Rulings for the drafter

- **State the unit with the fuel-economy figure.** The table is in gasoline gallon equivalents, so 7.1928 is **not**
  "7.19 miles per gallon of diesel". The article must show the 1.12 conversion before quoting 8.06 miles per diesel gallon.
- **Never call the figure "the truck's mpg" bare.** It is a category average from the 2024 highway statistics, and the
  catch section must say so.
- **The 22-stops-an-hour rate is an illustration, not a source claim.** No fetchable primary gives a stop rate; phrase it as
  a hypothetical the reader substitutes their own number into, and never attribute it.
- **Do not print a routing-software price.** None verified; the piece compares the mile and the minute, and leaves the license
  quote to the reader's own invoice.
- **No carbon arithmetic in this piece** — grams, factors and boundaries belong to `2026-10-09_last-mile-carbon-number-is-a-rate-table`;
  repeating them would re-argue a published article.
- FLAGGED (not used as a claim): a secondary vendor page reports a 2026 study of dynamic vs static routing at 24.3% lower operating
  cost; the underlying paper could not be located on nature.com, so no row was written for it and the draft must not cite it.
