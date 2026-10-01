-- Migration: route each vertical to a WordPress category (public.vertical_sites.wp_category_id)
-- Idempotent — safe to re-run. Apply in the Supabase SQL editor (same convention as 0003).
--
-- Background: both sites file every published post under a real category — 24/24 on giniloh.com
-- and 4/4 on wellroost.com — but a draft pushed by scripts/wp_draft.py landed in WordPress's
-- default (Uncategorized), leaving the operator a step they had already done by hand, and, if
-- missed, a published post that never appears on any category page.
--
-- The id is per-site (giniloh #4 is "Money & Wealth", wellroost #4 is "Energy & Efficiency"), so it
-- is routed per vertical here rather than derived from the vertical name in code. scripts/wp_draft.py
-- validates the id against the destination before pushing, so a copy-pasted value from the other
-- site fails loudly instead of silently misfiling a post.
--
-- Mappings below are marked either EVIDENCE (justified by an existing published post or by an exact
-- name match) or INFERRED (judgement — adjust with a single UPDATE if you disagree).

alter table public.vertical_sites add column if not exists wp_category_id integer;

alter table public.vertical_sites drop constraint if exists vertical_sites_category_positive_check;
alter table public.vertical_sites
  add constraint vertical_sites_category_positive_check
  check (wp_category_id is null or wp_category_id > 0);

-- ── giniloh.com ──────────────────────────────────────────────────────────────
-- Categories: 7 AI Stack & Tool TCO | 6 Artificial Intelligence & Future of Work |
--             9 Autonomous & Agentic Workflows | 8 Career & AI Resilience | 10 Supply Chain &
--             Operations | 2 Major Purchases & Assets | 3 Mental Models & Strategy | 4 Money & Wealth
--
-- EVIDENCE: the live build-vs-buy post (enterprisebuildvsbuy-the-250k-ai-upkeep-tax) is filed
-- under #7, and #7/#2/#3/#4 are the buckets the manual flow actually used (6 posts each).

-- EVIDENCE — exact category-name match
update public.vertical_sites set wp_category_id = 9, updated_at = now()
  where vertical_id in ('agentic_ai', 'agentic_resilience_failure', 'multi_agent_enterprise_fabric');
-- EVIDENCE — the published build-vs-buy article is in this category
update public.vertical_sites set wp_category_id = 7, updated_at = now()
  where vertical_id in ('enterprise_build_vs_buy', 'enterprise_ai_finops');
-- EVIDENCE — exact category-name match
update public.vertical_sites set wp_category_id = 8, updated_at = now()
  where vertical_id in ('career_velocity_equity_engineering');

-- INFERRED — tooling / spend visibility, no published precedent
update public.vertical_sites set wp_category_id = 7, updated_at = now()
  where vertical_id in ('ai_observability_qa', 'nhil_infrastructure_ops');
-- INFERRED — buying hardware or compute capacity is a major-purchase decision
update public.vertical_sites set wp_category_id = 2, updated_at = now()
  where vertical_id in ('gpu_hardware', 'workstation_compute_economics');
-- INFERRED — strategy / org design
update public.vertical_sites set wp_category_id = 3, updated_at = now()
  where vertical_id in ('enterprise_tech_leadership', 'enterprise_ai_governance');
-- INFERRED — personal finance decisions
update public.vertical_sites set wp_category_id = 4, updated_at = now()
  where vertical_id in ('expat_cross_border_relocation', 'personal_microeconomics_tinkering_tax');
-- Operations / supply chain — category #10 "Supply Chain & Operations", created in WordPress for
-- these seven (the manual flow never published one here, so #3 was the closest bucket until now).
-- Created via the REST API on cms.giniloh.com (slug supply-chain-operations); scripts/check_
-- vertical_sites.py fails if a routed vertical has no category, and the sweep names this file.
update public.vertical_sites set wp_category_id = 10, updated_at = now()
  where vertical_id in ('supply_chain', 'meio_working_capital_tco',
                        'control_tower_exception_orchestration', 'warehouse_automation_robotics_capex',
                        'demand_sensing_advanced_sop', 'last_mile_routing_fleet_carbon',
                        'supplier_risk_reshoring_decision');

-- ── wellroost.com ────────────────────────────────────────────────────────────
-- Categories: 4 Energy & Efficiency | 2 Home Cost Decisions | 15 Lifestyle |
--             5 Smart Home & Security | 3 Tools & Equipment
--
-- EVIDENCE: the published Emporia Vue monitor sits in #5, and the two heat-pump posts in #4.

-- EVIDENCE — name match + the published heat-pump/energy posts
update public.vertical_sites set wp_category_id = 4, updated_at = now()
  where vertical_id in ('home_equity_tco', 'home_infrastructure_lifecycle_tco', 'resilient_home_assets')
    and site_domain = 'wellroost.com';
-- EVIDENCE — name match + the published Emporia Vue post
update public.vertical_sites set wp_category_id = 5, updated_at = now()
  where vertical_id = 'smart_home_telemetry' and site_domain = 'wellroost.com';
-- INFERRED — contractor/tools work rather than a costing decision
update public.vertical_sites set wp_category_id = 3, updated_at = now()
  where vertical_id = 'home_ops_execution' and site_domain = 'wellroost.com';

-- Verify (expect 26 rows routed, 0 null):
--   select count(*) filter (where wp_category_id is null) as unrouted, count(*) from public.vertical_sites;
--   select site_domain, wp_category_id, count(*) from public.vertical_sites
--     group by 1, 2 order by 1, 2;
