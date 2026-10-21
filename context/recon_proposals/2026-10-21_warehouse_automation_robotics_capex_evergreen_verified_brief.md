# Verified Brief: warehouse_automation_robotics_capex — 2026-10-21 (evergreen)

Archetype: evergreen. Companion to `2026-10-21_warehouse_automation_robotics_capex_evergreen_brief.md`
(gate PASS, 7 verified rows, 3 hosts). Every claim below was re-fetched on 2026-10-21 and the verbatim
string is quoted from the fetched page.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|---|---|---|---|---|
| C1 | Station ceiling (2018 study) | At 1,000 SKUs and small orders, four robots per pick station reach 91% of the throughput ceiling the picker sets; a fifth robot adds six points (to 97%) and a sixth adds none | VERIFIED | https://arxiv.org/html/1801.06703v1 | "Table 10: Best unit throughput rate score for all scenarios, robots per pick station and numbers of pick stations … 1K-S-N 44 82 91 97 97 59 89 94 97 98 …" — row `1K-S-N`, one pick station, robots 2–6; entries are "the unit throughput rate as a percentage of the upper bound" |
| C2 | Catalogue changes the saturation point (2018 study) | At 10,000 SKUs with medium orders and returns, four robots per station reach only 59% of the ceiling; six robots reach 83% | VERIFIED | https://arxiv.org/html/1801.06703v1 | "10K-M-R 21 41 59 73 83 28 48 63 76 85 …" — same Table 10 row structure (one station, robots 2–6) |
| C3 | Replenishment share of robot time (2018 study) | Replenishment consumed 20.29% of overall robot time across the phase-2 runs | VERIFIED | https://arxiv.org/html/1801.06703v1 | "Replenishment operations only consume 20.29 % out of the overall time consumed by the robots in average across all phase 2 simulation runs." |
| C4 | Few robots can saturate a small catalogue (2018 study) | With 1,000 SKUs the unit throughput rate sits close to its theoretical maximum even with relatively few robots per station | VERIFIED | https://arxiv.org/html/1801.06703v1 | "Furthermore, we can conclude that with 1000 SKUs, the unit throughput rates are close to their theoretical maximum even with relatively few robots per stations." |
| C5 | Stable minimum fleet (2024 study) | A system with two picking stations and two replenishment stations needs at least 17 robots to be stable; two combi-stations reduce that to 16 | VERIFIED | https://arxiv.org/html/2403.12798v1 | "When using two-station types (each type has two stations), the minimum number of robots for the system to be stable is 17, while the number is reduced to 16 when using two combi-stations." |
| C6 | The ceiling on useful robots (2024 study) | Past 40 robots in that same example, extra robots cannot meaningfully raise the arrival rate | VERIFIED | https://arxiv.org/html/2403.12798v1 | "In particular, with more than 40 robots, it is not possible to significantly increase the arrival rate with additional robots." |
| C7 | Combi-stations at equal fleet (2024 study) | At the same 17 robots, the combi-station system cuts average order turnover time by about 64% | VERIFIED | https://arxiv.org/html/2403.12798v1 | "if we keep the same minimum number of robots of the two-station type system (namely 17 robots), the average order turnover time can be reduced by about 64% in the combi-station system." |
| C8 | Station handling time in the example (2024 study) | The 2024 example assumes 10 seconds average picking time per unit at a pick station and 30 seconds at a replenishment station | VERIFIED | https://arxiv.org/html/2403.12798v1 | "Average picking time of picking stations 1 and 2 : ν p 1 − 1 = ν p 2 − 1 = 10 s , average replenishment time of replenishment stations 1 and 2 … ν r 1 − 1 = ν r 2 − 1 = 30 s" |
| C9 | Published deployment ratio (S&S Activewear) | A PopPick deployment is designed for more than 4,500 lines per hour through 24 picking stations — 187.5 lines an hour per station | VERIFIED (vendor claim) | https://www.mmh.com/article/ss_activewear_partners_with_koerber_supply_chain_software_and_geekplus_on_robotics_deployment | "The system is designed to support more than 4,500 lines per hour through 24 picking stations, and incorporates autonomous mobility and slotting of inventory." |
| C10 | Fleet size at the same deployment | The same announcement reports 340 Geekplus robots in the first 750,000 sq. ft. site | VERIFIED (vendor claim) | same as C9 | "Deployment at three warehouse sites began with one site in Illinois with 340 Geekplus robots implemented in the 750,000 sq. ft. facility" |
| C11 | The 4-robots-per-associate claim (Locus) | One associate with four Locus robots picks 300-400 units per hour from bulk locations | VERIFIED (vendor claim) | https://locusrobotics.com/blog/p2g-unlimited-warehouse-throughput-fast-pick | "With a single associate working alongside four Locus robots, Fast Pick enables the picking of 300-400 units per hour from bulk locations." |
| C12 | The manual baseline Locus cites | The vendor puts the average manual picking rate at 40-60 units per hour "according to industry data" | VERIFIED (vendor claim, second-hand) | same as C11 | "the average manual picking rate is around 40-60 UPH according to industry data" |
| C13 | Adoption base (2026 survey) | 48% of surveyed companies use goods-to-person picking now; 51% are preparing updates or new deployments | VERIFIED | https://www.mmh.com/article/2026_automation_study_warehouse_automation_ticks_upward | "Goods-to-person picking solutions follow a similar pattern, with 48% of companies using them now and 51% preparing for updates or new deployments." |
| C14 | What buyers say they rank (2026 survey) | 92% rate durability, reliability and uptime very important; 95% call fast response times essential, up from 83%; 77% point to total cost of ownership, ROI and maintenance costs | VERIFIED | same as C13 | "companies prioritize durability, reliability and uptime, with 92% of survey participants rating these factors as very important … This year, 95% say fast response times are essential, up from 83% in last year's study … Most companies (77%) point to total cost of ownership, ROI and maintenance costs" |

## Gate rulings for the drafter
1. **Every percentage from the two studies is conditional on the example.** Table 10's entries are
   "the unit throughput rate as a percentage of the upper bound", and the upper bound is the rate the
   picker's handling time allows. Write "of the ceiling the picker sets", never "of capacity" or
   "utilisation". Always name the scenario (1,000 SKUs, small orders / 10,000 SKUs, medium orders) with
   the figure — a bare "91% of capacity" is a claim neither paper makes.
2. **The 17/40-robot figures belong to one small example** (two picking stations, two replenishment
   stations, 10 s picks, 30 s replenishments). Never generalise them into "40 robots is the ceiling" or
   "you need 17 robots". They are the illustration; the mechanism is the rule.
3. **Authorised arithmetic (the desk's own, and only these):** 4,500 lines ÷ 24 stations = 187.5 lines
   an hour per station (C9). 340 robots ÷ one site (750,000 sq ft) is a scale note, never a
   robots-per-station ratio — the article does not say how many stations that Illinois site runs, so do
   not divide 340 by 24.
4. **Locus's 4:1 is per associate in a person-to-goods layout, not per station.** Keep the noun
   ("associate") attached; a "four robots per station" claim sourced to Locus would be a fabrication.
5. **Two studies, one research line.** The 2024 paper applies the 2019 approximation method of the same
   group; describe both as peer-reviewed queueing studies and do not present them as two independent
   field measurements. No field-measured throughput audit exists in the verified set, and the article
   must say the deployment figures are announced design targets.
6. **No charging figure is verified.** Charging time as a share of a robot's day is not in any source
   row — say only that a robot on a charger is not in the pool (a mechanism, not a number).
7. **No prices, wages, payback months or vendor names beyond those cited.** Do not compute a payback
   from any of these figures; the article's arithmetic stops at lines per station and the saturation
   points.
