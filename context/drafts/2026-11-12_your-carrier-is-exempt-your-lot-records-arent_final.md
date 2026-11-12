---
title: "Your Carrier Owes Your Lot Nothing"
vertical: supply_chain
kind: evergreen
archetype: evergreen
evergreen: true
persona: ops_leader
one_big_thing: "The food traceability rule asks for one lot's records within 24 hours of a request, keeps them in scope for two years, and exempts the carrier that moved the load — so the compliance problem is the join between your receiving record and your shipment record, not the ping rate on the trailer."
date: 2026-11-12
slug: your-carrier-is-exempt-your-lot-records-arent
sources:
  - https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-1/subpart-S/section-1.1455
  - https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-1/subpart-S/section-1.1305
  - https://www.federalregister.gov/documents/2025/08/07/2025-14967/requirements-for-additional-traceability-records-for-certain-foods-compliance-date-extension
  - https://www.law.cornell.edu/cfr/text/21/1.1455
meta_title: "Your Carrier Owes Your Lot Nothing"
meta_description: "The traceability rule gives you 24 hours to produce one lot's records and keeps them for two years — while the carrier that hauled the load is exempt."
meta_description_source: "derived_from_lead"
---

<!-- lead -->

Twenty-four hours is the whole promise. On request, you produce the records for one lot of a listed food [1]. The trail runs from the dock that took the pallet to the truck that carried it away. The carrier that drove that truck owes nothing under the rule, because the traceability subpart exempts transporters of food outright [3]. The answer can only come from your own paperwork. The test is not how many location pings the trailer reports, but whether a receiving entry from twenty months ago can still name the lot you shipped.

<!-- tldr -->

## At a glance

- **The shift:** A record rule treated as a tracking project, when it is a filing one.
- **The number:** Twenty-four hours to produce a lot's records, held for two years.
- **The risk:** The lot code changes hands at every pack line, and the carrier keeps none of it.

<!-- tension -->

## The clock and the exemption

The rule lives in Subpart S of the Food and Drug Administration (FDA) rules on records for certain foods [1]. It was published in November 2022 with a compliance date of January 20, 2026. In August 2025 the agency proposed moving that date 30 months, to July 20, 2028, and the same document says the proposal does not amend the requirements [4]. That is the calendar; the substance has not moved since 2022.

Four duties, in order. First, a written traceability plan. Second, a lot code, assigned at the first critical tracking event for the food. Third, key data elements recorded at each of those events: the code, the quantity, the location, the date, and the party on either side of each handoff. Fourth, the records themselves, produced when the agency asks [1]. A critical tracking event is a defined point in the chain, covering harvest, cooling, initial packing, a change such as repacking or milling, and shipping or receiving.

Two sentences in the record section do most of the work. The first sets the retrieval rule: a request for official review gets the records within 24 hours [1]. It sits in the paragraph about having someone else keep them, which means a third party can hold the file while the clock stays yours. The second sentence sets the format. A routine request can be answered in whatever form you keep, and that includes original paper or a true copy, while an outbreak or emergency demands an electronic, sortable spreadsheet inside the same window [1]. Most vendors sell the second; most readers are held to the first.

Then the exemption that decides the design. The subpart does not apply to transporters of food [3]. A carrier's bill of lading was never going to be the record the rule wants. I read the record section and the exemption side by side, and they point in different directions: the one names a party the other has excused.

## By the numbers

- **24 hours to produce a lot's records:** The availability clock, unchanged when a third party stores the file [1].
- **Two years of retention:** How long each record stays in scope, counted from the day it was created or obtained [2].
- **$250,000 average food sales:** The ceiling under which a small retailer or restaurant sits outside the subpart [3].

<!-- tactical-insight -->

## What the drill finds

Pick one lot shipped fourteen months ago and try to produce its full record inside a working day. That is the test the rule sets, and it is not the test most systems are built for. A warehouse management system is organised by location and by order, while the rule is organised by lot. The code it wants is the one assigned at the first transformation, not the supplier's code printed on the pallet label.

The join is where it breaks. Your receiving entry names the supplier's lot, and your outbound shipment names the code your pack line assigned when it broke the pallet into cases. Between them sit the events the subpart cares about: a change happened, the quantity moved and so did the location. If that mapping lives in a spreadsheet on one planner's drive, the window is spent rebuilding it by hand.

The volume is worth sizing once. A distributor that brings in 40 lots a day of listed foods holds about 29,200 lot records inside the retention window, and any one of them has to be handed over on demand. That figure comes from a stated intake, not a published benchmark, and the reader's own lot count is the input.

What I keep coming back to is what the exemption implies about system design. A visibility platform that reads carrier scans will show where the pallet is, but it cannot tell an inspector which lot was in the trailer, because that fact was never the carrier's to hold. The record that answers the request is the one your receiving clerk signed, and the one your shipping clerk signed against it. That is also the retention problem this desk has already argued for exception logs, where the longest legal clock in a joined file sets the whole file's life ([the five-year exception record](/your-exception-log-owes-5-years/)).

<!-- nuanced-takeaway -->

## The catch

Two limits are worth stating plainly. The date may move again, and the 24 hours has an escape valve written into it: records are due within a day, or within a longer period the agency agrees to. A file that is complete but slow is a different failure from a file that is incomplete, and only the second one is a records problem.

The other limit is scope. The subpart reaches foods on a list the agency maintains and revises by notice, and a warehouse that never touches those foods is outside it entirely [1]. So the exposure is narrower than the word traceability suggests. For the distributor who does handle listed foods, the duty is a two-year file that resolves one lot in a day, with no carrier contribution to it. The part I find hard to settle is how many operations would pass that drill today, not because the data is missing but because the lot code stops at the pack line and the record of it was never joined to the shipment.

## Sources

- [1] U.S. Code of Federal Regulations, "21 CFR 1.1455 — How must records required by this subpart be maintained and made available?", eCFR title 21 current as of 11/09/2026 — https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-1/subpart-S/section-1.1455
- [2] U.S. Code of Federal Regulations, "21 CFR 1.1455(d) — Record retention", eCFR title 21 current as of 11/09/2026 — https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-1/subpart-S/section-1.1455
- [3] U.S. Code of Federal Regulations, "21 CFR 1.1305 — What foods and persons are exempt from this subpart?", eCFR title 21 current as of 11/09/2026 — https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-1/subpart-S/section-1.1305
- [4] Federal Register, "Requirements for Additional Traceability Records for Certain Foods: Compliance Date Extension" (proposed rule, 2025-14967), 7 August 2025 — https://www.federalregister.gov/documents/2025/08/07/2025-14967/requirements-for-additional-traceability-records-for-certain-foods-compliance-date-extension
- [5] Cornell Legal Information Institute, "21 CFR 1.1455" (second publication of the record-availability clock) — https://www.law.cornell.edu/cfr/text/21/1.1455
