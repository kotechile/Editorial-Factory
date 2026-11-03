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
meta_title: "Your Leak Alert: A 24-Hour Gap"
meta_title_source: "derived_from_title"
meta_description: "Brownsville Public Utilities Board (BPUB) turned on water-leak alerts on 1 November, but the warning can repeat only once every 24 hours at best."
meta_description_source: "derived_from_lead"
---

<!-- lead -->

Brownsville Public Utilities Board (BPUB) turned on water-leak alerts on 1 November, but the warning can repeat only once every 24 hours at best [1]. At lower water use, the wait stretches to weekly or every two weeks [1]. The meter underneath is sold as real time; the alert is not.

The same week, the local-first side picked up two missing pieces. The beta notes for Home Assistant 2026.11 add LoRaWAN (long-range wide-area network), a radio built for battery-powered sensors, and support for Zigbee switches that run with no battery at all [2]. One system meters your water on the utility's clock; the other lets you set your own.

<!-- tension -->

## A fast meter, a scheduled alert

BPUB's project page makes three promises on one screen. The smart-meter network — advanced metering infrastructure (AMI) — is described as "enabling real-time usage monitoring" [3]. The customer benefit is "Daily Usage Data", and leak detection is sold as finding problems "early through continuous usage monitoring" [3]. Those are three different clocks on one page, and only one of them belongs to the homeowner.

The cadence the utility actually quotes is slower still. A BPUB spokesperson told KRGV (the Rio Grande Valley news station) that the notification "will be every 24 hours, weekly, or biweekly depending on the consumption" [1]. The fastest second look is a day away; the slowest is a fortnight. A supply line that has been weeping for two weeks is no longer a leak; it is a rebuild.

My read: this is a choice about customer service, not a limit in the meter. The same network carries outage reports, bills, and customer alerts. A utility sizes the alert queue around the calls it can handle, not the damage a hidden slab leak can do. Brownsville is spending real money on the sensor network, with no direct charge to the customer for the swap [4][5]. What the money buys is a meter that knows a great deal and a message that speaks once a day.

That gap is where an owner-run system matters. LoRaWAN is the radio standard for sensors that sit beyond Wi-Fi, in a crawlspace, a shed or a meter pit, and Home Assistant now speaks it through a ChirpStack or The Things Network server [2]. The platform's own guide puts the usable range in kilometres, not metres, and one leak reading fits inside a short message [2][6].

## By the numbers

- **110,000 meters — the rollout:** 52,000 electric and 58,000 water meters, funded as a $29.7 million investment [4][5].
- **51 bytes — one LoRaWAN message:** the payload Home Assistant's new transport carries across roughly five to fifteen kilometres [2][6].

<!-- tactical-insight -->

## Where the clock gets set

The people closest to this problem are not waiting for the utility to shorten its interval. They read the portal for the daily number, and some add a flow meter at the main water line that can close the valve without asking anyone. The flow rate a monitor must catch decides whether it pays, as [the desk's earlier leak-threshold piece](/water-leak-monitor-rate-threshold/) sets out, and that number belongs to the house rather than the utility.

What changed this week is where such a device can live. A LoRaWAN sensor does not need the home's Wi-Fi, so the crawlspace, the detached garage and the far end of an irrigation line stop being blind spots. Home Assistant's new network page lists each device with its signal strength, the last time it reported and its battery state [2]. The battery line is the one I'd watch, because a sensor that dies quietly is worse than no sensor at all.

Zigbee Green Power answers that worry from the other side. The platform now supports devices that run without a battery: a wall switch powered by the press, or a sensor that lives off the light in the room [2]. No battery means no maintenance visit, and no maintenance visit means a sensor can stay in the place where water enters the house for years. Whether a leak sensor takes that path is a product question, not a radio one, and the release notes name no such product.

The signal to watch next is disclosure. The records BPUB has published describe how often the notice repeats, not the flow that sets it off [1][3]. A utility that published that flow level would let an owner compare it with the rate a home monitor uses. Until then, the two clocks run side by side and only one of them can be inspected.

<!-- nuanced-takeaway -->

## The trade for a shorter wait

The utility alert is free, covers every customer in the service area, and asks nothing of the household beyond a phone number [1][3]. A local monitor costs money, needs power and a place to install, and can fail in ways nobody notices until the ceiling stains. Setting the clock yourself is not free; it is a trade of money and attention for a shorter wait.

The owner-run option is also younger than the pitch suggests. LoRaWAN arrived in Home Assistant as a beta feature dated 28 October, and the stable release is still ahead [2]. The radio carries one short message at a time, enough for a reading and not enough for a conversation, and a reporting interval is a setting on the device, not a fixed feature of the radio [6]. Nothing here says a LoRaWAN sensor detects a leak faster than the utility's meter. It says the owner can choose when the sensor speaks.

What I keep circling is the wording on the utility's own page. "Real-time" and "daily" sit one line apart, and both are true of different parts of the same system [3]. The meter is fast; the message is scheduled. That is not a scandal, and it is not a reason to refuse the free alert. It is a reason to read the schedule before treating the alert as the plan.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Emporia Vue: How to Cut Energy Bills" -> /unveiling-the-emporia-vue-3-a-comprehensive-guide-to-home-energy-monitoring/ [same site (wellroost.com); same category; topical overlap: every] Link "Emporia Vue: How to Cut Energy Bills" in the section where the article touches every. -->
<!-- internal-link hint: "Water Leak Monitors" -> /water-leak-monitor-rate-threshold/ [same site (wellroost.com); same category; topical overlap: leak] Link "Water Leak Monitors" in the section where the article touches leak. -->
<!-- internal-link hint: "Your Hub's 4,292-Project Blind Spot" -> /your-hubs-4292-project-blind-spot/ [same site (wellroost.com); same category; topical overlap: november] Link "Your Hub's 4,292-Project Blind Spot" in the section where the article touches november. -->
## Related reading

- [Emporia Vue: How to Cut Energy Bills](/unveiling-the-emporia-vue-3-a-comprehensive-guide-to-home-energy-monitoring/) — more on Smart Home & Security
- [Water Leak Monitors](/water-leak-monitor-rate-threshold/) — more on Smart Home & Security
- [Your Hub's 4,292-Project Blind Spot](/your-hubs-4292-project-blind-spot/) — more on Smart Home & Security
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The shift:** Brownsville's new leak alerts repeat daily at best, while Home Assistant added support for long-range, batteryless sensors where leaks start.
- **The number:** 24 hours is the fastest repeat BPUB quotes; weekly at low flow [1].
- **The risk:** The free alert runs on the utility's clock, not yours.

## Sources
[1] KRGV, "New Brownsville PUB program will notify customers of water leaks" (2026-10-20): https://www.krgv.com/news/new-brownsville-pub-program-will-notify-customers-of-water-leaks
[2] Home Assistant, "2026.11 Beta: A lot in store!" (2026-10-28): https://rc.home-assistant.io/blog/2026/10/28/release-202611/
[3] Brownsville Public Utilities Board, "Advanced Meter Infrastructure" project page (read 2026-11-03): https://www.brownsville-pub.com/projects/advanced-meter-infrastructure
[4] Kurrant, "Brownsville Public Utilities Board Adds Water Leak Alerts To Smart Meter Rollout" (2026-10-22): https://kurrant.com/kurrantly-news/brownsville-public-utilities-board-adds-water-leak-alerts-to-smart-meter-rollout
[5] City of Brownsville, "BPUB UPGRADING TO SMART METERS FOR BETTER ACCURACY AND FASTER RESPONSE" (posted 2025-12-15): https://www.brownsvilletx.gov/CivicAlerts.aspx?AID=2888
[6] Home Assistant, "The Things Network" integration documentation (read 2026-11-03): https://www.home-assistant.io/integrations/thethingsnetwork
