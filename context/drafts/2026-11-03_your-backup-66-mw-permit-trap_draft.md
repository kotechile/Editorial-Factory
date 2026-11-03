---
title: "Your Backup's 6.6 MW Permit Trap"
vertical: nhil_infrastructure_ops
kind: evergreen
archetype: evergreen
evergreen: true
persona: it_ops_leader
one_big_thing: "Going behind the meter changes a site's regulatory identity rather than its supply: a gas plant crosses mandatory greenhouse-gas reporting at 6.6 MW running flat, the Title V major-source line at 8.5 MW, and PSD for carbon at 19.9 MW, while the 100-hour emergency-engine cap it abandons is the only thing keeping a 20 MW backup fleet at 5.4 tons of NOx a year instead of 470."
date: 2026-11-03
slug: your-backup-66-mw-permit-trap
meta_title: "Your Backup's 6.6 MW Permit Trap"
meta_description: "Go behind the meter and the plant stops being backup: a gas engine crosses federal greenhouse-gas reporting at 6.6 MW, Title V at 8.5 MW and PSD at 19.9 MW."
---

<!-- lead -->

The pitch for going behind the meter is a schedule argument: skip the utility queue, burn your own gas, keep the racks lit. Federal air rules read that move as a change of identity. A plant stops being backup because it now runs like a power station, and the permit file follows it behind the meter. On a gas engine at 8,120 Btu per kilowatthour, mandatory greenhouse-gas reporting starts at 6.6 megawatts (MW) running flat. That is under a third of one dense AI hall.

<!-- tension -->

## Three thresholds, three sizes

None of the federal tests asks how many megawatts you need. They ask how much fuel the site can burn, and what leaves the stack. Each one turns into a plant size you can put in front of a board.

The lowest rung is reporting. A facility in no listed source category reports to the Environmental Protection Agency (EPA) once its burners can take 30 million Btu per hour (mmBtu/hr) of heat input. The site must also emit 25,000 metric tons of carbon dioxide equivalent a year [1][10]. Both conditions apply, not either one.

Above that sits the operating permit. A major source emits, or can emit, 100 tons a year of any regulated pollutant [3]. Above that sits prevention of significant deterioration (PSD). Carbon becomes a regulated pollutant for a new major source that will emit 75,000 tons of CO2e a year [4]. Measured against a heat rate, the ladder reads like this.

| Rung | Threshold | Plant size, running flat | What it starts |
|---|---|---|---|
| Heat input | 30 mmBtu/hr of combustion capacity [1] | 3.7 MW | first condition of the reporting test |
| CO2e | 25,000 metric tons a year [1][10] | 6.6 MW | annual greenhouse-gas report to EPA |
| NOx | 100 tons a year of a regulated pollutant [3] | 8.5 MW at 1.0 g/HP-hr [5] | Title V operating permit |
| CO2e, again | 75,000 tons a year [4] | 19.9 MW | PSD, with carbon as a regulated pollutant |

The arithmetic is one line. Natural gas carries a default factor of 53.06 kg of CO2 per mmBtu [2], so 25,000 tonnes is 471,165 mmBtu of fuel a year. Spread across 8,760 hours, that is 53.8 mmBtu/hr, which is 6.6 MW at 8,120 Btu/kWh.

Now take the same machine to 20 MW. The site emits 75,484 tonnes, within 1% of the PSD line. That kind of coincidence decides a permit strategy by accident.

Duty cycle moves the whole ladder. The 6.6 MW plant reaches its tonnage only if it runs flat. At a load factor of one-fifth, the same tonnage needs 33 MW of nameplate.

## The hours you trade

Every data hall already owns a plant of roughly this size. The reason it never tripped these thresholds is a number that appears in none of them.

An emergency engine may run 100 hours a year for maintenance and testing. Of those, 50 may be non-emergency [6]. A 20 MW backup fleet inside that cap emits about 5.4 tons of NOx a year. That figure uses the 2.0 grams per horsepower-hour (HP-hr) standard for emergency engines [5].

Run the same fleet flat and it emits 470 tons. That is nearly five times the major-source line. Even at the tighter 1.0 g/HP-hr standard for non-emergency engines, it emits 235 [5].

The rule is blunt about the trade. Operate past the cap, and the engine "will not be considered an emergency engine under this subpart and must meet all requirements for non-emergency engines" [6]. The hour limit is the whole reason a backup fleet is cheap to permit. Prime power is what removes it.

## By the numbers

- **2.3 lb per MWh — turbine NOx limit:** a new gas turbine of 50 mmBtu/hr or less is held to 42 ppm at 15% oxygen, printed in the rule as 2.3 lb of NOx per MWh [7]. That puts the 100-ton line at 10.9 MW, above the engine's 8.5.
- **53.06 kg — carbon per unit of fuel:** the default factor for natural gas, weighted U.S. average, and the only number needed to turn a fuel bill into a tonnage [2].
- **13.41¢ — what the grid charges:** the 2025 average commercial retail price per kWh [9]. That is the price the plant must beat while carrying a reporting duty the grid never had.

My read is that the ladder is doing the work here, not the fuel contract.

<!-- tactical-insight -->

## What the ladder pushes operators toward

Read the rules in order, and three habits fall out of them. None of the three is a fuel decision.

The first is modularity. The reporting test is written per facility, so tonnage is a sum and not an average. A plant built from modules files differently from one large machine making the same megawatts.

The second is separation. A fleet kept inside the emergency definition cannot carry prime load. Prime power therefore lands on its own machines and its own permit file.

What I'm watching is the third. A simple-cycle machine at 9,750 Btu/kWh emits 1.14 lb of CO2 per kWh [8]. The average U.S. grid emits 0.81 lb, and gas-fired generation on it emits 0.96 lb [8]. A site that goes behind the meter to escape a queue reports a worse carbon number than the one it left. That number lands in the same sustainability report that justified the project.

<!-- nuanced-takeaway -->

## The catch

I could be wrong, but two things blunt this arithmetic. Both deserve a check before any number reaches a board deck.

The federal figures are floors. Part 70 treats a source in a severe ozone nonattainment area as major at 25 tons a year of NOx [3]. In an extreme area the line is 10 tons [3]. So the same engine can cross a permit line at a quarter of the federal tonnage, depending on where the hall sits. County and state rules decide more of this than the federal code does.

The machine decides the rung as much as the size does. A turbine's 2.3 lb per MWh is about three-quarters of what an engine held to 1.0 g/HP-hr puts out: 2.96 lb [5][7]. That is why the turbine's permit line sits above the engine's at the same output. It is also why one tonnage target can be met by two very different plants, at very different cost.

What survives all of it is the conversion. Take your own heat rate, divide your megawatts into mmBtu per hour, and multiply by 53.06 kg. Compare the result against three numbers: 25,000, 100, and 75,000.

If the hall itself is the open question, that ceiling is a building problem, [not a fuel one](/rack-power-density-ceiling-build-before-you-buy/). It gets settled before the permit file opens.

<!-- tldr -->

## At a glance

**The shift:** behind-the-meter gas turns a backup fleet into a reported source. **The number:** 6.6 MW flat is where reporting starts. **The risk:** the 100-hour cap that kept the fleet cheap to permit is gone, and the tonnage only goes up.

## Sources

[1] Legal Information Institute, Cornell Law School — 40 CFR § 98.2 "Who must report?" https://www.law.cornell.edu/cfr/text/40/98.2
[2] U.S. eCFR — 40 CFR Part 98 Subpart C, Table C-1, default CO2 emission factors and high heat values https://www.ecfr.gov/current/title-40/chapter-I/subchapter-C/part-98/subpart-C
[3] U.S. eCFR — 40 CFR § 70.2, definition of "major source" https://www.ecfr.gov/current/title-40/chapter-I/subchapter-C/part-70/section-70.2
[4] U.S. eCFR — 40 CFR § 52.21(b)(49)(iv)(A), prevention of significant deterioration https://www.ecfr.gov/current/title-40/chapter-I/subchapter-C/part-52/section-52.21
[5] U.S. eCFR — 40 CFR Part 60 Subpart JJJJ, Table 1, NOx standards for stationary spark-ignition engines https://www.ecfr.gov/current/title-40/chapter-I/subchapter-C/part-60/subpart-JJJJ
[6] U.S. eCFR — 40 CFR § 60.4243(d), compliance requirements for emergency stationary engines https://www.ecfr.gov/current/title-40/chapter-I/subchapter-C/part-60/subpart-JJJJ/section-60.4243
[7] U.S. eCFR — 40 CFR Part 60 Subpart KKKK, Table 1, NOx limits for new stationary combustion turbines https://www.ecfr.gov/current/title-40/chapter-I/subchapter-C/part-60/subpart-KKKK
[8] U.S. Energy Information Administration — FAQ, carbon dioxide per kilowatthour of U.S. electricity generation https://www.eia.gov/tools/faqs/faq.php?id=74&t=11
[9] U.S. Energy Information Administration — Electricity explained, prices and factors affecting prices https://www.eia.gov/energyexplained/electricity/prices-and-factors-affecting-prices.php
[10] U.S. Environmental Protection Agency — What is the GHGRP? https://www.epa.gov/ghgreporting/what-ghgrp
