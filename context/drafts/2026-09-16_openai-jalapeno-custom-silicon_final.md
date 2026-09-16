---
title: "OpenAI's custom chip beats Nvidia on power"
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
OpenAI’s first custom chip beat Nvidia on the one metric that limits Artificial Intelligence (AI) scale: power use [2]. The new Jalapeño chip runs models instead of training them. It does 1.5 to 1.9 times more work per watt than Nvidia's GB300 [2]. It also cuts wait times by up to 3.6 times. It draws under 550 watts, compared to 1,400 watts for the Nvidia part [2].

<!-- tension -->
## Buyers build their own chips

**Why it matters:** Power, not chip supply, now limits how fast companies can add server space [4]. OpenAI's hardware lead tracks success in tokens per megawatt, not tokens per second [4]. A chip wins by doing more useful work per watt. It no longer wins just by hitting a high peak speed.

**The big picture:** Every major tech lab has made this same choice. OpenAI calls Jalapeño a strong path alongside hardware from Nvidia, Advanced Micro Devices (AMD), Broadcom, Cerebras, and CoreWeave [3]. The largest buyers of merchant Graphics Processing Units (GPUs) are all building custom chips at once [5]. 

Google runs its Tensor Processing Unit (TPU) line. Amazon runs Trainium. Microsoft runs Maia. Meta's Iris chip also entered production this month [5].

> "The metric that matters is tokens generated per dollar per watt. Peak theoretical Tera Floating Point Operations Per Second (TFLOPS) on a spec sheet is vendor marketing." — Founder Note

Jalapeño marks the first time a custom lab chip posted a public test against Nvidia's top part [1]. The design went from a first sketch to tape-out—the final step before making the chip—in just nine months [1]. OpenAI even used its own Large Language Models (LLMs) to speed up parts of the design work [1].

<!-- tactical-insight -->
## The infrastructure playbook

You cannot buy a Jalapeño chip. It belongs to OpenAI and will not ship in high volume until 2027 or 2028 [4]. But this test signals a three-part shift in how to judge hardware.

- **Benchmark per watt, not per chip.** OpenAI tested Jalapeño on InferenceX across three models: Generative Pre-trained Transformer (GPT) Open Source Software (OSS) 120B, DeepSeek R1 670B, and Kimi K2.5 1T [2]. On the massive Kimi model, Jalapeño delivered 1.5 times the peak speed per watt and 3.4 times lower delay than Nvidia [2]. Track work-per-watt, or you are watching the wrong metric.
- **Match parts to workloads.** Jalapeño is built strictly to run models, not train them. Nvidia's general parts do both. High-end training runs still pay for that flexibility [3]. Keep training on flexible graphics chips. Move steady work to purpose-built silicon to lower your cost per token.
- **Right-size before you re-buy.** The cheapest upgrade is often the memory and silicon you already own. One software team cut its monthly server bill from $28,000 to $9,500. They did this by moving to the virtual Large Language Model (vLLM) memory manager with 8-bit Floating Point (FP8) math. Check your current hardware use before chasing new parts.

<!-- nuanced-takeaway -->
## The honest catch

**The catch:** These are vendor-reported numbers from before the chips hit real servers [4]. First production runs at the end of 2026 will be small. Large setups land in 2027, and a full scale-up extends into 2028 [4]. OpenAI has also not promised to pass these power savings through to Application Programming Interface (API) pricing [4].

The chip is real, but Nvidia still sells the vast majority of hardware. The test proves custom silicon is closing the cost gap. However, it will not threaten Nvidia's training lead for at least 18 months.

**Go deeper:** Explore the sources and internal links below.

<!-- tldr -->
- OpenAI's custom chip, Jalapeño, did 1.5 to 1.9 times more work per watt than Nvidia's GB300 on the August 25 InferenceX test [2].
- Power limits scale, pushing massive buyers like OpenAI, Google, Amazon, Microsoft, and Meta to build their own custom silicon [3][5].
- Server teams must track speed-per-watt and match specific parts to workloads, though Jalapeño will not ship at scale until 2027 [4].

## Sources
[1] OpenAI, "OpenAI and Broadcom unveil LLM-optimized inference chip" (June 24, 2026) — https://openai.com/index/openai-broadcom-jalapeno-inference-chip
[2] OpenAI, "Jalapeño's first results show industry-leading speed and efficiency in AI inference" (Aug 25, 2026) — https://openai.com/index/jalapeno-first-results/
[3] Sarah Friar, "The full stack behind abundant intelligence" (Aug 25, 2026) — https://openai.com/index/the-full-stack-behind-abundant-intelligence/
[4] TechTimes, "OpenAI Jalapeño Chip Posts 1.9x Efficiency Lead Over Nvidia; Huang Answers With $96B Quarter" (Aug 27, 2026) — https://www.techtimes.com/articles/325710/20260827/openai-jalapeno-chip-posts-19x-efficiency-lead-over-nvidia-huang-answers-96b-quarter.htm
[5] Reuters, "Meta to put AI chip into production in September as it looks to double computing capacity" (July 9, 2026) — https://www.reuters.com/world/asia-pacific/meta-put-ai-chip-into-production-september-it-looks-double-computing-capacity-2026-07-09

<!-- linkedin -->
OpenAI built its own chip. The first test just dropped — and it beats Nvidia where the power bill lives.

The numbers, from OpenAI's own August 25 results on InferenceX:

• 1.5–1.9× more work per watt than Nvidia's GB300
• 1.7–3.6× lower end-to-end delay
• 700 W rated (ran at ≤550 W), vs 1,400 W for the Nvidia part it beat

Jalapeño is a chip built just to run models. It was built from scratch with Broadcom in a nine-month tape-out. That is the fastest custom chip cycle OpenAI says has ever been done. It was even partly designed by OpenAI's own models.

The context is the real story. Power is now the ceiling on scale, not chips. Every lab is building captive silicon at once: Google, Amazon, Microsoft, and Meta. The biggest buyers of Nvidia hardware are all becoming their own suppliers.

The catch: These are vendor-reported numbers from before the chips hit real servers. First runs at the end of 2026 are tiny; the real ramp is 2027–2028. And OpenAI has not said it will pass the savings to developers.

For teams buying compute, the takeaway is blunt: Benchmark per watt, not per chip. Match parts to workloads — training stays on flexible graphics chips, while running models is where purpose-built silicon wins. And right-size what you already have before you re-buy.

The metric that matters was never peak speed. It is tokens per dollar per watt.

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

## Gate report
lead: PASS — Delivers the efficiency win over Nvidia in sentence 1 with zero throat-clearing.
tension: PASS — Frames the structural shift to captive silicon using "Why it matters:" and "The big picture:"; H2 is 5 words.
tactical-insight: PASS — Features 3 actionable bullets with bold lead-ins detailing practitioner moves; H2 is 3 words.
nuanced-takeaway: PASS — Presents the honest limitation about deployment timelines and API pricing with "The catch:" signpost; H2 is 3 words.
tldr: PASS — Exactly 3 scannable bullets summarizing the entire piece without a prose paragraph.
