---
title: "Your Camera Eats 66 GB: The Hidden Cost"
vertical: smart_home_telemetry
persona: pro_homeowner
one_big_thing: "A camera you own keeps its own video, and that turns a subscription into a disk purchase sized by two spec-sheet numbers — the code rate that sets roughly 66 GB a camera a day at 4K defaults, and the recorder's total frame-rate ceiling at that resolution — while the separate network and the blocked cloud account cost no storage at all."
date: 2026-10-27
slug: your-camera-eats-66-gb-daily
archetype: evergreen
evergreen: true
---

<!-- lead -->
The camera over your porch ships writing 6,144 kilobits a second, because that default was set for a vendor's cloud archive rather than for the box in your closet [1]. At that rate one ultra-high-definition (4K) camera eats about 66 gigabytes (GB) a day, and the phone app never mentions it [1]. That hidden cost is the whole purchase, since the size of the disk you buy and the daily volume it has to hold both follow from a single line on a spec sheet.

<!-- tension -->

## The big picture:

A home camera does not report readings; it sends a stream, and a recorder has to take that stream apart and decide what to keep. The camera in this example ships at 3840x2160 pixels and 25 frames a second in a packed format called H.265 [1]. Its code rate, the amount of data it spends each second, ships at 6,144 kilobits a second inside a published range of 4,096 to 8,192 [1]. That one number decides the whole purchase.

A cloud plan hides the number, because the vendor keeps the disk. Keep the video yourself and you inherit the bill in bytes, and one camera at the shipped rate fills about 66 GB a day [1]. Frigate, the open-source recorder many owners land on, splits the job into three streams: one for detection, one for recording, one for viewing [2].

Detection does not need the full rate. The default is 5 frames a second, which the project calls correct for almost all cameras [2], and it runs on a lighter copy of the stream that ships at 256 kilobits a second [1]. Recording is the expensive job, and Frigate suggests setting that feed to 15 frames a second in the camera's own settings [2]. The reason it gives for that advice is playback smoothness and network load, not disk space [2], which is worth repeating because the tip travels as a storage fix.

The recorder carries its own printed limit, and it is not stated as a camera count. The two-bay box in this example lists a ceiling of 17 channels and 170 frames a second at 4K in the older H.264 format, and 20 channels with 200 frames a second in H.265 [4]. It also ships with 2 camera licences, and the page says more cameras need bought ones [4]. Its frame limit and its licences are what a buyer meets at the third camera rather than at the first.

So the network work, the separate subnet and the blocked cloud account, is the cheap half of this project. My read is that the expensive half is a sizing sum most buyers start after the box is on the shelf, with the drives picked to match a guess.

## By the numbers

- **66.4 GB — One camera, one day:** At the shipped 6,144 kilobits a second, a single 4K camera writes about 66 GB a day [1], so four cameras kept for a month reach 7.96 terabytes (TB).
- **44 to 88 GB — The code-rate range:** The same camera can be set anywhere from 4,096 to 8,192 kilobits a second [1], which moves the daily archive by a factor of two in either direction.
- **194.2 hours — The seller's own card table:** A 512 GB card holds 194.2 hours, about eight days for one camera [1], which works out near 63 GB a day and lets a buyer test any capacity claim.
- **170 frames — The recorder's ceiling:** The two-bay box publishes 4K H.264 at 17 channels and 170 frames a second [4], so four cameras at 25 frames a second sit at 100 of those 170.

<!-- tactical-insight -->

## What I'd watch:

What I keep coming back to is that the settings matter more than the shopping list, and the settings are visible before the box is out of its carton.

- **The recording policy:** A documented Frigate setup keeps every frame for 3 days, motion video for 7 and alert video for 30 [3], which buys a month of the events that matter rather than a month of an empty driveway.
- **The detection stream:** Detection runs on the light copy at the default rate [2], so the heavy stream is only paid for once, at the moment it is recorded.
- **The licence count:** The box ships with a couple of free licences and the rest are bought one at a time [4], which is a cost that turns up at the third camera rather than in the first quote.
- **The cross-check:** Any seller's capacity table can be divided by the code rate it also publishes [1], and a table that disagrees with the arithmetic is worth a second look.

The pressure lands on the third and fourth cameras rather than the first. One camera on a card is a weekend project, while four cameras kept for a month is a disk decision made with real money, and the arithmetic above is the only honest way to make it.

<!-- nuanced-takeaway -->

## The catch

My read starts with two numbers the seller publishes about its own product, because they do not quite agree. The code rate implies 66.4 GB a day, the card table implies 63.3 [1], and the gap near 5% comes from rounding plus guesses the page never states. Treat that pair as a budget band, and expect a real camera to land inside it rather than exactly on one figure.

The frame cap belongs to that box's own recorder app, tested with drives fitted and under nonstop recording [4]. It says nothing certain about a different recorder app on the same hardware, and nothing at all about a laptop doing the same job. Where the pipeline changes, the number changes with it.

The same trap shows up in the electrical panel, where a published threshold gets read as your own load: [Your Panel Doesn't Need More Amps: The 80% Test](/panel-upgrade-80-percent-test/). A spec sheet describes a limit under stated conditions, and a house is rarely those conditions.

None of this makes a camera private. A separate network and a blocked cloud account are worth doing, but neither of them changes the bytes a camera writes on a Tuesday afternoon.

<!-- tldr -->

## At a glance

- **The Big Shift:** A camera you own keeps its own video, and that turns a monthly plan into a disk purchase. The size of that disk is set by the camera's code rate and by the recorder's frame ceiling, not by the brand on the box.
- **Why It Matters:** Most local camera projects get planned from a camera list and an app, then hit the bill when the fourth camera arrives and the drives are already bought and installed.
- **What I'd Watch:**
  - **The code-rate setting:** It decides the daily volume, so it belongs in the purchase notes rather than in a settings menu nobody opens twice.
  - **The recording policy:** Keeping everything for a few days and events for a month costs far less than keeping everything for a month.
  - **The recorder ceiling:** Throughput and licences are published separately, and both run out long before the box looks full.
- **The Catch:** The vendor's own two estimates differ by a few percent, the ceiling applies to one recorder app, and none of this arithmetic makes a camera private.

<!-- internal-links -->

## Sources

[1] Reolink, RLC-810A security camera specifications (code rate, frame rate, resolution, microSD capacity table) — https://reolink.com/product/rlc-810a/
[2] Frigate 0.18 documentation, "Camera setup" (detection frame rate, recording and viewing streams) — https://docs.frigate.video/frigate/camera_setup/
[3] Frigate 0.18 documentation, "Recording" (retention policy: continuous, motion, alerts and detections) — https://docs.frigate.video/configuration/record/
[4] Synology, DiskStation DS224+ specifications (Surveillance Station licences and maximum IP cameras with total frames per second) — https://www.synology.com/en-us/products/DS224+
