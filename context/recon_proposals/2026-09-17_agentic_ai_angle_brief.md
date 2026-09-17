# Angle Brief: agentic_ai — 2026-09-17

**Winner:** Salesforce's own researchers just measured the thing this vertical has been arguing for a year: reworking the harness around a smaller model lifted task success from 29.2% to 78.0% across seven enterprise benchmarks without touching model weights — and then fine-tuning the model to copy a stronger one made it *worse* (78.0% → 63.1%). That finding is now the explicit architecture of Salesforce's "Enterprise AI Harness," shipped at Dreamforce 2026 with MCP as the integration fabric.

**Scores:** N=8 A=9 S=9 → Composite=8.6

**Hook:** In a September 2026 preprint (arXiv:2609.09134), Salesforce researchers evolved the "harness" — the system prompt, tool set, execution hooks, and context-management scaffolding around a model — for a smaller Qwen model. Mean task success jumped from 29.2% to 78.0% (+48.8 points) with the model weights untouched. Then they fine-tuned that same model to imitate a stronger one: success *fell* to 63.1%. A targeted "on-policy correction" recovered it to 79.7%.

**Tension:** For two years the agentic story has been "a frontier model is a better agent." Salesforce's data inverts it: the leverage is in the deterministic boundary around the model — the harness — not the weights. And the counterintuitive kicker: upgrading a model inside a harness tuned for the old one can *regress* the system ("model–harness fit"). Salesforce productized the finding the same week: its Enterprise AI Harness (six capabilities — context, agency, action, governance, security, models) and Headless 360, which exposes the whole platform as MCP tools that Claude, ChatGPT, Cursor, and Agentforce can discover and invoke. Google Cloud (Gemini Enterprise over MCP) and AWS (Bedrock/Quick) both wired the same bridge on the same day.

**Target reader:** ai_architect

**Single claim to defend:** Salesforce's own research (arXiv:2609.09134, Sep 2026) found that evolving the agent harness around a smaller model lifted task success from 29.2% to 78.0% across seven enterprise benchmarks without changing model weights — while fine-tuning the model to imitate a stronger one dropped it to 63.1% — and Salesforce is now productizing that finding as the Enterprise AI Harness (context, agency, action, governance, security, models) with MCP as the integration fabric (Headless 360, Gemini Enterprise interop).

**Runner-ups + why rejected:**
- Koa CRM reasoning model (Sep 15): fresh and concrete ("3x fewer errors"), but a single-vendor model release; folded in as corroboration that even Salesforce keeps the model a swappable component inside the harness. N=7, S=6.
- Google A2A → AAIF governance consolidation (Aug 17–20): protocol-consolidation angle, but near-window-edge and already rejected as a runner-up on 09-10 (N=7 S=6, governance not practitioner-actionable). Retread per §3.5.
- Cloudflare "agentic internet" content rules (Sep 15): fresh but publisher-crawler governance, off-angle for ai_architect. N=6.
- Rubrik MCP support (Sep 15): single-vendor MCP release, table stakes. N=5.

**Prior-cycle de-dup check (passed):** OWASP Excessive Agency (09-03, permissions), Anthropic multi-agent turf war (09-07, safety), Google 4 patterns (09-10, determinism engineering patterns), OpenAI Agents API (09-14, loop runtime commoditization). This candidate is a "harness > model, quantified" thesis with a primary arXiv source and a fresh productization event — new source, new angle, new event. Not a retread.
