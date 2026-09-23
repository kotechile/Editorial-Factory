# Signals: gpu_hardware — 2026-09-23
**Window:** 2026-08-24 → 2026-09-23
**Queries run:** 12 (NVIDIA Rubin/Blackwell announcements · AMD MI400/HBM4 · export controls H20/H200 · HBM4 production · OpenAI-AMD warrant · Meta custom AMD MI450 · CoreWeave Vera Rubin bring-up · Broadcom/Marvell custom silicon · NVIDIA Hugging Face · SemiAnalysis Meta custom chip · Rubin HBM4 bandwidth · Hugging Face 86x revenue)
**Date-agnostic fallbacks:** used throughout (backend silently drops `after:`/`since:` filters); each hit timestamp-checked against window start.

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | NVIDIA agreed to acquire Hugging Face for $12,930,300,000 | https://blogs.nvidia.com/blog/nvidia-to-acquire-hugging-face | 2026-09-03 | "NVIDIA has agreed to acquire Hugging Face for $12,930,300,000" | open-source vs closed silicon / ecosystem moat | 95 |
| 2 | Hugging Face scale: 3M models, 500K datasets, 1M apps, 18M developers, 200K companies | https://blogs.nvidia.com/blog/nvidia-to-acquire-hugging-face | 2026-09-03 | "More than 18 million developers… share more than 3 million models, 500,000 datasets and 1 million applications. More than 200,000 companies use the platform" | open-source vs closed silicon | 88 |
| 3 | Huang neutrality pledge: "NVIDIA compute will not be required to build on or deploy through Hugging Face" | https://blogs.nvidia.com/blog/nvidia-to-acquire-hugging-face | 2026-09-03 | "Hugging Face will remain an open platform… NVIDIA compute will not be required" | open-source vs closed silicon | 85 |
| 4 | Price ≈ 86× ~$150M annualized revenue (The Information via TechCrunch; corroborated Forbes/Adweek) | https://techcrunch.com/2026/09/03/nvidia-confirms-it-will-buy-hugging-face-for-12-9-billion | 2026-09-03 | "$150 million in annualized revenue"; "86 times annual revenue" | ecosystem moat / unit economics | 84 |
| 5 | NVIDIA's buying power: $197B current assets, ~$60B quarterly profit (NYT) | https://www.nytimes.com/2026/09/03/technology/nvidia-hugging-face.html | 2026-09-03 | "$197 billion in current assets and nearly $60 billion in profits" | ecosystem moat | 70 |
| 6 | CoreWeave brings up multi-rack Vera Rubin NVL72 cluster | https://www.coreweave.com/news/coreweave-brings-up-multi-rack-nvidia-vera-rubin-nvl72-cluster | 2026-09-16 | "hundreds of NVIDIA Rubin GPUs into a single scale-out cluster" | inference economics | 65 |
| 7 | Broadcom "rocketing trend for custom AI accelerators" (Next Platform) | https://www.nextplatform.com/connect/2026/09/02/optics-still-driving-marvells-ai-business-more-than-custom-chips/5294018 | 2026-09-10 | custom-silicon backlog surging | custom silicon trend | 62 |

**Dropped (out of 30-day window, anchor-freshness rule):**
- Meta custom AMD MI450/MI455X cut-down (144GB HBM4, halved compute, SemiAnalysis "catastrophic") — core analysis dated 2026-08-03 ("Can AMD break the CUDA Moat?" + Aug 3 edit); out of window. Retained only as context for the custom-silicon pressure, not as a load-bearing signal.
- OpenAI-AMD 6GW warrant deal (Oct 6, 2025) — pre-window.
- AMD Instinct MI400 launch (July 23, 2026) — pre-window; Hot Chips recap was already a runner-up in the 09-16 cycle.
- HBM4 mass production (Samsung/SK Hynix, Feb 2026) — pre-window.
- US-China H200/H20 export-control swing (Dec 2025–June 2026) — pre-window.
