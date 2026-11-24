---
title: "Your Substation Waits 55 Months"
vertical: nhil_infrastructure_ops
persona: it_ops_leader
kind: evergreen
archetype: evergreen
evergreen: true
date: 2026-11-24
slug: your-substation-waits-55-months
one_big_thing: "The median wait from queue request to a live feed has doubled to over four years, and most of the power that ever applied withdrew without one — so the substation decision is a five-year money bet made now, not a detail settled when the racks are ordered."
meta_title: "Your Substation Waits 55 Months"
meta_title_source: "derived_from_title"
meta_description: "The median queue request now takes over four years to a live feed, and 77% of the power that applied withdrew. Your build clock is the grid queue, not the hardware roadmap."
sources:
  - https://www.osti.gov/biblio/3008763
  - http://rmi.org/resources/pjms-speed-to-power-problem-and-how-to-fix-it
  - https://www.latitudemedia.com/news/the-us-interconnection-queue-is-twice-its-installed-capacity
---

Your Substation Waits 55 Months

The clock on your next build is not the chip roadmap — it is the queue for a grid feed, where the median wait has doubled from under two years to over four [1]. A feed bigger than 200 megawatts took 55 months to go live [3]. By the time racks are ordered, the power call was supposed to be settled years earlier. It rarely is. The queue's own math is why.

<!-- tldr -->

## At a glance

This is about the wait between asking a utility for a power feed and getting one, and it concerns anyone planning a data hall, an edge site or a plant build. Most of the power that applies never gets built: drop-outs, not approvals, set the odds you plan against.

<!-- /tldr -->

<!-- tension -->

## The queue quietly became the build schedule

The waiting grew in steps, and each one resets what a build plan may assume. Projects that entered the queues before 2008 went live in under two years. Projects built in 2015 took about three. Projects reaching service in 2023 took about five [3], and the 2025 federal report puts the median for 2018–2024 builds at over four years [1]. What sits behind that climb? The queue turned into a lottery. Of all the power that applied from 2000 to 2019, 77% had dropped out by the end of 2024 and only 13% went live [1]. An application is cheap next to the value of holding a place in line, so developers apply early and often, and every serious request waits behind a crowd of hedged ones.

I read the two reports back to back before the pattern was plain to me: the queue is not slow because utilities are lazy. It is slow because it is full of requests nobody expects to survive.

<!-- /tension -->

## By the numbers

- **77% dropped out:** The share of power that applied from 2000–2019 and never went live [1].
- **55 months to live:** The median span for feeds over 200 megawatts, against 4-plus years past 100 [3].
- **544-day study:** One regional grid operator's completed cluster study, filed against a 540-day limit [2].

<!-- tactical-insight -->

## Where this bites

The cost lands on sequencing. The largest US regional grid operator now takes about eight years to bring a new plant online, while it runs its own power auctions on a two-to-three-year horizon [2]. A team that orders servers first and asks for the feed second has simply scheduled the wait after the spend — the worst possible ordering. From what the teams closest to the queue have chosen to do: apply earlier than feels right, treat the deposit as money spent buying an option with known drop-out odds, and pair the queue entry with power made on site, so the site can run while the feed matures. That bridge has its own rules to clear — see [The 40 kW Line: Why the AI Rack Is a Building Project](/rack-power-density-ceiling-build-before-you-buy/) for why the cooling and feed work is a dated build in its own right. The signal that answers the open question for your region is the grid operator's own study calendar, not a vendor's ship date.

<!-- /tactical-insight -->

<!-- nuanced-takeaway -->

## The catch

I will say the hard part plainly: no reform fixes your five-year wait. Federal queue reforms are in place, but the 2025 report finds it too early to measure their effect [1], and the first post-reform study cycle at that grid operator still took 544 days against a 540-day limit [2] — a reform meeting its target is not a queue that clears. So if your load truly needs the grid, the honest math treats your request as one of the 77% until it is not, and keeps the on-site bridge funded and permitted. The call was never "substation or no substation." It is whether you can afford to be wrong twice — once waiting for the feed, once waiting for the bridge.

<!-- /nuanced-takeaway -->

## Sources

- [1] Lawrence Berkeley National Laboratory, "Queued Up: 2025 Edition" (abstract) — https://www.osti.gov/biblio/3008763
- [2] RMI, "PJM's Speed to Power Problem and How to Fix It" — http://rmi.org/resources/pjms-speed-to-power-problem-and-how-to-fix-it
- [3] LatitudeMedia, "The US interconnection queue is twice its installed capacity" — https://www.latitudemedia.com/news/the-us-interconnection-queue-is-twice-its-installed-capacity
