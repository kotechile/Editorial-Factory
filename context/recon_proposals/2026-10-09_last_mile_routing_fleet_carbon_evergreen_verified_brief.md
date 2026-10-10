# Verified Brief: last_mile_routing_fleet_carbon — 2026-10-09 (evergreen)

Evergreen track (`skills/evergreen_topics.md`) — no news gate, no freshness window. Every
load-bearing figure below was fetched live this run and matched to the source that states it.
No Signal A/B split applies: this is a single-thesis evergreen topic, not a news synthesis.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| 1 | Diesel factor | Burning one gallon of diesel emits 10,180 grams of CO2 under the federal conversion factor EPA publishes for tailpipe accounting (gasoline: 8,887 grams) | VERIFIED | https://www.epa.gov/greenvehicles/greenhouse-gas-emissions-typical-passenger-vehicle | "CO 2 emissions from a gallon of gasoline: 8,887 grams CO 2 / gallon CO 2 emissions from a gallon of diesel: 10,180 grams CO 2 / gallon" |
| 2 | Diesel factor is a fuel-carbon constant, not a measurement | The 10,180 g/gal diesel factor was agreed as a common conversion factor in the 2010 joint EPA/DOT rulemaking, assumes all carbon in the diesel converts to CO2, and equals 10.180 × 10-3 metric tons CO2 per gallon | VERIFIED | https://www.epa.gov/energy/greenhouse-gases-equivalencies-calculator-calculations-and-references | "the agencies stated that they had agreed to use a common conversion factor of 10,180 grams of CO 2 emissions per gallon of diesel consumed (Federal Register 2010)" / "This value assumes that all the carbon in the diesel is converted to CO 2 (IPCC 2006). Calculation 10,180 grams of CO 2 /gallon of diesel = 10.180 × 10-3 metric tons CO 2 /gallon of diesel" |
| 3 | Grid factor (EIA) | U.S. net electricity generation in 2023 emitted about 0.81 pounds of CO2 per kWh — 1.53 billion metric tons over 4.18 trillion kWh | VERIFIED | https://www.eia.gov/tools/faqs/faq.php?id=74&t=11 | "In 2023, total annual U.S. net electricity generation by utility-scale electric power plants … was about 4.18 trillion kilowatthours (kWh) from all energy sources. U.S. net generation resulted in about 1.53 billion metric tons—1.69 billion short tons —of carbon dioxide (CO 2 ) emissions, which is about 0.81 pounds of CO 2 emissions per kWh." |
| 4 | Grid factor (EPA) differs from EIA's | EPA's equivalencies calculator uses 823.1 pounds of CO2 equivalent per MWh (0.8231 lb/kWh) — a different vintage and a CO2e rather than CO2 unit from EIA's 0.81 | VERIFIED | https://www.epa.gov/energy/greenhouse-gases-equivalencies-calculator-calculations-and-references | "The amount of carbon dioxide equivalent emitted per MWh is 823.1 pounds (EPA 2024)." |
| 5 | Electric efficiency (denominator for the EV number) | The weighted average combined electric efficiency of U.S. EV sales is 3.60 miles per kWh (DOE 2023); a light-duty all-electric vehicle drives 100 miles on 25-40 kWh | VERIFIED | https://www.epa.gov/energy/greenhouse-gases-equivalencies-calculator-calculations-and-references · https://afdc.energy.gov/fuels/electricity_benefits.html | "The weighted average combined electric efficiency of U.S. electric vehicles sales from 2019 and earlier is 3.60 miles per kWh (DOE 2023)." / "today's light-duty all-electric vehicles (or PHEVs in electric mode) can exceed 130 MPGe and can drive 100 miles consuming only 25–40 kWh" |
| 6 | Tariff class (the second published rate) | In 2025 the U.S. annual average retail price of electricity was 13.63¢ per kWh: commercial 13.41¢, industrial 8.62¢, residential 17.30¢, transportation 13.83¢ per kWh; state averages ran 35.72¢ (Hawaii) to 8.20¢ (North Dakota) | VERIFIED | https://www.eia.gov/energyexplained/electricity/prices-and-factors-affecting-prices.php | "In 2025, the U.S. annual average retail price of electricity was about 13.63¢ per kilowatthour (kWh). … residential 17.30¢ per kWh commercial 13.41¢ per kWh industrial 8.62¢ per kWh transportation 13.83¢ per kWh" / "ranged from 35.72¢ per kWh in Hawaii to 8.20¢ per kWh in North Dakota" |
| 7 | Boundary vocabulary (why two numbers are not comparable) | Emissions can be evaluated on a tailpipe basis, a well-to-wheel basis and a cradle-to-grave basis; an all-electric vehicle has zero tailpipe emissions but the electricity pathway carries upstream emissions | VERIFIED | https://afdc.energy.gov/vehicles/electric_emissions.html | "Emissions can be evaluated on a tailpipe basis, a well-to-wheel basis, and a cradle-to-grave basis." / "All-electric vehicles and PHEVs running only on electricity have zero tailpipe emissions, but electricity production, such as power plants, may generate emissions." |
| 8 | Context (scale of the freight footprint) | The U.S. transportation system moves a daily average of over 51 million tons of freight (about 57 tons per capita), and e-commerce sales increased 20-fold between 2000 and 2019 | VERIFIED | https://www.epa.gov/smartway/learn-about-smartway | "The U.S. transportation system moves a daily average of over 51 million tons of freight or about 57 tons of freight per capita E-Commerce sales increased 20-fold between 2000 and 2019" |

## Gate notes
- **Source floor: PASS** — the evergreen gate fetched 6 brief rows across 3 hosts (epa.gov, eia.gov,
  afdc.energy.gov) and every one contained the figure it was cited for. Recorded in the
  `<!-- evergreen-gate: -->` marker of the brief.
- **Row 4 is the point of the article, not a footnote.** Two federal sources publish two grid factors
  (0.81 lb CO2/kWh, EIA, 2023 data; 823.1 lb CO2e/MWh, EPA, 2024) and a carrier's claimed reduction can
  be earned by switching between them rather than by moving a single parcel. Rows 4 and 6 come from
  pages outside the brief's table on purpose — they are corroborating detail, and the brief's own rows
  still carry the floor.
- **Vendor vs measured:** all rows are government statistical or agency-guidance pages; no vendor
  claim is load-bearing and no row is a vendor's own marketing figure.
- **REMOVED: 0. FLAGGED: 0.**

## Figure set cleared for drafting (no other number may appear without a source)
10,180 grams CO2 per gallon of diesel · 8,887 grams CO2 per gallon of gasoline · 10.180 × 10-3 metric
tons CO2 per gallon · 0.81 pounds CO2 per kWh · 4.18 trillion kWh · 1.53 billion metric tons ·
823.1 pounds CO2e per MWh · 3.60 miles per kWh · 25-40 kWh per 100 miles · 13.63¢ per kWh (2025 U.S.
average) · 13.41¢ commercial · 8.62¢ industrial · 17.30¢ residential · 13.83¢ transportation ·
35.72¢ Hawaii · 8.20¢ North Dakota · 51 million tons of freight per day · 57 tons per capita ·
20-fold e-commerce growth 2000-2019.

**Editorial arithmetic permitted (label as the writer's own reading, never as a sourced figure):**
- A diesel van at 8 mpg emits 10,180 ÷ 8 ≈ 1,270 grams of CO2 per mile; at 6 mpg, ≈ 1,697.
- An electric van at 30 kWh per 100 miles draws 0.30 kWh per mile, which at 0.81 lb/kWh is
  0.243 lb ≈ 110 grams of CO2 per mile; at EPA's 823.1 lb/MWh it is ≈ 112 grams.
- 13.41 ÷ 8.62 ≈ 1.56, i.e. the published commercial class average is about 56% above the industrial
  class average for the same kilowatt-hour.
- 10,180 g ÷ 10.18 = 1 kg: the diesel factor is stated in two units on two government pages, which is
  itself the units trap the scorecard has to name.
