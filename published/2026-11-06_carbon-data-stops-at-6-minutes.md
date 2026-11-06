---
title: "Carbon Data Stops at 6 Minutes"
vertical: last_mile_routing_fleet_carbon
kind: evergreen
archetype: evergreen
evergreen: true
persona: supply_chain_architect
one_big_thing: "A last-mile carbon number is a fuel total multiplied by a published factor, and the only activity record federal rules specify for a truck resolves that total to a tenth of an hour (six minutes), a whole mile and a position written only at logged events, so the yearly figure can be sound while every stop-level and lane-level split inside it is a model."
date: 2026-11-06
slug: carbon-data-stops-at-6-minutes
meta_title: "Carbon Data Stops at 6 Minutes"
meta_description: "The federal record behind a carrier's carbon number is built to prove a driver's hours, and its six-minute resolution decides what a per-stop figure can mean."
image_path: "context/assets/illustrations/carbon-data-stops-at-6-minutes/featured.jpg"
image_style: "cinematic_still"
image_model: "flux"
image_alt: "Carbon Data Stops At 6 Minutes. Unbranded last-mile delivery truck with engine off, parked alone in a loading bay under a single amber"
image_caption: "Carbon Data Stops At 6 Minutes: The federal log behind a carrier's carbon number is built for hours, not per-stop fuel."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->

A last-mile carbon total rests on a federal driver log whose smallest time slice is six minutes [1]. That log exists to prove a driver's hours, not to price fuel [4]. The data underneath is the electronic logging device (ELD) file the carrier already keeps, and the figure arrives as kilograms of carbon dioxide equivalent (CO2e) per parcel. Federal rules require one of these devices in any truck rated at 10,001 pounds or more [3]. The file records engine hours in tenths of an hour and miles in whole miles, and it writes a position only when it already has a log entry to write [1]. Your carbon data stops at six minutes, so the yearly number can be exactly right while every stop-level cut inside it is a model.

<!-- tldr -->

## At a glance

- **The shift:** the federal log behind carrier carbon was built to prove hours, not to price fuel.
- **The number:** six minutes — the finest engine-on slice that log can express.
- **The risk:** any stop-level split finer than that slice is an estimate, not a record.

<!-- tension -->

## The file is built for hours

The rule appendix for the device lists six inputs: engine power, vehicle motion, miles, engine hours, position and time [1]. It also fixes when each one is written. The device must be able to grab a position once every five miles of driving. It writes the location only at events it already logs [1]. I keep circling that gap, because a device that can find a location more often than it writes one never catches a delivery at a door.

The events are sparse by design. A fresh entry appears when the truck is moving and nothing else has been logged in the previous hour [1]. The rest appear when something changes: a duty status, a login or logout, a fault, or the engine starting and stopping [1]. A delivery at a door is not one of those events. It stays invisible unless it lands on the hourly entry.

Time and distance are coarse too. Engine hours arrive in tenths, so a stop of four minutes sits below the grain [1]. The odometer is loose too. A missing engine link loosens that rule, which then lets recorded miles drift 10 percent across a day [1]. Each written position puts the truck within half a mile, and the rule accepts one that can be off by roughly a mile [1].

## By the numbers

- **0.1 hour — Engine grain:** engine time arrives in tenths, so six minutes is the smallest slice the file holds [1].
- **0.5 mile — Position accuracy:** each recorded position places the truck within half a mile, and only at logged events [1].
- **22.45 pounds — Carbon per gallon:** the factor a delivered fuel total meets, per gallon of distillate, which is diesel and similar fuel [5].

The device exists for a reason that has nothing to do with carbon. The Federal Motor Carrier Safety Administration (FMCSA) says the device syncs with the engine to record driving time automatically [4]. Hours are what the rule checks, so hours are what the file is built to capture. The record has to show when the truck moved and how long the driver was on duty. It also has to survive an audit, which is why carriers keep it for six months [2].

There is also a line that decides whether the record has to exist at all. The rule calls any vehicle rated at 4,536 kilograms (10,001 pounds) or more a commercial motor vehicle [3]. Most parcel vans sit below that line. The only federal vehicle-activity record does not cover the vans that run the final leg. For those vans the data feed is a contract term, and its detail is whatever the contract says.

<!-- tactical-insight -->

## What I'd watch

What I'm watching is the gap between what a contract can request and what the file already holds.

- **Engine-on seconds:** the time an engine ran at each stop, which no hourly entry can supply.
- **The fuel total:** gallons from the engine computer, kept beside the odometer's whole miles.
- **Six-month memory:** a monthly export, because a calendar year outlives the storage window [2].
- **The 10,001-pound line:** the vans under it, whose data feed the contract alone decides.

<!-- nuanced-takeaway -->

## The catch

What strikes me is that the fault sits in the data contract, not in the log. The carrier is not hiding a number. The file answers a different question, and that question is whether the driver's day was legal. A carbon inventory asks where the fuel went; the same log can only say roughly when it burned.

The fix is not complex. A fleet can ask for the engine's own fuel total and the engine-on intervals. Keep both beside the planned route, and let the method follow the data it has. When a per-parcel figure must be published, divide the engine's own fuel total by parcels and write the method in the note. Auditors will ask for that method anyway, so the note does double work. The money side of the same route has [a parallel measurement problem](/your-truck-mile-costs-2-2-driver-minutes/), and both clear up when the truck's own counters reach the file.

Two limits matter. Devices usually log more than the minimum, so a vendor can hand over minute-level data when the contract asks for it. The rule sets a floor, not a ceiling. The odometer allowance only matters where no engine link exists, so a properly wired truck has exact miles. Only the stop-level split stays a model.

The practical version is one line in the next carrier review. A contract that calls for engine hours, fuel totals and stop-level engine-on time as a data export turns a carbon figure back into a document about fuel.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Your Last-Mile Carbon Number Is a Rate Table" -> /last-mile-carbon-number-is-a-rate-table/ [same site (aichieve.net); same category; topical overlap: carbon, federal, last-mile] Link "Your Last-Mile Carbon Number Is a Rate Table" in the section where the article touches carbon, federal, last-mile. -->
<!-- internal-link hint: "Your 25-Minute Review Costs $66.67" -> /review-minute-costs-66-dollars/ [same site (aichieve.net); topical overlap: minutes, time, total] Link "Your 25-Minute Review Costs $66.67" in the section where the article touches minutes, time, total. -->
<!-- internal-link hint: "49.9% On Time: Shippers Stuck in the Gap" -> /shippers-stuck-in-the-gap/ [same site (aichieve.net); same category; topical overlap: time] Link "49.9% On Time: Shippers Stuck in the Gap" in the section where the article touches time. -->
## Related reading

- [Your Last-Mile Carbon Number Is a Rate Table](/last-mile-carbon-number-is-a-rate-table/) — more on Supply Chain & Operations
- [Your 25-Minute Review Costs $66.67](/review-minute-costs-66-dollars/)
- [49.9% On Time: Shippers Stuck in the Gap](/shippers-stuck-in-the-gap/) — more on Supply Chain & Operations
<!-- internal-links:end -->

## Sources

1. 49 CFR Part 395, Appendix A, ELD technical specification (eCFR, title 49 up to date as of 11/04/2026) — https://www.ecfr.gov/current/title-49/subtitle-B/chapter-III/subchapter-B/part-395
2. 49 CFR § 395.8, Driver's record of duty status (eCFR) — https://www.ecfr.gov/current/title-49/section-395.8
3. 49 CFR § 390.5, Commercial motor vehicle (Cornell Legal Information Institute e-CFR) — https://www.law.cornell.edu/cfr/text/49/390.5
4. Federal Motor Carrier Safety Administration, Electronic Logging Devices — https://www.fmcsa.dot.gov/hours-service/elds/electronic-logging-devices
5. U.S. Energy Information Administration, Carbon Dioxide Emissions Coefficients by Fuel (released 18 September 2024) — https://www.eia.gov/environment/emissions/co2_vol_mass.php
