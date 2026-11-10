---
title: "Your Pager Caps at 2 Incidents a Shift"
vertical: enterprise_tech_leadership
kind: evergreen
archetype: evergreen
evergreen: true
persona: eng_leader
one_big_thing: "A 24/7 rotation is a fixed machine: two always-staffed seats and week-long shifts put a single-site rotation at eight engineers, and two incidents per 12-hour shift — about six engineer-hours and $392 each — is the page budget that decides how many services that team can own."
date: 2026-11-10
slug: your-pager-caps-at-2-incidents
meta_title: "Your Pager Caps at 2 Incidents a Shift"
meta_description: "Two incidents per 12-hour shift is the published ceiling for on-call, and at six engineer-hours each it decides how many services one team can own."
image_path: "context/assets/illustrations/your-pager-caps-at-2-incidents/featured.jpg"
image_style: "cinematic_still"
image_model: "flux"
image_alt: "Pager Caps At 2 Incidents A Shift. An industrial alphanumeric pager rests on a brushed-steel control-room console, its amber status LED the"
image_caption: "Pager Caps At 2 Incidents A Shift: At six hours per incident, the cap decides how many services one team can own."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->

Two incidents per 12-hour shift is the ceiling Google publishes for its on-call engineers, and that number settles more about your architecture than most design reviews get to. The company's own average for one incident is six hours. Finding the root cause, fixing it, writing the post-incident review, and cleaning up the bugs that follow all count [1]. Two of those fill a 12-hour shift. So the number is a budget, and every service you wire to a pager draws on it.

<!-- tldr -->

## At a glance

- **The shift:** the pager, not the cloud bill, caps how many services one team can really own.
- **The number:** two incidents per 12-hour shift, at about six engineer-hours each [1].
- **The risk:** 48 services paging once a fortnight each spend 86% of a week's budget.

<!-- tension -->

## The rotation comes before the architecture

The rotation comes first, because its size is published arithmetic rather than a matter of taste. Google keeps two people on call at all times: a primary and a secondary. It caps on-call time at 25 percent of an engineer's working life. Of the rest, up to another 25 percent may go to other operational duties, and at least half of the engineer's time must go to engineering work [1]. With week-long shifts, each engineer carries one week in four. Two seats, one week in four, and the smallest single-site rotation lands at eight engineers. A dual-site team needs six per site to meet the same rule [1]. That headcount floor is the other half of [the price a service split charges](/monolith-split-price-the-premium/).

That is where headcount and money meet. Eight engineers at the median wage of $135,980 for a software developer in the United States comes to $1,087,840 of payroll. That is the cost of keeping one rotation staffed [4]. I read that line twice before I believed it: nobody signs it as an on-call cost, because it is hidden inside a hiring plan.

The page budget follows the same logic. Two incidents per 12-hour shift, across two shifts a day, is four incidents a day. That is 28 a week and 1,456 a year [1]. At six hours each, the ceiling is 168 engineer-hours a week. That is 4.2 full-time positions, or 52.5 percent of an eight-person team's 320-hour week [1]. A rotation running at its allowed page ceiling spends half its capacity on incidents. That is the same operational cap the chapter sets from the other direction. The ceiling is not a resting margin. It is the line where the team stops having time to fix the thing that is paging them.

Google is blunt about a bad pattern. The median number of pages per day should be zero. A component that pages every day signals that something else will break and push the count past what is permitted [1]. The workbook makes the same point from the other side. It treats each new paging alert as a cost that must be argued for. It also defends a 12-hour shift, because 12 hours overnight beats 24 [2].

The field version is not exotic: a 25-engineer group this desk has covered carried 48 services across three clusters. Give each service one page every two weeks. The team then sits at 24 incidents a week, or 86 percent of the budget, before anything breaks badly. At six hours an incident, that is 144 engineer-hours a week, or 3.6 people permanently on incident work [1].

## By the numbers

- **$392.28 per incident:** six engineer-hours of Google's average incident work, priced at the $65.38 median hourly wage [1].
- **$571,160 a year:** incident work at the full 28-a-week ceiling, against $1,087,840 of payroll for the eight engineers [1].
- **8 engineers:** the single-site staffing floor that falls out of the 25 percent on-call cap and week-long shifts [1].

<!-- tactical-insight -->

## Where operators start on Monday

Teams I have watched pull the last 90 days of pages and group alerts that share a root cause. That group count is the real incident count. It is almost always lower than the raw alert count and higher than the number in the post-incident records. Divide it by 28 and you have the share of the weekly budget already spent. For most teams, this is the first honest number they have seen about their pager.

The order matters more than the tooling.

- **Cut pages first.** This is the only lever that gives back capacity in the same quarter. A component that pages every day is not a source of incidents but a defect with a notification attached [1]. Retire the alert, or fix the thing behind it, and the budget moves the same day.
- **Resize the rotation second.** If a team cannot put two always-staffed seats on a rotation with one week in four, it does not have a round-the-clock service. It has a best-effort pager and a business-hours promise, and that belongs in the service-level objective rather than in an exit interview.
- **Change the shift pattern last.** A multi-site rotation can avoid overnight work altogether, and the shift pattern itself is a lever [2]. The escalation window is a configured setting. PagerDuty's guidance starts with a five-minute timeout on the first escalation, before anything else is tuned [3].

When a new service asks for a pager, ask for its expected pages per week. A team that cannot estimate that number has not thought through its failure modes. A team that knows the number has already shown whether the service is safe to put on a pager.

<!-- nuanced-takeaway -->

## The catch

Every figure here comes from one operator's published practice, and that operator is Google. That means multiple sites, dedicated reliability teams, and a six-hour incident average that reflects a class of system most readers do not run. My reading, held loosely: I would not quote their average as mine. A 40-minute incident average stretches the same shift much further; an incident that eats a whole day cuts its budget to one. Do the division with your own average.

The eight-engineer floor is not a law either. It falls out of two choices: two seats, and one week in four. Change the shift length and the floor moves. A different shift pattern, a paid on-call allowance, or a follow-the-sun partner arrangement all shift the arithmetic. None of them removes the need to staff two seats.

The wage is the softer number. The $135,980 is the national median for software developers in the Labor Department's Occupational Information Network survey [4]. A senior platform engineer costs more. So the dollar figure understates the real bill, while the engineer-hours hold.

What survives all three cautions is the shape: a fixed budget of attention, divided among the things allowed to page. That budget does not care what the services do, which framework they use, or how they are deployed. It cares how many of them can wake somebody up. Which makes the page count a better architecture review than the diagram. The diagram lists what you built. The pager lists what must be kept alive.

## Sources

- [1] Google, Site Reliability Engineering, Chapter 11, "Being On-Call" (Beyer, Jones, Petoff & Murphy, O'Reilly, 2016) — https://sre.google/sre-book/being-on-call/
- [2] Google, The Site Reliability Workbook, Chapter 8, "On-Call" (2018) — https://sre.google/workbook/on-call/
- [3] PagerDuty, Incident Response Documentation, "Being On-Call" — https://response.pagerduty.com/oncall/being_oncall/
- [4] O*NET OnLine, Summary Report for Software Developers (15-1252.00), 2025 wage vintage — https://onetonline.org/link/summary/15-1252.00
