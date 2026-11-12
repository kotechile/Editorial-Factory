# Evergreen Verified Brief: demand_sensing_advanced_sop — 2026-11-12

Companion to `2026-11-12_demand_sensing_advanced_sop_evergreen_brief.md` (gate PASS, 7/7 rows verified,
3 hosts: learn.microsoft.com, scmr.com, demand-planning.com). This file records the verbatims the
article was drafted against, so a later rewrite can be checked against the source's own words rather
than a paraphrase. It is not gated; the gate marker lives on the brief.

## Verbatims

1. **Microsoft Learn, master-planning performance** —
   "you can use the following formulas to calculate an initial value: If your industry is manufacturing:
   (Number of threads) = (Number of planned orders ÷ 1,000) Otherwise: (Number of threads) = (Number of
   items ÷ 1,000)".
   "In extreme cases, this difference might be as much as 30 minutes."
   "Time fences specify how far in the future master planning must calculate requirements. The larger the
   time fence is, the longer it takes master planning to run."
   "When you schedule master planning, don't schedule any other batch job at the same time. Be especially
   careful that you don't schedule any other heavy routines, such as inventory close, at the same time."

2. **Supply Chain Management Review, "Buffer or suffer" (Ponce, Duong & Holwerda, 2026-03-16)** —
   "This capstone analyzes the value of dynamic MEIO by running multiple planning scenarios for 61 SKUs
   across 31 nodes in our sponsor's retail network. Using Coupa's Supply Chain Guru … we modeled 18
   scenarios combining six update frequencies (annual to weekly) and three service level targets
   (90%, 95%, 99%)."
   "Dynamic MEIO reduced total inventory value by up to 63%—about $9.3 million annually—for just 61 SKUs.
   Even a conservative annual update cut working capital by 40%, freeing up cash without sacrificing
   service levels."

3. **Demand Planning / S&OP Blog (2024-02-22)** —
   "My team was brought in to optimize the inventory settings in their supply chain which had more than
   60 locations and 13 echelons. The project to right-size inventory resulted in a EUR 20 million saving".
   "Each item and location combination is assigned to one of the roughly 300 different groups … They now
   only review each group's safety stock factor instead of the safety stock for all 200,000 individual
   item/location combinations."

4. **Odoo 20.0 documentation, "Reordering rules"** (prose/Sources only — no digit-led cell is possible on
   this page) — "The scheduler is set to run once a day, by default."
   `Forecasted date = Current date + Vendor Lead Time + Horizon Days`.

## Arithmetic checked in the final

- 63% (best case, weekly) minus 40% (annual) = **23 points**, written as a ceiling ("at most 23 points"),
  never as an expectation.
- The 1,000 divisor is quoted as the documented *starting* value for thread count, not a performance law.
- "20 million euros" is the source's `EUR 20 million`, spelled out to keep the acronym gate clean.

## Refused at the brief stage (recorded so the refusal is auditable)

- The √N pooling law with a correlation term: `2026-10-19_four-warehouses-halve-stock`
  (meio_working_capital_tco) already argues it.
- The MEIO business case and its decay without re-tuning: that vertical's beat; only the
  parameter-governance number (200,000 → ~300 groups) is borrowed here, for a different claim.
