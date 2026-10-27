# Verified Brief: smart_home_telemetry — 2026-10-27 (evergreen)

Companion to `context/recon_proposals/2026-10-27_smart_home_telemetry_evergreen_brief.md` (gate PASS,
marker rows=6 fetched=6 hosts=3). Every row below was fetched on 2026-10-27 with the same fetch path the
evergreen gate uses (`scripts/citation_hub_dossier.fetch_source`, user-agent
`Mozilla/5.0 (compatible; EditorialFactorySourceVerifier/1.0)`), and each figure was read inside its own
sentence, not merely found somewhere on the page.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| C1 | Camera defaults (Reolink RLC-810A) | The camera's main stream ships with a 4,096-8,192 Kbps code rate, default 6,144 Kbps, and its substream a 64-512 Kbps rate, default 256 Kbps | VERIFIED | https://reolink.com/product/rlc-810a/ | "Code Rate Mainstream: 4096Kbps - 8192Kbps (default: 6144Kbps) Substream: 64Kbps - 512Kbps (default: 256Kbps)" |
| C2 | Camera defaults (Reolink RLC-810A) | The same camera records 3840x2160 (8.0 megapixels) at 25 frames/sec in H.265, with main-stream frame rate 2-25 fps (default 25) and substream 4-15 fps (default 10) | VERIFIED | https://reolink.com/product/rlc-810a/ | "Video Resolution 3840x2160 (8.0 Megapixels) at 25 frames/sec … Videoformat H.265 … Frame Rate Mainstream: 2fps - 25fps (default: 25fps) Substream: 4fps - 15fps (default: 10fps)" |
| C3 | Vendor capacity table (Reolink RLC-810A) | The vendor's own card table gives 48.5 hours on 128GB, 97.1 hours on 256GB and 194.2 hours on 512GB for this camera | VERIFIED | https://reolink.com/product/rlc-810a/ | "Supports up to 512GB microSD card (not included). 48.5hours 128GB 97.1hours 256GB 194.2hours 512GB" |
| C4 | Detector stream (Frigate 0.18 docs) | Detection runs at a default of 5 frames per second and that default is the recommendation | VERIFIED | https://docs.frigate.video/frigate/camera_setup/ | "The default frame rate of 5fps is correct for almost all cameras and rarely needs to be changed … Higher resolutions and frame rates will drive higher CPU usage on your server." |
| C5 | Recording stream (Frigate 0.18 docs) | Frigate recommends setting the recording feed to 15 fps in the camera's own firmware, while detection uses a separate stream and the viewing stream is rebroadcast as-is — the reason given is bandwidth and playback reliability, not disk | VERIFIED | https://docs.frigate.video/frigate/camera_setup/ | "Recording: This stream should be the resolution you wish to store for reference… I recommend setting this feed in your camera's firmware to 15 fps. Stream Viewing: This stream will be rebroadcast as is to Home Assistant… Setting this resolution too high will use significant bandwidth when viewing streams in Home Assistant, and they may not load reliably over slower connections." |
| C6 | Retention policy (Frigate 0.18 docs) | A documented storage-reducing policy keeps all video 3 days, only motion video for 7 days, then only motion overlapping an alert or detection to 30 days | VERIFIED | https://docs.frigate.video/configuration/record/ | "the following configuration will store all video for 3 days. After 3 days, only video containing motion will be saved for 7 days. After 7 days, only video containing motion and overlapping with alerts or detections will be retained until 30 days have passed." |
| C7 | Recorder ceiling and licences (Synology DS224+) | Surveillance Station on the DS224+ ships with 2 default licences; the unit's published ceiling is 4K H.264 at 17 channels / 170 total FPS and 4K H.265 at 20 channels / 200 total FPS (1080p: 25 channels, 750 FPS) | VERIFIED | https://www.synology.com/en-us/products/DS224+ | "Surveillance Station Default Licenses 2 (Additional cameras require purchase of licenses) Maximum IP Cameras and Total FPS (H.264) … 4K: 17 channels, 170 FPS Maximum IP Cameras and Total FPS (H.265) … 4K: 20 channels, 200 FPS … Performance figures are obtained from testing conducted with the device fully populated with drives, with their default memory configuration, and under a continuous recording setup." |
| C8 | Derived arithmetic (authorised, endpoints above) | 6,144 Kbps ÷ 8 × 86,400 s = 66.36 GB per camera per day; ×4 cameras ×30 days = 7.96 TB; the 8,192 Kbps top of the range gives 88.47 GB/day and the 4,096 Kbps floor 44.24 GB/day; the 256 Kbps substream is 2.76 GB/day, exactly 1/24 of the main default; the vendor table's 512 GB ÷ 194.2 h = 2.636 GB/h = 63.3 GB/day (implying ~5,859 Kbps); 170 FPS ÷ 25 fps = 6.8 cameras at 4K H.264 | COMPUTED | C1, C3, C7 | Recompute in the final; every percentage, day count and terabyte figure in the body must come from these divisions, never from the draft's own arithmetic |

## FLAGGED rulings the drafter must obey

1. **"Default", never "the bitrate".** 6,144 Kbps is a factory default inside a published 4,096-8,192 Kbps
   range (C1). The article says "the default it ships with" and never "every camera records at 6,144".
2. **Two independent estimators, ~5% apart.** The code-rate arithmetic gives 66.36 GB/day; the vendor's own
   capacity table implies 63.3 GB/day (C3, C8). Both are the same order and the difference is rounding plus
   the vendor's own assumptions, so the body writes "about 63 to 66 gigabytes a day" and never a single
   figure presented as measured. Neither is a measurement of a reader's own camera.
3. **The card table is a capacity table, not a benchmark.** It is the seller's own published hours for its own
   card, offered as a cross-check on the arithmetic, not as a tested retention result.
4. **The 170 FPS ceiling belongs to that box's own recorder software.** It is Synology's published figure for
   Surveillance Station with drives fitted and under continuous recording (C7). It is NOT a Frigate
   benchmark and must not be presented as one; the honest generalisation is "any recorder has a total
   frame-rate ceiling at a resolution, and it is published as throughput, never as a camera count".
5. **Frames are not bytes.** Frigate's 15 fps recording recommendation is about playback and bandwidth, not
   about disk (C5). The article must not claim that lowering fps cuts the archive; the code rate is the lever.
6. **Licences have a count, not a price.** The page states 2 default licences and that additional cameras
   require purchased licences (C7). No licence price is published there, so the article states no price.
7. **No hands-on claim.** This desk has no camera hardware: no "we tested", "in our tests", "we recorded".
   The piece is arithmetic on published documents.
8. **No subscription price and no product recommendation.** No camera cloud plan price is in this evidence
   set, so the piece makes no "cheaper than your plan" claim; and it names no product to buy.

## Claims removed (do not write)

- Any cloud-plan monthly price (not sourced), any NVR price, any drive price.
- Any licence price for extra cameras (page states the requirement only).
- Any power-wattage or electricity-cost leg — deliberately excluded; that mechanism is owned by
  `2026-10-10_self-hosting-break-even-one-hour-a-year`.
