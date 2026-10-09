---
title: "A Late Container's Bill Carries Two 30-Day Clocks"
vertical: control_tower_exception_orchestration
persona: supply_chain_architect
one_big_thing: "A demurrage or detention charge is settled by records, not by argument: U.S. rule 46 CFR Part 541 gives the carrier 30 calendar days from the last-accrued charge to issue the invoice, gives the shipper 30 days to contest it, and voids the obligation entirely if the required information is missing — so the control tower's stored event timestamps, not its alerts, are what decide whether the bill stands."
date: 2026-10-06
slug: demurrage-invoice-30-day-clocks
archetype: evergreen
evergreen: true
meta_title: "A Late Container's Bill Carries Two 30-Day Clocks"
meta_title_source: "derived_from_title"
meta_description: "A late fee for a delayed shipping container — demurrage, in trade terms — now carries two strict 30-day clocks."
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/demurrage-invoice-30-day-clocks/featured.jpg"
image_style: "document_flatlay"
image_model: "flux"
image_alt: "The Demurrage 30-Day Clocks. The Demurrage 30-Day Clocks. The Demurrage 30-Day Clocks. The Demurrage 30-Day Clocks. The 30-Da"
image_caption: "The Demurrage 30-Day Clocks: Using exact timestamps to win container fee disputes."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
A late fee for a delayed shipping container — demurrage, in trade terms — now carries two strict 30-day clocks. The carrier or port operator must send the bill within 30 calendar days of the last charge. If they miss that window, the billed party pays nothing [1]. 

The shipper then gets 30 calendar days from the invoice date to fight the charge [1]. What settles the dispute is simple. It comes down to whether the invoice dates match the exact time logs your own control tower saved.

<!-- tension -->

## The big picture:

A control tower exists to answer one simple question: where is the box. But the U.S. billing rule asks four different questions: when free time started and ended, when the container became available, what rate applies, and whether the carrier caused the delay [1]. 

Those are logged events, not quick alerts. A tower that pings when a trailer sits too long is not enough on its own. It only helps if it saves those steps with exact time stamps.

Section 541.6 of the Code of Federal Regulations (CFR) lists every item a valid bill must show. It demands four ID items, eight timing items, three rate items, and two certifications [1]. The timing list asks for the invoice date, the due date, the allowed free days, the start and end of free time, the box availability date, the earliest return date, and the exact dates charged [1].

The certification is the sharpest edge. The billing party must state that its own work did not cause the extra fees [1]. Fighting that claim means proving no appointment was offered, the port was closed, or no truck frame showed up — and all of that proof lives in your saved event data.

What strikes me is how this changes the tower's job. In this specific workflow, the tracking layer is not just a nice dashboard. It becomes the trusted log that proves whether a bill stands.

## By the numbers

- **30 days — Bill window:** A carrier or terminal operator must send a demurrage or detention invoice within 30 calendar days of the last charge, or the billed party owes nothing [1].
- **30 days — Contest window:** The billed party gets at least 30 calendar days from the invoice date to ask for a refund, and the billing party must try to resolve it within 30 days [1].
- **8 fields — Timing data:** Section 541.6 requires eight exact dates, including the free-time start and end and the box availability date, along with three rate items and two certifications [1].
- **70% — Container space:** Carriers in the Digital Container Shipping Association (DCSA) represent 70% of the global container shipping market, and its Track & Trace standard sets the shared names for container events [6].

<!-- tactical-insight -->

## What I'd watch:

- **The final charge date:** The bill window runs from when the charge last hit, not from when the invoice was written [1]. A tower logging only the alert date misses the one fact that decides if you pay.
- **The free-time boundary:** Free time is set by the carrier's pricing list and the service contract. I'd want to know if teams check the invoice's free-time dates against their own gate-out logs, or just trust the invoice's own math [1].
- **The second statement:** Operators treat the two certifications as a simple checklist. The second one — claiming the carrier did not cause the delay — is the one an importer can actually fight using time stamps [1].
- **One shared model:** The DCSA standard names the events a carrier reports [6]. Matching these up is cheaper when the control tower keeps those standard names instead of making up its own.
- **The 30-day queue:** The contest window acts like a strict service rule. I am watching whether dispute teams have enough staff to clear tickets in time, since a late dispute means you pay.

<!-- nuanced-takeaway -->

## The catch:

The rule does not set prices. Free time, daily rates, and port schedules come from each carrier's pricing list and contract, and they change with proper notice [1]. It only limits when a bill goes out, what it must show, and how long a shipper has to contest it: effective May 28, 2024, it cut an industry standard of about 60 days to bill down to 30 [2][3].

Scope matters, too. This is strictly a U.S. ocean import rule. Air and road freight fall under much looser rules.

One part is also missing. A federal appeals court struck down section 541.4 — the part naming who gets the bill — on September 23, 2025, so the current rule leaves it blank [1][5]. That pushes the question of who pays back to contracts and past court cases.

My read: the honest limit is that none of this helps a system that stores quick pings instead of hard milestones. The rule hands you a shield you can only use if you kept the receipts.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Same-Day Delivery Race Is Undoing a Decade of Route Optimization" -> https://giniloh.com/same-day-race-undoes-route-optimization/ [same site (giniloh.com); same category; topical overlap: shipping] Link "Same-Day Delivery Race Is Undoing a Decade of Route Optimization" in the section where the article touches shipping. -->
<!-- internal-link hint: "Tariff Split in Two" -> https://giniloh.com/tariff-split-reshoring-heavy-half/ [same site (giniloh.com); same category; topical overlap: trade] Link "Tariff Split in Two" in the section where the article touches trade. -->
<!-- internal-link hint: "Washington Cuts the Tariff on the Goods. The Fee on the Ship Is…" -> https://giniloh.com/goods-tariff-relief-vs-vessel-fee/ [same site (giniloh.com); same category; topical overlap: trade] Link "Washington Cuts the Tariff on the Goods. The Fee on the Ship Is…" in the section where the article touches trade. -->
## Related reading

- [Same-Day Delivery Race Is Undoing a Decade of Route Optimization](https://giniloh.com/same-day-race-undoes-route-optimization/) — more on Supply Chain & Operations
- [Tariff Split in Two](https://giniloh.com/tariff-split-reshoring-heavy-half/) — more on Supply Chain & Operations
- [Washington Cuts the Tariff on the Goods. The Fee on the Ship Is…](https://giniloh.com/goods-tariff-relief-vs-vessel-fee/) — more on Supply Chain & Operations
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** U.S. rule 46 CFR Part 541 puts two strict 30-day clocks on a late container fee — the carrier must bill within 30 days of the last charge, and the shipper has 30 days to fight it — and voids the bill if required details are missing [1].
- **Why It Matters:** The invoice is a test of your records. The free-time dates, the box availability date, and the certification that the carrier did not cause the delay can only be answered from saved time stamps [1].
- **What I'd Watch:**
  - **The final charge date:** When the fee last hit sets the bill window, so a tower that logs only alerts misses the date that decides if you pay [1].
  - **The math check:** Whether the invoice's free-time dates match the gate-out and availability events the tower saved [1].
  - **One shared model:** The DCSA Track & Trace standard, used by carriers covering 70% of container space, names the events a tower must match against [6].
- **The Catch:** The rule sets the clock and the content, not the price. Free time and rates live in the contract, the scope is U.S. ocean imports, and section 541.4 was struck down in 2025 so "who gets billed" is back to case law [1][5].

## Sources
[1] Federal Maritime Commission — 46 CFR Part 541, "Demurrage and Detention" (§§ 541.5–541.8), current Code of Federal Regulations (CFR) text: https://www.ecfr.gov/current/title-46/chapter-IV/subchapter-B/part-541
[2] Federal Register — "Demurrage and Detention Billing Requirements," final rule, 89 FR 14330, published 2024-02-26: https://www.federalregister.gov/documents/2024/02/26/2024-02926/demurrage-and-detention-billing-requirements
[3] Federal Register — "Demurrage and Detention Billing Requirements," effective-date notice, published 2024-05-14: https://www.federalregister.gov/documents/2024/05/14/2024-10515/demurrage-and-detention-billing-requirements
[4] Federal Maritime Commission — "FMC Publishes Final Rule on Detention and Demurrage Billing Practices": https://www.fmc.gov/articles/fmc-publishes-final-rule-on-detention-and-demurrage-billing-practices
[5] Federal Maritime Commission — "U.S. Court of Appeals Issues Decision in Case on Demurrage and Detention Billing Practices": https://www.fmc.gov/articles/u-s-court-of-appeals-issues-decision-in-case-on-demurrage-and-detention-billing-practices
[6] Digital Container Shipping Association — "DCSA establishes Track and Trace standards for the global container shipping industry": https://dcsa.org/newsroom/dcsa-establishes-track-and-trace-standards-for-the-global-container-shipping-industry

<!-- linkedin -->
I keep coming back to one line in the U.S. late fee rule: if the invoice is late, you do not owe it.

A carrier or port operator must send a late bill within 30 calendar days of the date the charge last hit. After that, the rule says the billed party pays nothing. You then get 30 days from the invoice date to fight it.

What struck me is what the bill must show. Section 541.6 lists eight exact dates — the start and end of free time, the box availability date, the exact dates charged — plus the rate and two certifications. One certification claims the carrier's own work did not cause the delay.

That last part is the catch. You can only answer it with your own saved logs: when the box actually became ready, whether a time slot was offered, or whether a truck frame showed up.

My read: on this workflow, the control tower stops being a simple dashboard. It becomes the trusted log that proves whether the bill stands. A tower that stores quick alerts instead of exact time stamps has nothing to argue with.

I am curious how others handle it: do your teams check free time against your own gate logs, or do they just trust the invoice's math?

## Gate report
lead: PASS — Direct, punchy opening that delivers the core consequence of the 30-day billing clock immediately in simple terms.
tension: PASS — Explains the shift cleanly with short sentences (none exceeding the 3-sentence maximum) and includes a distinct first-person observer cue ("What strikes me..."). Replaced jargon with plain English.
tactical-insight: PASS — Uses observation-based bullet points ("I'd want to know", "I am watching") rather than playbook commands, properly formatted.
nuanced-takeaway: PASS — Clearly highlights the regulatory limits, correctly explains the 541.4 update plainly, and includes an explicit observer cue ("My read:").
tldr: PASS — Strictly adheres to the 4-part Smart Brevity summary schema without extra prose, using highly readable vocabulary.
