---
title: "Your Miss Costs 9x the Chargeback"
vertical: control_tower_exception_orchestration
persona: supply_chain_architect
one_big_thing: "Roughly nine-tenths of the cost of a late delivery is decided after the delivery, in a retailer's supplier scorecard, and the automation built to catch exceptions sits in planning rather than execution — so a control tower that counts closed alerts is measuring the cheapest tenth of the loss."
date: 2026-10-27
slug: your-miss-costs-9x-the-chargeback
synthesis: true
sources:
  - https://www.cleo.com/news-cleo-research-shows-otif-failures-cost-100-billion-annually
  - https://dscinstitute.org/research/people-paradox-supply-chain-ai-report
---

<!-- lead -->
Cleo puts the yearly bill for late and short store deliveries in North America at about $100 billion. The piece a supplier can bill, rush or dispute comes to $10 billion to $11 billion [1][2]. That works out to a miss that costs 9x the chargeback, with shelf space, the next order and unsold stock carrying the rest [2]. The exception feed a control tower runs on holds the delivery event and the deduction. It holds none of that other cost. In the same fortnight, the Association for Supply Chain Management (ASCM) and the Digital Supply Chain Institute (DSCI) scored how much of this work machines do across 13 core jobs in the chain, and the average came back at 1.94 out of 5 [3].

<!-- tension -->

## The big picture:

I keep coming back to how the two reports split one failure between them. Cleo's study prices what happens after a miss, and a firm that sells software to prevent chargebacks wrote it [1][2]. It finds that the ledger a tower can reach holds about a tenth of the cost. The other nine tenths land in the scorecard a store keeps, in shelf slot, in promo support and in the size of the next order. None of those leave a record with a time stamp that a tracking system can read.

Cleo's CEO, Mahesh Rajasekharan, calls that a split in ownership. Logistics tracks delivery, finance tracks the money taken off the invoice, and sales tracks the business that went elsewhere [1]. A deduction, in the grocery trade, is what a store takes off an invoice when a load lands late or short. It is the one piece of the loss that reaches a finance system at all.

The second report says why software has not closed the gap. ASCM and DSCI scored use from 1, meaning no machine work, to 5, meaning a machine acts with no human check [4]. The average of 1.94 sits below the middle of that scale. Planning leads, at 2.28 for demand planning and 2.12 for supply and stock planning, while jobs that execute trail, and returns come last at 1.59 [4]. The layer a firm builds to catch exceptions is the least automated part of the chain it sits in.

The cut-off makes that gap costly in a set way. Stores such as Walmart, Kroger, Target, Costco and Publix set a bar often above 95%, while most suppliers sit at 85% to 91% [2]. Walmart takes 3% of the cost of the goods on orders that miss its 98% mark [2]. A supplier at 99% against a 95% bar earns nothing extra for the surplus, and one at 94% pays [2]. The spare points are worth zero and the missing points carry the scorecard.

## By the numbers

- **90% — Indirect share:** Cleo puts $85 billion to $90 billion of the $100 billion in lost shelf space, smaller orders, excess stock and factory drag, against $10 billion to $11 billion of chargebacks, rush freight and dispute work [1][2].
- **1.94 of 5 — Use across 13 jobs:** demand planning leads at 2.28 and supply and stock planning at 2.12, while returns come last at 1.59 on the same scale [4].
- **60% to 70% — Disputes written off:** the trade spends $1.16 billion a year fighting deductions, and one analyst who does it for a single store channel costs $80,000 to $120,000 [2].
- **$11 billion to $23 billion — Model gain:** a five- to 10-point lift in on-time, in-full (OTIF) rates is said to recover that much, or 1.1 to 2.1 times the whole direct bill [2][6].

<!-- tactical-insight -->

## What I'd watch:

What I'd watch next is which number the tower starts to report, because the two reports make the one it reports now look cheap. The teams closest to the work are already moving, and the moves show up on public pages rather than in demos.

- **The scorecard as the ledger:** a store's call on shelf slot and order size is where the nine tenths land, and it is read each quarter rather than each load [2]. Whether a tower shows that number instead of the alert count tells you which of the two it reports.
- **The 99% to 94% drop:** a spare point above the bar earns nothing, so each point is worth zero on one side and a fine on the other [2]. That gap is where exception rules earn their keep, and a rule tuned to close more alerts walks past it.
- **Where the machines went:** planning tools buy capability, not autonomy (/planning-ai-buys-capability-not-autonomy/), and the job scores here put a number on that [4]. The jobs that carry the exception are the ones the planning layer predicts.
- **The set of measures analysts propose:** time to spot a change, gather context, decide, approve and act, plus backlog, share closed by a machine, override rate, repeat rate and loss avoided [7]. That list can be run against any vendor demo, and it treats the exception as a loop rather than a bell.

One more sign sits above all of these. Gartner asked 2,002 tech chiefs and found 13% who say AI has given them large or lasting value, with use-case success at one in five [5]. Half expect AI to raise the total cost of their tech stack [5]. The money has gone out against a case the exception layer has not had to prove.

<!-- nuanced-takeaway -->

## The catch

My read is that the $100 billion is a vendor's model and should be used as one. The report names its method as industry benchmarks, public store programs, wage and freight cost data and scenario modelling [1]. Trade coverage adds the label that matters: these are modelled sums, not savings anyone has booked [6]. The 90% share is the strongest claim here and the softest number, because those indirect lines are the ones an invoice cannot show.

The use survey has its own limits. It drew 144 replies and used 107, and it got 11 CEOs; its authors label the job-level splits as directional [4]. A score of 1.94 is how a small group rates itself, not a gauge of what a machine can do. The 33% who named an unclear business case as their top block are voicing the same doubt this piece keeps circling [4].

Nor is all of the nine tenths a tower's to win back. Some shelf loss comes from price, range and promo calls that no exception feed ever sees, and a firm can lift its delivery rate while a buyer trims the range anyway. The chargeback is the only part of the bill that arrives with a number on it, which is why it owns the reporting. I could be wrong, but the better test may be whether the scorecard moves once the exception rate falls, not whether the two move together in a model.

<!-- tldr -->

## At a glance

- **The Big Shift:** Cleo prices late and short store deliveries at about $100 billion a year, with roughly 90% of it in lost shelf space, smaller orders and excess stock rather than in the chargebacks suppliers track. In the same fortnight, ASCM and DSCI scored machine use across 13 supply chain jobs at 1.94 of 5, with planning ahead of execution.
- **Why It Matters:** a control tower built to catch exceptions is measuring about a tenth of the cost, and the AI budget has gone to the planning jobs above it. The service bar is a cliff, so spare points earn nothing while missing points carry the scorecard.
- **What I'd Watch:** whether the next version of the tower reports commercial risk rather than alert volume.
  - **Scorecard pull:** whether dashboards carry the store's shelf and order call, which is where the indirect loss lands.
  - **Execution use:** whether the 1.59 at the bottom of the job list moves, since that is where exceptions are actually closed.
  - **Loop time:** the analysts' set of spot, gather, decide, approve and act, which any vendor demo can be run against.
- **The Catch:** the $100 billion is a vendor's scenario model, not an audited loss, and the use figures come from 107 replies. Part of the indirect cost is commercial rather than operational, and no exception tool reaches it.

## Sources

[1] Cleo, "Cleo Research Estimates OTIF Failures Cost North American CPG and Food & Beverage Manufacturers Approximately $100 Billion Annually", 20 October 2026 — https://www.cleo.com/news-cleo-research-shows-otif-failures-cost-100-billion-annually
[2] FreightWaves, "Late, short deliveries cost food and CPG makers $100 billion", 22 October 2026 — https://www.freightwaves.com/news/cleo-otif-failures-cost-cpg-100-billion
[3] Digital Supply Chain Institute, "The People Paradox in Supply Chain AI Integration", October 2026 — https://dscinstitute.org/research/people-paradox-supply-chain-ai-report
[4] FreightWaves, "Workforce gaps keep supply chain AI stuck in pilot mode", 23 October 2026 — https://www.freightwaves.com/news/ascm-dsci-supply-chain-ai-workforce-readiness
[5] Gartner, "Gartner Survey Finds Only 13% of CIOs Say Their Enterprise Has Realized Significant or Transformational Value from AI", 19 October 2026 — https://www.gartner.com/en/newsroom/press-releases/2026-10-19-gartner-survey-finds-only-13-percent-of-cios-say-their-enterprise-has-realized-significant-or-transformational-value-from-ai
[6] Supply Chain 24/7, "Late and Incomplete Deliveries Cost Manufacturers $100 Billion a Year", 26 October 2026 — https://www.supplychain247.com/article/cleo-report-late-incomplete-deliveries-manufacturers-100-billion
[7] Logistics Viewpoints (ARC Advisory Group), "From Detection to Resolution: The Anatomy of a Supply Chain Exception", 19 October 2026 — https://logisticsviewpoints.com/2026/10/19/from-detection-to-resolution-the-anatomy-of-a-supply-chain-exception
