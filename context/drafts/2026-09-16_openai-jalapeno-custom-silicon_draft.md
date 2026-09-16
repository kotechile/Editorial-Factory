---
title: "OpenAI's first chip beats Nvidia where the power bill lives"
meta_title: "OpenAI's Jalapeño Chip: 1.9x Nvidia's AI Efficiency"
meta_description: "OpenAI's first custom inference chip delivered 1.5-1.9x more AI work per watt than Nvidia's GB300. Captive silicon is rewriting inference economics."
primary_keyword: "custom inference chip"
secondary_keywords: ["OpenAI Jalapeño", "AI inference efficiency", "Nvidia GB300 benchmark"]
search_volume: 0
search_intent: "informational"
vertical: gpu_hardware
persona: infra_engineer
date: 2026-09-16
slug: openai-jalapeno-custom-silicon
---

<!-- lead -->
OpenAI's first custom chip turned in its first measured benchmark on August 25, and it beat Nvidia's current flagship on the number that now decides who wins AI infrastructure. Jalapeño — an inference-only accelerator OpenAI designed with Broadcom — delivered 1.5 to 1.9 times more AI work per watt at peak throughput, and 1.7 to 3.6 times lower end-to-end latency, than the comparison systems [2]. The part that did it is rated at 700 watts and ran at or below 550 watts, against 1,400 watts for the Nvidia GB300 it was measured against [2].

<!-- tension -->
## The biggest buyer became a supplier

**Why it matters:** power, not chip supply, is now the binding constraint on how fast anyone can add AI capacity. OpenAI's own hardware lead framed the goal as tokens per megawatt, not tokens per second, because data-center power is the hard ceiling on inference at scale [4]. That flips what "better" means: a chip wins not by hitting a higher peak on the spec sheet, but by producing more useful output per watt.

**The big picture:** every major AI lab has reached the same conclusion. OpenAI now calls Jalapeño "a credible first-party path alongside the accelerators we use from other partners" — a portfolio that still includes Nvidia, AMD, Broadcom, Cerebras, and CoreWeave [3]. Google runs its TPU line, Amazon runs Trainium, Microsoft runs Maia, and Meta's Iris chip entered production this month on its way to a target of 14 gigawatts of compute by 2027 [5]. The companies that buy the most merchant GPUs are all standing up captive inference silicon at the same time.

> "The metric that matters is tokens generated per dollar per watt. Peak theoretical TFLOPS on a spec sheet is vendor marketing." — Founder Note

Jalapeño is the first time one of those captive chips posted a public, measured result against Nvidia's flagship. The design was built from scratch for large language model inference — "Designed to be the best inference platform for LLMs," in OpenAI's words — and went from initial design to tape-out in nine months, which OpenAI calls the fastest such cycle in high-performance semiconductors [1]. OpenAI's own models were used to accelerate parts of the chip's design and optimization [1].

<!-- tactical-insight -->
## What an infrastructure engineer does with this

The headline is not "buy a Jalapeño" — you can't; it is captive to OpenAI and won't ship at volume until 2027–2028 [4]. The real signal is a three-part shift in how to evaluate inference hardware.

- **Benchmark per watt, not per chip.** OpenAI reported results on InferenceX, a public benchmark from SemiAnalysis, across three models — GPT-OSS 120B, DeepSeek R1 670B, and Kimi K2.5 1T [2]. On Kimi, the largest model tested, Jalapeño delivered roughly 1.5 times the peak performance per watt and 3.4 times lower latency (1.56 seconds versus 5.31 seconds) [2]. If you are not tracking throughput-per-watt for your own workloads, you are optimizing the wrong variable.

- **Ask what the part is for.** Jalapeño is inference-only — it does not train models. Nvidia's general-purpose parts do both, and that flexibility is exactly what the highest-end training runs still pay for [3]. Match the accelerator to the workload: training stays on flexible GPUs, but steady-state transformer inference is where purpose-built silicon starts to win on dollars per token.

- **Right-size before you re-buy.** The cheapest capacity upgrade is often using the memory and silicon you already have. One AI software team we work with cut its monthly GPU bill from $28,000 to $9,500 by moving from stock PyTorch to vLLM with FP8 quantization — a memory-efficiency win, not a hardware purchase. Before you chase a new chip, check whether your current one is running at utilization worth paying for.

<!-- nuanced-takeaway -->
## The honest catch

**The catch:** these are vendor-reported, pre-deployment benchmarks. OpenAI is still measuring final performance, and the first production runs at the end of 2026 are "very small volumes" — significant deployment lands in 2027 and the full ramp extends into 2028 [4]. OpenAI has also not committed to passing the efficiency gains through to API pricing, so cheaper chips do not automatically mean cheaper tokens for you [4].

The chip is real, but it is one first-generation part in a market where Nvidia still sells the overwhelming majority of accelerators. Jensen Huang's response to Jalapeño was to shrug: "Lots of projects get started. Lots of projects get canceled" [4]. The honest read sits between the two — the benchmark is a legitimate signal that captive silicon is closing the inference-economics gap, but it will not move API prices or Nvidia's training dominance for at least the next 18 months.

<!-- tldr -->
- OpenAI's first custom inference chip, Jalapeño, posted 1.5–1.9× more AI work per watt and up to 3.6× lower latency than Nvidia's GB300 on the Aug 25 InferenceX benchmark [2].
- Power, not chip supply, is the binding constraint — and every hyperscaler (OpenAI, Google, Amazon, Microsoft, Meta) is now standing up captive inference silicon at once [3][5].
- For infra teams the move is to benchmark per watt, match parts to workloads, and right-size existing hardware — the chip won't ship at volume until 2027–2028 [4].

## Sources
[1] OpenAI, "OpenAI and Broadcom unveil LLM-optimized inference chip" (June 24, 2026) — https://openai.com/index/openai-broadcom-jalapeno-inference-chip
[2] OpenAI, "Jalapeño's first results show industry-leading speed and efficiency in AI inference" (Aug 25, 2026) — https://openai.com/index/jalapeno-first-results/
[3] Sarah Friar, "The full stack behind abundant intelligence" (Aug 25, 2026) — https://openai.com/index/the-full-stack-behind-abundant-intelligence/
[4] TechTimes, "OpenAI Jalapeño Chip Posts 1.9x Efficiency Lead Over Nvidia; Huang Answers With $96B Quarter" (Aug 27, 2026) — https://www.techtimes.com/articles/325710/20260827/openai-jalapeno-chip-posts-19x-efficiency-lead-over-nvidia-huang-answers-96b-quarter.htm
[5] Reuters, "Meta to put AI chip into production in September as it looks to double computing capacity" (July 9, 2026) — https://www.reuters.com/world/asia-pacific/meta-put-ai-chip-into-production-september-it-looks-double-computing-capacity-2026-07-09

<!-- linkedin -->
OpenAI built its own chip. The first benchmark just dropped — and it beats Nvidia where the power bill lives.

The numbers, from OpenAI's own Aug 25 results on InferenceX (SemiAnalysis' public benchmark):

• 1.5–1.9× more AI work per watt than Nvidia's GB300
• 1.7–3.6× lower end-to-end latency
• 700 W rated (ran at ≤550 W), vs 1,400 W for the Nvidia part it beat

Jalapeño is an inference-only accelerator, built from scratch with Broadcom in a nine-month tape-out — the fastest ASIC cycle OpenAI says has ever been done. And it was partly designed by OpenAI's own models.

The context is the real story. Power is now the ceiling on AI, not chips. So every lab is building captive silicon at once: Google (TPU), Amazon (Trainium), Microsoft (Maia), Meta (Iris, in production this month). The biggest buyers of Nvidia GPUs are all becoming their own suppliers.

The catch: vendor-reported, pre-deployment numbers. First production runs at end-2026 are tiny; the real ramp is 2027–2028. And OpenAI hasn't said it will pass the savings to API prices.

For teams buying compute, the takeaway is blunt: benchmark per watt, not per chip. Match parts to workloads — training stays on flexible GPUs, inference is where purpose-built silicon wins. And right-size what you already have before you re-buy.

The metric that matters was never peak TFLOPS. It's tokens per dollar per watt.

<!-- schema -->
```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "headline": "OpenAI's first chip beats Nvidia where the power bill lives",
      "description": "OpenAI's first custom inference chip delivered 1.5-1.9x more AI work per watt than Nvidia's GB300. Captive silicon is rewriting inference economics.",
      "datePublished": "2026-09-16T06:00:00Z",
      "author": {
        "@type": "Person",
        "name": "Simon"
      },
      "publisher": {
        "@type": "Organization",
        "name": "Editorial Factory"
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is OpenAI's Jalapeño chip?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Jalapeño is OpenAI's first custom inference-only accelerator, co-designed with Broadcom and built from scratch for serving large language models. It went from design to tape-out in nine months, and OpenAI plans initial deployment by the end of 2026."
          }
        },
        {
          "@type": "Question",
          "name": "How much faster is Jalapeño than Nvidia's GB300?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "OpenAI's Aug 25 InferenceX benchmark reports 1.5 to 1.9 times more AI work per watt and 1.7 to 3.6 times lower latency than the comparison systems, at a 700-watt rating against the GB300's 1,400 watts."
          }
        },
        {
          "@type": "Question",
          "name": "Can you buy or rent a Jalapeño chip?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No. Jalapeño is captive to OpenAI and its data-center partners. First production runs at the end of 2026 are very small, with significant deployment in 2027 and a full ramp into 2028."
          }
        }
      ]
    }
  ]
}
```

<!-- internal-links -->
- **Anchor:** `[the memory bandwidth that gates inference]` -> `https://editorialfactory.io/published/2026-09-09_nvidia-279b-memory-bottleneck.md` (*Nvidia's $279B Memory Bet*)
- **Anchor:** `[agentic AI workloads driving GPU demand]` -> `https://editorialfactory.io/published/2026-09-07_anthropic-multiagent-turf-war.md` (*Anthropic's Multi-Agent Framework Turf War*)
- **Anchor:** `[AI adoption without the earnings to match]` -> `https://editorialfactory.io/published/2026-09-08_mckinsey-ai-roi-flat-build-vs-buy-flip.md` (*AI ROI Flat: Build vs Buy Flip*)
