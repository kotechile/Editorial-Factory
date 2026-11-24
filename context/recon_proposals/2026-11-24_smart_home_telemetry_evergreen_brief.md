# Evergreen Brief: smart_home_telemetry — 2026-11-24
**Archetype:** evergreen
**Vertical:** smart_home_telemetry
**Persona:** pro_homeowner
**Decision the reader is facing:** Whether to leave smart-home devices on the same Wi-Fi as laptops and NAS drives, or move them to a separate network segment — a guest SSID at minimum, a firewalled IoT VLAN at best — given that the devices demonstrably phone home to third parties and get recruited into botnets and residential proxy pools. The decision bites at every new device join: the moment you plug in a camera, TV or thermostat, you are either extending your trusted network to it or not.
**Durability:** The two trust findings are standing measurement results (a TV's outbound calls on power-on, an app's PII to four analytics firms) and government advisories that stay accurate as written; the FBI's segmentation recommendation is standing guidance. The advisories are dated in the brief — the BADBOX record as of the FBI's June 5, 2025 PSA, the residential-proxy guidance as of its March 12, 2026 PSA — and the article repeats those dates. All figures cited as of retrieval 2026-11-24.
**De-dup:** `2026-10-27_your-camera-eats-66-gb-daily` is the nearest prior artifact in the corpus and touches the same world — it notes a separate network "costs no storage" — but its mechanism is storage sizing from bitrates, not the trust boundary between a camera's traffic and a laptop's. `2026-11-24_your-doorbell-wont-need-the-cloud` argues cloud-independence of one device, not isolation of many. A corpus grep for vlan/segmentation/guest-network mechanisms across `published/` and `context/recon_proposals/` returns no home-network article.
**Thesis:** Every smart device you plug in is a stranger on your trusted network — the measured traffic (a TV calling ten third parties in one minute, an app shipping PII to four analytics firms) and the FBI's standing segmentation guidance say the flat network is a decision you already made by default, and moving devices behind a firewall is the cheapest trust upgrade in the house.

**Lead:** §2 evidence source 2 — the vertical's own `primary_angles` ("isolated IoT VLANs and zero-cloud camera privacy") — crossed with the persona's want for "local-first reliability" and the intel feed's device-evaluation material. The consumer-truth anecdote of the cloud-API lockout (a rebuilt local system) supplies the owner's standing position: devices you cannot reason about are devices you do not trust.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | EFF — "Ring Doorbell App Packed with Third-Party Trackers" | https://www.eff.org/deeplinks/2020/01/ring-doorbell-app-packed-third-party-trackers | 2026-11-24 | Four main analytics — testing of the Ring Android app found personal data (names, private IP addresses, persistent identifiers) delivered to four main analytics and marketing companies, including Facebook | measured |
| 2 | Princeton CITP — "Announcing IoT Inspector: Studying Smart Home IoT Device Behavior" | https://blog.citp.princeton.edu/2018/04/23/announcing-iot-inspector-a-tool-to-study-smart-home-iot-device-behavior | 2026-11-24 | 50 home IoT devices — the lab's own analysis across more than 50 devices; one Samsung TV talked to Google Play, Netflix, Spotify, Facebook and six more services in its first power-on minute without any account | measured |
| 3 | FBI PSA I-060525-PSA — "Home Internet Connected Devices Facilitate Criminal Activity" | https://www.fbi.gov/investigate/cyber/alerts/2025/home-internet-connected-devices-facilitate-criminal-activity | 2026-11-24 | 2024 — the home-IoT botnet campaign the FBI profiles was identified in 2023 and disrupted in 2024; its successor infects home IoT devices (TV streaming sticks, picture frames) with backdoor malware | measured |
| 4 | FBI PSA I-031226-PSA — "Evading Residential Proxy Networks" | https://www.fbi.gov/investigate/cyber/alerts/2026/evading-residential-proxy-networks-protecting-your-devices-from-becoming-a-tool-for-criminals | 2026-11-24 | 2026 — the FBI's March 12, 2026 PSA documents compromised home IoT devices recruited as residential proxies and tells owners to use network segmentation and firewall rules | measured |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| IoT network segmentation: flat Wi-Fi vs guest SSID vs firewalled VLAN | 8 | 9 | 8 | 7 | 8.1 | **winner** |
| 200A service ceiling vs smart load management | 9 | 9 | 8 | 9 | 8.8 | refused by hand — mechanism already argued in `2026-10-13_panel-upgrade-80-percent-test` (cross-vertical) |
| Matter-certified device choice guide | 6 | 7 | 5 | 5 | 5.8 | dropped — commoditized, thin evidence |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=4 fetched=4 sources=4 hosts=3 decision="sha1:365254fc47" dedup="matched a prior artifact: 2026-10-27_your-camera-eats-66-gb-" window_days=180 checked_at=2026-11-24T19:12:10+00:00 -->
<!-- evergreen-gate:end -->
