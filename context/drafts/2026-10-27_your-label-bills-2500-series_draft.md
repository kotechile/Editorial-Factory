---
title: "Your Label's Bill: 2,500 Series"
vertical: enterprise_tech_leadership
persona: eng_leader
one_big_thing: "A monitoring bill is counted in time series, one per unique mix of a metric name and its label values, so a label whose values come from your customer data turns one metric into thousands of billable series and moves the bill after the code ships."
date: 2026-10-27
slug: your-label-bills-2500-series
archetype: evergreen
evergreen: true
---

<!-- lead -->
One line of measuring code can turn a single metric into 2,500 billable series. That count is the bill, because the tools meter series and not servers.

A series is one unique mix of a metric name and its label values. Prometheus writes that rule down in its own naming guide [1]. So a label whose values come from your data, and not from your design, adds to the count every time the traffic produces a value nobody has seen before.

<!-- tension -->

## The big picture:

The per-host rate is the number a buyer argues over, and it reads like a cap on spend. Most of the time it buys an allowance. The tool bundles a fixed pool of custom metrics with each watched host, counts that pool by the hour across the whole account, and bills anything past it as usage rather than at a listed rate [4].

Grafana Cloud sells the same quantity another way, as a rate per active series above a monthly fee [3]. The bit that stuck with me is what that gap does to two estates of the same size. A fleet of small hosts with light measuring is cheap on a per-host bundle. A handful of big hosts, with labels drawn from a customer list, is not.

Neither vendor hides anything. Both publish the meter, and both publish the counting rule next to the price. What drifts is the code. A label added in a pull request to make a dashboard easier to slice, holding a tenant name or a request number, is a standing addition to the count, and it ships with nobody costing it.

The old instinct was that monitor spend tracks the size of the estate. It tracks the shape of the data model instead. That is why a team can retire hosts and still watch the bill climb.

## By the numbers

- **2,500 series — One metric, three labels:** a metric split by method (5 values), status code (10) and endpoint (50) resolves to 5 × 10 × 50 distinct series. That is 250 times the cap Prometheus advises [2].
- **10 — The working cap:** the project says to keep a metric's tally of distinct series below ten, and to hold the few that pass it to a handful across the whole system [2].
- **$6.50 per 1,000 — The series rate:** at that rate the metric above costs $16.25 a month on its own, and the monthly plan fee includes 10,000 active series [3].
- **100 per host — The bundled pool:** the biggest tool includes 100 custom metrics per host on its standard plan, counted by the hour across the account, at $15 per host per month billed yearly [4].

<!-- tactical-insight -->

## What I'd watch:

My read is that this is a review problem wearing a buying costume, and the reviewers are the people who write the measuring code.

- **Label source:** whether a label holds a closed list the code owns, such as method, status or region, or an open list the data supplies, such as tenant, account or request. The open kind is the one that grows, and it is invisible on a dashboard.
- **The allowance against the estate:** hosts times the bundled pool is the only series number the rate card prints. A count above it is priced on a call with sales, so that gap is worth knowing before the renewal and not after [4].
- **Which meter fits the shape:** many small hosts suit the per-host bundle, and a few big hosts with rich labels suit a per-series rate. Both vendors print enough for a team to work out its own answer.
- **Where the detail goes instead:** log ingest is metered by the gigabyte on the same page as the series count [4]. Pushing a wide label into logs moves the bill rather than removing it, and that trade usually gets made in a hurry [2].
- **What the count does to a query:** Prometheus ties a large number of series to slower queries as well as higher cost, so the label that lifts the invoice also ages the dashboards [2].

<!-- nuanced-takeaway -->

## The catch:

The ten-and-100 guidance is project advice and not a measured limit. It says what keeps a time-series store healthy, not what a vendor will charge, and the gap between the two is the meter [2][3][4].

My read, held loosely: the sums are the part that lasts. A label's value count is a number a team can work out before a change merges, whoever meters it, and that count holds even when the rate and the vendor change.

The second limit is day-to-day. Wide detail is often what makes an outage debuggable, and cutting a label to cool a bill costs somebody a query at three in the morning. The cheaper trade is usually to keep the detail in traces or logs, where it is metered by volume and not by mix.

The same shift runs through [the $2.7 trillion AI bill that turned cost control into a buying requirement](/ai-spend-27t-cost-visibility-mandate/): what a platform charges for is more and more a property of how the buyer's system is built.

<!-- tldr -->

## At a glance

- **The Big Shift:** Monitor bills are counted in time series, one per unique mix of a metric name and its label values, so what a team pays depends on how it labels its data rather than on how many servers it runs.
- **Why It Matters:** The per-host rate reads like a cap and acts like an allowance. Anything past it is metered as usage, and the labels that lift a bill are usually added to make a dashboard easier to read.
- **What I'd Watch:** how the count moves as an estate changes shape.
  - **Label source:** whether a label holds a closed list the code controls or an open one the customer data supplies.
  - **The allowance:** the bundled pool per host, times the estate, is the only series number the rate card prints.
  - **Meter shape:** a per-host bundle against a per-series rate, which suit opposite estate shapes.
  - **The second copy:** detail moved into logs is metered by volume instead.
- **The Catch:** the caps are project advice rather than measured limits, the two price shapes cited are examples and not the market, and trimming a label costs debugging detail.

## Sources
[1] Prometheus, "Naming" best practices — https://prometheus.io/docs/practices/naming/
[2] Prometheus, "Instrumentation" best practices — https://prometheus.io/docs/practices/instrumentation/
[3] Grafana Labs, "Grafana Cloud pricing" — https://grafana.com/pricing/
[4] Datadog, "Pricing" — https://www.datadoghq.com/pricing/
