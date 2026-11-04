# Signals: gpu_hardware — 2026-11-04
**Window:** 2026-10-05 → 2026-11-04
**Queries run:** 14

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | Microsoft puts Maia 300 on the memory-bound path | https://blogs.microsoft.com/blog/2026/10/12/microsoft-to-expand-azure-maia-system-to-multi-gigawatt-deployments | 2026-10-12 | Eight HBM4 stacks give 18.0 TB/s of peak memory bandwidth inside a 950-watt TDP; a 96-accelerator rack holds 27.6 TB of HBM and 1.7 PB/s of aggregate bandwidth in a 167-kilowatt envelope; Microsoft expects 40% more tokens per megawatt than leading GPU-based systems | inference economics | 92 |
| 2 | Qualcomm validates compute-under-memory silicon | https://www.qualcomm.com/news/onq/2026/11/qualcomm-hbc-validated-silicon-ai-inference | 2026-11-02 | First-generation HBC silicon exercised the full memory read-write path and near-memory computations at production-representative dimensions; the Dragonfly AI250 that will carry it samples in the first half of 2027; a data center product has taped out | memory bandwidth ceilings | 88 |
| 3 | The lab numbers behind HBC | https://www.nextplatform.com/ai/2026/11/02/qualcomm-has-eyes-on-the-ai-inference-datacenter-with-hbc-and-ai250/5306954 | 2026-11-02 | Qualcomm executives say HBC delivers as much as 18 times the memory bandwidth of LPDDR and an energy-efficiency measurement of five times the terabit-per-second-per-watt of HBM4, taken on first-generation lab silicon | open-source vs closed silicon | 85 |

## Dated background

- Nvidia's custom high-bandwidth memory design (NVHBM) was announced 2026-08-26 and reported again on 2026-10-26; it moves the memory controller off the GPU into the HBM base die and is not a JEDEC standard: https://www.theregister.com/ai-ml/2026/10/26/nvidia-sidesteps-jedec-hbm-standard/5305323
- NVIDIA's own NVHBM announcement post (2026-08-26, outside the window): https://blogs.nvidia.com/blog/nvlink-fusion-nvhbm-custom-high-bandwidth-memory/
- Microsoft's Maia 200 production claim and its 1.7x tokens-per-watt figure sit in the same 2026-10-12 post and are background to the Maia 300 numbers, not a separate event.

## Notes on dating

- Row 1 is the 2026-10-12 launch post; the 18.0 TB/s, 950-watt, 27.6 TB and 1.7 PB/s figures are Microsoft's own published specifications.
- Rows 2 and 3 are the same day (2026-11-02): row 2 is Qualcomm's own validation post, row 3 is the trade interview that carries the 18x and 5x comparisons, which the vendor post states only in a chart image.
- The NVHBM material is background: its announcement date (2026-08-26) is outside the window, so it is not an anchor.

## Candidate Synthesis Pairs

<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=3 candidates=0 heuristic=- window=2026-10-05..2026-11-04 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->
