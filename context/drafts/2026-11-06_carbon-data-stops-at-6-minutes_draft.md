---
title: "Carbon Data Stops at 6 Minutes"
vertical: last_mile_routing_fleet_carbon
kind: evergreen
archetype: evergreen
evergreen: true
persona: supply_chain_architect
one_big_thing: "A last-mile carbon number is a fuel total multiplied by a published factor, and the only activity record federal rules specify for a truck resolves that total to a tenth of an hour, a whole mile and a position written only at logged events, so the yearly figure can be sound while every per-stop and per-lane split inside it is a model."
date: 2026-11-06
slug: carbon-data-stops-at-6-minutes
meta_title: "Carbon Data Stops at 6 Minutes"
meta_description: "The federal record behind a carrier's carbon number is built to prove a driver's hours, and its resolution decides what a per-stop figure can actually mean."
---

<!-- lead -->

A regional parcel carrier sends its shipper a carbon figure in kilograms of CO2e per parcel. That number is only as good as the activity data under it, and the data is the electronic logging device (ELD) file the carrier already produces [4]. Federal rules require the device in any truck rated at 10,001 pounds or more [3]. What the file records, and how finely, is fixed by those rules: engine hours in tenths, miles in whole miles, a position written only when something happens [1]. Your carbon number can be exactly right for the year and six minutes coarse at the stop.

<!-- tldr -->

## At a glance

- **The shift:** the federal record behind carrier carbon was built to prove hours, not to price fuel.
- **The number:** six minutes — the finest engine-on slice that record can express.
- **The risk:** any per-stop split finer than that grain is an assumption wearing a figure.

<!-- tension -->

## The big picture:

The appendix that governs the device reads like an architecture document. It lists six inputs: engine power, vehicle motion, miles, engine hours, position and time [1]. It also says when each one is written. A position must be acquirable at least once every 5 miles of driving, yet the device writes location only at the events it already logs [1]. I keep coming back to that split, because a capability is not a record.

The events are sparse by design. A new intermediate log appears when the truck is moving and nothing else has been logged in the previous hour [1]. The rest arrive when something changes: a duty status, a login or logout, a fault, or the engine starting and stopping [1]. A delivery at a door is not one of those events. It stays invisible unless it lands on the hourly entry.

Time and distance carry their own grain. Engine hours are converted to tenths of an hour, and miles to whole miles [1]. With no link to the engine control module, the miles need only be accurate to within 10 percent of the odometer over a day [1]. The position value is accurate to half a mile, which the rule says leaves reporting accuracy near a mile [1].

## By the numbers

- **0.5 mile — Fix accuracy:** each recorded fix places the truck within half a mile, and only at logged events [1].
- **0.1 hour — Engine grain:** engine time arrives in tenths, which is six minutes, the smallest slice the file holds [1].
- **22.45 pounds — Carbon per gallon:** the factor a delivered fuel total meets, per gallon of distillate [5].

The device exists for a reason that has nothing to do with carbon. The safety agency calls it a unit that syncs with the engine to record driving time automatically [4]. Hours are what the rule polices, so hours are what the spec optimises. A record has to show when the truck moved, how long the driver was on duty, and that the paper trail survives an audit. Carriers must keep it for six months [2].

There is also a threshold that decides whether the record exists at all. A commercial motor vehicle is one rated at 4,536 kilograms, or 10,001 pounds, or more [3]. Most parcel vans are built under that line. The only activity record federal rules specify does not reach the vehicles that do the last mile. For those vans the feed is a buying term, and its detail is whatever the contract says.

<!-- tactical-insight -->

## What I'd watch:

What I'm watching is the gap between what a contract can request and what the file already holds.

- **Engine-on seconds:** the time an engine ran at each stop, which no hourly fix can supply.
- **The fuel total:** gallons from the engine control module, kept beside the odometer's whole miles.
- **Six-month memory:** a monthly export, because a calendar year outlives the window.
- **The 10,001-pound line:** the vans under it, whose telematics is a negotiated term.

<!-- nuanced-takeaway -->

## The catch

My read is that the fault sits in the data contract. The carrier is not hiding a number; the file answers a different question, and that question is whether the driver's day was legal. A carbon inventory asks where the fuel went. The same export can only say roughly when it burned.

The repair is not exotic. A fleet can request the engine total and the engine-on intervals, keep both beside the planned route, and let the method follow the data it has. Where a per-parcel figure must be published, divide the engine's own fuel total by parcels and write the method in the note. An auditor will ask for that method anyway. The money side of the same route has [a parallel measurement problem](/your-truck-mile-costs-2-2-driver-minutes/), and both clear up when the vehicle's own counters reach the file.

Two limits deserve air. Devices usually log more than the minimum, so a vendor can hand over minute-level data when the contract asks for it. The rule sets a floor, not a ceiling. The allowance for an unlinked odometer only matters where no engine link exists, so a properly wired truck has exact miles and only the split stays a model.

The practical version is one line in the next carrier review. What changes the number is engine hours, fuel and stop-level engine-on time as an export rather than a dashboard screenshot. With those in hand, a carbon figure is a document about fuel again.

<!-- internal-links -->

## Sources

1. 49 CFR Part 395, Appendix A, ELD technical specification (eCFR, title 49 up to date as of 11/04/2026) — https://www.ecfr.gov/current/title-49/subtitle-B/chapter-III/subchapter-B/part-395
2. 49 CFR § 395.8, Driver's record of duty status (eCFR) — https://www.ecfr.gov/current/title-49/section-395.8
3. 49 CFR § 390.5, Commercial motor vehicle (Cornell Legal Information Institute e-CFR) — https://www.law.cornell.edu/cfr/text/49/390.5
4. Federal Motor Carrier Safety Administration, Electronic Logging Devices — https://www.fmcsa.dot.gov/hours-service/elds/electronic-logging-devices
5. U.S. Energy Information Administration, Carbon Dioxide Emissions Coefficients by Fuel (released 18 September 2024) — https://www.eia.gov/environment/emissions/co2_vol_mass.php
