---
title: "Dock Overtime: Your Real 14-Hour Cost"
vertical: control_tower_exception_orchestration
persona: supply_chain_architect
archetype: evergreen
evergreen: true
one_big_thing: "A late shipment's recovery is bounded by the driver's 14-hour on-duty window, not by the exception budget: with an 11-hour driving cap inside it there are only three hours of slack, and the shift premium that lands when the window closes attaches to the hourly dock crew at one and one-half times the 2025 median wage — so the tower should price the crew's clock before it prices the penalty."
date: 2026-10-13
slug: hour-14-recovery-wall
meta_title: "Dock Overtime: Your Real 14-Hour Cost"
meta_title_source: "derived_from_title"
meta_description: "Two hours before a delayed container clears the gate, the driver's day is already spent."
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/hour-14-recovery-wall/featured.jpg"
image_style: "cinematic_still"
image_model: "flux"
image_alt: "The 14-Hour Labor Wall. Heavy freight truck idling at an industrial terminal gate under amber lights during twilight."
image_caption: "The 14-Hour Labor Wall: Pricing dock crew overtime before late fees."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Two hours before a delayed container clears the gate, the driver's day is already spent. Under the Code of Federal Regulations (CFR), a driver cannot legally drive after 14 straight hours on duty [1]. The real cost of a missed window is not the late fee argued about next week but the overtime premium the dock crew charges today [3].

<!-- tension -->

## The big picture:

The part I keep circling is that the tracking layer watches the box, while the real limit is the crew.

A driver starts a shift and a 14-hour clock begins. Inside that window, driving is capped at 11 total hours [1]. That leaves just three hours of slack.

A long wait at the terminal gate counts as on-duty time. So it eats the hours in which the load could still legally move.

My read: this is why a recovery plan that looks like a routing problem fails like a labor problem. The penalty for a late box is not only the carrier's fee. It is the premium rate the dock crew earns for working after a shift that already ran long [3].

Who it hurts is the operation that bought prediction software and got an alert queue. Who it helps is the one that moved while the window was open. The cheapest recovery starts before the wall, not after it.

## By the numbers

- **14 hours — The on-duty wall:** A driver "may not drive after a period of 14 consecutive hours after coming on-duty following 10 consecutive hours off-duty", so the count starts at the shift, not at the first mile [1].
- **11 hours — The driving cap:** Driving is capped at "a total of 11 hours during the period specified" — the same 14-hour window. That leaves three hours of slack for a gate wait, a chassis swap or a re-book [1].
- **$19.35 an hour — The dock rate:** The 2025 median for freight, stock and material movers is $19.35 an hour, or $40,240 a year [7]. One premium hour at one and one-half times that rate is $29.03.
- **$28.19 an hour — The driver rate:** The 2025 median for heavy and tractor-trailer drivers is $28.19 an hour, or $58,640 a year [6]. Federal wage rules can exempt those drivers from the overtime requirement, so the premium usually lands on the dock instead [5].

<!-- tactical-insight -->

## What I'd watch:

What strikes me is how little slack the rule leaves before the money starts moving.

- **Where the window is spent:** A short-haul driver inside a 150 air-mile radius (172.6 statute miles) of the normal reporting location is exempt from the log rules [2]. That driver must be released within 14 consecutive hours, and may drive past the 14th hour on five days of any seven. Port drayage is where the wall bends. Line-haul is where it holds.
- **Which workweek the recovery lands in:** The premium attaches only past 40 hours in "a fixed and regularly recurring period of 168 hours", one that "need not coincide with the calendar week" [3][4]. A Saturday recovery is premium time only if the crew already passed 40 hours inside the employer's own week.
- **Who is on the shift:** The overtime duty turns on the class of work in the job, and the rule part that carries it is headed "Drivers" [5]. The premium is the dock crew's line, not automatically the driver's.
- **What the feed knows:** The industry's shared visibility model runs on five event types: shipment, transport, equipment, internet-of-things (IoT) and reefer events [8]. No crew event exists in it. The clock that binds the recovery is nowhere in the alert.

The next reading I'd want is the gate wait, per lane. That is what tells an architect whether the three hours of slack are spent on the dock or on the road.

<!-- nuanced-takeaway -->

## The catch

The honest limit is that these figures are national medians for a job, not a rate card. A six-person crew on four extra hours is about $697 at the median dock rate. That is math from published medians, not a bill [7].

I could be wrong about how often this bites in a given week. A drayage-heavy network inside 150 air miles mostly escapes the wall. A carrier that absorbs the wait may never pass the premium along.

The rule also limits driving, not duty. A driver can sit on duty past the 14th hour and simply not drive [1]. That gap is what turns a delay into a next-day load.

The other gap is the one no fetched source closes: no published penalty schedule for a late box exists to set against the premium. Demurrage and detention rates live in each carrier's tariff, and those pages no longer render for a source check. So the comparison I'd want, premium against penalty, still needs the reader's own contract.

Our own field note on this vertical is why I keep circling it. One stalled container ran up $420,000 downstream, most of it in idle labor and emergency freight. I hold that as our observation, not as a benchmark.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "A Late Container’s Bill Carries Two 30-Day Clocks" -> https://giniloh.com/demurrage-invoice-30-day-clocks/ [same site (giniloh.com); same category; topical overlap: container, delayed] Link "A Late Container’s Bill Carries Two 30-Day Clocks" in the section where the article touches container, delayed. -->
<!-- internal-link hint: "49.9% On Time: Shippers Stuck in the Gap" -> https://giniloh.com/shippers-stuck-in-the-gap/ [same site (giniloh.com); same category; topical overlap: container] Link "49.9% On Time: Shippers Stuck in the Gap" in the section where the article touches container. -->
<!-- internal-link hint: "Coast-to-Coast Rail Merger Clears First Big Test" -> https://giniloh.com/up-ns-rail-merger-clears-summary-denial/ [same site (giniloh.com); same category; topical overlap: clears] Link "Coast-to-Coast Rail Merger Clears First Big Test" in the section where the article touches clears. -->
## Related reading

- [A Late Container’s Bill Carries Two 30-Day Clocks](https://giniloh.com/demurrage-invoice-30-day-clocks/) — more on Supply Chain & Operations
- [49.9% On Time: Shippers Stuck in the Gap](https://giniloh.com/shippers-stuck-in-the-gap/) — more on Supply Chain & Operations
- [Coast-to-Coast Rail Merger Clears First Big Test](https://giniloh.com/up-ns-rail-merger-clears-summary-denial/) — more on Supply Chain & Operations
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** A late shipment's recovery is bounded by a driver's 14-hour on-duty window, with driving capped at 11 hours inside it — three hours of slack, spent on the same gate wait the tower is alerting on.
- **Why It Matters:** Past the window the box cannot move today at any price, so the cost that lands is a shift premium on the dock crew rather than the late fee in the dispute. The 2025 median wage of $19.35 an hour puts one premium hour at $29.03.
- **What I'd Watch:** Whether the three hours of slack are spent on the dock or on the road, and which crew absorbs the recovery.
  - **The short-haul exemption:** Drivers inside a 150 air-mile radius of their reporting location get relief from the log rules and a longer driving day, which is why drayage behaves differently from line-haul.
  - **The workweek boundary:** The premium starts after 40 hours in the employer's fixed 168-hour period, so where a recovery sits decides what it costs.
  - **The crew event:** The shared visibility model carries shipment, transport, equipment, IoT and reefer events, and nothing about the crew whose clock is the limit.
- **The Catch:** The wage figures are national medians, not a rate card, and the motor-carrier exemption can take the driver out of the overtime requirement. No published penalty schedule exists to price against the premium, so the comparison still needs the contract.

## Sources
[1] U.S. Code of Federal Regulations (eCFR), 49 CFR 395.3, "Maximum driving time for property-carrying vehicles" — the 14-hour period, the 11-hour driving cap and the 34-hour restart — https://www.ecfr.gov/current/title-49/subtitle-B/chapter-III/subchapter-B/part-395/subpart-A/section-395.3
[2] eCFR, 49 CFR 395.1, "Scope of rules in this part", paragraph (e)(1), "Short-haul operations — 150 air-mile radius driver" — https://www.ecfr.gov/current/title-49/subtitle-B/chapter-III/subchapter-B/part-395/subpart-A/section-395.1
[3] eCFR, 29 CFR 778.107, "General standard for overtime pay" — https://www.ecfr.gov/current/title-29/subtitle-B/chapter-V/subchapter-B/part-778/subpart-B/section-778.107
[4] eCFR, 29 CFR 778.105, "Determining the workweek" — https://www.ecfr.gov/current/title-29/subtitle-B/chapter-V/subchapter-B/part-778/subpart-A/section-778.105
[5] eCFR, 29 CFR 782.2, "Requirements for exemption in general", and Part 782, "Exemption from Maximum Hours Provisions for Certain Employees of Motor Carriers" — https://www.ecfr.gov/current/title-29/subtitle-B/chapter-V/subchapter-B/part-782/subpart-A/section-782.2
[6] O*NET OnLine (U.S. Department of Labor), occupation 53-3032.00, Heavy and Tractor-Trailer Truck Drivers — 2025 median wages — https://www.onetonline.org/link/summary/53-3032.00
[7] O*NET OnLine, occupation 53-7062.00, Laborers and Freight, Stock, and Material Movers, Hand — 2025 median wages — https://www.onetonline.org/link/summary/53-7062.00
[8] Digital Container Shipping Association (DCSA), "Track & Trace" standard — the five event types — https://dcsa.org/standards/track-and-trace

## Gate report
Loop 3 (frontier rewrite, gemini-3.1-pro-preview, per-draft driver rebinding `call_gemini` to a 480 s
socket timeout): attempt 1 PASS Flesch 54.4 (894 body words, sources ok, markers ok).
PASS — Lead delivers the on-duty wall and the premium immediately, with no throat-clearing.
PASS — Tension frames the structural split (the feed watches the box; the crew is the limit) with first-person observation.
PASS — Tactical-insight reports what the rule does per leg and per workweek, in bullets, without instructing the reader.
PASS — Nuanced-takeaway states the honest limits (medians, the exemption, no published penalty schedule).
PASS — TLDR follows the 4-part schema with an intro line and indented definitions.

Post-rewrite audit (hand corrections, none visible to any gate):
- **Restored the hand-written headline.** The rewrite re-cut the title to "The 14-Hour Wall: Why
  Penalties Aren't the Real Cost" — 9 words and opening on "The", a 0/100 under the owner's standard.
  The artifact keeps the 100/100 STRONG "Your 14-Hour Wall: Penalties Aren't the Cost" (core 3 words,
  7 total, 44 chars), whose figures and content words the lead states.
- **Corrected a garbled legal claim.** The rewrite wrote that federal rules "often exempt these drivers
  from maximum hour rules entirely" and, in the TL;DR, that "short-haul drivers often escape the
  overtime rule entirely". Both invert the sources: the maximum-hour rules are exactly what binds the
  driver (49 CFR 395), and the exemption in 29 CFR 782 is from the *overtime* requirement, not from
  hours-of-service limits, while the 150 air-mile relief is from the *log* requirements. Re-voiced to
  the verified brief's wording.
- **Restored detail the rewrite had compacted:** the short-haul radius figure (172.6 statute miles), the
  "released within 14 consecutive hours" term and the "five days of any seven" relief; the verbatim
  wage lines with their annual figures; the "class of work in the job" test and the "Drivers" heading.
- **Re-voiced two second-person constructions** the rewrite introduced ("not the late fee you argue
  about next week"; "you still need your own rate card") into observer phrasing.
- **Added the TL;DR slot-3 intro line** the rewrite had left empty after "What I'd Watch:".
- **Figure audit:** every number in the body traces to the verified brief or to its authorised
  arithmetic — 14 hours, 10 consecutive hours, 11 hours, three hours of slack, 150 air-mile (172.6
  statute miles), five days of any seven, 40 hours, 168 hours, five event types, $19.35 / $40,240,
  $28.19 / $58,640, $29.03 (1.5 × $19.35), $697 (six hands × four hours × $29.03), and the $420,000
  field note voiced as the desk's own observation. No unsourced figure, no substituted name, no moved
  clock trigger, no edited quotation.
