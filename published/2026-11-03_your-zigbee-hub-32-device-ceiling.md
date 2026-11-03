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
meta_title: "Your Zigbee Hub's Silent 32-Device Cap"
meta_title_source: "derived_from_title"
meta_description: "A Zigbee hub hands out 32 direct connections, and the cap is silent: the sensor that will not pair is often the one that arrived after the table filled."
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/your-zigbee-hub-32-device-ceiling/featured.jpg"
image_style: "component_assembly"
image_model: "nanobanana"
image_alt: "Zigbee Hub'S Silent 32-Device Cap. Brushed-steel coordinator rail with 32 child sockets, one occupied by a router module branching 15"
image_caption: "Zigbee Hub'S Silent 32-Device Cap: A firmware child table caps the network, not radio range."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->

A Zigbee hub hands out 32 direct connections, and the cap is silent: the sensor that will not pair is often the one that arrived after the table filled. The limit sits in the hub's radio firmware, not in the Zigbee standard, so two local-control stacks quote different ceilings for the same room [1][2]. Most mains-powered devices join as routers, and the documentation's own example has each router taking one of the coordinator's slots and contributing sixteen children of its own [1]. The number worth computing before any purchase is 32 plus 15 per router. A bigger hub will not move that number. The real cap is a table of children, not the reach of the radio.

<!-- tension -->

## The ceiling is a table

The Home Assistant documentation for its Zigbee Home Automation (ZHA) integration puts the upper limit at 32 direct children, with hundreds more able to join through routers [1]. Its worked example takes a current hub and three routers to 77 devices: 32 coordinator slots, minus the three routers, plus sixteen per router [1].

Zigbee2MQTT's answer page gives the same house different arithmetic. Its default firmware on a last-generation coordinator "supports 20 devices connected directly," and a device used as a router "has a limit of 21 devices" [2][3]. The page's own example starts at 15 rather than 20 and lands on 55 devices with two routers [2]. Run the page's own 20 through the same sum and the result is 60. Neither page tells a buyer which figure to trust.

I read those two pages side by side and came away convinced both are right: the gap is packaging, not physics. The cap lives in the chip and in the firmware image burned onto it, so one home fills at 55 devices while another, on a newer stick, runs fine at 77. Home Assistant's documentation says the older hardware "will not work properly" once the network has more than 15 to 20 devices [4], which is the band the Zigbee2MQTT example opens inside.

That is the part worth carrying into a purchase. A larger antenna will not raise this number, and a second hub is the expensive way to buy slots that a mains-powered plug adds for free.

## By the numbers

- **21600 seconds — Sleepy sensor alarm:** a battery-powered device with no activity is counted unavailable after six hours by default [5].
- **-80 dBm — Noise floor:** received signal at -80 and below marks a noisy link where messages may be lost, while -60 and above is strong [6].

<!-- tactical-insight -->

## Where the next router goes

The documentation's first move is to place routers close to one another rather than buy a stronger coordinator, because range comes from the mesh [7]. Radio noise is the other half of the same failure. The page names universal serial bus (USB) 3.x ports and their cables as known sources of trouble in the 2.4 GHz band [7]. The fix it gives is a shielded extension cable on a USB 2.0 port, holding the adapter away from the hub and the access point [7].

I checked the troubleshooting order against the buying order, and they run opposite ways: people reach for the antenna and the bigger hub first, while the cable and the cheap router come last.

Both faults arrive dressed as one. A device that goes quiet because its parent's table is full and one that goes quiet because the link is noisy both show the same unavailable badge. For the devices that hang off that radio, [smart home security](/categories/smart-home-security/) is where the buying decisions are gathered on this site.

<!-- nuanced-takeaway -->

## The catch

The sum counts slots, not metres. The same page says a real house will need far more routers than the example implies to extend coverage [7]. A table that admits 77 devices says nothing about whether the far end of the house can hear them.

A full table and a noisy link look the same from the sofa. Both show up as a device that drops out, and the default availability timeout [5] turns a sleeping sensor and a dropped one into the same red badge. The badge says a device is gone; it never says why. Router child aging compounds it: a sleeping device can be dropped from its parent's table and still keep working through that router, so a missing link on the map is not a lost device [8].

I would not call these ceilings promises. A mesh that stalls at 40 devices has likely run out of table, and the answer is a mains-powered router. A mesh that stalls at 12 has a noise problem, and the answer is a cable and a channel change. Same symptom, different repair.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Emporia Vue: How to Cut Energy Bills" -> /unveiling-the-emporia-vue-3-a-comprehensive-guide-to-home-energy-monitoring/ [same site (wellroost.com); same category; topical overlap: table] Link "Emporia Vue: How to Cut Energy Bills" in the section where the article touches table. -->
<!-- internal-link hint: "Your Hub's 4,292-Project Blind Spot" -> /your-hubs-4292-project-blind-spot/ [same site (wellroost.com); same category; topical overlap: hub's] Link "Your Hub's 4,292-Project Blind Spot" in the section where the article touches hub's. -->
<!-- internal-link hint: "Smart Home & Security" -> /categories/smart-home-security/ [same site (wellroost.com); same category; the article's own category hub (Smart Home & Security)] Link "Smart Home & Security" in the section where the article touches this topic. -->
## Related reading

- [Emporia Vue: How to Cut Energy Bills](/unveiling-the-emporia-vue-3-a-comprehensive-guide-to-home-energy-monitoring/) — more on Smart Home & Security
- [Your Hub's 4,292-Project Blind Spot](/your-hubs-4292-project-blind-spot/) — more on Smart Home & Security
- [Smart Home & Security](/categories/smart-home-security/) — more on Smart Home & Security
<!-- internal-links:end -->

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
