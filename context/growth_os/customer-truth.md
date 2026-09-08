# Customer Truth & Field Reality (`customer-truth.md`)

This document captures real customer friction, anonymized case studies, operational pain points, and live benchmark numbers. Injected into our content machine to ground every article in practitioner truth rather than theoretical speculation.

---

## 1. Practitioner Field Notes by Vertical

### Vertical: `agentic_ai`
- **Anecdote 1: The Infinite Loop Incident**: A Fortune 500 financial team deployed an autonomous multi-agent tool calling loop to resolve account discrepancy tickets. Because error handling was non-deterministic, two agents entered an unconstrained back-and-forth critique loop, burning $4,200 in OpenAI API credits in 45 minutes before hitting rate limits.
  *Lesson:* Deterministic recursion budgets (max steps = 5) and cost ceilings per session are mandatory.
- **Anecdote 2: Tool Calling Hallucination**: A customer built an agent with 35 separate tool definitions. Accuracy collapsed to 41% because the LLM confused overlapping parameter schemas. When reduced to 6 atomic tools with strict JSON schemas, accuracy climbed to 93%.
  *Lesson:* Fewer, distinct tools beat massive tool registries.
- **Anecdote 3: Context Window Degradation**: Long agent trajectories degraded in quality past 12,000 tokens of chat history. The fix wasn't a larger context window, but a state summary compaction pass between loops.

---

### Vertical: `enterprise_tech_leadership`
- **Anecdote 1: The Cloud Egress Shock**: A high-volume data ingest startup was paying $68,000/month in AWS NAT Gateway and inter-AZ data transfer fees alone. Moving steady-state pipeline workloads to dedicated metal reduced their monthly infrastructure cost to $14,200.
- **Anecdote 2: Microservice Sprawl**: A 25-engineer engineering org had 48 microservices across 3 Kubernetes clusters. Onboarding a new backend engineer took 3 weeks. Consolidating into 2 modular monoliths cut deployment cycle time from 4 days to 25 minutes.

---

### Vertical: `gpu_hardware`
- **Anecdote 1: The vLLM / TensorRT-LLM Tuning Win**: An AI SaaS company cut their monthly GPU cloud bill from $28,000 to $9,500 simply by switching from standard PyTorch inference to vLLM with PagedAttention and FP8 quantization on H100s, tripling throughput per GPU.
- **Anecdote 2: Cold Starts on Serverless GPU**: Serverless GPU container spin-up latencies of 15–30 seconds were unacceptable for interactive user sessions. Pre-warmed pools with dynamic batching were essential.

---

### Vertical: `supply_chain`
- **Anecdote 1: The Section 301 Reclassification**: A mid-sized importer faced retroactive $1.2M duties because customs reclassified an electronic component under a different HTS code. They had no automated tariff change alert system in place.
- **Anecdote 2: Warehouse Automation Bottleneck**: Buying autonomous mobile robots (AMRs) increased picking throughput by 40%, but packing and dock loading became the new bottleneck, resulting in zero net improvement in truck turnaround time.

---

### Vertical: `home_systems_reno`
- **Anecdote 1: The Panel Upgrade Surprise**: A homeowner bought a $18,000 cold-climate heat pump + EV charger only to find their 100A main electrical panel required a $4,500 utility service upgrade that took 9 months to permit.
- **Anecdote 2: The Auxiliary Heat Spike**: Installing an undersized heat pump caused electric resistance heat strips to run during a 10°F cold snap, resulting in an $850 monthly electric bill.

---

## 2. Extraction Guidelines for the Drafter
- Pick 1 specific customer truth / field anecdote per article to make the tension tangible.
- Quote or paraphrase the exact dollar figures, percentages, or operational bottlenecks.
