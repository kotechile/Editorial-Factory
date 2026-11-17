---
title: "Your Washer Now Costs 100,000 Calls"
vertical: smart_home_telemetry
kind: news
persona: pro_homeowner
one_big_thing: "The specification that now decides a home's running cost is not whether a device works with your hub but which interface answers without an account — SmartThings priced the cloud path to its appliances by the call and set a hard cutoff, while Nabu Casa priced a one-time box for the physical port."
date: 2026-11-17
slug: your-washer-100000-calls
synthesis: true
sources:
  - https://community.smartthings.com/t/changes-to-the-smartthings-integration-for-home-assistant-what-s-happening-and-what-you-need-to-do/311942
  - https://www.home-assistant.io/blog/2026/11/11/no-device-left-behind-home-assistant-connect-aux-2/
meta_title: "Your Washer Now Costs 100,000 Calls"
meta_description: "SmartThings put its cloud API on a 100,000-call monthly plan and set a December cutoff, eight days before Nabu Casa sold a $69 box for the port you own."
---

<!-- lead -->
SmartThings set a cutoff this month because it has begun charging for the road its appliances take into Home Assistant. In December the integration that ties a washer, a dryer or a fridge stops working unless its owner pays for a plan capped at 100,000 calls a month [1]. The same deadline, in the company's own words, also hits owners in countries where that plan is not sold [1]. Access now costs a bill nobody can price in advance. Eight days later, the local-first side put a box on sale whose only job is to reach devices that still answer on a wire.

<!-- tldr -->

## At a glance

- **The shift:** SmartThings now meters the cloud path to your appliances; Nabu Casa sells a one-off box for the physical one.
- **The number:** $69 — what that box costs once.
- **The risk:** The cutoff also hits owners who cannot buy the plan.

<!-- tension -->

## A meter on the cloud side

The plans went live on 4 November [2]. Home Assistant's 2 December release takes out the old integration and adds the new one, and the old one dies on 15 December [1]. The plan itself is "a flat monthly rate per developer account", and the announcement never prints the rate [2]. I read that gap as the most telling line in the document.

The free half of the table matters just as much. The phone app stays free, the routines inside it stay free, and the local drivers that run on a hub stay free [2]. The toll falls on one road only: a separate program that reads the same devices over the vendor's cloud. Control is free until it leaves the company's own app.

The cap is 100,000 calls a month, shared across ten apps on one account, and tied to the account rather than to a house [2]. That line explains the design. A household with a second home and a rental pays once, and a household running three chatty dashboards spends out of the same pot. What I keep coming back to is who this helps: an installed base of washers and fridges becomes steady income without one new appliance sold.

The counter-move landed eight days later. Nabu Casa shipped the Home Assistant Connect AUX-2, a deck-of-cards box with two serial ports, a Bluetooth relay, an audio jack, a slot for a radio stick and Power over Ethernet (PoE) [3]. Its pitch is plain: pull a device "off some hellish proprietary cloud and back under your control" [3]. One vendor put a meter on the road into its cloud. The other sold a key to the socket on the device.

## By the numbers

- **100,000 calls a month:** The cap on one developer account, shared across ten apps [2].
- **$69:** The one-time price of the box that reaches a serial, audio or Bluetooth port [3].
- **$35:** What a rival board already costs for the same casting and Bluetooth jobs [4].

<!-- tactical-insight -->

## Where the port decides

The box's own job list is the fair measure of it. It wakes an amplifier, drives solar or climate gear over a serial line, reads a Bluetooth thermometer through three walls, and holds a radio stick up wherever reception is stronger [3]. A washer has none of those ports, and neither does a fridge.

The Verge's review makes the same point from the other side. The device does nothing an ESP32 board and a few parts could not do, and "that's not a knock against the Aux-2. That's the whole point" [4]. What the money buys is a case, a power supply and firmware that already speaks the platform's language.

The math of the cap is worth stating on SmartThings' own numbers. A month of 100,000 calls is about 3,330 a day, and a program that asks one device for its state every 30 seconds makes 2,880 calls a day — 86% of that daily share. The plan rewards the event stream the vendor bundles inside it, and it punishes anything that asks on a timer.

The appliance path is not empty, but it is unofficial. A community integration called LocalThings reads Samsung washers, dryers and fridges straight off the home network with no cloud account, and checks the rest every 30 seconds where an appliance does not push its changes [5]. It is one developer's code page, not a word from the maker. What I'm watching next is whether the December release ships on time, and whether the country list appears before the deadline rather than after it.

<!-- nuanced-takeaway -->

## The catch

Two limits hold this argument down. The first is physical: the port rule protects gear that has a port, and the appliance in the headline has none, so its local control comes from a volunteer's code page or not at all. The second is symmetry — Nabu Casa runs its own cloud service, Home Assistant Link, so the local-first side is not a charity either [3].

Where I've landed is that the difference sits in what the fee is attached to. One charges for a road into hardware the owner bought and cannot otherwise reach. The other charges for ease the owner can turn down and still keep the house running. That is the line worth checking before the next appliance purchase, and the [utility meter's own hourly rows](/your-meter-bills-from-hourly-rows/) are a reminder that the billing unit was always picked upstream.

## Sources

- [1] SmartThings Community, "Changes to the SmartThings integration for Home Assistant…", 4 November 2026 — https://community.smartthings.com/t/changes-to-the-smartthings-integration-for-home-assistant-what-s-happening-and-what-you-need-to-do/311942
- [2] SmartThings Blog, "SmartThings API Additional Details for Developers and Business Partners", 30 October 2026 — https://blog.smartthings.com/smartthings-updates/smartthings-api-additional-details-for-developers-and-business-partners/
- [3] Home Assistant, "No device left behind: Home Assistant Connect AUX-2", 11 November 2026 — https://www.home-assistant.io/blog/2026/11/11/no-device-left-behind-home-assistant-connect-aux-2/
- [4] The Verge, "Hands on with Home Assistant's new 'smart home multi-tool'", 11 November 2026 — https://www.theverge.com/tech/1031601/home-assistant-connect-aux-2-hands-on
- [5] GitHub, "LocalThings: Control your Samsung appliances from Home Assistant over your home network" (README) — https://github.com/mbillow/localthings
