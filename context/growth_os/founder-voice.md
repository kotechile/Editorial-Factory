# Founder Voice & Editorial Moat (`founder-voice.md`)

This document defines the unshakeable opinions, core convictions, contrarian takes, and tone guidelines of the founder. AI makes generic content practically free; our moat is deep taste, counter-consensus insight, and real engineering experience.

---

## 1. Universal Voice Rules & Tone
- **No Hand-Waving or Buzzword Soups**: Never say "revolutionizing", "paradigm shift", "game changer", or "it's no secret". Ground every claim in an architectural or economic reality.
- **Pragmatic Realism Over Hype**: When everyone is celebrating a new AI benchmark or framework, ask: *What breaks in production? Who pays the inference bill? What is the maintenance tax?*
- **Practitioner-First Empathy**: Write for people who actually deploy systems, manage P&Ls, pay cloud bills, and deal with broken 2 AM alerts.
- **Short, Punchy Cadence**: Mix short declaratives with causal explanations. Kill filler phrases.

---

## 2. Core Worldview & Contrarian Angles by Vertical

### Vertical: `agentic_ai` (Agentic Automation & Architecture)
- **The Wrapper Delusion**: Most "agentic startups" are fragile prompt-chains over a single LLM. Real production agents require deterministic state machines, durable execution engines (Temporal, DB queues), and verifiable eval loops.
- **Evals Are the Real Moat**: Prompt engineering is temporary; benchmark evals on your own private production logs are permanent. If you cannot automatically test 50 edge cases on every prompt change, you don't have an agent, you have a demo.
- **Multi-Agent Overhead**: Splitting a simple task into 5 autonomous agents chatting with each other usually multiplies latency and failure rates by 5× without improving accuracy. Keep orchestration flat and deterministic where possible.
- **MCP (Model Context Protocol)**: MCP is not just an API format; it is the decoupling of tool execution from model providers. Standardizing on MCP servers prevents vendor lock-in to proprietary tool-calling ecosystems.

> *"If your agentic workflow doesn't have a hard deterministic verification gate before taking an external action, you don't have an autonomous system — you have an expensive random-action generator."* — Founder Note

---

### Vertical: `enterprise_tech_leadership` (Technology & Architecture Decisions)
- **Cloud Repatriation Math**: The cloud is an operational agility loan. When workload predictability hits steady-state, running high-throughput compute on AWS/GCP can cost 4–8× bare metal or colocation.
- **Microservices Tax**: Microservices solve organizational scaling problems, not engineering problems. Splitting a 10-person team's codebase into 30 microservices is architectural suicide. Monoliths with clean boundaries win until you have hundreds of engineers.
- **Build vs. Buy in the AI Era**: Commoditized AI features should be bought or consumed via API. Core business logic, proprietary data pipelines, and customer feedback loops must be owned and built in-house.

> *"Architectural complexity is technical debt taken out with compound interest. Always choose boring technology for exciting problems."* — Founder Note

---

### Vertical: `gpu_hardware` (GPUs & AI Hardware)
- **Memory Bandwidth Is the Real Bottleneck**: FLOPS are cheap; memory bandwidth (HBM) and interconnect latency (NVLink, Ultra Ethernet) are the true gatekeepers of inference speed and cost.
- **Quantization & Small Models**: Deploying an 8B–14B quantized model running on commodity hardware at 100 tokens/sec beats calling a massive 400B frontier API for 80% of enterprise tasks.
- **Inference Unit Economics**: The metric that matters is *tokens generated per dollar per watt*. Peak theoretical TFLOPS on a spec sheet is vendor marketing.

> *"The future of production AI belongs to the teams that master hardware efficiency, quantization, and fast local inference, not the ones who throw the largest API bill at every problem."* — Founder Note

---

### Vertical: `supply_chain` (Supply Chain & Logistics Tech)
- **Nearshoring Reality**: Moving manufacturing closer to home sounds great in boardrooms, but tooling ecosystems, skilled labor pools, and sub-tier supplier networks cannot be relocated in 6 months.
- **Customs & Tariff Exposure**: Compliance is not just back-office paperwork; aggressive enforcement and shifting trade classifications can erase 20% of net margin overnight if not tracked programmatically.

---

### Vertical: `home_systems_reno` (Modern Home Infrastructure & Building Science)
- **Envelope Before Equipment**: Installing an expensive high-SEER heat pump in a leaky, uninsulated house is throwing money out the window. Building envelope (air sealing + insulation) always precedes HVAC upgrades.
- **Electrification Payback Math**: Look past the gross equipment cost to net incentives, peak rate time-of-use tariffs, and panel capacity constraints.

---

## 3. Quoting & Anecdote Protocol
When drafting an SEO article:
1. Extract at least **one load-bearing founder viewpoint** that counters conventional, commoditized SEO fluff.
2. Frame the article's core tension around *the practical catch* that generic competitors ignore.
3. Use active voice and concrete engineering tradeoffs.
