---
title: "Your Trailer's Last Foot Costs 2,500"
vertical: supply_chain
persona: ops_leader
kind: evergreen
archetype: evergreen
evergreen: true
one_big_thing: "A five-axle trailer loaded to exactly 80,000 pounds with 34,000 on each tandem can still be illegal: the Federal Highway Administration's own worked example fails at 68,000 pounds on the four-axle trailer bridge against a 65,500-pound limit because the first drive axle and the last trailer axle sit 35 feet apart instead of 36, so one foot of wheelbase is worth 2,500 pounds of freight."
date: 2026-11-05
slug: your-trailers-last-foot-costs-2500
meta_title: "Your Trailer's Last Foot Costs 2,500"
meta_title_source: "derived_from_title"
meta_description: "A trailer can hit 80,000 pounds legally on every axle and still fail the bridge formula, because the spacing between its axle groups decides the load."
meta_description_source: "derived_from_lead"
---

<!-- lead -->
A five-axle tractor-trailer crosses a scale at exactly 80,000 pounds, with 34,000 on the drive tandem and 34,000 on the trailer tandem. Read against the federal limits, that load is legal: the gross is at the cap and each tandem is at its ceiling [1][2]. The Federal Highway Administration (FHWA) publishes a worked example in which that same truck fails. Its four-axle trailer group carries 68,000 pounds against a 65,500-pound limit, because the first drive axle and the last trailer axle sit 35 feet apart instead of 36 [3]. Your trailer's last foot of wheelbase costs 2,500 pounds of freight.

<!-- tension -->

## The big picture:

**Three ceilings, and a remainder.** Federal law caps gross vehicle weight at 80,000 pounds, a tandem at 34,000 and a single axle at 20,000 [1][2]. A planner who checks those three numbers and finds them satisfied has not yet proved the load legal, though the arithmetic already shows the squeeze. Two tandems at their ceiling leave 12,000 pounds for the steering axle, and that figure is a remainder rather than a rule. Every trailer is also two capacities at once, a floor area and a legal weight, and the weight side is where [the same capacity arithmetic that sizes a pick face](/your-golden-zone-costs-10-miles/) meets a tape measure.

**The spacing test.** The fourth check is the bridge formula, and I have not seen a load plan that carries it. For any group of two or more consecutive axles it sets a ceiling from the number of axles and the distance between the outermost pair, then rounds the answer to the nearest 500 pounds [3]. Spread the same group over a longer span and it may carry more; pack it into a shorter one and the ceiling falls. The test applies to interior groups as well as to the whole truck, and FHWA names the critical combinations as axles one through three, one through five, and two through five [3]. The last of those is the trailer bridge. At 97 inches of spacing the bridge table allows 38,000 pounds on a pair, above the cap that governs spacing up to 96 inches [3].

**A truck that passes every check but one.** In FHWA's example the short group clears at 46,000 pounds against a 51,000 ceiling, and the full span clears at 80,000 against 80,000 [3]. The trailer bridge then breaks: 68,000 pounds against 65,500 at 35 feet. The agency's remedy is blunt, remove some load or increase the spacing. Federal law carries one narrow relief, under which two consecutive sets of tandem axles may each carry 34,000 pounds provided the first and last axle of the pair sit at least 36 feet apart [3]. Without that relief the formula allows only 66,000 to 67,500 pounds at 36 to 38 feet.

**Where the state sits.** A state may not enforce anything below these figures on the Interstate System, including when a portable scale reads against the carrier [4]. That makes the federal numbers a floor under enforcement as well as a ceiling on weight, which is why a ticket written slightly over the gross is an argument about method rather than a settled debt.

## By the numbers

- **4,000 pounds — The allowance:** five percent of a full legal load is the widest tolerance a portable scale may produce, and such scales are usually within 2 or 3 percent of true weight [2].
- **500 pounds per inch — The tire floor:** a state may not limit tire loading below 500 pounds per inch of tread width, and may not apply that limit to steering-axle tires [4].
- **38,000 pounds — Two axles, 97 inches:** at 97 inches of spacing the bridge table allows 38,000 on a pair, above the cap that governs spacing up to 96 inches [3].
- **1,000 pounds — The threshold that is not a tolerance:** a fine schedule with no penalty below a set figure counts as an unauthorized tolerance provision, whatever the figure [2].

<!-- tactical-insight -->

## What I'd watch:

- **Where the trailer tandems sit.** Sliding them forward shortens the trailer bridge and lowers what the group may carry; sliding them back raises it and takes weight off the drives. It is one setting per trailer, and it belongs on the routing sheet beside the pickup time.
- **The wheelbase on the spec sheet.** A shorter trailer bought for turning radius can put the first and last axle under the spacing a full load assumes, and nothing about the freight changes when that happens.
- **The scale's method.** A weight ticket rests on a portable scale's accuracy band, so the printout and the weighing method carry the argument, not the number alone.
- **The permit question.** Non-divisible loads can be permitted outside the axle and gross limits [2]. An oversize move should open with that question rather than with a heavier tractor.

<!-- nuanced-takeaway -->

## The catch

My read is that this is a records problem before it is a physics problem. The spacing lives on the trailer's specification and in the dispatch record, the weight lives on the invoice, and the two rarely meet in one field. A planner holding the tare, the axle ratings and the outer-bridge distance can compute the legal payload before anything is loaded.

Two limits apply to the arithmetic. The 12,000-pound steering figure assumes both tandems are full, and a real load almost never sits exactly there, because the distribution is the planner's choice. The examples above are the agency's, not a measurement of any reader's fleet, and the tare has to come from the reader's own registration.

The practical version is smaller than a compliance program. One distance, taken from the first drive axle to the last trailer axle, tells you whether a trailer may carry the 34,000 pounds on each tandem that a full load assumes. When it cannot, the plan is wrong before anyone argues about the rate.

<!-- tldr -->

## At a glance

- **The shift:** the binding limit on a loaded trailer is a spacing measurement, not the reading on the scale.
- **The number:** one foot between the drive and trailer tandems is worth 2,500 pounds of freight.
- **The risk:** a load that meets every quoted ceiling can still be over the bridge limit and turned back at the ramp.

<!-- internal-links -->

## Sources
[1] Cornell Law School Legal Information Institute — 23 U.S.C. § 127, "Vehicle weight limitations — Interstate System" — https://www.law.cornell.edu/uscode/text/23/127
[2] Cornell Law School Legal Information Institute — 23 CFR § 658.17, "Weight" — https://www.law.cornell.edu/cfr/text/23/658.17
[3] Federal Highway Administration — "Bridge Formula Weights," FHWA-HOP-19-028, August 2019 — https://ops.fhwa.dot.gov/freight/publications/brdg_frm_wghts/index.htm
[4] eCFR — 23 CFR Part 658, "Truck Size and Weight, Route Designations — Length, Width and Weight Limitations" (title 23 current as of 11/03/2026) — https://www.ecfr.gov/current/title-23/chapter-I/subchapter-G/part-658
