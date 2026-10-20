# Verified Brief: smart_home_telemetry — 2026-10-20

**Evergreen run** (`skills/evergreen_topics.md`). Gate marker: PASS, 4/4 rows verified, 3 hosts
(arxiv.org ×2, github.com, eia.gov), de-dup matched `2026-10-13_panel-upgrade-80-percent-test`.
No news gate ran here (no 30-day window, no virality Judge, no synthesis seed).

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| 1 | NILM accuracy | A 2026 peer-reviewed NILM model reports 90% average precision and 96% recall for two-appliance classification, and 77% precision with 80% recall for four appliances | VERIFIED | https://arxiv.org/html/2608.18780v2 | "the proposed approach achieves an average precision of 90% and recall of 96% for two-appliance classification, and 77% precision and 80% recall for four appliances on the REDD dataset" |
| 2 | NILM accuracy | In the same four-appliance model the per-appliance numbers collapse unevenly: fridge 0.84 precision / 0.94 recall, microwave 0.75 / 0.95, dish washer 0.10 / 0.08, electric furnace 0.50 / 0.15 | VERIFIED | https://arxiv.org/html/2608.18780v2 (Table III) | "TABLE III : Precision and Recall of the TM trained on multiple appliances Appliance Precision Recall Fridge 0.84 0.94 Microwave 0.75 0.95 Dish Washer 0.10 0.08 Electric Furnace 0.50 0.15" |
| 3 | NILM accuracy | The evaluation is REDD, collected from 6 residential buildings; buildings 1, 2, 4, 5 and 6 train the model and building 3 is held out for testing; the model is 17 KB and runs at 0.43 ms per sample on an ESP32 | VERIFIED | https://arxiv.org/html/2608.18780v2 | "Experiments are conducted on the REDD dataset, which was collected from 6 residential buildings … Buildings 1, 2, 4, 5, and 6 are used for training, while Building 3 is selected for testing because it contains measurements for all appliances considered in this study." / "The trained model occupies only 17 KB of flash memory and achieves an inference latency of 0.43 ms on an ESP32" |
| 4 | Identification accuracy | Four-class appliance identification from spectrograms reaches 88.9% accuracy and 88% F1 with a ResNet18, while the same team's AlexNet variant reaches 80.67% accuracy and 81% F1 | VERIFIED | https://arxiv.org/html/2301.03018v2 (Table III) | "ResNet18 wavelets 0.001 88.9% 88% AlexNet wavelets 0.001 80.67% 81%" and the abstract's "88.9% for appliance identification (with Resnet-based model)" |
| 5 | Threshold caveat | Per-appliance home-level accuracy runs 86.58% (refrigerator) to 94.6% (dish washer) only "for carefully chosen values of thresholds" — the authors' own qualification | VERIFIED | https://arxiv.org/html/2301.03018v2 (Table II) | "Table II demonstrates that the accuracy of the proposed DL model remained quite high, and varied from 86.58% to 94.6%, for all the four appliances (for carefully chosen values of thresholds)." |
| 6 | Independent reproduction | An open sequence-to-point/transformer reproduction on REFIT lands per-appliance F1 between 0.5671 (microwave) and 0.8478 (washing machine), with fridge 0.7929, kettle 0.7309 and dish washer 0.6069 — one model per appliance, not a multi-appliance classifier | VERIFIED | https://github.com/goruck/nilm | "kettle 0.7309 … microwave 0.5671 … fridge 0.7929 … dishwasher 0.6069 … washingmachine 0.8478" (transformer results table); the page trains appliances individually: "The seq2point learning models for the appliances were trained individually" |
| 7 | Stakes | Space heating and air conditioning together were 52% of a US household's annual energy consumption in 2020 | VERIFIED | https://www.eia.gov/energyexplained/use-of-energy/homes.php | "more than half—52% in 2020—of a household's annual energy consumption is for just two energy end uses: space heating and air conditioning" |
| 8 | Mechanism note | The paper's own explanation for why the two-appliance case separates well: the fridge's cycles are low-power transitions with long durations, the microwave's are high-power transitions over short durations | VERIFIED | https://arxiv.org/html/2608.18780v2 | "The two appliances are easily separable because the fridge cycles are characterized by low-power transitions and long operating durations, whereas microwave cycles typically involve high-power transitions over short durations" |

## Attribution rules for the drafter (read before writing)

1. **Nobody is claiming a consumer product's accuracy.** No vendor page for an appliance-identifying
   monitor could be fetched (sense.com and dl.acm.org both return `unreachable` to the verifier), so the
   article must never print "your monitor is 77% accurate". The measured numbers describe the *research
   class* the feature comes from. Say "the published record for this kind of model", never "Emporia" or
   "Sense" accuracy figures.
2. **One in four is arithmetic, not a source claim**: 100 − 77 = 23, so "about one in four" is a derived
   gloss on row 1 and must be labelled as arithmetic if stated.
3. **Row 6 is a single-appliance reproduction** (one model per appliance on REFIT), not a four-appliance
   classifier. The F1 spread 0.5671–0.8478 speaks to how much per-appliance difficulty varies; it must not
   be folded into the 77% average.
4. **Row 2's dishwasher collapse is reported, not explained.** The paper explains the fridge/microwave
   separation (row 8) and prints the four-appliance table without diagnosing the dishwasher. Do not invent
   a cause, and do not generalise that a dishwasher in your home will measure 0.10.
5. **REDD is six houses in one US city**, with building 3 held out. Any sentence about the benchmark carries
   that scale.
6. **No prices.** No fetchable first-party price row exists for this piece, and the desk's 2026-10-13
   evergreen already spent the branch-CT price rows; the article argues about measurement, not shopping.
7. **Derived arithmetic allowed:** 8,760 hours in a year; hours × watts ÷ 1000 = kWh; nothing else.

## Verdict

7 claims VERIFIED, 0 FLAGGED, 0 REMOVED. Draft proceeds to `skills/story_draft.md` → Loop 3
(`skills/claude_humanizer.md`). The topic does not carry a date-bound price, rate or cap, so there is no
"as of" figure to police beyond citing each measurement to its own paper; the EIA share is the agency's
2020 statement and must be attributed to that year in the body.
