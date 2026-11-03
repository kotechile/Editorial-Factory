---
title: "Your Leak Alert: A 24-Hour Gap"
vertical: smart_home_telemetry
kind: news
persona: pro_homeowner
one_big_thing: "A utility's smart-meter leak alert is a notification schedule, not a detector: the cadence belongs to the utility, and only an owner-run sensor lets you choose the interval and the threshold that match what a leak costs."
date: 2026-11-03
slug: your-leak-alert-24-hours-at-best
synthesis: true
sources:
  - https://www.krgv.com/news/new-brownsville-pub-program-will-notify-customers-of-water-leaks
  - https://rc.home-assistant.io/blog/2026/10/28/release-202611/
---

<!-- lead -->

The Brownsville Public Utilities Board (BPUB) turned on leak alerts for its water customers on 1 November. The message your phone can receive runs on a schedule: every 24 hours at best, and weekly or biweekly when the flow is lower [1]. The meter underneath is sold as real time. The alert is not.

In the same week, the local-first layer picked up two pieces it had been missing. The beta notes for Home Assistant 2026.11 add LoRaWAN, a long-range radio built for battery-powered sensors, and support for Zigbee switches that run without a battery at all [2]. One layer meters your water on the utility's clock. The other lets you set a clock of your own.

<!-- tension -->

## A fast meter, a scheduled alert

BPUB's own project page makes three promises on one screen. The advanced metering infrastructure (AMI) system is described as "enabling real-time usage monitoring", the customer benefit is "Daily Usage Data", and leak detection is sold as identifying problems "early through continuous usage monitoring" [3]. Those are three different clocks on one utility page, and only one of them belongs to the homeowner.

The cadence the utility actually quotes is slower still. A BPUB spokesperson told KRGV (the Rio Grande Valley news station) that the notification "will be every 24 hours, weekly, or biweekly depending on the consumption" [1]. The fastest the system will look again is a day later; the slowest is a fortnight. A supply line that has been weeping for two weeks is no longer a leak. It is a rebuild.

My read is that this is a service-design choice, not a limit in the meter. The same AMI network supports outage reporting, billing reads and customer alerts, and a utility sizes the alert queue around the calls it can handle rather than the damage curve of a slab. Brownsville is spending real money on the sensing layer: about 52,000 electric meters and 58,000 water meters, funded as a $29.7 million investment, with no direct charge to the customer for the swap [4][5]. What the money buys is a meter that knows a great deal and a message that speaks once a day.

That gap is where the local-first layer becomes relevant. LoRaWAN is the radio protocol for sensors that sit beyond Wi-Fi, in a crawlspace, a shed or a meter pit, and Home Assistant now speaks it through a ChirpStack or The Things Network server [2]. The platform's own documentation puts the envelope at roughly five to fifteen kilometres of reach on 51 bytes a message [6]. A leak signal fits inside 51 bytes with room to spare.

## By the numbers

- **110,000 meters — the rollout:** 52,000 electric and 58,000 water meters, funded as a $29.7 million investment [5].
- **24 hours at best — the alert cadence:** the fastest repeat BPUB describes, stretching to weekly or biweekly at lower consumption [1].
- **51 bytes — one LoRaWAN message:** the payload Home Assistant's new transport carries across roughly five to fifteen kilometres [2][6].

<!-- tactical-insight -->

## Where the clock gets set

The people closest to this problem are not waiting for the utility to shorten its interval. They read the portal for the daily number, and some add a flow device at the main that can close the valve without asking anyone. The flow rate a monitor must catch decides whether it pays, as [the desk's earlier flow-threshold piece](/water-leak-monitor-rate-threshold/) sets out, and that number belongs to the house rather than the utility.

What changed this week is where such a device can live. A LoRaWAN sensor does not need the home's Wi-Fi, so the crawlspace, the detached garage and the far end of an irrigation line stop being blind spots. Home Assistant's new network page lists each device with its signal strength, the last time it reported and its battery state [2]. The battery line is the one I would watch, because a sensor that dies quietly is worse than no sensor at all.

Zigbee Green Power answers that worry from the other side. The platform now supports devices that run without a battery: a wall switch powered by the press, or a sensor that lives off the light in the room [2]. No battery means no maintenance visit, and no maintenance visit means a sensor can stay in the place where water enters the house for years. Whether a leak-specific device ships on that profile is a product question, not a protocol one, and the release notes name no such product.

The signal to watch next is disclosure. BPUB has not published the flow threshold that triggers its notice, only the cadence at which the notice repeats [1]. A utility that published the threshold would let an owner compare it with the rate his own monitor uses. Until then, the two clocks run side by side and only one of them can be inspected.

<!-- nuanced-takeaway -->

## The catch

The utility alert is free, covers every customer in the service area, and asks nothing of the household beyond a phone number [1][3]. A local monitor costs money, needs power and an installation, and can fail in ways nobody notices until the ceiling stains. Setting the clock yourself is not free. It is a trade of capital and attention for a shorter interval.

The local layer is also younger than the pitch suggests. LoRaWAN arrived in Home Assistant as a beta feature dated 28 October, and the stable release is still ahead [2]. The radio carries 51 bytes at a time, which is enough for a reading and not enough for a conversation, and a reporting interval is a setting on the device rather than a property of the protocol [6]. Nothing here says a LoRaWAN sensor detects a leak faster than the utility's meter. It says the owner can choose when the sensor speaks.

What I keep circling is the wording on the utility's own page. "Real-time" and "daily" sit one line apart, and both are true of different parts of the same system [3]. The meter is fast; the message is scheduled. That is not a scandal, and it is not a reason to refuse the free alert. It is a reason to read the cadence before treating the alert as the plan.

<!-- tldr -->

## At a glance

- **The shift:** Brownsville's new leak alerts repeat daily at best, while Home Assistant just added the long-range, batteryless sensors that can sit where leaks start.
- **The number:** 24 hours is the fastest repeat BPUB quotes; weekly or biweekly at lower flow [1].
- **The risk:** the free alert is a backstop on the utility's clock, not a detector on yours.

## Sources
[1] KRGV, "New Brownsville PUB program will notify customers of water leaks" (2026-10-20): https://www.krgv.com/news/new-brownsville-pub-program-will-notify-customers-of-water-leaks
[2] Home Assistant, "2026.11 Beta: A lot in store!" (2026-10-28): https://rc.home-assistant.io/blog/2026/10/28/release-202611/
[3] Brownsville Public Utilities Board, "Advanced Meter Infrastructure" project page (read 2026-11-03): https://www.brownsville-pub.com/projects/advanced-meter-infrastructure
[4] Kurrant, "Brownsville Public Utilities Board Adds Water Leak Alerts To Smart Meter Rollout" (2026-10-22): https://kurrant.com/kurrantly-news/brownsville-public-utilities-board-adds-water-leak-alerts-to-smart-meter-rollout
[5] City of Brownsville, "BPUB UPGRADING TO SMART METERS FOR BETTER ACCURACY AND FASTER RESPONSE" (posted 2025-12-15): https://www.brownsvilletx.gov/CivicAlerts.aspx?AID=2888
[6] Home Assistant, "The Things Network" integration documentation (read 2026-11-03): https://www.home-assistant.io/integrations/thethingsnetwork
