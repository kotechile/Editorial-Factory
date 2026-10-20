---
title: "Your Exception Log Owes 5 Years"
vertical: control_tower_exception_orchestration
persona: supply_chain_architect
one_big_thing: "The record a control tower writes when an exception fires is a joined file — a carrier scan, a temperature reading, the dock hours paid and the customs entry — so its retention is set by the longest legal clock among those inputs (five years from the date of entry for anything that backs an entry, twelve months past the end of the carrier agreement for a sanitary-transport temperature record, three years for payroll records, two years for time cards), which makes the retention parameter an architecture decision rather than a storage setting."
date: 2026-10-20
slug: your-exception-log-owes-5-years
archetype: evergreen
evergreen: true
---

<!-- lead -->
A customs record that backs an entry has to be kept for five years from the date of entry [1]. Your exception log probably keeps the event behind it for a quarter of that. Every time a tower flags a late box, it writes four records at once: the carrier's scan, the temperature reading, the dock hours that were paid, and the customs entry the freight was declared on. Each one carries its own legal clock. Five years is the longest clock in that set, and it starts the day the entry is filed [1].

<!-- tension -->

## The big picture:

The tower's exception is not one record. It is a joined record, and a joined record inherits the longest clock of its parts.

The customs clock comes first. Anything a shipper has to keep under the customs recordkeeping rule is kept for five years from the date of entry, or five years from whatever activity created it [1]. A drawback claim is the odd one out here. Its record runs to the third anniversary of the day the claim was paid, so the clock starts at payment and not at entry [1].

Then the temperature file. Under the food-safety rule for sanitary transport, the specifications and operating temperatures a shipper gives its carriers are kept for 12 months beyond the end of the agreements with those carriers [2]. I keep coming back to that wording, because "beyond the end" is doing a lot of work.

The clock does not start when the box moves. It starts when the contract stops. A five-year carrier agreement therefore keeps a temperature record from year one alive for about six years, which is longer than the customs clock sitting beside it in the same file [1, 2].

The labour inputs are shorter, and they differ from each other. Payroll records are preserved for at least three years [3]. Time cards, wage rate tables and work schedules are preserved for at least two [4]. Both clocks are shorter than customs, so on their own they would never bind. They bind the moment an exception file includes them, because the file is kept as one thing.

The tax file is the last input, and it is the one most towers never think about. Freight invoices support a deduction. The base period for keeping records behind a tax return is three years, and it rises to six years when unreported income tops 25 percent of the gross income on the return [5].

So the honest range on a single exception is two years at the floor and six years at the ceiling, and the ceiling is set by whichever input lives longest.

## By the numbers

- **5 years — Customs clock:** A record kept under the customs rules "shall be kept for 5 years from the date of entry, if the record relates to an entry, or 5 years from the date of the activity which required creation of the record" [1].
- **12 months — Temperature clock:** Sanitary-transport records are kept "for a period of 12 months beyond the termination of the agreements with the carriers", so the agreement's end date, not the shipment date, starts the clock [2].
- **3 years vs 2 years — Wage clocks:** Employers "shall preserve for at least 3 years" their payroll records, while time cards and rate tables are held "for a period of at least 2 years" [3, 4].
- **25% — Tax clock trigger:** Records are kept six years when unreported income is "more than 25% of the gross income shown on your return", against a three-year base period [5].

<!-- tactical-insight -->

## What I'd watch:

The architects I watch are not arguing about storage price. They are arguing about what the join is allowed to touch.

- **The agreement end date in the schema.** The temperature clock is measured from contract termination, so a tower that stores only shipment dates cannot compute it at all. Whoever holds the carrier contract's end date holds the retention answer [2].
- **Where the join happens.** A hot tier that keeps 90 days and then deletes on roll deletes the linked file, not just the raw scan. The cheap design keeps the join and drops the stream behind it, which is the opposite of what most object-storage policies do.
- **The longest input, not the average.** A file that mixes a temperature record with an entry record has one retention answer, and it is five years [1, 2]. Setting it per table is how a team ends up with an orphaned join.
- **The drawback carve-out.** Claims records run from payment to the third anniversary [1]. Any tower that also touches duty recovery is holding a clock that no shipment date predicts.
- **What the platforms publish.** I have not seen a visibility platform put a retention default next to its coverage numbers. That is the question I would want answered in a security review, because the coverage claim is about the present and the retention number is about the audit three years out.

I'm watching whether buyers start asking for that number in the same conversation where they ask about carrier count. My read is that it will show up first in the RFPs from importers who have already been through one records request.

<!-- nuanced-takeaway -->

## The catch

The duty and the data sit in different places, and I want to be careful about that. The five-year customs obligation attaches to the party required to make and keep the record, which is tied to who filed the entry [1]. A tower often holds the data without carrying the obligation, and a broker may be the recordkeeper of the entry itself. The tower is still the place an auditor asks first, because it is where the events live.

These are federal clocks, and they are floors rather than ceilings. A carrier contract, a state rule or a litigation hold can extend any of them, and none of that shows up in a storage policy.

The storage arithmetic is also real in a way this piece underplays. Five years of event-level telemetry is a lot of rows, and temperature data at sub-minute resolution is worse. The affordable version keeps the linked exception file and a daily roll-up, not the raw stream, which is a design decision someone has to defend to a security reviewer.

I could be wrong about how many towers prune at 90 days. I have not surveyed them, and it is a configuration, not a published habit. What I am confident about is narrower and more useful: the retention number is set by the longest input in the join, and in an import file that input is five years out [1].

<!-- tldr -->

## At a glance

- **The Big Shift:** A control tower's exception record is a joined file, not a single event. Its retention is therefore set by the longest legal clock among its inputs, and in an import context that clock is five years from the date of entry.
- **Why It Matters:** A tower configured with a 90-day hot tier and a delete-on-roll policy destroys the linked file that settles a chargeback, a demurrage dispute or a customs records request, and the loss only shows up when someone asks for the evidence.
- **What I'd Watch:** Which inputs the join touches, and whether the design keeps the link rather than the stream.
  - **Agreement end date:** The sanitary-transport clock runs 12 months past the end of the carrier agreement, so a schema that stores only shipment dates cannot compute its own retention.
  - **The join versus the stream:** Keeping the linked exception file and a daily roll-up costs far less than five years of raw telemetry, and it survives an audit.
  - **Platform retention defaults:** The number a visibility vendor publishes beside its coverage claim, which is the first thing I would ask for in a security review.
- **The Catch:** The customs obligation attaches to whoever filed the entry, not automatically to the tower; state rules and contracts can extend every clock; and the honest floor for an exception file is still a real storage bill.

## Sources
[1] Cornell Law School, Legal Information Institute — 19 CFR § 163.4, Record retention period (U.S. Customs and Border Protection): https://www.law.cornell.edu/cfr/text/19/163.4
[2] U.S. Food and Drug Administration — 21 CFR § 1.912, record retention for shippers, receivers, loaders and carriers (Sanitary Transportation of Human and Animal Food), eCFR current text: https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-1/subpart-O/section-1.912
[3] U.S. Department of Labor, Wage and Hour Division — 29 CFR § 516.5, Records to be preserved 3 years: https://www.ecfr.gov/current/title-29/subtitle-B/chapter-V/subchapter-A/part-516/section-516.5
[4] U.S. Department of Labor, Wage and Hour Division — 29 CFR § 516.6, Records to be preserved 2 years: https://www.ecfr.gov/current/title-29/subtitle-B/chapter-V/subchapter-A/part-516/section-516.6
[5] Internal Revenue Service — How long should I keep records?: https://www.irs.gov/businesses/small-businesses-self-employed/how-long-should-i-keep-records
