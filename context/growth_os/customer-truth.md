# Customer Truth & Field Reality (`customer-truth.md`)

This document captures real customer friction, anonymized case studies, operational pain points, and live benchmark numbers. Injected into our content machine to ground every article in practitioner truth rather than theoretical speculation.

---

## 1. Practitioner Field Notes by Vertical

### Vertical: `agentic_ai` (Agentic Runtime & Architecture)
- **Anecdote 1: The Infinite Loop Incident**: A Fortune 500 financial team deployed an autonomous multi-agent tool calling loop to resolve account discrepancy tickets. Because error handling was non-deterministic, two agents entered an unconstrained back-and-forth critique loop, burning $4,200 in OpenAI API credits in 45 minutes before hitting rate limits.
  *Lesson:* Deterministic recursion budgets (max steps = 5) and cost ceilings per session are mandatory.
- **Anecdote 2: Tool Calling Hallucination & Schema Bloat**: A customer built an agent with 35 separate tool definitions. Accuracy collapsed to 41% because the LLM confused overlapping parameter schemas. When reduced to 6 atomic tools with strict JSON schemas and MCP endpoints, accuracy climbed to 93%.
  *Lesson:* Fewer, distinct tools beat massive tool registries.
- **Anecdote 3: Flat Context Degradation vs L1-L4 Tiering**: Long agent trajectories degraded in reasoning quality past 12,000 tokens when using a single flat history. Implementing a 4-tier memory hierarchy (L1 scratchpad, L2 compacted summary, L3 vector store, L4 SQL entities) reduced token overhead by 68% and eliminated trajectory drift.

---

### Vertical: `ai_observability_qa` (Observability, Evals & Quality)
- **Anecdote 1: Flamegraph Reveals 14x Redundant Retries**: An enterprise customer suspected model latency issues when average task completion reached 42 seconds. A trace flamegraph revealed the model was repeatedly failing a hidden regex validation on a date field, silently re-prompting itself 14 times per task. Fixing the tool schema cut task latency to 2.8 seconds.
- **Anecdote 2: LLM-as-a-Judge Drift**: A team using GPT-4 to judge synthetic agent outputs noticed their pass rate rose from 74% to 96% over two months. An audit revealed the judge model suffered from severe length-bias and sycophancy. Replacing single-turn judge prompts with a calibrated bifurcated QA pipeline (deterministic JSON assertions + multi-evaluator consensus) dropped the true pass rate back to 68% and surfaced 22 production-critical regressions.

---

### Vertical: `agentic_resilience_failure` (Resilience & Failure Engineering)
- **Anecdote 1: The Compound Failure Mathematics ($0.95^{10}$)**: A customer launched an autonomous DevOps agent requiring a 10-step chain of API calls (provisioning VMs, DNS updates, TLS generation, DB migration). Although each individual tool call boasted a 95% success rate, the end-to-end task completion rate stalled at 59.8% ($0.95^{10}$), causing constant human paging. Adding transactional checkpoints with idempotent retries brought end-to-end reliability to 98.4%.
- **Anecdote 2: Mid-Task API Crash Without Checkpointing**: An automated invoice reconciliation agent failed at Step 8 of a 9-step workflow due to a Stripe 504 timeout. Because state was kept in volatile memory, the entire run restarted, resulting in duplicate ledger entries and $18,000 in double-booked disbursements. Implementing durable execution checkpoints with rollback triggers resolved the issue completely.

---

### Vertical: `enterprise_ai_governance` (Enterprise Enablement & Agent Security)
- **Anecdote 1: The Rogue Agent Data Exfiltration**: An engineering team created an unmonitored shadow AI agent to summarize internal Jira issues and customer support logs. An indirect prompt injection embedded inside an external ticket caused the agent to dump customer PII to an external webhook. The enterprise responded by implementing zero-trust egress firewalls and migrating all shadow agents to an audited, centrally managed gateway.
- **Anecdote 2: Prompt Cache Miss CFO Shock**: A customer deployed an enterprise search assistant expecting token costs of $0.0015/query based on prompt caching rates. Because dynamic timestamps and random session IDs were injected at the head of the system prompt, prompt caching failed on 99% of requests, inflating monthly API costs from $3,200 to $29,000. Refactoring the prompt layout to stabilize cache prefixes restored 94% cache hit rates.

---

### Vertical: `supply_chain` (Supply Chain Orchestration & Physical Logistics)
- **Anecdote 1: The 20-Year SAP Customization Wall**: A $400M industrial distributor spent $12M over 18 months attempting to customize their monolithic SAP ERP to support multi-carrier regional parcel routing. The project stalled due to brittle ABAP dependencies. Inserting an event-driven 3-layer integration stack with an API-first TMS connected 6 regional carriers in 45 days at $420k total cost.
- **Anecdote 2: Multi-Echelon Inventory Optimization (MEIO) Cash Release**: A consumer electronics brand holding $85M in finished goods across 4 regional hubs implemented MEIO. By calculating echelon stock decouples rather than localized single-node safety buffers, they liberated $18.4M in working capital within 90 days while improving on-time in-full (OTIF) fulfillment from 91.2% to 97.6%.
- **Anecdote 3: The Fixed AS/RS Capex Trap**: A 3PL invested $22M into a rigid high-bay AS/RS facility engineered specifically for standard pallet heights. Two years later, their anchor retail client shifted to oversized polybags and custom carton dimensions, rendering 40% of the cranes obsolete. Transitioning to leased AMRs on a RaaS model enabled dynamic aisle re-slotting within 72 hours.
- **Anecdote 4: The Tier-3 Photoresist Plant Fire**: An automotive Tier-1 supplier experienced a 6-week factory halt because a single Tier-3 chemical supplier in Kumamoto, Japan suffered a cleanroom fire. The OEM and Tier-1 had zero visibility into sub-tier single-source dependencies until component shipments stopped arriving.
- **Anecdote 5: Autonomous Demurrage & Detention Agent**: An international apparel importer faced $320,000/month in marine terminal container demurrage due to slow document handling and missed drayage appointment slots. Deploying an autonomous exception agent that auto-monitored terminal telematics, rescheduled drayage appointments, and auto-filed detention disputes reduced total penalty fees by 72% ($230,000/month net savings).
- **Anecdote 6: The Section 301 Reclassification Shock**: A mid-sized importer faced retroactive $1.2M duties because customs reclassified an electronic component under a different HTS code without warning. Integrating real-time customs tariff change webhooks into their S&OP pipeline prevented an additional $2.8M in unexpected duty liabilities.

---

### Vertical: `enterprise_tech_leadership` (Technology & Architecture Decisions)
- **Anecdote 1: The Cloud Egress Shock**: A high-volume data ingest startup was paying $68,000/month in AWS NAT Gateway and inter-AZ data transfer fees alone. Moving steady-state pipeline workloads to dedicated metal reduced their monthly infrastructure cost to $14,200.
- **Anecdote 2: Microservice Sprawl**: A 25-engineer engineering org had 48 microservices across 3 Kubernetes clusters. Onboarding a new backend engineer took 3 weeks. Consolidating into 2 modular monoliths cut deployment cycle time from 4 days to 25 minutes.

---

### Vertical: `gpu_hardware` (GPUs & AI Hardware)
- **Anecdote 1: The vLLM / TensorRT-LLM Tuning Win**: An AI SaaS company cut their monthly GPU cloud bill from $28,000 to $9,500 simply by switching from standard PyTorch inference to vLLM with PagedAttention and FP8 quantization on H100s, tripling throughput per GPU.
- **Anecdote 2: Cold Starts on Serverless GPU**: Serverless GPU container spin-up latencies of 15–30 seconds were unacceptable for interactive user sessions. Pre-warmed pools with dynamic batching were essential.

---

### Vertical: `home_systems_reno` (Modern Home Infrastructure & Building Science)
- **Anecdote 1: The Panel Upgrade Surprise**: A homeowner bought a $18,000 cold-climate heat pump + EV charger only to find their 100A main electrical panel required a $4,500 utility service upgrade that took 9 months to permit.
- **Anecdote 2: The Auxiliary Heat Spike**: Installing an undersized heat pump caused electric resistance heat strips to run during a 10°F cold snap, resulting in an $850 monthly electric bill.

---

## 2. Extraction Guidelines for the Drafter
- Pick at least 1 specific customer truth / field anecdote per article to make the technical tension tangible.
- Quote or paraphrase exact dollar figures, failure probabilities ($0.95^{10}$), or latency numbers.
- Explicitly trace how the architectural decision directly avoids the field failure.
