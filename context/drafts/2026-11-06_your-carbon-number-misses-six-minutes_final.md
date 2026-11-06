---
title: "Your Carbon Number Misses Six Minutes"
vertical: last_mile_routing_fleet_carbon
kind: evergreen
archetype: evergreen
evergreen: true
persona: supply_chain_architect
one_big_thing: "A last-mile carbon number is a fuel total multiplied by a published factor, and the only activity record federal rules specify for a truck resolves that total to a tenth of an hour, a whole mile and a position written only at logged events, so the yearly figure can be sound while every per-stop and per-lane split inside it is a model."
date: 2026-11-06
slug: your-carbon-number-misses-six-minutes
meta_title: "Your Carbon Number Misses Six Minutes"
meta_description: "The federal record behind a carrier's carbon number is built to prove a driver's hours, and its resolution decides what a per-stop figure can actually mean."
---

<!-- lead -->

Your last-mile carbon figure sits on a federal driver log, and that log slices time into six-minute blocks because it was built to prove driver hours, not fuel burn [4]. A regional parcel carrier usually reports that figure in kilograms of carbon dioxide equivalent (CO2e) per parcel, and the record underneath is the electronic logging device (ELD) file the carrier already keeps [4]. Federal rules require one of these devices in any truck rated at 10,001 pounds or more [3]. The file records engine hours in tenths of an hour, miles in whole miles, and a position only when the device already has a log entry to write [1]. Your yearly number can be exactly right while every per-stop split inside it is a model.

<!-- tldr -->

## At a glance

- **The shift:** the federal record behind carrier carbon was built to prove hours, not to price fuel.
- **The number:** six minutes — the finest engine-on slice that record can express.
- **The risk:** any per-stop split finer than that slice is an estimate, not a record.

<!-- tension -->

## The file is built for hours

The rule that defines the device lists six inputs: engine power, vehicle motion, miles, engine hours, position and time [1]. It also fixes when each one is written. The device must be able to grab a position at least once every five miles of driving, but it writes the location only at events it already logs [1]. I keep circling that gap, because a device that can find a location far more often than it writes one never catches a delivery at a door.

The events are sparse by design. A fresh entry appears between required records when the truck is moving and nothing else has been logged in the previous hour [1]. The rest appear when something changes: a duty status (whether the driver is on duty or off duty), a login or logout, a fault, or the engine starting and stopping [1]. A delivery at a door is not one of those events, so it stays invisible unless it happens to land on the hourly entry.

Time and distance are coarse too. Engine hours arrive in tenths of an hour, and miles in whole miles [1]. Without a link to the engine control module (ECM) — the truck's engine computer — recorded miles only need to stay close to the odometer over a day [1]. Each position written places the truck within a short distance, and the rule accepts a fix that can be off by roughly a mile [1].

## By the numbers

- **0.5 mile — Position accuracy:** each recorded position places the truck within half a mile, and only at logged events [1].
- **10 percent — Odometer gap:** without an engine link, recorded miles only need to stay within 10 percent of the odometer over a day [1].
- **22.45 pounds — Carbon per gallon:** the factor a delivered fuel total meets, per gallon of distillate (diesel and similar fuels) [5].

The device exists for a reason that has nothing to do with carbon. The Federal Motor Carrier Safety Administration (FMCSA), the trucking safety agency, says the device syncs with the engine to record driving time automatically [4]. Hours are what the rule checks, so hours are what the file is built to capture. The record has to show when the truck moved and how long the driver was on duty, and it has to survive an audit. Carriers must keep it for six months [2].

There is also a line that decides whether the record has to exist at all. The rule calls any vehicle rated at or above 4,536 kilograms (10,001 pounds) a commercial motor vehicle [3]. Most parcel vans sit below that line, so the only federal vehicle-activity record does not cover the vans that run the final delivery leg. For those vans, the data feed is a contract term, and its detail is whatever the contract says.

<!-- tactical-insight -->

## What I'd watch

What I'm watching is the gap between what a contract can request and what the file already holds.

- **Engine-on seconds:** the time an engine ran at each stop, which no hourly entry can supply.
- **The fuel total:** gallons from the engine computer, kept beside the odometer's whole miles.
- **Monthly export:** a calendar year outlives the storage window, so operators keep a copy [2].
- **The van line:** the vans below the federal threshold, whose vehicle data feed is a negotiated term.

<!-- nuanced-takeaway -->

## The catch

My read is that the fault sits in the data contract, not in the log. The carrier is not hiding a number; the file answers a different question, and that question is whether the driver's day was legal. A carbon inventory asks where the fuel went; the same log can only say roughly when it burned.

Fleets that close this gap ask for the engine's own fuel total and the engine-on intervals, keep both beside the planned route, and let the method follow the data it has. When a per-parcel figure must be published, the workable path is to divide the engine's own fuel total by parcels and write the method in the note. Auditors will ask for that method anyway, so the note does double work. The money side of the same route has [a parallel measurement problem](/your-truck-mile-costs-2-2-driver-minutes/), and both clear up when the truck's own counters reach the file.

Two limits matter. Devices usually log more than the minimum, so a vendor can hand over minute-level data when the contract asks for it; the rule sets a floor, not a ceiling. The allowance for an unlinked odometer only matters where no engine link exists, so a properly wired truck has exact miles and only the stop-level split stays a model.

The practical version sits in one line in the next carrier review: a contract term for engine hours, fuel totals, and stop-level engine-on time as an export, not a dashboard screenshot. With those in hand, a carbon figure is a document about fuel again.

<!-- internal-links -->

## Sources

1. 49 CFR Part 395, Appendix A, ELD technical specification (eCFR, title 49 up to date as of 11/04/2026) — https://www.ecfr.gov/current/title-49/subtitle-B/chapter-III/subchapter-B/part-395
2. 49 CFR § 395.8, Driver's record of duty status (eCFR) — https://www.ecfr.gov/current/title-49/section-395.8
3. 49 CFR § 390.5, Commercial motor vehicle (Cornell Legal Information Institute e-CFR) — https://www.law.cornell.edu/cfr/text/49/390.5
4. Federal Motor Carrier Safety Administration, Electronic Logging Devices — https://www.fmcsa.dot.gov/hours-service/elds/electronic-logging-devices
5. U.S. Energy Information Administration, Carbon Dioxide Emissions Coefficients by Fuel (released 18 September 2024) — https://www.eia.gov/environment/emissions/co2_vol_mass.php

## Gate report

- lead — PASS — opens with one figure and the causal why, then expands CO2e and ELD in plain words.
- tldr — PASS — three-line At a glance under 50 words with shift, number, and risk.
- tension — PASS — explains the mechanism with a first-person cue, glosses duty status, ECM, and the vehicle threshold.
- tactical-insight — PASS — reports observations rather than commands, with scannable bullets and no unglossed jargon.
- nuanced-takeaway — PASS — closes on a contract decision, carries one internal link, and introduces no new concept.
