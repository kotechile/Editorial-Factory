---
title: "19 Minutes: Your Spot Discount's Real Bill"
vertical: workstation_compute_economics
kind: evergreen
archetype: evergreen
evergreen: true
persona: infra_engineer
one_big_thing: "Spot cards are priced up to 91% below on-demand but come back on a warning measured in seconds, so the number that decides the rental is the checkpoint gap — the square root of twice the failure gap times the write cost, about 19 minutes at Meta's measured failure rate with a one-minute write."
date: 2026-11-17
slug: 19-minutes-your-spots-real-bill
meta_title: "19 Minutes: Your Spot Discount's Real Bill"
meta_description: "A spot card hour costs up to 91% less and can vanish on a 30-second warning. Price the hours the job loses, not the hours it rents: save every 19 minutes."
---

<!-- lead -->

Spot machines (rented cloud computers a provider can take back at short notice) are the cheapest way to hire a graphics card by the hour, and the saving rests on a number that never shows up in the quote. That number is how much work a job throws away each time a provider takes the machine back. Do the math on the failure rate and the write time, and the discount's real bill comes due 19 minutes into the run — the gap between saves, when a save takes a minute. A job that writes less often is buying a cheaper clock, not a cheaper run.

<!-- tldr -->

## At a glance

- **The shift:** Rented cards now come back on a warning of 30 seconds or less.
- **The number:** 19 minutes between saves at Meta's measured failure rate.
- **The risk:** A save slower than the gap never catches up with the failures.

<!-- tension -->

## The Clock Is Not The Notice

The rule that prices this has been in use for fifty years [1]. It answers a narrow question: how often should a long job save its state, when the machine can fail mid-run? Save too often and the writes eat the clock. Save too rarely and every failure throws away hours. The answer is the square root of twice the failure gap times the write cost [1]. It has stayed the working rule ever since, for machines that fail more often than the job ends.

Two published runs give that rule real numbers. A training run the size of the paper's example takes about 35 days. At a one-hour failure gap it would take roughly 840 stops, and saving every half hour would throw away about half the compute [1]. Meta published the other end of the scale for Llama 3: 466 stops in a 54-day span of pre-training, 419 of them unexpected, while the run still held above 90% effective training time — the share of elapsed time spent on useful work rather than on restarts [2].

What I find hard to square is how rarely this math reaches a rental decision. Teams compare the spot rate with the on-demand rate, accept that a machine can vanish, and learn in week three that the only thing between a discount and a deadline is how often the job writes to disk. A warning with 30 seconds on it is not a grace period. It is permission to stop cleanly. The bill for the discount is paid in minutes, not in dollars.

<!-- By the numbers -->

## By the numbers

- **3.09 hours:** Llama 3's failure gap, from 1,296 hours of pre-training split by 419 unexpected interruptions [2].
- **840 interruptions:** what a 35-day run takes at a one-hour gap, where half-hour saves throw away half the compute [1].
- **91%:** the most Google's Spot price can save against on-demand, and it can change daily [3].

<!-- tactical-insight -->

## What The Fleet Teams Assume

Meta's operators plan for failure instead of hoping to avoid it. Their reliability write-up treats at least one interruption a day as normal, and holds effective time above 90% anyway [2]. That is the stance the discount is priced for: a job that can lose a few minutes and keep going, not a job that hopes to finish in one sitting.

The vendor rules make the timer mandatory. Google's older preemptible machines stop after 24 hours whether or not anything failed [4]. Google's Spot machines and Azure's reclaim with seconds left — 30 seconds in Azure's own docs, and with no service-level guarantee at all [5]. I would want the write time before trusting any of that. A save that takes four minutes cannot act on a 30-second warning.

This is a sizing argument, not a discount argument. The gap grows with the square root of the write cost. A save that takes five minutes pushes the gap to 43 minutes at Llama 3's failure rate, and a ten-minute save pushes it past an hour. Write cost follows model size and disk speed, so the discount is easiest to keep on the models that are cheapest to own outright.

<!-- nuanced-takeaway -->

## Where The Formula Bends

My read, held loosely: 19 minutes is a starting point, and the shape of the curve matters more than the point. The formula is a first-order approximation [1]. A team that lands at 30 minutes instead of 19 has not made an error worth a rewrite, because the cost of a wrong gap rises slowly on either side of the best value.

The bigger caution is where the failure rate came from. Llama 3's numbers describe a very large fleet, where one failure every 3.09 hours was measured across thousands of cards at once [2]. A four-card rented job fails less often, so its own gap is longer, and the fleet figure errs toward saving too much. That error is cheap. The reverse is not: borrow a quiet month as an estimate, and a run finds out halfway through that it was luck.

The local box is the other side of the question. A workstation gets no reclaim warning and no hourly meter, but it does have a failure rate, and the same rule applies to it. The [payback model that sets a workstation against the rental spread](/local-ai-payback-cloud-gpu-spread/) prices the hours you pay for. The interval rule prices the hours you lose, and only the rented lane loses them to somebody else's schedule.

## Sources
- [1] "Optimal Checkpoint Interval with Availability as an Objective Function" (derivation and worked example of the Young/Daly interval), read 2026-11-17: https://arxiv.org/html/2410.18124v1
- [2] "The Llama 3 Herd of Models" (pre-training reliability section: interruptions and effective training time), read 2026-11-17: https://arxiv.org/html/2407.21783v1
- [3] Google Cloud, "About Spot VMs" (discount ceiling and daily price change), read 2026-11-17: https://cloud.google.com/compute/docs/instances/spot
- [4] Google Cloud, "Preemptible VM instances" (24-hour maximum and preemption notice), read 2026-11-17: https://cloud.google.com/compute/docs/instances/preemptible
- [5] Microsoft Learn, "Azure Spot Virtual Machines" (30-second eviction notice, no SLA), read 2026-11-17: https://learn.microsoft.com/en-us/azure/virtual-machines/spot-vms
