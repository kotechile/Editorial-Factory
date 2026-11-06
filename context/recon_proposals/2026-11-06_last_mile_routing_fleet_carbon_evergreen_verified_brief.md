# Verified Brief: last_mile_routing_fleet_carbon — 2026-11-06

Topic: what the electronic logging device (ELD) record actually resolves, and what a last-mile carbon
number can be allocated to once its fuel total is multiplied by a published factor.
Companion to `2026-11-06_last_mile_routing_fleet_carbon_evergreen_brief.md` (gate: PASS, 5 rows,
3 hosts).

Regulatory text is read from 49 CFR Part 395 Appendix A on the eCFR (title 49 "up to date as of
11/04/2026", last amended 10/28/2026). Appendix A is only published inside the part page, so rows 1
and 2 cite that page; the retention row cites the per-section page because its evidence window lands
on the operative sentence there.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| 1 | Position accuracy | CMV position measurement must be accurate to 0.5 mile of absolute position | VERIFIED | https://www.ecfr.gov/current/title-49/subtitle-B/chapter-III/subchapter-B/part-395 | "CMV position measurement must be accurate to ±0.5 mile of absolute position of the CMV when an ELD measures a valid latitude/longitude coordinate value." (App. A § 4.3.1.6(c)) |
| 2 | Position sampling | A valid position must be acquired at least once every 5 miles of driving, but location is only written at ELD events | VERIFIED | same part page | "An ELD must be able to acquire a valid position measurement at least once every 5 miles of driving; however, the ELD records CMV location information only during ELD events as specified in section 4.5.1 of this appendix." (§ 4.3.1.6(g)) |
| 3 | Position accuracy, as reported | Reporting accuracy of a fix is on the order of 1 mile | VERIFIED | same part page | "Measurement accuracy combined with the reporting precision requirement implies that position reporting accuracy will be on the order of ±1mile of absolute position of the CMV during the course of a CMV's commercial operation." (§ 4.3.1.6(e)) |
| 4 | Position failure | 60 cumulative minutes without a fix in a 24-hour period sets a positioning malfunction | VERIFIED | same part page | "When such elapsed time exceeds a cumulative 60 minutes over a 24 hour period, the ELD must set and record a positioning compliance malfunction." (§ 4.3.1.6(c)) |
| 5 | Event cadence | While in motion, an intermediate log is recorded if no duty-status or intermediate log event occurred in the previous hour | VERIFIED | same part page | "When a CMV is in motion, as described in section 4.3.1.2 of this appendix, and there has not been a duty status change event or another intermediate log event recorded in the previous 1-hour period, the ELD must record a new intermediate log event." (§ 4.5.1.2(a)) |
| 6 | Engine hours | Engine hours are carried in tenths of an hour, accurate within 0.1 hour | VERIFIED | same part page | "Engine hours must use or must be converted to hours in intervals of a tenth of an hour." (§ 4.3.1.4(a)); "must be accurate within ±0.1 hour of the engine's total operation within a given ignition power on cycle." (§ 4.3.1.4(b)) |
| 7 | Miles | Vehicle miles are whole miles, and without an engine link the odometer need only be within 10% over 24 hours | VERIFIED | same part page | "Vehicle miles information must use or must be converted to units of whole miles." (§ 4.3.1.3(a)); "the accumulated vehicle miles indication must be obtained or estimated from a source that is accurate to within ±10% of miles accumulated by the CMV over a 24-hour period as indicated on the vehicle's odometer display." (§ 4.3.1.3(c)) |
| 8 | Engine events | The device must be functional within a minute of engine power and records power-up/shutdown within a minute | VERIFIED | same part page | "An ELD must be powered and become fully functional within 1 minute of the vehicle's engine receiving power" (§ 4.3.1.1); "an ELD must record the event within 1 minute of occurrence" (§ 4.5.1.6(a)) |
| 9 | Retention | Records of duty status and supporting documents are kept six months | VERIFIED | https://www.ecfr.gov/current/title-49/section-395.8 | "A motor carrier shall retain records of duty status and supporting documents required under this part for each of its drivers for a period of not less than 6 months from the date of receipt." (§ 395.8(k)(1)); "The driver shall retain a copy of each record of duty status for the previous 7 consecutive days" (§ 395.8(k)(2)) |
| 10 | Coverage | A commercial motor vehicle is one rated at 10,001 pounds or more | VERIFIED | https://www.law.cornell.edu/cfr/text/49/390.5 | "Has a gross vehicle weight rating or gross combination weight rating, or gross vehicle weight or gross combination weight, of 4,536 kg (10,001 pounds) or more, whichever is greater" (§ 390.5) |
| 11 | Coverage, applied | A van rated below 10,001 pounds is outside Part 395, so its telematics is voluntary | FLAGGED | same Cornell page plus § 395.1 | The 10,001-pound definition is verbatim above. The *application* is an inference: Part 395 governs drivers of commercial motor vehicles required to keep a record of duty status, so a lighter van falls outside it in interstate operation. The article states the threshold and the consequence in one sentence and does not claim anything about intrastate rules, which vary by state. |
| 12 | The device's purpose | The ELD exists to record driving time automatically | VERIFIED | https://www.fmcsa.dot.gov/hours-service/elds/electronic-logging-devices | "An ELD synchronizes with a vehicle engine to automatically record driving time, for easier, more accurate hours of service (HOS) recording." (Federal Motor Carrier Safety Administration, page last updated 2 October 2023) |
| 13 | Carbon factor | A gallon of distillate fuel oil carries 22.45 pounds of CO2 | VERIFIED | https://www.eia.gov/environment/emissions/co2_vol_mass.php | "Diesel and Home Heating Fuel (Distillate Fuel Oil) 22.45 gallon 10.19 gallon 163.45 74.14" — pounds CO2 per gallon 22.45, kilograms per gallon 10.19, pounds per million Btu 163.45 (U.S. Energy Information Administration, release date 18 September 2024) |

## Derived arithmetic (not a source claim — the drafter must show the inputs)

1. **Position fixes per route.** At one intermediate log per hour of motion and location written only
   at events, a route with about four hours of driving carries roughly four hourly logs plus the
   duty-status and engine events at each end — on the order of six to nine location records. Split
   across 120 stops, that is 13 to 20 stops per fix. The spec allows the device to *acquire* a fix
   every 5 miles (12 for a 60-mile route), but acquisition is not recording.
2. **Time resolution.** A tenth of an hour is six minutes, so the finest engine-on interval the file
   expresses is six minutes; a three-minute dwell at a door is below it.
3. **Distance resolution.** Miles are whole miles and the position is accurate to half a mile, so
   stop-level distance attribution is a modelling choice, not a reading.

## Drafter rules

- Do not say the ELD "measures" or "reports" fuel. It records miles, engine hours, position and
  duty status; fuel comes from the engine control module (ECM) or from fuel-card purchases.
- Say "at ELD events" when describing when location is written, and keep the 5-mile figure for what
  the device must be *capable* of — the two numbers answer different questions.
- A vendor may log finer data than the minimum; the article can say so, because the minimum is what a
  carrier must be able to produce, not the most a device does.
- The three derived figures above are arithmetic: show 4 driving hours and 120 stops, or drop them.
- Every quotation below is verbatim from the table; if a rewrite needs a shorter phrasing, paraphrase
  without quotation marks rather than clipping a quote.
