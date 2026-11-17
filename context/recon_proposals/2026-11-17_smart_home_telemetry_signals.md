# Signals: smart_home_telemetry — 2026-11-17
**Window:** 2026-10-18 → 2026-11-17
**Queries run:** 19 (8 date-agnostic web fan-outs across the vertical's six configured sources and five primary angles; 1 Hacker News Algolia `search_by_date` sweep on the window epoch plus a `home assistant` keyword follow-up; 1 intelligence-MCP pull via `home_lifestyle_intel_client.py --recent 30 --vertical smart_home_telemetry --format signals`, which returned 10 rows — three Wirecutter product guides, Remodelista interiors, a Canary Media permitting piece, an Ars Technica Microsoft 365 outage — none on the local-first/telemetry beat, so none was used; 6 primary-source fetches; 2 Discourse `.json` date lookups; 1 repository README fetch; 1 published-corpus de-dup grep).

**Window note (what was dropped, not softened).**
- **The SmartThings paid-API *story* is not new; the deadline is.** The 2026-11-03 sweep recorded "SmartThings' $4.99 API plan remains a June 2026 announcement (out of window)" and dropped it. The June announcement is still out of window and the $4.99 figure is old boilerplate elsewhere on the blog — it does **not** appear in this announcement, which publishes no rate at all. What is in-window is the **plan launch on 2026-11-04**, the **Home-Assistant-specific migration post of 2026-11-04**, and the **2026-12-15 cutoff** those two set. Rows 1–2 rest only on the in-window documents.
- **The Marketplace (HACS → Home Assistant Marketplace) retread was avoided.** It was published as `your-hubs-4292-project-blind-spot` on 2026-10-27 and the 2026-11-03 signals file flagged it as a retread. The 2026.11 release appears here only for its *action-history* telemetry feature (row 5), never for Marketplace.
- **EcoFlow's request to the `ha-ef-ble` maintainers** was posted 2026-10-01 — before the window opened — and re-surfaced on Hacker News 2026-10-22. The HN submission does not make the event fresh, so it is dated background, not a row.
- **Belkin Wemo (cloud off 2026-01-31), Devolo Home Control (2025-12-31), Wink, Insteon, Nest thermostat 1st/2nd gen, Google Dropcam** all re-surfaced in the sweep and are all outside the window; each was already carried or argued in earlier runs.
- **Matter 1.5 / 1.5.1** (2025-11 and 2026-03-31) is outside the window; the 2026 "Matter 2.0" pages that ranked for it are undated SEO material with no first-party record.
- Also read and set aside: SPAN/Schneider/Leviton smart-panel cost guides (all undated marketing pages — the $8,000–$15,000 service-upgrade figure appears in no primary document), CT-clamp buying guides on an Alibaba affiliate host, and the four "best smart water monitor" roundups (affiliate, no first-party specification).

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | SmartThings Blog — "SmartThings API Additional Details for Developers and Business Partners" | https://blog.smartthings.com/smartthings-updates/smartthings-api-additional-details-for-developers-and-business-partners/ | 2026-10-30 | Paid API plans go live **2026-11-04**. The **Developer Plan** is "a flat monthly rate per developer account" whose quota is "**up to 100,000 cloud API calls per month and up to 10 active app installs across locations**", tied to the developer account "not to individual physical hardware locations". The plan's own free/paid table lists "Direct Open Authorization (OAuth) Cloud API Calls (Individual Developer Use)" and "Business API Usage" as **Paid**, while "Local Edge Drivers, Profiles, & Hub Integrations" stay **Free**. Subscribers also get "Near real-time events via Server-Sent Events (SSE)". **No monthly price is stated anywhere in the announcement.** | Home Assistant is reclassified as a "custom OAuth App" and priced by the call | 92 |
| 2 | SmartThings Community — "Changes to the SmartThings integration for Home Assistant: what's happening and what you need to do" | https://community.smartthings.com/t/changes-to-the-smartthings-integration-for-home-assistant-what-s-happening-and-what-you-need-to-do/311942 | 2026-11-04 (created 2026-11-04T16:17Z; 2,301 views, 25 posts) | Key dates, verbatim: "**December 2, 2026:** Home Assistant release that removes the ability to configure the old integration and introduces the new one"; "**December 15, 2026:** Paid Developer Plan required. After this date, the current integration will no longer work with SmartThings." And the lockout clause: "The December 15, 2026 date applies to **all** Home Assistant users **including users in countries where the Developer Plan is not available**." Also: "Developer Plan users are allowed 100,000 calls/mo per account and up to 10 OAuth apps." | The cutoff is universal; the replacement plan is not universally buyable | 95 |
| 3 | Home Assistant Blog — "No device left behind: Home Assistant Connect AUX-2" | https://www.home-assistant.io/blog/2026/11/11/no-device-left-behind-home-assistant-connect-aux-2/ | 2026-11-11 | Nabu Casa launches Connect AUX-2 at "**$69 / €59**": PoE or USB-C power, Ethernet or Wi-Fi, two RS-232 serial ports, Bluetooth proxy, combo analog/digital audio jack, Grove port. Pitch verbatim: "The most sustainable device is the one you already own… use Connect AUX-2 to save a device from the scrap heap, or **pull it off some hellish proprietary cloud and back under your control**." Serial control targets "that old (but still functioning) solar or climate equipment"; TVs can be blocked from the internet and driven locally instead. "AUX-2 never sips more than a watt or two." | The counter-move is a one-off box, priced once, on the port you own | 90 |
| 4 | The Verge — "Hands on with Home Assistant's new 'smart home multi-tool'" | https://www.theverge.com/tech/1031601/home-assistant-connect-aux-2-hands-on | 2026-11-11 | Hands-on: setup by browser firmware flash then ESPHome discovery; restored a garage-fridge temperature alert after Aqara Zigbee sensors that "frequently drop connection… chew through coin cell batteries". On the value question, verbatim: "The Aux-2 doesn't do anything you couldn't do already with an ESP32 board and various accessories… **That's not a knock against the Aux-2. That's the whole point.**" Names a $35 Apollo Automations Cast-1 doing the casting/proxy jobs. Serial control (the inverter/TV path) "is the most intriguing feature" and was **not tested** in the review. | What the $69 buys is a port and a firmware, not a capability | 84 |
| 5 | Home Assistant Blog — "2026.11: A lot in store!" | https://www.home-assistant.io/blog/2026/11/04/release-202611/ | 2026-11-04 | The release adds a local record of what the system did: "Every action, on the record", "Live logs for each integration", "See what triggered it", "Follow a trace into the script it called", plus "Remove bad readings from your history" and backups on local drives. Also Matter cameras with two-way audio and LoRaWAN. (Marketplace appears in this release and is **not** used here — published 2026-10-27.) | The home server now keeps its own audit trail, unmetered | 78 |
| 6 | Home Assistant — Connect AUX-2 product page | https://www.home-assistant.io/connect/aux-2/ | 2026-11-17 (observation; standing page) | Product page states the serial, Bluetooth and audio roles and the $69/€59 price; sold by Nabu Casa as "one of the Open Home Foundation's commercial partners", whose work "helps fund its mission to keep smart homes private, sustainable, and shaped by you". | The vendor selling local control is the same one that could meter it | 70 |
| 7 | LocalThings — Home Assistant custom integration (README) | https://github.com/mbillow/localthings | 2026-11-17 (observation; standing repo) | "Control your Samsung appliances from Home Assistant over your home network, with no cloud account." Covers "washers, dryers, refrigerators, air conditioners, ovens"; "After setup, LocalThings never contacts Samsung's servers"; "Appliance that support push send changes as they happen. LocalThings checks the rest **every 30 seconds**"; setup needs the appliance's IP address. Maintained by one developer under a personal account, distributed through HACS. | The appliance escape hatch exists, is unofficial, and polls for what the cloud streams | 72 |

## Dating note
Rows 1 from 2026-10-30, rows 2 and 5 from 2026-11-04, rows 3 and 4 from 2026-11-11 all carry the publisher's own publication date inside the window. Rows 6 and 7 are standing pages with no publication date: their Date cell is the **observation date** (2026-11-17), and the event each describes is stated inside the claim cell. No row's claim is dated outside 2026-10-18 → 2026-11-17 except where the claim cell names a future date (2026-12-02, 2026-12-15) — those are scheduled events reported by the primary source on an in-window publication.

## Primary sources (corroboration — every URL an artifact may cite must appear in this file)

SmartThings leg:
- https://blog.smartthings.com/smartthings-updates/smartthings-api-additional-details-for-developers-and-business-partners/
- https://community.smartthings.com/t/changes-to-the-smartthings-integration-for-home-assistant-what-s-happening-and-what-you-need-to-do/311942
- https://developer.smartthings.com/smartthingsapi (the plan page the announcement points at for pricing and country availability)

Home Assistant / Nabu Casa leg:
- https://www.home-assistant.io/blog/2026/11/11/no-device-left-behind-home-assistant-connect-aux-2/
- https://www.home-assistant.io/connect/aux-2/
- https://www.theverge.com/tech/1031601/home-assistant-connect-aux-2-hands-on
- https://www.home-assistant.io/blog/2026/11/04/release-202611/

Reality-audit leg (the escape hatch that is not a contract):
- https://github.com/mbillow/localthings

## Dated background (not anchors — outside the window or not citable, kept for provenance)
- https://github.com/rabits/ha-ef-ble/discussions/521 (maintainer post 2026-10-01: EcoFlow asked the `ha-ef-ble` project to stop, citing an unsafe BLE protocol and a coming local API; re-surfaced on Hacker News 2026-10-22 — event predates the window)
- https://community.smartthings.com/t/a-new-enhanced-smartthings-api-experience/309947 (the June 2026 announcement topic: created 2026-06-23, 25,318 views, 331 posts — the sustained user objection, out of window)
- https://blog.smartthings.com/smartthings-updates/a-new-enhanced-smartthings-api-experience/ (June 2026 original announcement, out of window)
- https://www.belkin.com/support-article?articleNum=335419 (Wemo cloud shutdown 2026-01-31 — prior-era example, out of window)
- https://www.wespeakiot.com/devolo-ends-its-home-control-smart-home-system-cloud-services-to-shut-down-by-end-of-2025 (Devolo Home Control, cloud off 2025-12-31 — out of window)
- https://innovation.consumerreports.org/the-last-hurrah-how-to-handle-and-harden-unsupported-iot-devices (Consumer Reports on end-of-life device handling, 2026-05-20 — out of window; its "local API before disconnection" recommendation is background reasoning only)

## Candidate Synthesis Pairs


<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=7 candidates=0 heuristic=- window=2026-10-18..2026-11-17 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->

