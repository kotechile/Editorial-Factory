# Signals: smart_home_telemetry — 2026-11-24
**Window:** 2026-10-25 → 2026-11-24
**Queries run:** 9 (web_search fan-out ×4 angles, HN Algolia ×4, home_lifestyle_intel MCP ×1)

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | SmartThings paywalls its cloud API; Home Assistant integration dies Dec 15 | https://community.smartthings.com/t/changes-to-the-smartthings-integration-for-home-assistant-what-s-happening-and-what-you-need-to-do/311942 | 2026-11-04 | $4.99/mo Developer Plan; 100,000 cloud API calls/mo; up to 10 installed apps; free individual API access ended Nov 3; current HA integration "will no longer work" after Dec 15, 2026; plan sold in only 9 countries | local-first home automation vs cloud subscription fragility | 92 |
| 2 | Dec 15 cutoff hits Home Assistant users in countries where the plan is not sold at all | https://matterhome.io/news/smartthings-api-paid-plans-december-cutoff | 2026-11-24 (updated; first ran Nov 2) | "December 15 date applies to every Home Assistant user, including users in countries where the Developer Plan is not available" (Canada, Australia, Spain, Sweden named); escape hatch: Matter multi-admin sharing keeps devices on Home Assistant without Samsung's cloud API | cloud paywall → migration pressure | 84 |
| 3 | The quota math and the exit route, quantified | https://localsmarthomeguide.com/articles/smartthings-api-developer-plan-home-assistant-integration-paywall | 2026-11-06 | 100,000 calls/mo ≈ ~3,300 calls/day; heavy use "can impact functionality"; $4.99/mo ≈ ~$60/yr attached to one cloud-only washer; Zigbee/Z-Wave devices can move to HA's own radios and stop needing Samsung entirely | local-first vs paying per cloud API call | 78 |
| 4 | Home Assistant 2026.11 ships Matter 1.5 cameras and two-way talk (released 2026-11-04) | https://www.home-assistant.io/blog/2026/11/04/release-202611/ | 2026-11-04 | "With Matter 1.5, cameras are part of the standard, and Home Assistant now supports them"; live video "streamed with WebRTC, directly between your browser and the camera"; Labs "Two-way audio" adds a talk button for Matter cameras and Reolink RTSP cameras; two-way audio "works when you open Home Assistant over HTTPS" | local-first camera/doorbell vs cloud subscription | 86 |
| 5 | Matter camera coverage of the same release | https://www.matteralpha.com/industry-news/matter-cameras-and-two-way-talk-officially-arrive-in-home-assistant-2026-11 | 2026-11 (2026.11 release coverage) | Cameras were already supported in the Matter.js backend; 2026.11 exposes them to the frontend; talk button appears on live streams; at launch two-way audio works with Matter cameras and Reolink RTSP | frontend exposure of the local camera path | 80 |

## Dated background (outside window — context, not signal rows)
- Nabu Casa renames Home Assistant Cloud → **Home Assistant Link** effective in the **2026.12 release on December 2, 2026** (announced Oct 2, 2026: https://www.nabucasa.com/news/2026-10-02-cloud-becomes-link — "It's the same subscription under the hood, just a new name"; $6.50/mo or $65/yr on nabucasa.com/link). In-window only as a forward-dated event; the collision with signal #1 lands in the same December 2 release train.
- Belkin Wemo cloud shutdown (Jan 31, 2026) is the standing precedent that a vendor cloud shutdown bricks cloud-only devices; not in window.
- Berkeley Lab load-management cost bands ($300–600 circuit sharing / $400–900 pausing / $3,000–5,000 smart panels) and TECH Clean California's 4.6% heat-pump panel-replacement rate: evergreen electrical-service context, not a 30-day signal.

## Candidate Synthesis Pairs

<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=5 candidates=0 heuristic=- window=2026-10-25..2026-11-24 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->
