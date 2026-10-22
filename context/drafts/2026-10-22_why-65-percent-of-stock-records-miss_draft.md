---
title: "Your Stock Records Are 65% Wrong"
vertical: demand_sensing_advanced_sop
persona: ops_leader
one_big_thing: "The stock record the plan reads is wrong more often than the forecast it is netted against, the error gathers by product group rather than by site, and it grows with how often an item is restocked — so the next planning dollar is better spent on a count program aimed at records that claim stock the shelf does not hold than on a better sensing engine."
date: 2026-10-22
slug: why-65-percent-of-stock-records-miss
archetype: evergreen
evergreen: true
---

<!-- lead -->
At one big retailer, 65% of stock records did not match what sat on the shelf, and that gap between the record and the real count cut profit by more than ten percent [1]. A later study of nearly 370,000 records across 37 stores at another chain found the same share wrong [2]. Those records are where a sales and operations planning (S&OP) run starts, so the forecast is not the only number in your plan that misses.

<!-- tension -->

## The big picture:

A plan sets a forecast against the stock it expects to have. That balance opens with whatever the enterprise resource planning (ERP) system says is on hand, and every step after it carries the same error forward. When the record claims too much stock, the plan orders nothing and the line waits. When it claims too little, the plan buys what the warehouse already holds.

What strikes me is how much older this problem is than the forecast debate. The 2001 study found wide gaps between stores inside one chain, all of them running the same software [1]. The software did not decide which stores kept good records, which puts the real limit in the counting process rather than in the planning tool.

The 2008 study then showed where the error gathers. Of all the spread in record error, 26.4% sat between product groups and 2.7% between stores [2]. Put plainly, how wrong a record is depends about ten times more on which product line the item sits in than on which building holds it.

A 2026 grocery study of roughly 24,000 items across 11 stores adds the reason. Error rose with average stock level, with how often an item is restocked and with whether it spoils, and it fell when items were on promotion [3]. That last direction is the one I did not expect, and it undercuts the common story that promo weeks are what wreck the data.

The money case is the part planning teams rarely hear. In the same study, a stock count lifted store sales 11% in a field test, and all of that gain landed on items whose records claimed more stock than the shelf held [3]. The count did not sharpen the forecast. It fixed the position the forecast was being measured against.

## By the numbers

- **65% — Records that miss:** Sixty-five percent of nearly 370,000 stock records from 37 stores of one retailer were wrong, and an earlier study of a second retailer found the same share [2][1].
- **26.4% vs 2.7% — Where the error sits:** Share of the spread in record error that sits between product groups, against the share that sits between stores, so counts belong to groups before sites [2].
- **11% — Sales lift from a count:** Store-wide sales gain from a stock count in a grocery study of about 24,000 items in 11 stores, all of it on items whose records claimed more stock than there was [3].
- **95% to 99% — The planning floor:** Record accuracy that material requirements planning (MRP) and ERP systems need to work well, a band warehouse teams report passing 99% once counting is run properly [5][4].

<!-- tactical-insight -->

## What I'd watch:

I keep coming back to order of spend, because each item below costs less than the sensing licence it protects. What I am watching is which teams do these things before the upgrade rather than after it.

- **Count by product group first:** The spread figures put ten times more of the explainable error in the group than in the site, so a count plan built per warehouse is aimed at the smaller half of the problem [2].
- **Chase the records that overclaim:** That is where the sales gain landed, and it is also the error that makes a planner order stock it does not have [3].
- **The active tenth:** Counting the 10% of spots that moved since the last count, with weight on fast movers and costly items, is the version of counting trade press reports lifting accuracy to 99% [4].
- **The stage nearest the customer:** When counts are scarce, a two-step chain with similar error rates gains more from counting the later stage, which a 2014 paper proves for that case [6].
- **A go/no-go number:** Under the 95% to 99% band an ERP planning run needs, a sharper forecast is being fed into a wrong balance, and the symptom shows up in the exception queue, not the accuracy report [5].

<!-- nuanced-takeaway -->

## The catch:

My read is that a good record is a starting point, not a stand-in for forecast work. Four limits keep it honest.

- The studies count records, not money. A wrong record on a cheap slow item and a wrong record on a high runner are not the same exposure, which is why the way the gain gathered on overclaims matters more than the headline share.
- The 11% lift came from one grocery chain of 11 stores in a field test. It belongs to that setting and should not be read into a warehouse.
- A count is a stock of being right, not a flow. Accuracy decays with every receipt, pick and return, so the repeated cost of counting is the true price of the number.
- None of this removes demand risk. A better record makes the plan act on the right stock; it does not say what next month will sell, and a sensing layer still has to earn its place on forecast error.

<!-- tldr -->

## At a glance

- **The Big Shift:** The stock record that an S&OP plan sets its forecast against is wrong far more often than the forecast itself, and the error runs about ten to one by product group rather than by site.
- **Why It Matters:** A plan that orders against a record claiming stock that is not there is tying up working capital in a phantom, and the count that fixed those records lifted store sales 11% in the study that ran it.
- **What I'd watch:**
  - **Group-first counting:** Assigning counts by product group and how fast an item moves, rather than evenly per site, because that is where the measured spread sits.
  - **Overclaim bias:** Aiming the count at records that say more stock exists than the shelf holds, the items where the sales gain landed.
  - **The accuracy floor:** Treating the 95% to 99% record band as the entry price for a planning upgrade rather than a warehouse key indicator.
- **The Catch:** The figures come from retail and grocery studies that count records rather than money, the 11% lift is one chain's field test, and a correct record still does not answer what demand will do next.

## Sources
[1] Raman, DeHoratius & Ton, "Execution: The Missing Link in Retail Operations", California Management Review 43(3), Spring 2001 — https://cmr.berkeley.edu/2001/05/43-3-execution-the-missing-link-in-retail-operations
[2] DeHoratius & Raman, "Inventory Record Inaccuracy: An Empirical Analysis", Management Science 54(4):627–641, April 2008 — https://ideas.repec.org/a/inm/ormnsc/v54y2008i4p627-641.html
[3] Rekik, Oliva, Glock & Syntetos, "Inventory record inaccuracy in grocery retailing", arXiv:2506.05357v3, 8 June 2026 — https://arxiv.org/abs/2506.05357
[4] Modern Materials Handling, "Rethink Cycle Counting in your Operations", 9 May 2017 — https://www.mmh.com/article/rethink_cycle_counting_in_your_operations
[5] Strategos, "Cycle Counting & Inventory Record Accuracy" (practitioner reference) — https://strategosinc.com/RESOURCES/10-Inventory/CC1-inventory_record_accuracy.htm
[6] Kök & Shang, "Evaluation of cycle-count policies for supply chains with inventory inaccuracy and implications on RFID investments", European Journal of Operational Research 237(1):91–105, 2014 — https://ideas.repec.org/a/eee/ejores/v237y2014i1p91-105.html
