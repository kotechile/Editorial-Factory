---
title: "Your Pager Caps at 2 Incidents a Shift"
vertical: enterprise_tech_leadership
kind: evergreen
archetype: evergreen
persona: eng_leader
one_big_thing: "A 24/7 rotation is a fixed machine: two always-staffed seats and week-long shifts put a single-site rotation at eight engineers, and two incidents per 12-hour shift — about six engineer-hours and $392 each — is the page budget that decides how many services that team can own."
date: 2026-11-10
slug: your-pager-caps-at-2-incidents
meta_title: "Your Pager Caps at 2 Incidents a Shift"
meta_description: "Two incidents per 12-hour shift is the published ceiling for on-call, and at six engineer-hours each it decides how many services one team can own."
---

<!-- lead -->

Two incidents per 12-hour shift. That is the ceiling Google publishes for its on-call engineers, and it settles more about your architecture than most design reviews get to. The company's own average for one incident — root cause, remediation, postmortem, the bugs that follow — is six hours [1]. Two of those fill a shift. So the number is a budget, and every service you wire to a pager draws on it.

<!-- tldr -->

## At a glance

- **The shift:** the pager, not the cloud bill, caps how many services one team can own.
- **The number:** two incidents per 12-hour shift, about six engineer-hours each [1][2].
- **The risk:** a team carrying 48 services is already near 86% of its weekly page budget.

<!-- tension -->

## The rotation comes before the architecture

Start with the machine that answers the pages, because its size is published arithmetic rather than a matter of taste. Google keeps two people on call at all times, a primary and a secondary, and caps on-call time at 25% of an engineer's working life; at least 50% must go to engineering work [1]. With week-long shifts, each engineer carries one week in four. Two seats, one week in four, and the minimum single-site rotation lands at eight engineers. A dual-site team needs six per site to honour the same rule [1].

That is where the money and the headcount meet. Eight engineers at the national median software-developer wage of $135,980 is $1,087,840 of payroll to keep one rotation staffed [4]. Nobody signs that number off as an on-call cost, because it is buried inside a hiring plan.

The page budget is the other half. Two incidents per 12-hour shift, two shifts a day, is four incidents a day, 28 a week, 1,456 a year [1]. At six hours each, the ceiling is 168 engineer-hours a week — 4.2 full-time equivalents, or 52.5% of an eight-person team's 320-hour week [1][4]. I read that line three times before I believed it: a rotation running at its permitted page ceiling spends half its capacity on incidents. That is exactly the operational cap the same chapter sets from the other direction. The ceiling is not a comfortable margin. It is the line where the team stops having time to fix the thing that is paging them.

Google is blunt about what a bad distribution looks like: the median pages per day should be 0, and a component that pages every day is a signal that something else will break and push the count past what is permitted [1]. The workbook repeats the point from the other side, treating every new paging alert as a cost that has to be argued for, and defends a 12-hour shift on the grounds that 12 hours overnight beats 24 [2].

The field version of this is not exotic. A 25-engineer organisation this desk has covered was carrying 48 services across three clusters. Give each of those services one page a fortnight — a modest, healthy rate — and the team is at 24 incidents a week, 86% of the budget, before anything breaks badly. At six hours an incident that is 144 engineer-hours a week, or 3.6 people permanently on incident work [1][4].

## By the numbers

- **$392.28 per incident:** six engineer-hours at the $65.38 median hourly wage for software developers [1][4].
- **$571,160 a year:** incident work at the full 28-a-week ceiling, against $1,087,840 of payroll for the eight engineers who carry the rotation [1][4].
- **8 engineers:** the single-site floor that the 25% on-call cap and week-long shifts produce, with 6 per site for a dual-site team [1].

<!-- tactical-insight -->

## What I would do on Monday

Pull the last 90 days of pages and group alerts that share a root cause. That group count is your incident count, and it is almost always smaller than the alert count and larger than the number in the retro documents. Divide by 28. The result is how much of the budget you are already spending, and it is the first honest number most teams have seen about their pager.

Then decide in that order: reduce the pages, then resize the rotation, then change the shift pattern. Reducing pages is the only lever that buys back capacity in the same quarter. A component that pages daily is not an incident source, it is a defect with a notification attached [1]. Retire the alert, or fix the thing behind it, and the budget moves the same day.

On sizing, the rule is a division rather than a belief. If the team cannot put two always-staffed seats on a rotation with one week in four, it does not have a 24/7 service; it has a service with a best-effort pager and a business-hours promise. Say so in the service-level objective (SLO) rather than in the exit interview. Twelve-hour shifts let a team with sites in different places avoid overnight entirely, and the escalation window itself is a configured parameter — the paging vendor's own guidance is a five-minute timeout on the first escalation, which is the interval to tune before you tune anything else [2][3].

For a new service, ask for its expected pages per week before it gets a pager, and write the number down. A service that cannot estimate its pages has not thought about its failure modes, and a service that knows the number has just made the admission decision for you.

<!-- nuanced-takeaway -->

## The catch

Every figure here comes from one operator's published practice, and that operator is Google: multiple sites, dedicated site reliability engineering (SRE) teams, and an incident average of six hours that reflects a class of system most readers do not run. A 40-minute incident average stretches the same 12-hour shift much further; an incident that ties up a whole day cuts the shift's budget to one. My reading is that the eight-engineer floor matters more than the six-hour average, because the floor is structural and the average is yours to measure.

The eight engineers is not a law either. It falls out of two parameters — two seats and one week in four — so changing the shift length changes the floor. A 12-hour shift pattern, a compensated on-call allowance, or a follow-the-sun partner arrangement all move the arithmetic, and none of them removes the need to staff two seats.

The wage is the softer number. O*NET's $135,980 is a national median across software developers, and a senior platform engineer costs more than that, so the dollar figure understates the real bill while the engineer-hours hold.

What survives all three caveats is the shape: a fixed budget of attention, divided among the things allowed to page. That budget does not care what the services do, which framework they use, or how they are deployed. It cares how many of them can wake somebody up. Which makes the page count a better architecture review than the diagram — the diagram lists what you built, and the pager lists what you actually have to keep alive.

## Sources

- [1] Google, Site Reliability Engineering, Chapter 11, "Being On-Call" (Beyer, Jones, Petoff & Murphy, O'Reilly, 2016) — https://sre.google/sre-book/being-on-call/
- [2] Google, The Site Reliability Workbook, Chapter 8, "On-Call" (2018) — https://sre.google/workbook/on-call/
- [3] PagerDuty, Incident Response Documentation, "Being On-Call" — https://response.pagerduty.com/oncall/being_oncall/
- [4] O*NET OnLine, Summary Report for Software Developers (15-1252.00), 2025 wage vintage — https://onetonline.org/link/summary/15-1252.00
