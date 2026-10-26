---
title: "Ops leaders: Why 98% line fill ships 18% short"
vertical: sales_order_service_level_otif
persona: ops_leader
archetype: evergreen
evergreen: true
one_big_thing: "Order fill is not a blurrier copy of line fill — it is roughly line fill raised to the power of the lines on the order, so a 98% line fill is an 81.7% complete-order rate on a ten-line basket, and the cheapest points to buy back sit in the few SKUs that appear on the most orders rather than in more stock spread evenly."
date: 2026-10-26
slug: your-98-fill-rate-18-dont-ship
meta_title: "Ops leaders: Why 98% line fill ships 18% short"
meta_title_source: "derived_from_title"
meta_description: "One in five ten-line orders ships short, even though the desk's line fill reads 98%. At 98% per-line stock, 18.3% of ten-line baskets fail to ship complete…"
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/your-98-fill-rate-18-dont-ship/featured.jpg"
image_style: "technical_isometric"
image_model: "nanobanana"
image_alt: "The Math Of Short Orders. A ten-compartment industrial order routing tray with one empty slot in an isometric technical drawing."
image_caption: "The Math Of Short Orders: Why high line fill still leaves your orders short."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
One in five ten-line orders ships short, even though the desk's line fill reads 98% [1]. At 98% per-line stock, 18.3% of ten-line baskets fail to ship complete, and a twenty-line order drops to 66.8% [1].

Line fill tracks individual items, while order fill requires a perfect box. One missing stock-keeping unit (SKU) fails the whole shipment [1]. No push at the packing line closes that gap, because the math itself dictates the drop.

<!-- tension -->

## The big picture:

An order ships complete only if every line is in stock. That makes the order-level score the line rate raised to the power of the basket size [1].

A five-line order with one shortage still scores 80% on lines, but as baskets grow, the two numbers drift apart [1]. Customers do not feel a high line fill; they feel a box missing the exact item they needed [1].

My read is that this order-level metric remains the most under-reported number on the warehouse floor. One firm that publishes an order-level report calls it the best service metric there is. It also notes the figure is rarely used, because many teams file it as a stock measure [2].

Their client records reveal how wide the gap runs. A $30 million food business averaged 2.25 lines per order and called its backorder rate low, only to log an 11.5% failure rate when it finally counted complete orders [2].

At 2.25 lines, the math alone predicts an 11-point drop from a 90% line fill [1][2]. The reality is worse: complete orders run 10 to 15 points below the line rate [2]. My read is that shortages clustering on the same items account for the extra distance.

## By the numbers

- **88.5% — Order fill at 2.25 lines:** First-week order-level counting at a $30 million food business whose backorder rate looked low [2].
- **76.5% — Order fill against a 90% assumption:** One apparel company's first season after misreading a 10% backorder rate as good service [2].
- **96% — Line fill hiding an 82% order fill:** One industrial distributor where three or four slow-moving items sat on a huge share of orders [3].
- **92% to 98% — Quoted healthy band:** The range one logistics provider gives for fill rate, defining it strictly as an order-level number [4].

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 220" style="background:#0f172a; border-radius:8px; font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif; margin:16px 0; max-width:100%; height:auto;">
  <text x="20" y="36" fill="#f8fafc" font-size="16" font-weight="600">Ops leaders: Why 98% line fill ships 18% short</text>
  <text x="20" y="52" fill="#94a3b8" font-size="12">Figures as stated in this article&#x27;s own numbers section (verified figures, %)</text>
  <!-- Row 1 -->
  <text x="20" y="84" fill="#e2e8f0" font-size="13" font-weight="500">Order fill at 2.25 lines</text>
  <rect x="240" y="70" width="300" height="18" rx="4" fill="#1e293b"/>
  <rect x="240" y="70" width="265" height="18" rx="4" fill="#818cf8"/>
  <text x="515" y="84" fill="#f1f5f9" font-size="13" font-weight="600">88.5%</text>
  <text x="569" y="84" fill="#64748b" font-size="11">([2])</text>
  <!-- Row 2 -->
  <text x="20" y="132" fill="#e2e8f0" font-size="13" font-weight="500">Line fill hiding order fill</text>
  <rect x="240" y="118" width="300" height="18" rx="4" fill="#1e293b"/>
  <rect x="240" y="118" width="288" height="18" rx="4" fill="#818cf8"/>
  <text x="538" y="132" fill="#f1f5f9" font-size="13" font-weight="600">96%</text>
  <text x="592" y="132" fill="#64748b" font-size="11">([3])</text>
  <!-- Row 3 -->
  <text x="20" y="180" fill="#e2e8f0" font-size="13" font-weight="500">Quoted healthy band</text>
  <rect x="240" y="166" width="300" height="18" rx="4" fill="#1e293b"/>
  <rect x="240" y="166" width="276" height="18" rx="4" fill="#818cf8"/>
  <text x="526" y="180" fill="#f1f5f9" font-size="13" font-weight="600">92%</text>
  <text x="580" y="180" fill="#64748b" font-size="11">([4])</text>
</svg>

<!-- tactical-insight -->

## What I'd watch:

The industrial distributor case is the one to copy. Their line fill looked excellent on paper, but the true order fill sent management into a panic [3].

The root cause was not broad stock trouble. Three or four slow-moving items appeared on a huge share of orders, and fixing those few lines moved the order number sharply [3].

What strikes me here is that this requires a ranking most planning tools omit: SKUs sorted by how many orders they touch, rather than how badly they fill. A short line that appears on one order in fifty barely dents the score, but the same short line on one order in three holds it down entirely.

- **Order-level scoring:** Operators mark each order as a complete hit or a miss, rather than averaging lines and calling it service [3].
- **Basket size splits:** A ten-line order and a two-line order do not belong in one figure, because the exponent math punishes them differently [1].
- **Inverse target math:** A 95% complete-order target requires 99.5% per-line stock at ten lines, and 99.7% at twenty lines [1].
- **Tail checks by reach:** The SKUs that recur across large baskets decide the final score, and they are usually slow movers with chronic shortages rather than the big-volume items a planner watches [3].

I'd watch whether this order-level number survives a meeting with finance. It is easy to pull from order history and hard to argue with once the biggest customers appear in the data. 

<!-- nuanced-takeaway -->

## The catch

The math is a model, not a measurement. It assumes every line is in stock on its own, but real shortages cluster on the same items in the same weeks.

That is why the measured gap of 10 to 15 points runs wider than the model at small baskets [2]. I read the baseline math as a floor, never as a forecast for a named customer.

The client figures come from one firm's unnamed jobs, not a broad survey. They prove the gap is real without sizing it for your business [2]. The distributor case ran in March 2018, serving as a lasting picture of the mechanic rather than a current benchmark [3]. The quoted healthy band is one provider's rule of thumb, not an industry census [4].

Then there is cost, which this math does not settle. Buying 99.5% per-line stock to hit a 95% complete-order target is a massive inventory decision.

The exponent math tells you what it takes, but it does not tell you whether the customer is worth the cash. The same failure, priced per repair, frames the other half of this choice: [Your $30 Exception Bill Is Wrong](/your-30-exception-bill-is-wrong/) puts a wage on each broken order rather than on the missing line.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "49.9% On Time: Shippers Stuck in the Gap" -> /shippers-stuck-in-the-gap/ [same site (aichieve.net); same category; topical overlap: ships] Link "49.9% On Time: Shippers Stuck in the Gap" in the section where the article touches ships. -->
<!-- internal-link hint: "63.6% OTIF: Your Hidden Quantity Gap" -> /your-hidden-quantity-gap/ [same site (aichieve.net); same category; topical overlap: orders] Link "63.6% OTIF: Your Hidden Quantity Gap" in the section where the article touches orders. -->
<!-- internal-link hint: "7 Days Notice Rewrites Your Duty" -> /7-days-notice-rewrites-your-duty/ [same site (aichieve.net); same category; topical overlap: line] Link "7 Days Notice Rewrites Your Duty" in the section where the article touches line. -->
## Related reading

- [49.9% On Time: Shippers Stuck in the Gap](/shippers-stuck-in-the-gap/) — more on Supply Chain & Operations
- [63.6% OTIF: Your Hidden Quantity Gap](/your-hidden-quantity-gap/) — more on Supply Chain & Operations
- [7 Days Notice Rewrites Your Duty](/7-days-notice-rewrites-your-duty/) — more on Supply Chain & Operations
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** Order fill counts only the orders that shipped complete, so it falls as line fill raised to the power of the lines per order. A 98% line fill works out to an 18.3% failure rate on a ten-line basket [1].
- **Why It Matters:** The line metric is the one most order desks report, while complete orders run 10 to 15 points lower in one firm's records [2]. The service a customer actually feels can be far worse than the morning report claims.
- **What I'd Watch:** How the number is built, and which SKUs carry the weight.
  - **Order-level scoring:** Each order counted as a strict hit or miss, not as an average of its lines [3].
  - **Basket splits:** The biggest orders scored separately, because the math punishes them the hardest [1].
  - **Reach ranking:** SKUs sorted by how many orders they sit on, which is where the cheapest points are [3].
- **The Catch:** The math assumes lines are in stock independently and real shortages cluster, so it sets a floor rather than a forecast. The cost of buying those last few percentage points is not settled here.

## Sources

[1] Inventoros — "Order Fill Rate: Definition, Formula, and How to Calculate It" (19 June 2026) — https://inventoros.com/blog/order-fill-rate
[2] F. Curtis Barry & Co. — "Use Initial Order Fill Rate to Measure Your Customer Service" (undated, retrieved 26 October 2026) — https://www.fcbco.com/blog/use-initial-order-fill-rate-to-measure-customer-service
[3] Benchmarking Success (Rob O'Byrne) — "Understanding Fill Rate KPIs: Line Fill Rate" (March 2018) — https://www.benchmarkingsuccess.com/understanding-fill-rate-kpis-line-fill-rate
[4] DCL Logistics — "Fill Rate: Definition, Formula, and How to Calculate It" (7 July 2026) — https://dclcorp.com/blog/fulfillment/fill-rate

## Gate report

- PASS — lead: Delivers the core stakes and inverse relationship immediately in the first sentence without throat-clearing, keeping figures tight to the explanation.
- PASS — tension: Frames the shift with the mandatory 'The big picture' H2 and a single direct sentence, backed by a cleanly formatted 'By the numbers' section isolating four key figures.
- PASS — tactical-insight: Uses clear observations instead of commands, formats a strong bulleted list with bold lead-ins, and includes a first-person observer cue.
- PASS — nuanced-takeaway: Opens with 'The catch' H2, highlights the model's clustering limitations clearly, includes a first-person cue, and closes on a direct decision link.
- PASS — tldr: Strictly follows the 4-part Smart Brevity schema under 'At a glance', translating the complex exponent math into plain English for an executive audience.
