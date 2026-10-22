# Verified Brief: demand_sensing_advanced_sop — 2026-10-22 (evergreen)

Source of the topic: `context/recon_proposals/2026-10-22_demand_sensing_advanced_sop_evergreen_brief.md`
(evergreen gate PASS, 5 rows / 5 hosts, 2026-10-22T20:03:23Z). All five gate rows were re-fetched below
and their verbatim cells re-extracted from the retrieved body — not copied from the brief.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|---|---|---|---|---|
| 1 | Position accuracy (2001) | At one leading retailer, 65% of inventory records were inaccurate, and these execution problems cut profits by more than 10% | VERIFIED | https://cmr.berkeley.edu/2001/05/43-3-execution-the-missing-link-in-retail-operations | "At one leading retailer, sixty-five percent of their inventory records were inaccurate (i.e., recorded inventory levels did not reflect actual inventory levels)." / "These execution problems reduce profits by more than 10%." |
| 2 | Same 2001 study — the software is not the constraint | Performance varies substantially among stores in the same chain running identical information technology | VERIFIED | https://cmr.berkeley.edu/2001/05/43-3-execution-the-missing-link-in-retail-operations | "Moreover, performance along these two dimensions of execution varies substantially among stores within the same chain that use identical information technology." |
| 3 | Position accuracy (2008, larger sample) | 65% of nearly 370,000 inventory records across 37 stores were inaccurate | VERIFIED | https://ideas.repec.org/a/inm/ormnsc/v54y2008i4p627-641.html | "Examining nearly 370,000 inventory records from 37 stores of one retailer, we find 65% to be inaccurate." |
| 4 | Where the error lives | 26.4% of the variance in record inaccuracy lies between product categories, only 2.7% between stores | VERIFIED | https://ideas.repec.org/a/inm/ormnsc/v54y2008i4p627-641.html | "26.4% of the total variance in IRI lies between product categories and that 2.7% lies between stores." |
| 5 | Position accuracy (2026, grocery) | ~24,000 SKUs sold in 11 stores | VERIFIED | https://arxiv.org/abs/2506.05357 | "The analysis covers ~24,000 stock keeping units (SKUs) sold in 11 stores." |
| 6 | What drives the drift | Inaccuracy rises with average inventory level, restocking frequency and perishability, and **falls** with promotional activity | VERIFIED | https://arxiv.org/abs/2506.05357 | "We find that IRI is positively associated with average inventory level, restocking frequency, and whether the item is perishable, and negatively associated with promotional activity." |
| 7 | The money leg | An inventory audit produced an 11% store-wide sales lift, all of it concentrated on items whose records overstated stock | VERIFIED | https://arxiv.org/abs/2506.05357 | "While performing an inventory audit is found to lead to an 11% store-wide sales lift, the audit has heterogeneous effects with all the sales lift concentrated on items exhibiting negative IRI (i.e., where system inventory is greater than actual inventory)." |
| 8 | The money leg, second half | The audit's benefit is larger on perishable items | VERIFIED | https://arxiv.org/abs/2506.05357 | "The benefits of inventory audits are also found to be more pronounced on perishable items, that are associated with higher IRI levels." |
| 9 | Achievable accuracy | Practitioner cases move accuracy from 75% or 80% to more than 99% with a well-run cycle-count program | VERIFIED (trade press, dated 9 May 2017) | https://www.mmh.com/article/rethink_cycle_counting_in_your_operations | "Lamphier, Hanrahan and Mullen all note they've seen inventory accuracy rise from 75% or 80% to more than 99% when cycle counting is well implemented." |
| 10 | How a count budget is aimed | Count the ~10% of locations that had activity since the last count, and aim at fast-moving, high-value, high-concern SKUs | VERIFIED (trade press, dated 9 May 2017) | https://www.mmh.com/article/rethink_cycle_counting_in_your_operations | "Cycle counts can be performed in a basic location sequence, or more purposefully by counting 10% of locations within the warehouse that have had activity since the last cycle count, for example." / "The advantage is that you can focus on fast-moving product, high-value product or high-concern SKUs such as upcoming sale items." |
| 11 | The planning-system requirement | An MRP/ERP planning engine needs 95%–99% record accuracy to work properly | VERIFIED (practitioner claim) | https://strategosinc.com/RESOURCES/10-Inventory/CC1-inventory_record_accuracy.htm | "MRP and ERP systems require very high accuracies (95%-99%) to function well." |
| 12 | Allocation when counts are scarce | For a two-stage chain with identical error distributions and counting costs, more frequent counts at the downstream stage are more effective | VERIFIED (qualitative — abstract carries no figure, so it is cited in prose and is NOT a gate row) | https://ideas.repec.org/a/eee/ejores/v237y2014i1p91-105.html | "For a two-stage system with identical error distributions and counting costs, we prove that it is more effective to conduct more frequent cycle counts at the downstream stage." |

## Discrepancies and flags recorded for the drafter
- **Two 65% figures, one year apart, are two different retailers.** Row 1 is the 2001 California Management
  Review study; row 3 is the 2008 Management Science study of 37 stores and ~370,000 records. Do not merge
  them into one "65% of records" statistic attributed to one paper, and do not present either as a 2026
  benchmark.
- **The counter-intuitive direction must survive drafting.** Row 6 says inaccuracy *falls* with promotional
  activity. The article may not say promotions corrupt the records; the drift belongs to high-velocity,
  frequently restocked, perishable stock.
- **Row 7 is a grocery quasi-experiment on 11 stores.** It may not be generalised into "audits lift sales
  11% everywhere", and it is not a distribution-centre result.
- **Row 9/10 is trade press from 9 May 2017, reporting three named practitioners' client cases.** Cite the
  year in the sentence; it is an illustration of achieved accuracy, not a current survey.
- **Row 11 is an undated consultancy page.** It is the planning-system requirement, stated as a
  practitioner rule of thumb — never as a measured finding.
- **Row 12 is qualitative.** The paper proves the downstream-priority result for a two-stage system only;
  the article may say "in the two-stage case the paper proves", nothing stronger.
- Nothing in the corpus was removed for want of a source; the two numbers deliberately NOT used are the
  supplier knowledgebase's restatement of a 28% inventory-value figure (unverifiable against the primary
  paper) and any "% of companies" survey statistic, neither of which this run could fetch.

## Arithmetic checked before drafting
- 26.4% (between categories) against 2.7% (between stores) is a ratio of roughly ten to one — state it as
  "about ten times", computed from those two figures, never as a new percentage.
- 75%→99% is 24 percentage points; 80%→99% is 19. Say "twenty-odd points", not "24% better".
- 65% of records is a count of records, not of units, units of stock, or dollars. Keep the noun attached.
