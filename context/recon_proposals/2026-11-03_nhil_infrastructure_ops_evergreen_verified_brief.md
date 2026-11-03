# Evergreen Verified Brief: nhil_infrastructure_ops — 2026-11-03

**Brief:** `2026-11-03_nhil_infrastructure_ops_evergreen_brief.md` — gate PASS, 10 sources verified on 4 hosts (ecfr.gov, law.cornell.edu, eia.gov, epa.gov), marker written 2026-11-03T18:05Z.

**Thesis defended by the draft:** behind-the-meter gas is a change of regulatory identity, not of supply; the federal thresholds convert to 6.6 MW (GHG reporting), 8.5 MW (Title V) and 19.9 MW (PSD) on a gas engine at 8,120 Btu/kWh running flat, and the 100-hour emergency-engine cap is what kept the backup fleet cheap to permit.

## Verbatim quotes, read from the fetched page (not from the API listing)

### [1] https://www.law.cornell.edu/cfr/text/40/98.2

> (3) A facility that in any calendar year starting in 2010 meets all three of the conditions listed in this paragraph (a)(3). For these facilities , the annual GHG report must cover emissions from stationary fuel combustion sources only. (i) The facility does not meet the requirements of either paragraph (a)(1) or (a)(2) of this section. (ii) The aggregate maximum rated heat input capacity of the stationary fuel combustion units at the facility is 30 mmBtu /hr or greater. (iii) The facility emits 25,000 metric tons CO 2 e or more per year in combined emissions from all stationary fuel combustion sources. (4) A sup

### [2] https://www.ecfr.gov/current/title-40/chapter-I/subchapter-C/part-98/subpart-C

> Natural gas mmBtu/scf kg CO 2 /mmBtu (Weighted U.S. Average) 1.026 × 10 −3 53.06 Petroleum products—liquid mmBtu/gallon kg CO 2 /mmBtu Disti

### [3] https://www.ecfr.gov/current/title-40/chapter-I/subchapter-C/part-70/section-70.2

> A major stationary source of air pollutants, as defined in section 302 of the Act, that directly emits, or has the potential to emit, 100 tpy or more of any air pollutant subject to regulation (including any major source of fugitive emissions of any such pollutant, as determined by rule by the Admin

### [4] https://www.ecfr.gov/current/title-40/chapter-I/subchapter-C/part-52/section-52.21

> ( iv ) Beginning January 2, 2011, the pollutant GHGs is subject to regulation if: ( A ) The stationary source is a new major stationary source for a regulated NSR pollutant that is not GHGs, and also will emit or will have the potential to emit 75,000 tpy CO 2 e or more; or ( B ) The stationary source is an existing major stationary source for a regulated NSR pollutant that is not GHGs, and also will have an emission

### [5] https://www.ecfr.gov/current/title-40/chapter-I/subchapter-C/part-60/subpart-JJJJ

> Non-Emergency SI Natural Gas b and Non-Emergency SI Lean Burn LPG b 100≤HP<500 7/1/2008 2.0 4.0 1.0 160 540 86 1/1/2011 1.0 2.0 0.7 82 270 60 Non-Emergency SI Lean Burn Natural Gas and LPG 500≤HP<1,350 1/1/2008 2.0 4.0 1.0 160 540 86 7/1/2010 1.0 2.0 0.7 82 270 60 Non-Emergency SI Natural Gas and Non-Emergency SI Lean Burn LPG (except lean burn 500≤HP<1,350) HP≥500 7/1/2007 2.0 4.0 1.0 160 540 86 HP≥500 7/1/2010 1.0

### [6] https://www.ecfr.gov/current/title-40/chapter-I/subchapter-C/part-60/subpart-JJJJ/section-60.4243

> If you do not operate the engine according to the requirements in paragraphs (d)(1) through (3), the engine will not be considered an emergency engine under this subpart and must meet all requirements for non-emergency engines. ( 1 ) There is no time limit on

### [7] https://www.ecfr.gov/current/title-40/chapter-I/subchapter-C/part-60/subpart-KKKK

> New turbine firing natural gas, electric generating ≤50 MMBtu/h 42 ppm at 15 percent O 2 or 290 ng/J of useful output (2.3 lb/MWh). New turbine firing natural gas, mechan

### [8] https://www.eia.gov/tools/faqs/faq.php?id=74&t=11

> resulted in about 1.53 billion metric tons—1.69 billion short tons —of carbon dioxide (CO 2 ) emissions, which is about 0.81 pounds of CO 2 emissions per kWh. Emissions from electricity generation vary by type of energy source and by type and efficiency of the electric power plant. The amount of CO 2 produced per kWh during any period var

### [9] https://www.eia.gov/energyexplained/electricity/prices-and-factors-affecting-prices.php

> of electricity was about 13.63¢ per kilowatthour (kWh). 1 The annual average retail electricity prices by major types of utility customers in 2025 were: residential 17.30¢ per kWh commercial 13.41¢ per kWh industrial 8.62¢ per kWh transportation 13.83¢ per kWh Electricity prices vary by locality Electricity prices vary by locality based on the availability of power pl

### [10] https://www.epa.gov/ghgreporting/what-ghgrp

> Direct emissions sources that have annual emissions of less than 25,000 metric tons of CO 2 e, unless the source is required to report regardless of their total annual emissions. For additional details, see Who is Required to Repo

## Prose-carried claims (verified by eye, quoted above, deliberately NOT gate rows)

- **§ 98.2(a)(3) is a three-part test.** A facility outside the listed source categories reports only if it meets *all three* conditions: not in (a)(1)/(a)(2), aggregate maximum rated heat input **≥ 30 mmBtu/hr**, and **≥ 25,000 metric tons CO2e per year** from all stationary fuel combustion sources. The 30 mmBtu/hr condition alone is not sufficient, and the article says so.
- **§ 60.4243(d) caps emergency operation.** 100 hours per calendar year for maintenance and testing, of which up to 50 may be non-emergency; there is no time limit during an actual emergency. Operating past the cap means the engine "will not be considered an emergency engine under this subpart and must meet all requirements for non-emergency engines" — the sentence the article quotes.
- **§ 70.2's nonattainment ladder** is carried in prose in the catch: 100 tpy in Marginal/Moderate ozone areas, 50 tpy in Serious, 25 tpy in Severe, 10 tpy in Extreme, for VOC or NOx.
- **Table JJJJ row read:** non-emergency lean-burn natural gas 500–1,350 HP built on/after 1 July 2010 = 1.0 g/HP-hr NOx (82 ppmvd); emergency engines ≥130 HP = 2.0 g/HP-hr.

## Arithmetic in the draft, recomputed from the cited figures

| Line | Derivation | Result |
|---|---|---|
| Heat input per MW at 8,120 Btu/kWh | 8,120 Btu/kWh × 1,000 kWh/MWh ÷ 10⁶ | 8.12 mmBtu/h |
| 30 mmBtu/hr in MW | 30 ÷ 8.12 | 3.7 MW |
| 25,000 t in fuel | 25,000,000 kg ÷ 53.06 kg/mmBtu | 471,165 mmBtu/yr (53.8 mmBtu/h flat) → 6.6 MW |
| 75,000 t in MW | 1,413,494 mmBtu/yr ÷ 8,760 ÷ 8.12 | 19.9 MW |
| 20 MW flat, CO2e | 20 × 8.12 × 8,760 × 53.06 kg | 75,484 t (0.6% above the 75,000 line) |
| 6.6 MW at a one-fifth load factor | 6.6 ÷ 0.2 | 33 MW |
| NOx, 1.0 g/HP-hr | 1,341 hp/MW × 1.0 g × 8,760 h | 11.75 t/MW-yr → 100 t at 8.5 MW |
| NOx, 2.0 g/HP-hr | double the above | 23.49 t/MW-yr → 100 t at 4.3 MW |
| 20 MW fleet, 100 h/yr at 2.0 g/HP-hr | 26,820 hp × 2.0 g × 100 h | 5.4 t |
| 20 MW fleet flat at 2.0 / 1.0 g/HP-hr | × 8,760 h | 470 t / 235 t |
| Turbine at 2.3 lb/MWh | 2.3 × 8,760 ÷ 2,204.62 | 9.14 t/MW-yr → 100 t at 10.9 MW |
| Engine NOx in lb/MWh | 1.0 g/HP-hr × 1,341 hp × 2.20462 ÷ 1,000 | 2.96 lb/MWh (turbine 2.3 = 78% of it) |
| CO2 intensity at 9,750 Btu/kWh | 53.06 kg/mmBtu × 9.75 | 517 kg/MWh = 1.14 lb/kWh (grid 0.81; grid gas 0.96) |

**Known limit of the turbine rung:** Subpart KKKK Table 1 prints the ≤50 mmBtu/h gas turbine limit as "42 ppm at 15 percent O2 or 290 ng/J of useful output (2.3 lb/MWh)". The article cites the rule's own 2.3 lb/MWh parenthetical and derives the 10.9 MW line from it; it does not attempt a ppm-to-lb conversion of its own, because that conversion depends on the F-factor and the O2 correction and would be a derived number no source states.
