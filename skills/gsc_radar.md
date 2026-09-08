# SKILL: Google Search Console (GSC) Opportunity Radar

## 1. Objective
Identify high-impact search queries directly from Google Search Console (GSC) analytics to drive demand-led editorial drafting.

## 2. Trigger Criteria
A query qualifies as an SEO content candidate when it meets any of the following:
1. **Striking Distance Gate**:
   - Total Impressions ≥ **500** in the last 28 days.
   - Average Position between **8.0 and 25.0** (page 2 or bottom of page 1).
2. **Emerging Demand Spike**:
   - Week-over-Week (WoW) impression growth ≥ **50%**.
   - Minimum impression floor of **300**.
3. **Low-CTR High-Volume Term**:
   - Impressions ≥ **1,000** with CTR < 3.0%.

## 3. Execution Protocol

### Step 1 — Fetch Analytics Data
Run the GSC Analyzer:
```bash
python3 scripts/gsc_analyzer.py --vertical <vertical_id> --min-impressions 500 --min-pos 8 --max-pos 25 --wow-threshold 50 --export-md
```

### Step 2 — Opportunity Scoring
Each query is evaluated on a composite **Opportunity Score (0–100)**:
- **Volume Factor (35%)**: Relative monthly impressions.
- **Position Factor (30%)**: Proximity to top 5 rankings (`1 - (pos-1)/30`).
- **Growth Velocity (25%)**: Week-over-Week trend.
- **CTR Gap (10%)**: Room for CTR lift via superior headlines & meta descriptions.

### Step 3 — Output Artifact
Generates: `context/recon_proposals/YYYY-MM-DD_gsc_<vertical>_opportunities.md`

## 4. Failure Handling
If no queries clear the threshold for a vertical:
- Broaden the impression threshold to 300 impressions.
- If still empty, fall back to the 30-day industry news radar (`skills/radar_30day.md`) — never invent demand.
