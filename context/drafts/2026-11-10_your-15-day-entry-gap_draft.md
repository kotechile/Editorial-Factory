---
title: "Your 15-Day Entry Gap: Then Custody"
vertical: control_tower_exception_orchestration
kind: evergreen
archetype: evergreen
evergreen: true
persona: supply_chain_architect
one_big_thing: "An import shipment runs on customs deadlines the control tower does not own — 24 hours before lading for the security filing, 15 calendar days after landing for the entry, six months to a general-order sale, one year to deemed liquidation and 180 days to protest — so the escalation rule has to be computed from the entry's own timestamps, not from the carrier milestone feed."
date: 2026-11-10
slug: your-15-day-entry-gap
---

<!-- lead -->
A container lands on a Tuesday and nobody files an entry, so 15 calendar days later the freight is general-order merchandise: in the port director's custody, at the consignee's risk and expense [3]. Six months after importation it can be sold [4]. No control tower raises that alarm, because the clock starts on landing while the tower's own event model starts on a carrier scan. The exception that costs the most in an import lane is not a late vessel, it is an entry gap nobody computed.

<!-- tldr -->

## At a glance

**The shift:** import exceptions become countdowns computed from the entry, not alerts raised from a scan.
**The number:** 15 calendar days from landing to file the entry.
**The risk:** a missed entry moves your freight into Customs custody at your expense.

<!-- tension -->

## Five clocks, five start events

One import box carries five deadlines, and each begins on a different event:

1. **Security filing, 24 hours before lading** — the importer's identifying data must reach Customs a day before the cargo loads onto the vessel at the foreign port [1].
2. **Entry, 15 calendar days after landing** — miss it and the goods become general-order merchandise, held in Customs custody at the consignee's risk and expense [2].
3. **General-order period, six months from importation** — that is the window before the freight is subject to sale [4].
4. **Liquidation, one year from entry** — if Customs does not fix the final duty in time, the entry is deemed liquidated at the rate the importer asserted, and no notice is required [5].
5. **Protest, 180 days after liquidation** — that is the only window in which the duty can be challenged [7].

An entry that is filed but incomplete, because the estimated duty was not paid, falls under the same custody rule [3]. Each clock starts on an event that lives outside a visibility platform. Lading happens at a foreign terminal in the carrier's own system. Landing is a Customs event, and a tower's "arrived" scan can come before or after it. The entry is a document a broker files, and liquidation is an accounting act inside Customs' system. A tower built on shipment milestones can be complete, current and blind to all five.

My read is that this is a data-model gap, not a notification gap. The countdown has to reference the broker's filing record, the landing event and the entry number, and those three identifiers usually sit in a different store from the container events. That is also why the deadline never turns up in a post-incident review: the alert that would have fired belongs to a system nobody joined to the tower.

The difference between a delay and a miss is worth stating plainly. A late vessel shifts a delivery date, and the freight arrives when it arrives. A missed entry stops being logistics at all, because the goods leave the commercial chain and sit in custody, accruing charges the consignee owes and cannot negotiate.

## By the numbers

- **180 days after liquidation:** the protest window, after which the entry's duty is final [7].
- **$25.13 an hour:** the median wage of the cargo and freight agent who re-checks a missing entry by hand [8].

<!-- tactical-insight -->

## What the entry lane needs

The architects I watch who get this right treat the entry as a first-class object rather than an attachment to a shipment. It carries its own identifiers, its own filer and its own status, and once it sits in the same store as the container events the countdown becomes a query instead of a project.

The second thing they do is split two jobs that look like one. A live alert exists to save the load, so it should fire on the fastest signal available. A compliance countdown exists to protect the company, so it should fire on the firmest record, the filed entry, even when that record lags the dock by hours. Wiring both to the same feed is how a tower ends up paging on a scan and missing a deadline.

The third is ownership of silence. A filing that was never made produces no event, so the rule has to be built on absence: no confirmation by a set number of hours before lading, no entry number by a set number of days after landing. Those rules sound trivial to write and are rarely written, because an event-driven platform is designed to react to things that happen.

<!-- nuanced-takeaway -->

## The catch

What I find hard to square is how little of this a platform purchase fixes. The clocks are public and the arithmetic is simple, but the hard part is contractual: the broker holds the filing data, the carrier holds the lading event, and Customs holds the liquidation, so the tower is only as good as three data-sharing agreements it does not control. An importer who cannot get the broker feed has bought a faster view of the wrong events.

There is a second limit, and it runs the other way. Customs can extend the one-year liquidation clock. It grants a year at a time, the extensions can total three years, and after four years the entry is deemed liquidated regardless [6]. A countdown presented as a single date will be wrong on the entries that matter most, which are the ones under review.

The record that settles an entry's deadlines is the same exception log the five-year retention rule covers, down to the entry the log backs ([Your exception log owes 5 years](/your-exception-log-owes-5-years/)). A deadline computed from an event nobody stored is a number with no evidence behind it.

## Sources

- [1] 19 CFR 149.2, Importer security filings — https://www.ecfr.gov/current/title-19/chapter-I/part-149/subpart-A/section-149.2
- [2] 19 CFR 142.2, Time for filing entry — https://www.ecfr.gov/current/title-19/chapter-I/part-142/subpart-A/section-142.2
- [3] 19 CFR 127.1, Merchandise considered general order merchandise — https://www.ecfr.gov/current/title-19/chapter-I/part-127/subpart-A/section-127.1
- [4] 19 CFR 127.4, General order period defined — https://www.ecfr.gov/current/title-19/chapter-I/part-127/subpart-A/section-127.4
- [5] 19 CFR 159.11, Entries liquidated by operation of law — https://www.ecfr.gov/current/title-19/chapter-I/part-159/subpart-B/section-159.11
- [6] 19 CFR 159.12, Extension of time for liquidation — https://www.ecfr.gov/current/title-19/chapter-I/part-159/subpart-B/section-159.12
- [7] 19 U.S.C. 1514, Protest of decisions of the Customs Service — https://www.law.cornell.edu/uscode/text/19/1514
- [8] O*NET OnLine, 43-5011.00 Cargo and Freight Agents (median wages, 2025) — https://www.onetonline.org/link/summary/43-5011.00
- [9] U.S. Customs and Border Protection, Importer Security Filing and Additional Carrier Requirements, final rule, 73 FR 66381 — https://www.federalregister.gov/documents/2008/11/25/E8-27048/importer-security-filing-and-additional-carrier-requirements
