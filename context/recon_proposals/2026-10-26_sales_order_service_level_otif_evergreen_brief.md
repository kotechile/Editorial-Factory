# Evergreen Brief: sales_order_service_level_otif — 2026-10-26
**Archetype:** evergreen
**Vertical:** sales_order_service_level_otif
**Persona:** ops_leader
**Decision the reader is facing:** Whether to close this year's in-full gap by spreading more inventory across the catalogue or by fixing the few SKUs that sit on most orders — the call that bites the week a customer scores completeness at order level while the internal dashboard still reports a 98% fill rate.
**Durability:** The load-bearing claim is arithmetic — order fill falls as line fill raised to the power of the lines on the order — so it holds in 12 months and in 10 years; the cited figures are as of their own publication dates (inventory-software explainer dated June 19, 2026; logistics provider's benchmark page dated July 7, 2026; a practitioner case published March 2018; an undated consultancy client dataset), and no retailer programme year, price, rate or contract term is load-bearing.
**De-dup:** `2026-10-19_your-30-exception-bill-is-wrong` is this vertical's nearest prior evergreen artifact (the per-exception cost as wage × handle time, published 2026-10-19); this piece never prices a touch — it argues that the in-full score is an order-level function of line-level availability, which no corpus artifact has argued. Also checked and distinguished: `2026-10-19_your-hidden-quantity-gap` (news, OTIF fell on quantity as buyer buffers thinned), `2026-10-26_33-of-your-shrink-isnt-theft` (today's news run, where loss dollars are booked and which software layer is funded), and cross-vertical `2026-10-19_four-warehouses-halve-stock` (the square-root pooling law, which takes a 98% fill rate as an input and never separates order fill from line fill) and `2026-10-08_safety-stock-forecast-error-not-demand-noise` (sizes the buffer off forecast error, not off the basket arithmetic).
**Thesis:** Order fill is not a blurrier copy of line fill — it is roughly line fill raised to the power of the lines on the order, so a 98% line fill is an 81.7% in-full score on a ten-line order, and the cheapest points to buy back are the few SKUs that appear on the most orders rather than more stock spread evenly.

**Lead:** The vertical's own beat, `primary_angles` #2 and #1 — "the fill-rate threshold that triggers chargeback exposure" and "OTIF root-cause decomposition" — crossed with what the persona is actually deciding (`ops_leader` wants physical-to-digital friction fixes and working-capital math). The specific material is the measurable gap between the line-level metric an internal dashboard reports and the order-level completeness a customer experiences: four practitioner sources state that gap, and two of them state it in client numbers. GSC was checked as a bonus signal only (`scripts/gsc_analyzer.py --vertical sales_order_service_level_otif --export-md` returned 0 high-potential opportunities at this site's current impression volume), which is not a veto.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | Inventoros, "Order Fill Rate" explainer (June 19, 2026) | https://inventoros.com/blog/order-fill-rate | 2026-10-26 | 81.7% — 0.98^10 = 81.7%: a 98% per-line availability leaves an 81.7% order fill rate on a ten-line order, and 0.98^20 = 66.8% on a twenty-line order | vendor claim (the arithmetic is checkable, the framing is the vendor's) |
| 2 | F. Curtis Barry & Co., "Use Initial Order Fill Rate to Measure Your Customer Service" | https://www.fcbco.com/blog/use-initial-order-fill-rate-to-measure-customer-service | 2026-10-26 | 88.5% — a $30 million food business averaging 2.25 lines per order showed an 88.5% initial customer order fill rate in its first week of reporting, having described its backorder rate as "low" | measured (consultancy client engagements, unnamed clients) |
| 3 | F. Curtis Barry & Co., same article | https://www.fcbco.com/blog/use-initial-order-fill-rate-to-measure-customer-service | 2026-10-26 | 76.5% — a $25 million apparel company inferred a 90% service rate from a backorder rate of about 10%, but its first initial order fill report showed 76.5% for an entire season | measured (consultancy client engagements, unnamed clients) |
| 4 | Benchmarking Success (Rob O'Byrne), "Understanding Fill Rate KPIs: Line Fill Rate" (March 2018) | https://www.benchmarkingsuccess.com/understanding-fill-rate-kpis-line-fill-rate | 2026-10-26 | 96% — one mid-sized industrial supplies distributor ran a 96% line fill rate against a roughly 82% order fill rate, and three or four slow-moving items with chronic stock issues appeared on a huge proportion of orders | measured (practitioner case) |
| 5 | Benchmarking Success, same article | https://www.benchmarkingsuccess.com/understanding-fill-rate-kpis-line-fill-rate | 2026-10-26 | 75% — 7,500 perfectly filled lines out of 10,000 lines in 1,000 orders is a 75% line fill rate, while order fill could be as low as 0% if every other order missed on a line | measured (worked example) |
| 6 | DCL Logistics, "Fill Rate: Definition, Formula, and How to Calculate It" (July 7, 2026) | https://dclcorp.com/blog/fulfillment/fill-rate | 2026-10-26 | 92 — the order fill rate benchmark the provider quotes is a 92-98% range, which is the band a line-level dashboard reads as healthy | vendor claim |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| Order fill decays exponentially in lines per order: the 98% that reads as 82% in-full, and why the SKU on most orders beats more stock | 9 | 9 | 7 | 9 | 8.5 | **winner** |
| The 95-to-99 service-level ladder: what the last four points of cycle service level cost in safety stock (z 1.65 → 2.33) | 8 | 9 | 6 | 7 | 7.6 | dropped — the service factor is only fetchable on a Wikipedia article and one vendor explainer, and no fetchable page prices the step |
| Retailer deduction break-even: buy the last two points of in-full or pay 3% of the goods value | 9 | 7 | 5 | 8 | 7.35 | dropped — every threshold and penalty rests on deduction-management vendors restating retailer programmes; the 2026-10-19 verified brief already barred the 3% figure as unprimary, and no retailer document was retrievable again today |
| Split-shipment break-even under ATP allocation: ship the short line now or hold the order | 8 | 8 | 5 | 8 | 7.25 | dropped — no fetchable carrier rate card (the desk's probes of fedex.com, ups.com and odfl.com surcharge pages return navigation only), so the freight leg of the break-even has no anchor |
| OTIF root-cause decomposition by share (stockout vs credit hold vs master-data error vs carrier delay) | 8 | 7 | 5 | 7 | 6.9 | dropped — no measured source publishes the share of misses by cause; any decomposition would be invented |

## Notes for the verifier
- Rows 2–3 are two figures from one consultancy article, and rows 4–5 are two figures from one practitioner article: the six rows are four distinct documents on four hosts, not six independent studies.
- Row 1's arithmetic is reproducible by hand (0.98^10). The article may state the exponent rule, the 81.7% and the 66.8% from that row, and may compute the inverse rule (target order fill ^ (1 / lines per order)) because both inputs are stated in the sentence — but no other derived figure may be added.
- The article must not claim the independence model is exact: the same consultancy reports initial order fill running 10-15 full percentage points below the item fill rate, which is wider than the exponent alone predicts at a 2.25-line basket (0.90^2.25 = 78.9%, an 11-point gap) — that measured sentence rides in prose under row 3, not as its own row, because its own figure cell matched a neighbouring sentence.
- No retailer is named as buying on a line metric, and no chargeback percentage appears: this is about the arithmetic of completeness, not about a retailer's programme.
- Row 4's "82%" is the source's "around 82%" and row 4's basket is not stated — the implied 4.9 lines per order is the writer's own arithmetic and must be labelled as such, or left out.

## Gate result

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=6 fetched=6 sources=4 hosts=4 decision="sha1:56f4a86eb8" dedup="matched a prior artifact: 2026-10-19_your-30-exception-bill-" window_days=180 checked_at=2026-10-26T20:03:45+00:00 -->
<!-- evergreen-gate:end -->
