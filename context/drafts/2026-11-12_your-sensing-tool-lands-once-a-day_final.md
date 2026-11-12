---
title: "Batch Runs Cap What Sensing Buys"
vertical: demand_sensing_advanced_sop
kind: evergreen
archetype: evergreen
evergreen: true
persona: ops_leader
one_big_thing: "A demand-sensing subscription changes the model, not the scheduled job that turns it into orders: a master-planning run's width starts at the item or planned-order count divided by 1,000, its length grows with the time fence, and it is not supposed to share its window with another heavy routine, so cadence is a budget — and the measured premium for refreshing weekly rather than annually is at most 23 points of inventory, against 40 points that came from the one-time re-set."
date: 2026-11-12
slug: your-sensing-tool-lands-once-a-day
image_path: "context/assets/illustrations/your-sensing-tool-lands-once-a-day/featured.jpg"
image_style: "cinematic_still"
image_model: "flux"
image_alt: "Batch Runs Cap What Sensing Buys. Master-planning schedule board with a sliding metal time-fence track in a dark control room."
image_caption: "Batch Runs Cap What Sensing Buys: Weekly over annual is worth at most 23 inventory points; the one-time reset bought 40."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
A real-time planning subscription changes the model. It does not change the scheduled job that turns the model into orders, and the job is where the cadence lives [4]. Microsoft's own performance guide prices that run in threads, starting at one thread per 1,000 planned orders or per 1,000 items [1]. Frequency is therefore a budget drawn from three things: item count, horizon length and window. A licence does not move any of them. That gap is why so many sensing pilots arrive as a weekly report with a better forecast inside it.

<!-- tldr -->

## At a glance

- **The shift:** Cadence is a runtime budget, not a feature in the licence.
- **The number:** 23 points is the most a weekly refresh added over an annual one.
- **The risk:** A narrow daily run re-imports the error the full run smoothed.

<!-- tension -->

## Where the day goes

The fence is the first cost. Requirements are computed out to a date, and Microsoft states the trade without hedging: the larger the time fence, the longer the run [1]. The second cost is the tail. Two adjacent coverage tasks in one run can differ in length by as much as 30 minutes, so a single slow item can set the duration of the whole job [1].

The third cost is the calendar. The same guide tells administrators not to schedule master planning beside another heavy routine, and names inventory close as the one to avoid [1]. None of those three costs is a switch the vendor can flip.

Strip the plumbing away and the real question is what frequency is worth. The best public answer is a capstone published in Supply Chain Management Review in March 2026, covering 61 items on 31 nodes across 18 scenarios that ran from annual refreshes to weekly ones [2]. The fastest cadence cut inventory value by up to 63%, about $9.3 million a year [2]. A conservative annual refresh still cut working capital by 40% [2]. I read the two results as a pair, because both scenarios ran through the same optimizer on the same network, so the clock was the only difference between them.

Sit those two results together and the cadence is worth at most 23 points, because the 40 came from the re-set itself. That ordering is the useful part. The first pass over a network's parameters, re-setting levels nobody had touched in years, buys most of the money. The refresh buys the remainder, and the remainder is what needs the runtime budget.

## By the numbers

- **63% of inventory value:** the capstone's best case, at a weekly refresh [2].
- **$9.3 million a year:** what that cut was worth in the sponsored retail network [2].
- **200,000 item-location records:** the review planners did by hand before the work was grouped [3].

<!-- tactical-insight -->

## Where the fast clock belongs

The case that shows the parameter side comes from a supply chain with more than 60 sites and 13 echelons, where planners set safety stock one item and one site at a time [3]. The project released 20 million euros of inventory, and grouping is what made it survivable: each item and location pair went into one of roughly 300 groups, and planners reviewed a group factor every month or quarter instead of every record [3]. The saving was real. The upkeep was the constraint.

Cadence needs the same split, and I keep the two questions apart when I read these proposals: how often the engine can fire, and what firing more often buys. An item with a 90-day lead time gains nothing from a daily run, because the order it triggers is fixed a quarter out. An item with a five-day lead time gains, because a day of signal moves this week's order. The short-fence run belongs to the second group. The full-catalogue run stays monthly, and keeping them apart is what the runtime budget is for.

<!-- nuanced-takeaway -->

## The catch

Those 23 points are a ceiling from one study, and a small one: an optimizer was doing the re-setting, and the annual case was already dynamic on the parameters it held [2]. I read the 63% and the 40% together, since the same re-set did the heavy work in both. A narrow daily run also carries a risk the full run covered, because items off the fast clock are planned against older numbers, and nobody can compute where that boundary sits. Frequency is worth buying once the parameters are right, and worth little before then. Either way, the cycle that consumes the planning hours is [the larger line item](/your-planning-cycle-costs-7-managers/).

<!-- internal-links -->

## Sources

- [1] Microsoft Learn, "Improve master planning performance — Dynamics 365 Supply Chain Management" — https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/master-planning-performance
- [2] Eva Ponce, Vi Duong and Nic Holwerda, "Buffer or suffer: Dynamic Multi-Echelon Inventory Optimization in action" — Supply Chain Management Review, 2026-03-16 — https://www.scmr.com/article/buffer-or-suffer-dynamic-multi-echelon-inventory-optimization-in-action
- [3] Demand Planning / S&OP Blog, "Say No to Siloed Planning With Multi-Echelon Inventory Optimization" — 2024-02-22 — https://demand-planning.com/2024/02/22/say-no-to-siloed-planning-with-multi-echelon-inventory-optimization
- [4] Odoo 20.0 documentation, "Reordering rules" — https://www.odoo.com/documentation/20.0/applications/inventory_and_mrp/inventory/warehouses_storage/replenishment/reordering_rules.html
