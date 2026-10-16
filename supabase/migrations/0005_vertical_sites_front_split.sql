-- Migration: vertical -> FRONT routing after the giniloh.com / aichieve.net split
--                                  (public.vertical_sites, supersedes 0003's cms.<domain> rule)
-- Idempotent — safe to re-run. Apply in the Supabase SQL editor (same convention as 0003/0004).
--
-- Background (owner, 2026-10-15): giniloh.com was split into two reader fronts — giniloh.com and
-- aichieve.net — and BOTH are served by the one existing CMS, cms.giniloh.com. A vertical therefore
-- routes an article to a *property*, not to a CMS, and `site_domain` now names the FRONT the article
-- is published for while `cms_base_url` names the library that holds it (which may be another front's
-- host: the aichieve.net rows point at cms.giniloh.com, exactly as the giniloh.com rows do).
--
-- 0003 encoded the opposite invariant — `cms_base_url = 'https://cms.' || site_domain` — which the
-- split makes wrong: it forbids 19 of the 31 rows below. That constraint is dropped here and replaced
-- by the shape check that still holds (a `cms.<domain>` https host, no trailing slash). Front coverage
-- is checked by scripts/check_vertical_sites.py against context/frontends.json, which is the front
-- registry the rest of the tooling reads — SQL cannot enumerate it without a second copy of the list.
--
-- The CMS carries the same routing per post: cms.giniloh.com registers a `vertical` taxonomy (one term
-- per vertical id, mu-plugin `vertical-taxonomy.php`) and a post with no term publishes to NO front, so
-- scripts/wp_draft.py resolves the term on the destination and refuses to publish a vertical whose term
-- is missing. cms.wellroost.com registers no such taxonomy (one front serves it).
--
-- NOTE: this table is shared with the other producer publishing through these CMSes — rows for
-- verticals context/verticals.json does not declare ('personal_investing', 'pro_app_notes',
-- 'consumer_cost_per_use', 'personal_compute_hardware', 'giniloh_product_guides') are theirs, not stale
-- rows of ours. The guard reports them as notices.
--
-- Verify (run after applying):
--   select site_domain, count(*) from public.vertical_sites group by 1 order by 1;
--   -- expect: aichieve.net 19 | giniloh.com 7 | wellroost.com 5   (31 rows)
--   select count(*) filter (where wp_category_id is null) as unrouted, count(*) from public.vertical_sites;

-- 0003's rule no longer describes the estate. Re-running 0003 would re-add it, so this file must be
-- applied AFTER it (0003, 0004, then this).
alter table public.vertical_sites drop constraint if exists vertical_sites_cms_host_check;

do $$
declare
  c record;
begin
  for c in
    select * from (values
      ('vertical_sites_cms_host_shape_check',
       'cms_base_url ~ ''^https://cms\.[a-z0-9.-]+$'''),
      ('vertical_sites_frontend_url_check',
       'frontend_url = ''https://'' || site_domain'),
      ('vertical_sites_no_trailing_slash_check',
       'right(cms_base_url, 1) <> ''/'' and right(frontend_url, 1) <> ''/'''),
      ('vertical_sites_id_shape_check',
       'vertical_id ~ ''^[a-z0-9_]+$''')
    ) as t(name, expr)
  loop
    if not exists (
      select 1 from pg_constraint
      where conname = c.name and conrelid = 'public.vertical_sites'::regclass
    ) then
      execute format('alter table public.vertical_sites add constraint %I check (%s)', c.name, c.expr);
    end if;
  end loop;
end $$;

-- Seed / repair. Re-runnable: the routing fields of an existing row are updated in place (an operator's
-- mute is preserved — `active` is set on INSERT only, never reset here), and wp_category_id is left as
-- 0004 set it.
insert into public.vertical_sites (vertical_id, cms_base_url, site_domain, frontend_url, wp_category_id) values
  -- ── aichieve.net — the AI / enterprise-technical property (served by cms.giniloh.com) ──
  ('agentic_ai',                           'https://cms.giniloh.com', 'aichieve.net', 'https://aichieve.net', 9),
  ('agentic_resilience_failure',           'https://cms.giniloh.com', 'aichieve.net', 'https://aichieve.net', 9),
  ('ai_observability_qa',                  'https://cms.giniloh.com', 'aichieve.net', 'https://aichieve.net', 7),
  ('control_tower_exception_orchestration','https://cms.giniloh.com', 'aichieve.net', 'https://aichieve.net', 10),
  ('demand_sensing_advanced_sop',          'https://cms.giniloh.com', 'aichieve.net', 'https://aichieve.net', 10),
  ('enterprise_ai_finops',                 'https://cms.giniloh.com', 'aichieve.net', 'https://aichieve.net', 7),
  ('enterprise_ai_governance',             'https://cms.giniloh.com', 'aichieve.net', 'https://aichieve.net', 3),
  ('enterprise_build_vs_buy',              'https://cms.giniloh.com', 'aichieve.net', 'https://aichieve.net', 7),
  ('enterprise_tech_leadership',           'https://cms.giniloh.com', 'aichieve.net', 'https://aichieve.net', 3),
  ('gpu_hardware',                         'https://cms.giniloh.com', 'aichieve.net', 'https://aichieve.net', 2),
  ('last_mile_routing_fleet_carbon',       'https://cms.giniloh.com', 'aichieve.net', 'https://aichieve.net', 10),
  ('meio_working_capital_tco',             'https://cms.giniloh.com', 'aichieve.net', 'https://aichieve.net', 10),
  ('multi_agent_enterprise_fabric',        'https://cms.giniloh.com', 'aichieve.net', 'https://aichieve.net', 9),
  ('nhil_infrastructure_ops',              'https://cms.giniloh.com', 'aichieve.net', 'https://aichieve.net', 7),
  ('pro_app_notes',                        'https://cms.giniloh.com', 'aichieve.net', 'https://aichieve.net', 11),
  ('supplier_risk_reshoring_decision',     'https://cms.giniloh.com', 'aichieve.net', 'https://aichieve.net', 10),
  ('supply_chain',                         'https://cms.giniloh.com', 'aichieve.net', 'https://aichieve.net', 10),
  ('warehouse_automation_robotics_capex',  'https://cms.giniloh.com', 'aichieve.net', 'https://aichieve.net', 10),
  ('workstation_compute_economics',        'https://cms.giniloh.com', 'aichieve.net', 'https://aichieve.net', 2),

  -- ── giniloh.com — the personal-finance / consumer decision property ──
  ('career_velocity_equity_engineering',   'https://cms.giniloh.com', 'giniloh.com',  'https://giniloh.com', 8),
  ('consumer_cost_per_use',                'https://cms.giniloh.com', 'giniloh.com',  'https://giniloh.com', 2),
  ('expat_cross_border_relocation',        'https://cms.giniloh.com', 'giniloh.com',  'https://giniloh.com', 4),
  ('giniloh_product_guides',               'https://cms.giniloh.com', 'giniloh.com',  'https://giniloh.com', 4),
  ('personal_compute_hardware',            'https://cms.giniloh.com', 'giniloh.com',  'https://giniloh.com', 2),
  ('personal_investing',                   'https://cms.giniloh.com', 'giniloh.com',  'https://giniloh.com', 4),
  ('personal_microeconomics_tinkering_tax','https://cms.giniloh.com', 'giniloh.com',  'https://giniloh.com', 4),

  -- ── wellroost.com — the home / property property (its own CMS, no vertical taxonomy there) ──
  ('home_equity_tco',                      'https://cms.wellroost.com', 'wellroost.com', 'https://wellroost.com', 4),
  ('home_infrastructure_lifecycle_tco',    'https://cms.wellroost.com', 'wellroost.com', 'https://wellroost.com', 4),
  ('home_ops_execution',                   'https://cms.wellroost.com', 'wellroost.com', 'https://wellroost.com', 3),
  ('resilient_home_assets',                'https://cms.wellroost.com', 'wellroost.com', 'https://wellroost.com', 4),
  ('smart_home_telemetry',                 'https://cms.wellroost.com', 'wellroost.com', 'https://wellroost.com', 5)
on conflict (vertical_id) do update
  set cms_base_url = excluded.cms_base_url,
      site_domain  = excluded.site_domain,
      frontend_url = excluded.frontend_url,
      updated_at   = now();
