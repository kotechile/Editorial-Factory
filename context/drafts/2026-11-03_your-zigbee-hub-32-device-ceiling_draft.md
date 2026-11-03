---
title: "Your Zigbee Hub's Silent 32-Device Cap"
vertical: smart_home_telemetry
kind: evergreen
archetype: evergreen
evergreen: true
persona: pro_homeowner
one_big_thing: "A Zigbee hub's device limit is a firmware child table rather than radio range: the coordinator holds 32 direct children, most mains-powered devices join as routers that take one slot and add their own children, so the number to compute is 32 plus 15 per router — and the cap moves with the firmware, not with the antenna."
date: 2026-11-03
slug: your-zigbee-hub-32-device-ceiling
---

<!-- lead -->

A Zigbee hub hands out 32 direct connections, and the sensor that will not pair is often the one that arrived when the table was full. That cap is silent: it is set in the hub's radio firmware, not in the Zigbee standard, so two local-control stacks quote different numbers for the same house [1][2]. Most mains-powered devices join as routers, and in the docs' own example each router takes one of the coordinator's slots and brings sixteen of its own [1]. The real limit is a table of children, not the reach of the radio.

<!-- tension -->

## The ceiling is a table

The Home Assistant docs for its Zigbee Home Automation (ZHA) integration state the cap plainly: the library under it "has an upper limit that is 32 direct children", though hundreds of devices can still join through routers [1]. The worked example puts a current hub with three routers at 77 devices: 32 slots, less the three the routers hold, plus sixteen per router [1].

The second stack tells a different story in the same house. Zigbee2MQTT's answer page says its default firmware on a last-generation coordinator "supports 20 devices connected directly", and that a device used as a router "has a limit of 21 devices" [2][3]. Its own example starts at 15 instead of 20 and lands on 55 devices with two routers [2]. Run the page's own 20 through the same sum and you get 60. Neither page says which figure a buyer should trust, which is the useful part of reading them side by side.

My read: both pages are right, and the gap is packaging, not physics. The cap lives in the firmware image and the chip that runs it, so one home is full at 55 devices while another, with a newer stick, is fine at 77. Home Assistant's docs put the older hardware at 15 to 20 devices before it stops working well [4], which is the band the Zigbee2MQTT example opens inside.

That is the part worth carrying into a purchase. A bigger antenna will not raise this number, and a second hub is the costly way to buy slots that a mains-powered plug would have added for free.

## By the numbers

- **21600 seconds — Sleepy sensor alarm:** a battery-powered device with no activity is counted unavailable after 21600 seconds, which is six hours, by default [5].
- **-80 dBm — Noise floor:** received signal at -80 and below marks a noisy link where messages may be lost, while -60 and above is strong [6].
- **21 devices — Router table:** an older coordinator chip used as a router carries 21 children of its own [3].

<!-- tactical-insight -->

## Where the next router goes

The docs push the cheap fix first: put routers close to each other rather than chase one stronger coordinator, because range comes from the mesh [7]. The other half is radio noise, and the same page names universal serial bus (USB) 3.x ports and their cables as known sources of trouble in the 2.4 GHz band [7]. The fix it gives is a shielded extension cable on a USB 2.0 port, holding the adapter away from the hub and the access point [7].

What the field reports, and what the docs' own troubleshooting section repeats, is that these two faults arrive dressed as one. A device that goes quiet because its parent's table is full and one that goes quiet because the link is noisy both show up as the same unavailable badge. What I keep circling is how the buying order runs backwards: the antenna and the bigger hub come first, and the cheap router that settles the table comes last. For the devices that sit on that radio, [smart home security](/categories/smart-home-security/) is where the buying decisions are collected on this site.

<!-- nuanced-takeaway -->

## The catch

The sum counts slots, not metres. The docs say plainly that in practice you will need far more routers than the example implies to extend coverage [7]. A table that admits 77 devices says nothing about whether the far end of the house can hear them.

A full table and a noisy link also look the same from the sofa. Both show up as a device that drops out, and the default that decides when the software calls it unavailable runs in hours [5], so a sleeping sensor and a dropped one give the same red badge. The badge tells you a device is gone; it never tells you why. Router child aging adds to it: a sleeping device can be pulled from its parent's table without ever leaving the network [8].

Where I have landed: these ceilings are budgets, not promises. A mesh that stalls at 40 devices has likely run out of table, and the answer is a mains-powered router. A mesh that stalls at 12 has a noise problem, and the answer is a cable and a channel change. Same symptom, different repair.

<!-- tldr -->

## At a glance

**The shift:** A Zigbee hub's device limit is a firmware child table, not radio range.
**The number:** 32 direct children, plus 15 for each mains-powered router.
**The risk:** Capacity is not coverage, and a full table looks exactly like a noisy link.

## Sources

[1] Home Assistant — Zigbee Home Automation (ZHA) integration documentation, 2026.10.4, "Limitations / Using router devices to add more devices". https://www.home-assistant.io/integrations/zha/
[2] Zigbee2MQTT — FAQ, "I read that Zigbee2MQTT has a limit of 20 devices…". https://www.zigbee2mqtt.io/guide/faq/
[3] Zigbee2MQTT — FAQ, same answer, the router limit and worked example. https://www.zigbee2mqtt.io/guide/faq/
[4] Home Assistant — ZHA documentation, "Supported but not recommended Zigbee adapters" (deprecated coordinator firmware). https://www.home-assistant.io/integrations/zha/
[5] Home Assistant — ZHA documentation, "Global options" (availability timeouts). https://www.home-assistant.io/integrations/zha/
[6] Home Assistant — ZHA documentation, "How to interpret RSSI and LQI values". https://www.home-assistant.io/integrations/zha/
[7] Home Assistant — ZHA documentation, "Zigbee interference avoidance and network range/coverage optimization". https://www.home-assistant.io/integrations/zha/
[8] Home Assistant — ZHA documentation, "Router child aging" (sleepy end devices leaving a parent's child table). https://www.home-assistant.io/integrations/zha/
