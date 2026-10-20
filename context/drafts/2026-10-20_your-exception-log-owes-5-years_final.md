---
title: "Your Exception Log Owes 5 Years"
vertical: control_tower_exception_orchestration
persona: supply_chain_architect
one_big_thing: "The record a control tower writes when an exception fires is a joined file — a carrier scan, a temperature reading, the dock hours paid and the customs entry — so its retention is set by the longest legal clock among those inputs (five years from the date of entry for anything that backs an entry, twelve months past the end of the carrier agreement for a sanitary-transport temperature record, three years for payroll records, two years for time cards), which makes the retention parameter an architecture decision rather than a storage setting."
date: 2026-10-20
slug: your-exception-log-owes-5-years
archetype: evergreen
evergreen: true
image_path: "context/assets/illustrations/your-exception-log-owes-5-years/featured.jpg"
image_style: "document_flatlay"
image_model: "flux"
image_alt: "Exception Log Retention. An overhead flat-lay of overlapping institutional documents and carrier scans resting on a steel"
image_caption: "Exception Log Retention: Why joined records demand a five-year data hold."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
A customs record that backs an entry must be kept for five years [1]. Your control tower's exception log probably drops this data too early. When a system flags a late box, it writes a joined record: the scan, the temp reading, dock hours, and the customs entry.

Each part of that file has its own legal clock. Five years is the longest clock in that group, and it starts the day the entry is filed [1].

<!-- tension -->

## The big picture:

The tower's exception is a joined record. A joined record takes on the longest legal clock of its parts.

The customs clock comes first. Anything that backs a customs entry is kept for five years from the entry date [1]. A drawback claim runs longer. It expires on the third year after the day the claim is paid [1].

Temp files carry a different trap. Under the food-safety rule, a shipper keeps the temperature instructions and written agreements it gives its carriers for 12 months past the end of the carrier deal [2].

The clock starts when the contract stops, not when the box moves. A five-year deal keeps a year-one temp record alive for about six years [1, 2].

Work inputs run shorter. Payroll records need three years of holding time [3]. Time cards and wage rate tables need two years [4].

Tax files are the last piece. Freight bills back up tax write-offs. These need a three-year base hold, which jumps to six years if income left off the return tops 25 percent of the gross income shown on it [5].

My read: A single exception has a two-year floor and a six-year ceiling. The ceiling is always set by the input that lives longest.

## By the numbers

- **5 years — Customs clock:** A record kept under the customs rules "shall be kept for 5 years from the date of entry" or from the date of the activity [1].
- **12 months — Temp clock:** Food transport records are kept "for a period of 12 months beyond the termination of the agreements with the carriers" [2].
- **3 years vs 2 years — Wage clocks:** Employers "shall preserve for at least 3 years" their payroll records, while time cards and wage rate tables are held "for a period of at least 2 years" [3, 4].
- **25% — Tax clock trigger:** Records are kept six years when income left off the return is "more than 25% of the gross income shown on your return" [5].

<!-- tactical-insight -->

## What I'd watch:

The builders I watch are not fighting about storage costs. They are fighting about what the join touches.

- **The deal end date:** The temp clock counts from contract end. A tower storing only ship dates cannot figure out its own hold time [2].
- **Where the join happens:** A hot tier that clears data on a 90-day cycle wipes the linked file, not just the raw scan. The cheap build keeps the join and drops the raw stream behind it.
- **The longest input:** A file mixing a temp record with an entry record defaults to five years [1, 2]. Setting hold times per table creates dead links.
- **The drawback carve-out:** Claims records run three years from payment [1]. Any tower touching duty refunds holds a clock that no ship date can predict.
- **Platform defaults:** I rarely see a tracking tool put a hold default next to its coverage numbers.

I am watching if buyers start asking for that hold number during early vendor talks. I expect it will show up first in Requests for Proposal (RFPs) from importers who just lived through a records audit.

<!-- nuanced-takeaway -->

## The catch

The duty and the data sit in different places. The five-year customs rule binds the party forced to make and keep the record, which points back to who filed the entry [1].

A control tower often holds the data without carrying the legal burden. A customs broker might be the real recordkeeper. Still, auditors will ask the tower first because the events live there.

These federal clocks act as floors, not ceilings. A carrier contract, a state rule, or a legal hold can stretch any of them. None of that shows up in a basic storage plan.

The storage math is also a real limit. Five years of event data makes a huge number of rows, and fast temp readings make it worse.

I could be wrong about how many towers clear data at 90 days, since it is a private setting and not a public habit. But the hold time is set by the longest input in the join, and in an import file, that input reaches five years out [1].

<!-- tldr -->

## At a glance

- **The Big Shift:** A control tower's exception record is a joined file, so its hold time is set by the longest legal clock among its parts. In an import context, that clock is five years from the entry date.
- **Why It Matters:** A tower set up with a 90-day hot tier and a rolling clear policy wipes the linked file needed to settle a fee dispute or a customs records request.
- **What I'd Watch:** Which inputs the join touches, and whether the build keeps the link rather than the stream.
  - **Agreement end date:** The food transport clock runs 12 months past the end of the carrier deal, meaning a setup storing only ship dates fails to compute its own hold time.
  - **The join versus the stream:** Keeping the linked exception file and a daily roll-up costs far less than storing five years of raw events.
  - **Platform hold defaults:** The hold number a tracking vendor prints next to its coverage claim is a key security review metric.
- **The Catch:** The legal customs burden falls on whoever filed the entry, not strictly on the tower, and state rules or contracts can stretch every federal clock.

## Sources
[1] Cornell Law School, Legal Information Institute — 19 CFR § 163.4, Record retention period (U.S. Customs and Border Protection): https://www.law.cornell.edu/cfr/text/19/163.4
[2] U.S. Food and Drug Administration — 21 CFR § 1.912, record retention for shippers, receivers, loaders and carriers (Sanitary Transportation of Human and Animal Food), eCFR current text: https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-1/subpart-O/section-1.912
[3] U.S. Department of Labor, Wage and Hour Division — 29 CFR § 516.5, Records to be preserved 3 years: https://www.ecfr.gov/current/title-29/subtitle-B/chapter-V/subchapter-A/part-516/section-516.5
[4] U.S. Department of Labor, Wage and Hour Division — 29 CFR § 516.6, Records to be preserved 2 years: https://www.ecfr.gov/current/title-29/subtitle-B/chapter-V/subchapter-A/part-516/section-516.6
[5] Internal Revenue Service — How long should I keep records?: https://www.irs.gov/businesses/small-businesses-self-employed/how-long-should-i-keep-records

## Gate report
lead: PASS — Core five-year retention news delivered immediately in a 14-word opening sentence with zero throat-clearing.
tension: PASS — 'The big picture:' header used correctly; paragraphs kept to 1-3 sentences; simple vocabulary raises readability; 'By the numbers' contains 4 bolded stats with clear metric titles.
tactical-insight: PASS — 'What I'd watch:' header used; structures 5 key observations as bullet points; first-person cues included ("I am watching...", "I expect..."); jargon "DELETE" replaced with "clears".
nuanced-takeaway: PASS — 'The catch' header used correctly; clearly explains the limitation (duty vs. data holding) in short, readable sentences; first-person cue ("I could be wrong...") included.
tldr: PASS — 'At a glance' header used; strictly follows the 4-part Smart Brevity schema with indented sub-bullets under 'What I'd Watch'; plain-English summary without buzzwords.
