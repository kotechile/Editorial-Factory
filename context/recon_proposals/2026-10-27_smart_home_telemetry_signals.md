# Signals: smart_home_telemetry — 2026-10-27
**Window:** 2026-09-27 → 2026-10-27
**Queries run:** 13 web fan-outs across the vertical's six configured sources (home_lifestyle_intel, home_assistant_community, matter_thread_consortium, hackaday, reddit_homelab, github_trending) + 1 intel-MCP pull (`home_lifestyle_intel_client.py --recent 30 --vertical smart_home_telemetry --format signals` — 10 items, none on the local-first/telemetry beat: Remodelista interiors, Canary Media FirstEnergy rate case, Ars Technica devices, Redfin mortgage rates) + 11 primary-source fetches and 5 GitHub API reads. Every hit timestamp-checked against the window; every date below is the publisher's own date field or a merged-at timestamp, not a search snippet.

**Window note (freshness discipline — three strong-looking legs dropped, not softened).**
- **Sense exiting direct-to-consumer energy monitors** — the Latitude Media story that reads as current carries its own byline date **2025-11-03**, and Sense's own announcement behind it is older still ("we'll stop selling the Sense Monitor by December 31, 2025"). Out of window by eleven months; dropped.
- **SmartThings API paywall ($4.99/month personal plan)** — announced June 2026, effective "October 2026". The anniversary of an announcement is not a 30-day signal; carried only as dated background so the URL exists if a drafter needs it, never as an anchor.
- **Zigbee 4.0 / Suzi sub-GHz** — the announcement is 2025-11-18 and Suzi certification opened 2026-09-02, before the window opens. The only in-window artefact is a CSA one-pager (2026-10-15) with no figure. Dropped.
- Also read and set aside: FirstEnergy Ohio rate case (2026-10-27, a distribution-charge story, not telemetry), the Morgan Lewis smart-meter-data analysis (2026-10-20) whose underlying bill was introduced 2026-09-04 — outside the window.

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | Home Assistant core — PR #183502 "Add Marketplace integration" (merged) | https://github.com/home-assistant/core/pull/183502 | 2026-10-01 | The community store is merged into Home Assistant itself: PR opened 2026-09-28, merged 2026-10-01, so the development branch (2026.11) ships a built-in `marketplace` integration. Body: "This brings HACS into Home Assistant as the Marketplace." | The platform takes ownership of the code-supply chain it used to point at | 93 |
| 2 | HACS — issue #5590 "HACS is moving to Home Assistant as Marketplace" | https://github.com/hacs/integration/issues/5590 | 2026-10-16 | Maintainer's own announcement: "Starting with the Home Assistant 2026.11 release in November, it ships built-in as the **Marketplace** integration. Development now happens in Home Assistant itself, so this repository is no longer the place for new work." The repo (7,847 stars, 1,612 forks) stops taking new work | The largest local-first ecosystem's app store stops being a separate project | 88 |
| 3 | HACS installer — PR #67 "Add Home Assistant 2026.11+ marketplace integration check" (merged) | https://github.com/hacs/get/pull/67 | 2026-10-17 | The installer refuses to run on 2026.11 and newer: "This PR adds validation to prevent HACS installation on Home Assistant 2026.11 and newer versions, where HACS has been replaced by the native Marketplace integration." Created 2026-10-16, merged 2026-10-17 | The old route is closed on purpose: you cannot keep the separate store after updating | 85 |
| 4 | HACS docs — "HACS and the Marketplace" | https://hacs.xyz/docs/marketplace | 2026-10-27 (observation; page published ahead of 2026.11) | Migration rules, first-party: "You don't need to do anything. When Home Assistant starts after the update, the Marketplace takes over from HACS"; "AppDaemon apps and Python scripts are no longer managed. Their files stay where they are and keep working, but they don't get updates anymore"; "HACS can't be installed on Home Assistant 2026.11 or newer. Home Assistant blocks the custom integration, because the Marketplace replaces it"; the catalog itself still lives in `hacs/default` | Capability narrows as the store moves in: two content types lose update management | 86 |
| 5 | Home Assistant docs — Marketplace integration | https://next.home-assistant.io/integrations/marketplace/ | 2026-10-27 (observation; 2026.11 docs) | The platform's own warning, verbatim: "Nothing published in the Marketplace is tested, audited, or supported by the Home Assistant project"; "Marketplace content can compromise the security of Home Assistant, your home, and your network"; "Marketplace content runs in Home Assistant. It can access your home, your data, and the system that runs Home Assistant"; "You use everything you install from the Marketplace at your own risk"; "The Marketplace is available to administrators only"; "The catalog contains thousands of projects" | One click to install code that can read the house — with a warning dialog as the only gate | 95 |
| 6 | Home Assistant docs — Security / non-qualifying vulnerabilities | https://www.home-assistant.io/security/ | 2026-10-27 (observation; standing policy) | The project's own scope excludes exactly this risk class: "Attacks that require the user to install a malicious other software, like a third-party integration, app (formerly known as add-ons), or plugin"; also "Home Assistant assumes every user is trusted and does not enforce user privileges" | The accountability for third-party code is contractually the owner's — and now the install button is the platform's | 92 |
| 7 | hacs/default — the catalog itself (first-party list, read 2026-10-27) | https://raw.githubusercontent.com/hacs/default/master/integration | 2026-10-27 (observation) | **4,292** integration entries in `integration`, **957** in `plugin` (dashboard cards/themes) — the exact catalog the Marketplace reads, counted from the file, not estimated | The scale of what one click can reach | 90 |
| 8 | Consumer Reports — "Some smart home companies still lag on security basics" | https://innovation.consumerreports.org/some-smart-home-companies-still-lag-on-security-basics | 2026-10-15 | Third annual survey of **80** manufacturers: **84%** give researchers an easy-to-find contact; **11** have no dedicated security contact; **27 of 80** still lack a formal vulnerability disclosure program; only **a third** are definitively tracking vulnerabilities across their products; **21%** publish a `security.txt`; answers came from **25 of 80** companies, down from **52** last year. Verbatim: "the number of companies without a dedicated security contact is 11 this year, up from 10 last year"; "only a third of the 80 companies we investigated are definitively doing this" | The vendors whose code the owner now installs at will still owe the owner a disclosure channel at a sixth to a third of the field | 91 |

## Candidate Synthesis Pairs

<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=8 candidates=0 heuristic=- window=2026-09-27..2026-10-27 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->

## Primary sources (corroboration — every URL an artifact may cite must appear in this file)

Signals 1–5 (the Marketplace leg):
- https://github.com/home-assistant/core/pull/183502
- https://github.com/hacs/integration/issues/5590
- https://github.com/hacs/get/pull/67
- https://hacs.xyz/docs/marketplace
- https://next.home-assistant.io/integrations/marketplace/
- https://github.com/hacs/default
- https://raw.githubusercontent.com/hacs/default/master/integration
- https://github.com/hacs/integration
- https://paulusschoutsen.nl/ohf-daily/edition/2026-10-18/article/hacs-marketplace-version-guidance
- https://localsmarthomeguide.com/articles/hacs-becomes-home-assistant-marketplace-2026-11

Signal 6 (the accountability scope):
- https://www.home-assistant.io/security/

Signal 8 (the vendor-disclosure leg):
- https://innovation.consumerreports.org/some-smart-home-companies-still-lag-on-security-basics
- https://innovation.consumerreports.org/what-the-ftc-report-means-for-consumers

## Dated background (not anchors — outside the window, kept for provenance)
- https://github.com/OpenHomeFoundation/roadmap/issues/186 (2026-06-11 — the foundation's own open issue asking for the power to "centrally disable malicious or vulnerable integrations and Apps"; records that a Repairs notice is the only remedy today)
- https://www.home-assistant.io/blog/2021/01/22/security-disclosure (2021 — the HACS directory-traversal disclosure the roadmap issue cites as the last real test of this class)
- https://community.smartthings.com/t/a-new-enhanced-smartthings-api-experience/309947 (2026-06 — the SmartThings API $4.99/month personal plan, effective October 2026; announcement is outside the window)
- https://www.home-assistant.io/integrations/smartthings (the platform's own breaking-change note for that fee)
- https://sense.com/consumer-blog/looking-ahead-the-next-chapter-for-sense (2025 — hardware exit; out of window)
- https://www.latitudemedia.com/news/is-the-era-of-direct-to-consumer-energy-hardware-coming-to-a-close (2025-11-03 — out of window)
- https://csa-iot.org/newsroom/matter-1-5-1-enhancing-camera-performance-and-expanding-device-flexibility (2026-03-31 — out of window)
