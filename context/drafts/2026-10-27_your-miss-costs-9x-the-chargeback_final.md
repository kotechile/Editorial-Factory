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
Late and short store deliveries cost North American suppliers roughly $100 billion a year, against $10 billion to $11 billion they can bill, rush or dispute [1][2]. That works out to a miss that costs 9x the chargeback, with shelf space, the next order and unsold stock carrying the rest [2]. The exception feed a control tower runs on holds the load event and the deduction. None of that other cost passes through it. In the same fortnight, two trade bodies scored how much of this exception work machines do across 13 core jobs in the chain. The Association for Supply Chain Management (ASCM) and the Digital Supply Chain Institute (DSCI) put the average at 1.94 out of 5 [3].

<!-- tension -->

## The big picture:

I keep coming back to how the two reports split one failure between them.

Cleo's study prices what happens after a load fails, finding that the ledger a tower can reach holds only a tenth of the cost [1][2]. The rest lands in the scorecard a store keeps, in shelf placement, in promo support, and in the size of the next order. None of those losses leaves a record with a time stamp that a tracking system can read. Mahesh Rajasekharan, Cleo's CEO, calls the result fragmented accountability [1]. Logistics tracks the truck, finance tracks the money deducted from the invoice, and sales tracks the orders that went to a rival. A deduction, in the grocery trade, is what a store takes off an invoice when a load lands late or short.

The second report explains why software has not closed this gap. The two bodies scored use from 1, meaning no machine work, to 5, meaning a machine acts with no human check [4]. The average score sits well below the middle of that scale. Planning tools lead the pack, while the jobs that do the work trail far behind, with returns coming in last [4]. The layer a firm builds to catch problems remains the least automated part of the chain.

The cut-off makes that gap costly in a set way. Stores like Walmart, Kroger, Target, Costco, and Publix set delivery bars often above 95%, while benchmarks put many suppliers at 85% to 91% [2]. Walmart takes 3% of the cost of goods on orders that miss its 98% mark [2]. A supplier hitting 99% against a 95% target earns nothing extra, but one dropping to 94% pays the fine [2]. The spare points are worth zero, so the missing points carry the entire scorecard.

## By the numbers

- **90% — Indirect cost share:** Cleo puts $85 billion to $90 billion of the total loss in lost shelf space, smaller orders, and excess stock, leaving just $10 billion to $11 billion in direct costs such as chargebacks, rush freight and dispute work [1][2].
- **1.94 of 5 — Machine use score:** Demand planning leads the 13 core jobs at 2.28 and supply and stock planning at 2.12, while the jobs that do the work trail, and returns sit last at 1.59 [4].
- **60% to 70% — Disputed fines lost:** The trade spends $1.16 billion a year fighting deductions, and one person doing that work for a single store channel costs $80,000 to $120,000 [2].
- **$11 billion to $23 billion — Modeled recovery:** A five- to 10-point lift in on-time, in-full (OTIF) rates is modeled to recover $11 billion to $23 billion, or 1.1 to 2.1 times the entire direct bill [2][6].

<!-- tactical-insight -->

## What I'd watch:

What I'd watch next is which metric the control tower starts to report. The current focus on alert volume looks cheap next to the numbers above. The teams closest to the work are already shifting focus, and these moves show up in live ops rather than vendor demos.

- **The scorecard as ledger:** A store's call on shelf space and order size is where the real loss lands, and buyers read it each quarter, not each load [2]. I am watching whether towers pull that sales data instead of just counting alerts.
- **The penalty threshold drop:** A spare point above the target earns nothing, so each point is worth zero on one side and a strict fine on the other [2]. The gap right at the threshold is where the rules earn their keep.
- **The planning layer gap:** [Planning tools buy capability, not autonomy](/planning-ai-buys-capability-not-autonomy/), and the job scores here put a number on that limit [4]. The jobs that carry the exception are the ones the planning layer merely predicts.
- **The measure set:** Analysts propose timing the whole loop to spot a change, gather context, decide, approve, and act [7]. That list treats the exception as a full cycle rather than a simple alarm.

One more sign sits above all of these. Gartner asked 2,002 tech chiefs and found only 13% say AI has given them lasting value. Use-case success sits at one in five [5]. Half expect AI to raise the total cost of their tech stack [5]. The money has flowed out against a case the exception layer has not yet had to prove.

<!-- nuanced-takeaway -->

## The catch

My read is that the headline loss figure is a vendor's model and operators should treat it as one.

The report names its method as industry benchmarks, public store programs, wage and freight cost data, and scenario modeling [1]. Trade coverage adds the label that matters most: these are modeled sums, not hard savings any supplier has actually booked [6]. That hidden share is the strongest claim here but the softest number, simply because an invoice cannot show those missing future orders.

The automation survey carries its own limits. It drew 144 replies and used 107, with just 11 C-suite executives, so its authors clearly label the job-level splits as directional [4]. A low score shows how a small group rates itself, not what a machine can do. The 33% who named an unclear business case as their top block are voicing the exact doubt this piece keeps circling [4].

Nor is all of that hidden loss a tower's to win back. Some shelf loss comes from price, range and promo calls that no alert feed ever sees. A firm can lift its delivery rate while a buyer trims the product range anyway. The chargeback remains the only part of the bill that arrives with a clear number on it, which is why it owns the reporting. I could be wrong, but the better test is whether the scorecard moves once the exception rate falls, not whether the two move together in a model. The gap I would want on one screen is the exception rate beside the scorecard, and no vendor demo here showed both.

<!-- tldr -->

## At a glance

- **The Big Shift:** Cleo prices late and short store loads at about $100 billion a year, with roughly 90% hiding in lost shelf space and smaller orders rather than in tracked chargebacks. In the same fortnight, ASCM and DSCI scored machine use across 13 supply chain jobs at 1.94 of 5, with planning ahead of execution.
- **Why It Matters:** A control tower built to catch exceptions measures only a tenth of the true cost. Meanwhile the bulk of AI budgets has gone to the planning jobs above it. The service bar acts as a cliff, meaning spare points earn nothing while missed targets carry heavy scorecard penalties.
- **What I'd Watch:** Whether the next version of the control tower reports commercial risk rather than just alert volume.
  - **Scorecard pull:** Whether dashboards carry the store's shelf and order decisions, which is where the hidden loss lands.
  - **Execution use:** Whether the 1.59 score at the bottom of the job list moves, since that is where teams close exceptions.
  - **Loop time:** The analysts' set of spot, gather, decide, approve, and act, which buyers can run against any vendor demo.
- **The Catch:** The headline figure is a vendor's model rather than an audited loss, and part of that hidden cost is a sales problem rather than an ops one.

## Sources

[1] Cleo, "Cleo Research Estimates OTIF Failures Cost North American CPG and Food & Beverage Manufacturers Approximately $100 Billion Annually", 20 October 2026 — https://www.cleo.com/news-cleo-research-shows-otif-failures-cost-100-billion-annually
[2] FreightWaves, "Late, short deliveries cost food and CPG makers $100 billion", 22 October 2026 — https://www.freightwaves.com/news/cleo-otif-failures-cost-cpg-100-billion
[3] Digital Supply Chain Institute, "The People Paradox in Supply Chain AI Integration", October 2026 — https://dscinstitute.org/research/people-paradox-supply-chain-ai-report
[4] FreightWaves, "Workforce gaps keep supply chain AI stuck in pilot mode", 23 October 2026 — https://www.freightwaves.com/news/ascm-dsci-supply-chain-ai-workforce-readiness
[5] Gartner, "Gartner Survey Finds Only 13% of CIOs Say Their Enterprise Has Realized Significant or Transformational Value from AI", 19 October 2026 — https://www.gartner.com/en/newsroom/press-releases/2026-10-19-gartner-survey-finds-only-13-percent-of-cios-say-their-enterprise-has-realized-significant-or-transformational-value-from-ai
[6] Supply Chain 24/7, "Late and Incomplete Deliveries Cost Manufacturers $100 Billion a Year", 26 October 2026 — https://www.supplychain247.com/article/cleo-report-late-incomplete-deliveries-manufacturers-100-billion
[7] Logistics Viewpoints (ARC Advisory Group), "From Detection to Resolution: The Anatomy of a Supply Chain Exception", 19 October 2026 — https://logisticsviewpoints.com/2026/10/19/from-detection-to-resolution-the-anatomy-of-a-supply-chain-exception

## Gate report

lead: PASS — States stakes immediately with one clear figure ($100 billion) and explains the "why" without throat-clearing.
tension: PASS — Follows H2 spacing rules perfectly. Breaks down the structural gap with plain language and clear, active sentences.
tactical-insight: PASS — Uses first-person observer cues. Bullets present observations rather than commands, formatted cleanly.
nuanced-takeaway: PASS — Separates the vendor's model from audited reality and closes on an observation rather than advice; the body's one internal link sits in the tactical section, as an observation.
tldr: PASS — Distinctly separated by H2. Follows the exact 4-part Smart Brevity format with concise, scannable summaries.
