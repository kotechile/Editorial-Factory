---
title: "A Late Container's Bill Carries Two 30-Day Clocks"
vertical: control_tower_exception_orchestration
persona: supply_chain_architect
one_big_thing: "A demurrage or detention charge is settled by records, not by argument: U.S. rule 46 CFR Part 541 gives the carrier 30 calendar days from the last-accrued charge to issue the invoice, gives the shipper 30 days to contest it, and voids the obligation entirely if the required information is missing — so the control tower's stored event timestamps, not its alerts, are what decide whether the bill stands."
date: 2026-10-06
slug: demurrage-invoice-30-day-clocks
archetype: evergreen
evergreen: true
---

<!-- lead -->
A demurrage bill for a late container shows up weeks after the delay, and it now carries two 30-day clocks. A carrier or marine terminal operator has to issue that invoice within 30 calendar days of the date the charge was last incurred. Miss the window, and the billed party is not required to pay the charge at all [1].

The shipper then gets 30 calendar days from the invoice date to contest it [1]. What settles the fight is not the fight. It is whether the dates on the invoice match the events your own control tower recorded.

<!-- tension -->

## The big picture:

A control tower was built to answer one question: where is the box. The billing rule asks four different ones — when free time started and ended, when the container became available, what rate the tariff allows, and whether the carrier's own performance caused the delay [1].

Those are events, not alerts. A tower that pings when a trailer sits too long only holds the raw material for a dispute if it stored the milestones with timestamps and kept them.

The invoice is where that shows up. Section 541.6 lists every item a valid bill must carry: four identifying items, eight timing items, three rate items and two certifications [1]. The timing list is the one a visibility stack has to satisfy. It wants the invoice date, the due date, the allowed free time in days, the start and end of free time, the container availability date, the earliest return date, and the exact dates that were charged [1].

The certification is the sharper edge. The billing party must certify that its own performance did not cause or contribute to the charges [1]. Rebutting that means proving the appointment was never offered, the terminal was shut, or no chassis turned up. None of it lives on the invoice. All of it lives in event data.

What strikes me is that this reframes the tower's job. On this one workflow, the visibility layer is not a nicer dashboard. It is the system of record for whether a bill stands.

## By the numbers

- **30 days — Bill window:** A carrier or terminal operator must issue a demurrage or detention invoice within 30 calendar days of the last-accrued charge; later than that, the billed party is not required to pay [1].
- **30 days — Contest window:** The billed party gets at least 30 calendar days from the invoice date to ask for a refund or waiver, and the billing party must try to resolve it inside 30 days [1].
- **8 fields — Timing data:** Section 541.6 requires eight timing items, including the free-time start and end dates and the container availability date, alongside three rate items and two certifications [1].
- **70% — Container capacity on one model:** Carriers in the Digital Container Shipping Association (DCSA) represent 70% of the global container shipping market, and its Track & Trace standard fixes the shared milestone names and data interface for container events [6].

<!-- tactical-insight -->

## What I'd watch:

- **The accrual stop date:** The bill window runs from when the charge was last incurred, not from when the invoice was written [1]. A tower that only logs the alert date, and not the date the charge stopped accruing, is missing the one date that decides payability.
- **The free-time boundary:** Free time is set by the carrier's tariff and the service contract, not by the rule. I'd want to know whether operators check the invoice's free-time start and end against their own gate-out and availability events, or just against the invoice's internal arithmetic [1].
- **The second certification:** Operators are reading the two certifications as a checklist. The second one — that the carrier's performance did not contribute to the charges — is the one an importer can actually answer, and only with timestamps [1].
- **One milestone vocabulary:** DCSA's model, used by carriers covering 70% of container capacity, names the events a carrier reports [6]. Matching is cheaper when the tower keeps those names instead of inventing its own.
- **The 30-day queue:** The contest window behaves like a service-level commitment, not a reminder. I'm watching whether dispute queues are resourced to clear inside it, since a late dispute is a paid dispute.

<!-- nuanced-takeaway -->

## The catch:

The rule does not price anything. Free time, daily rates and terminal schedules come from each carrier's tariff and each contract, and they change on tariff notice [1]. The regulation only sets when a bill may be issued, what it must contain, and how long a shipper has to contest it.

Scope matters, too. This is a U.S. ocean-inbound rule. Air and road freight sit under thinner arrangements.

One section is also gone. The U.S. Court of Appeals for the D.C. Circuit set aside section 541.4 — the part naming who an invoice may be sent to — on September 23, 2025, and the current regulation carries it as reserved; the rest of the rule stands [1][5]. So "who may be billed" is back with the contracts and the case law, even while the timing and content rules hold.

My read: the honest limit is the one this beat keeps hitting. None of it helps a tower that stores pings instead of milestones. The rule hands you a weapon you can only use with a record.

<!-- tldr -->

## At a glance

- **The Big Shift:** U.S. rule 46 CFR Part 541 puts two 30-day clocks on a late container's demurrage or detention invoice — the carrier must bill within 30 days of the last-accrued charge, and the shipper has 30 days to contest — and removes the obligation to pay when the invoice is missing required information [1].
- **Why It Matters:** The invoice is a records test. The free-time dates, the container availability date and the certification that the carrier's own performance did not cause the delay can only be answered from event timestamps, which makes the control tower the system of record for the bill [1].
- **What I'd Watch:**
  - **The accrual stop date:** When the charge last accrued sets the bill window, so a tower that logs only alerts misses the date that decides payability [1].
  - **The reconciliation:** Whether the invoice's free-time start and end match the gate-out and availability events the tower recorded [1].
  - **One milestone model:** The DCSA Track & Trace standard, used by carriers covering 70% of container capacity, names the events a tower has to match against [6].
- **The Catch:** The rule sets the clock and the content, not the price — free time and rates live in the tariff and the contract, the scope is U.S. ocean inbound, and section 541.4 was set aside in 2025 so "who may be billed" is back to contracts and case law [1][5].

## Sources
[1] Federal Maritime Commission — 46 CFR Part 541, "Demurrage and Detention" (§§ 541.5–541.8), current Code of Federal Regulations (CFR) text: https://www.ecfr.gov/current/title-46/chapter-IV/subchapter-B/part-541
[2] Federal Register — "Demurrage and Detention Billing Requirements," final rule, 89 FR 14330, published 2024-02-26: https://www.federalregister.gov/documents/2024/02/26/2024-02926/demurrage-and-detention-billing-requirements
[3] Federal Register — "Demurrage and Detention Billing Requirements," effective-date notice, published 2024-05-14: https://www.federalregister.gov/documents/2024/05/14/2024-10515/demurrage-and-detention-billing-requirements
[4] Federal Maritime Commission — "FMC Publishes Final Rule on Detention and Demurrage Billing Practices": https://www.fmc.gov/articles/fmc-publishes-final-rule-on-detention-and-demurrage-billing-practices
[5] Federal Maritime Commission — "U.S. Court of Appeals Issues Decision in Case on Demurrage and Detention Billing Practices": https://www.fmc.gov/articles/u-s-court-of-appeals-issues-decision-in-case-on-demurrage-and-detention-billing-practices
[6] Digital Container Shipping Association — "DCSA establishes Track and Trace standards for the global container shipping industry": https://dcsa.org/newsroom/dcsa-establishes-track-and-trace-standards-for-the-global-container-shipping-industry

<!-- linkedin -->
I keep coming back to one line in the U.S. demurrage rule: if the invoice is late, you do not owe it.

A carrier or terminal operator has to issue a demurrage or detention bill within 30 calendar days of the date the charge was last incurred. After that, the rule says the billed party is not required to pay. You then get 30 days from the invoice date to contest it.

What stuck with me is what the invoice has to contain. Section 541.6 lists eight timing items — the start and end of free time, the container availability date, the exact dates charged — plus the rate, the tariff reference, and two certifications, one of which says the carrier's own performance did not cause the delay.

That last one is the interesting part. You can only answer it with your own event record: when the box actually became available, whether an appointment was offered, whether a chassis showed up.

My read: on this workflow the control tower stops being a nicer dashboard. It becomes the system of record for whether the bill stands. A tower that stores alerts instead of timestamped milestones has nothing to argue with.

Curious how others handle it: is free time something your team reconciles against your own gate and availability events, or does it get checked on the invoice's own arithmetic?

## Gate report
