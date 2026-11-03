# Evergreen Brief: smart_home_telemetry — 2026-11-03

**Archetype:** evergreen
**Vertical:** smart_home_telemetry
**Persona:** pro_homeowner
**Decision the reader is facing:** When a matured Zigbee network starts dropping devices — whether to replace the coordinator with a "better" one, or to add mains-powered routers — a decision that bites the first time a sleepy sensor reads `unavailable` for six hours and the owner diagnoses a dead device instead of a full child table.
**Durability:** The arithmetic outlives every product cited here: a Zigbee coordinator hands out a finite number of direct-child slots, a mains-powered device acting as a router costs one of those slots and contributes its own child table, so capacity is `direct children + routers × (router children − 1)`. The ceilings themselves are as of 2026-11-03, read from the Home Assistant 2026.10.4 ZHA documentation and the Zigbee2MQTT FAQ, and they are firmware and stack properties rather than version properties — the same coordinator class is documented at 15-20, 20 and 32 direct children depending on which firmware it is running. Re-read both pages once a year; the rule and the two worked examples do not move, and any figure a reader recomputes from their own adapter's child table stays correct even after the docs change.
**De-dup:** `2026-10-27_your-camera-eats-66-gb-daily` is this vertical's nearest prior evergreen artifact (seven days ago, the zero-cloud camera archive: bytes per day, licence count, decode ceiling), and `2026-10-20_monitor-77-percent-guess-where-it-fails` is the one before it (what an inferred appliance number may be spent on). Neither sizes a radio network: the camera piece is a storage and licence budget for a recorder, the monitor piece is a measurement-versus-model argument about one instrument, the panel piece (`2026-10-13_panel-upgrade-80-percent-test`) is ampacity against a load calculation, and the water piece (`2026-10-06_water-leak-monitor-rate-threshold`) is a flow-rate threshold on a valve. The news neighbours — `2026-11-03_your-leak-alert-24-hours-at-best` (who sets the notification clock), `2026-10-27_your-hubs-4292-project-blind-spot` (distribution versus accountability), `2026-10-13_local-api-isnt-in-the-contract` (interface ownership after an acquisition), `2026-10-06_local-first-smart-home-cost-squeeze` (memory-price repricing) — carry no device-count, child-table or mesh-capacity claim at all. Cross-vertical check, as the skill requires: the whole corpus was grepped for `zigbee`, `child table`, `direct children`, `coordinator` and `mesh network`, and the only hits are passing mentions inside other verticals' articles and the two evergreen briefs above; no artifact anywhere in `published/` computes a node ceiling.
**Thesis:** A Zigbee mesh's device limit is a child-table budget, not a range problem — the coordinator holds 32 direct children, every mains-powered router takes one of those slots back and adds sixteen of its own, so the number to compute before buying anything is 32 + 15 per router, and the same coordinator class is documented at 15-20, 20 and 32 direct children depending on firmware, which is why "my mesh is full" is answered by a plug, not a bigger hub.

**Lead:** persona `pro_homeowner` wants "TCO depreciation math, local-first reliability" (`context/personas.json`), and the founder's standing position in `founder-voice.md` §3 `smart_home_telemetry` bullet 1 (*The Local-First Imperative*) declares a hub running "Home Assistant, Matter/Thread, Zigbee/Z-Wave" locally the only architecture that is not "fragile consumer e-waste". That declaration has a capacity ceiling nobody quotes, and the material came from reading the two implementations' own documentation — the Home Assistant ZHA integration page and the Zigbee2MQTT FAQ — rather than from a topic invented at the desk. It sits under the vertical's `primary_angles` line 1 (*local-first home assistant vs cloud subscription fragility*) at its hardware end: the local system's own limit, not the cloud's. Demand corroboration only: `context/recon_proposals/2026-10-20_gsc_smart_home_telemetry_opportunities.md` returned 0 candidate queries (impressions too thin on a young site), which per the skill never vetoes a lead. Not a news sweep: no 30-day window, no virality Judge, no `synthesize_topics.py` seed.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | Home Assistant — Zigbee Home Automation (ZHA) integration docs, 2026.10.4, "Using router devices to add more devices" | https://www.home-assistant.io/integrations/zha/ | 2026-11-03 | 77 devices — a coordinator's ceiling is 32 direct children, and the docs' own worked example takes three 16-child routers to a total limit of 77 devices (Coordinator: 32 Zigbee End devices − 3 routers = 29; Router one/two/three: + 16 each) | documentation — the stack's own published limit (Zigpy child table), not a laboratory measurement |
| 2 | Home Assistant — ZHA integration docs, 2026.10.4, "Supported but not recommended Zigbee adapters" | https://www.home-assistant.io/integrations/zha/ | 2026-11-03 | 15-20 devices — a legacy CC2530/CC2531 coordinator "will not work properly if the Zigbee network has more than 15-20 devices" | documentation — a support limit the project states for deprecated firmware |
| 3 | Home Assistant — ZHA integration docs, 2026.10.4, "How to interpret RSSI and LQI values" | https://www.home-assistant.io/integrations/zha/ | 2026-11-03 | -80 — RSSI values at -80 and below (that is, -85, -90) indicate a "noisy" environment where "you may risk losing messages", against -60 and above (-50, -40) as strong signal | documentation — a vendor-stack interpretation band, stated as guidance rather than a calibrated threshold |
| 4 | Home Assistant — ZHA integration docs, 2026.10.4, "Global options" | https://www.home-assistant.io/integrations/zha/ | 2026-11-03 | 21600 — a battery-powered device with no activity is considered unavailable after 21600 seconds (6 hours) by default, the timeout that turns a sleeping sensor into a false alarm | documentation — a shipped default the reader inherits |
| 5 | Zigbee2MQTT — FAQ, "I read that Zigbee2MQTT has a limit of 20 devices…" | https://www.zigbee2mqtt.io/guide/faq/ | 2026-11-03 | 55 devices — the FAQ's worked example with two CC2531 routers prints a 55-device limit (Coordinator: 15 − 2 routers = 13; Router 1: 21; Router 2: 21), although the same answer's prose says the default CC2531 firmware "supports 20 devices connected directly" — the same arithmetic from its own 20 gives 60 | documentation — a project FAQ whose example and prose disagree (the article must print both) |
| 6 | Zigbee2MQTT — FAQ, same answer, router limit | https://www.zigbee2mqtt.io/guide/faq/ | 2026-11-03 | 21 devices — a CC2530/CC2531 used as a router "has a limit of 21 devices", so each router contributes 21 slots while consuming one of the coordinator's | documentation — a firmware child-table limit for the router role |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| The Zigbee child-table ceiling and the +15-per-router rule | 9 | 9 | 8 | 9 | 8.8 | **winner** |
| The 6-hour `unavailable` default as a false-alarm generator | 8 | 9 | 7 | 8 | 8.0 | dropped as a topic — it settles one setting, not a purchase; folded into the winner as its diagnosis section |
| A Zigbee channel plan against Wi-Fi 1/6/11 | 8 | 9 | 7 | 7 | 7.9 | dropped — the fetchable page gives the band (channels 11 to 26) and a qualitative overlap warning, so every candidate figure is a two-digit channel number the matcher cannot separate from navigation digits; no measured overlap figure on a retrievable page I probed |
| UPS runtime for hub + ONT + router through a 4-hour outage | 9 | 8 | 5 | 9 | 7.8 | dropped — the two hosts that carry a runtime or capacity figure (`apc.com` product page, `batteryuniversity.com` BU-201) both returned `unreachable` to the verifier, so no runtime row could clear the floor |

## Arithmetic the article must state (and must not get wrong)

- Home Assistant's own example: 32 − 3 + (3 × 16) = **77**, i.e. capacity = 32 + 15 per router.
- Zigbee2MQTT's own example: 15 − 2 + (2 × 21) = **55** as printed; from the same answer's stated 20 direct devices it is 20 − 2 + 42 = **60**. Both belong in the piece, with the discrepancy labelled as the page's, not the article's.
- The portable rule: capacity = direct_children + routers × (router_children − 1). A router is not free — it spends one coordinator slot.
- Legacy CC2531 class: 15-20 direct children, which brackets both of the FAQ's numbers and explains why the two sources disagree.

## Notes for the drafter

- Do not claim a Zigbee node limit from the standard itself (the widely repeated 65,000-node figure): no fetchable primary states it, so it is not in this brief and must not appear.
- Do not present 32 as universal — it is the ZHA/Zigpy child table on a CC2652-class coordinator; the FAQ's 20/21 figures are a different stack on older firmware. The disagreement is the story.
- The `unavailable` timeout (21600 s) is a diagnostic aid, never evidence that a device is joined or healthy.
- RSSI bands are the doc's own guidance (it also says not to judge RSSI or LQI on its own), so quote it as a band and keep the caveat in the same paragraph.

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=6 fetched=6 sources=2 hosts=2 decision="sha1:595610bf36" dedup="matched a prior artifact: 2026-10-27_your-camera-eats-66-gb-" window_days=180 checked_at=2026-11-03T19:04:36+00:00 -->
<!-- evergreen-gate:end -->
