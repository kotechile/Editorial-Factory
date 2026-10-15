#!/usr/bin/env python3
"""Tests for the reader-front registry — run: python3 scripts/test_frontends.py

Hermetic: no network. The URL lists below are the real sitemap <loc> values captured from the
three fronts on 2026-10-15 and embedded verbatim, so the served-category and candidate-shape
rules are exercised against the front ends' actual published output. Everything else is
constructed. The registry under test is the shipped context/frontends.json.
"""

from __future__ import annotations

import contextlib
import json
import pathlib
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import frontends as fe  # noqa: E402

PASS, FAIL = [], []


def check(name, condition, detail=""):
    (PASS if condition else FAIL).append(name)
    print(f"  [{'ok ' if condition else 'FAIL'}] {name}{'' if condition else f'  <- {detail}'}")


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
REGISTRY = REPO_ROOT / "context" / "frontends.json"

# Real sitemap <loc> values, captured 2026-10-15 (giniloh.com /sitemap.xml, wellroost.com and
# aichieve.net /sitemap-index.xml -> sitemap-0.xml). Embedded so the suite needs no network.
AICHIEVE_URLS = [
    "https://aichieve.net/",
    "https://aichieve.net/100-case-eval-925-coverage/",
    "https://aichieve.net/about/",
    "https://aichieve.net/agent-audit-trail-not-evidence/",
    "https://aichieve.net/agent-failure-topology-not-model/",
    "https://aichieve.net/agent-failures-tests-stayed-green/",
    "https://aichieve.net/agent-memory-poisoning-write-path/",
    "https://aichieve.net/agent-memory-tiering-l1-l4/",
    "https://aichieve.net/agent-reliability-pass-k-not-one-green-run/",
    "https://aichieve.net/agent-safety-gate-moves-to-verified-state/",
    "https://aichieve.net/agent-timeout-false-alarm-budget/",
    "https://aichieve.net/agent-tool-count-ceiling/",
    "https://aichieve.net/agentic-ai-adoption-soars-but-profits-stall-in-2026/",
    "https://aichieve.net/ai-coding-seats-measure-or-renew/",
    "https://aichieve.net/ai-incident-clock-4-hours-not-15-days/",
    "https://aichieve.net/ai-spend-27t-cost-visibility-mandate/",
    "https://aichieve.net/air-freight-wont-price-a-year/",
    "https://aichieve.net/apps/",
    "https://aichieve.net/articles/",
    "https://aichieve.net/author/gini-loh/",
    "https://aichieve.net/automation-payback-splits-by-sku-geometry/",
    "https://aichieve.net/aws-cannot-restore-bahrain/",
    "https://aichieve.net/azure-control-plane-single-point-of-failure/",
    "https://aichieve.net/build-wait-payback-threshold/",
    "https://aichieve.net/buying-ai-quality-when-the-score-belongs-to-the-judge/",
    "https://aichieve.net/cache-boundary-decides-input-bill/",
    "https://aichieve.net/caseproof-stop-signing-3m-warehouse-automation-deals-on-a-vendors/",
    "https://aichieve.net/categories/",
    "https://aichieve.net/categories/artificial-intelligence-future-of-work/",
    "https://aichieve.net/categories/supply-chain-operations/",
    "https://aichieve.net/control-tower-silent-exception/",
    "https://aichieve.net/demurrage-invoice-30-day-clocks/",
    "https://aichieve.net/diesel-620-electric-freight-certificate-gap/",
    "https://aichieve.net/durable-execution-not-a-transaction/",
    "https://aichieve.net/enterprisebuildvsbuy-the-250k-ai-upkeep-tax/",
    "https://aichieve.net/facturgate-the-deterministic-pre-send-gate-converter-for-european-e/",
    "https://aichieve.net/fed-rate-hike-inverts-working-capital-trap/",
    "https://aichieve.net/fine-tune-vs-rent-by-token/",
    "https://aichieve.net/flat-price-was-the-hedge/",
    "https://aichieve.net/forecast-accuracy-is-not-shock-protection/",
    "https://aichieve.net/freight-scale-bet-vs-contract-duration/",
    "https://aichieve.net/fuel-surcharge-peg-mpg-audit/",
    "https://aichieve.net/gate-the-step-not-the-model/",
    "https://aichieve.net/goods-tariff-relief-vs-vessel-fee/",
    "https://aichieve.net/gpu-hour-price-set-by-memory/",
    "https://aichieve.net/hour-14-recovery-wall/",
    "https://aichieve.net/inventory-carrying-cost-rate/",
    "https://aichieve.net/kill-switch-misses-half-your-agents/",
    "https://aichieve.net/kv-cache-is-the-concurrency-ceiling/",
    "https://aichieve.net/last-mile-carbon-number-is-a-rate-table/",
    "https://aichieve.net/local-ai-payback-cloud-gpu-spread/",
    "https://aichieve.net/maskills-multi-agent-skills-optimization/",
    "https://aichieve.net/mcp-skills-extension/",
    "https://aichieve.net/multi-agent-orchestration-building-the-one-person-enterprise/",
    "https://aichieve.net/nearshoring-doesnt-move-the-trade-case/",
    "https://aichieve.net/nvidia-says-its-gpus-arent-sold-out-its-cfos-279-billion-memory-bet/",
    "https://aichieve.net/one-skill-too-many-green-test/",
    "https://aichieve.net/openai-just-made-the-agent-loop-a-commodity/",
    "https://aichieve.net/openais-custom-chip-beats-nvidia-on-power-2/",
    "https://aichieve.net/owned-shuttles-or-rented-robots/",
    "https://aichieve.net/parcelproof-stop-bleeding-28-on-carrier-invoices/",
    "https://aichieve.net/planner-as-router-fold-the-model-choice-into-the-plan/",
    "https://aichieve.net/planning-ai-buys-capability-not-autonomy/",
    "https://aichieve.net/prefill-decode-two-pool-gap/",
    "https://aichieve.net/rack-power-density-ceiling-build-before-you-buy/",
    "https://aichieve.net/rack-ride-through-two-second-duty/",
    "https://aichieve.net/remediator-recovers-46-percent/",
    "https://aichieve.net/reshoring-moved-the-tariff-upstream/",
    "https://aichieve.net/retry-is-the-failure-amplifier/",
    "https://aichieve.net/retry-permission-leaves-the-caller/",
    "https://aichieve.net/safety-stock-forecast-error-not-demand-noise/",
    "https://aichieve.net/same-day-race-undoes-route-optimization/",
    "https://aichieve.net/self-hosted-ai-when-to-buy-vs-rent-gpus/",
    "https://aichieve.net/shippers-stuck-in-the-gap/",
    "https://aichieve.net/sla-credit-is-not-insurance/",
    "https://aichieve.net/slow-movers-hold-your-stock/",
    "https://aichieve.net/stale-grants-travel-the-graph/",
    "https://aichieve.net/stripe-accounting-software-solving-the-payout-black-box-with/",
    "https://aichieve.net/tariff-cliff-already-priced-in/",
    "https://aichieve.net/tariff-split-reshoring-heavy-half/",
    "https://aichieve.net/the-cloud-bill-break-even-when-renting-servers-stops-paying/",
    "https://aichieve.net/the-sticker-price-lies-why-mexico-beats-china-on-total-landed-cost/",
    "https://aichieve.net/token-price-record-low-budget-overrun/",
    "https://aichieve.net/token-prices-just-halved-the-cfo-still-cant-read-the-bill/",
    "https://aichieve.net/tools/",
    "https://aichieve.net/tools/gpu-compute/",
    "https://aichieve.net/tools/master-asset-tco/",
    "https://aichieve.net/up-ns-rail-merger-clears-summary-denial/",
    "https://aichieve.net/vendor-replacement-ai-ceiling/",
    "https://aichieve.net/wage-floor-sets-robot-payback/",
    "https://aichieve.net/warehouse-pick-error-tax-payback/",
    "https://aichieve.net/why-importers-forfeit-duty-refunds/",
    "https://aichieve.net/you-think-youre-governing-your-agents/",
    "https://aichieve.net/your-32gb-card-gone/",
    "https://aichieve.net/your-chip-stopped-deciding/",
    "https://aichieve.net/your-cluster-hidden-clock/",
    "https://aichieve.net/zet-scale-ev-truck-residual-value-risk/",
]
GINILOH_URLS = [
    "https://giniloh.com/categories/ai-stack-tool-tco/",
    "https://giniloh.com/categories/artificial-intelligence-future-of-work/",
    "https://giniloh.com/categories/autonomous-agentic-workflows/",
    "https://giniloh.com/categories/business-automation-operations/",
    "https://giniloh.com/categories/career-ai-resilience/",
    "https://giniloh.com/categories/major-purchases-assets/",
    "https://giniloh.com/categories/mental-models-strategy/",
    "https://giniloh.com/categories/money-wealth/",
    "https://giniloh.com/categories/supply-chain-operations/",
    "https://giniloh.com/calculators/career-ai-resilience/",
    "https://giniloh.com/calculators/coffee-arbitrage/",
    "https://giniloh.com/calculators/decision-intelligence/",
    "https://giniloh.com/calculators/expat-evaluator/",
    "https://giniloh.com/calculators/gpu-compute/",
    "https://giniloh.com/calculators/lease-break/",
    "https://giniloh.com/calculators/money-flow/",
    "https://giniloh.com/calculators/no-code-terminator/",
    "https://giniloh.com/calculators/raise-velocity/",
    "https://giniloh.com/calculators/relocation-cost/",
    "https://giniloh.com/calculators/tech-debt-repair/",
    "https://giniloh.com/calculators/total-comp/",
]
WELLROOST_URLS = [
    "https://wellroost.com/categories/energy-efficiency/",
    "https://wellroost.com/categories/home-cost-decisions/",
    "https://wellroost.com/categories/lifestyle/",
    "https://wellroost.com/categories/smart-home-security/",
    "https://wellroost.com/categories/tools-equipment/",
    "https://wellroost.com/tools/lease-break-calculator/",
    "https://wellroost.com/tools/move-or-improve-calculator/",
    "https://wellroost.com/tools/remodeling-roi-calculator/",
    "https://wellroost.com/tools/remodelytics/",
]

URLS_BY_DOMAIN = {"giniloh.com": GINILOH_URLS, "wellroost.com": WELLROOST_URLS,
                  "aichieve.net": AICHIEVE_URLS}

RESERVED = ("about", "contact", "privacy", "terms", "author", "articles", "apps", "showcase",
            "search", "feed", "insights")

ROW = {"domain": "example.com", "frontend_url": "https://example.com", "article_path": "/{slug}/",
       "category_path": "/categories/{slug}/", "tool_path": "/tools/{slug}/"}


def write_registry(payload):
    path = pathlib.Path(tempfile.mkdtemp()) / "frontends.json"
    path.write_text(payload if isinstance(payload, str) else json.dumps(payload), encoding="utf-8")
    return path


@contextlib.contextmanager
def registry(payload):
    """Point every path-less public function at a temporary registry."""
    path = write_registry(payload)
    original = fe.DEFAULT_PATH
    fe.DEFAULT_PATH = path
    try:
        yield path
    finally:
        fe.DEFAULT_PATH = original


def raises(fn):
    try:
        fn()
    except fe.FrontendsError:
        return True
    except Exception as exc:  # noqa: BLE001 - any other exception is a failure of the contract
        return f"raised {type(exc).__name__}: {exc}"
    return False


# --------------------------------------------------------------------------- the registry

print("the shipped registry")
rows = fe.load()
check("load() reads the shipped context/frontends.json", len(rows) == 3, len(rows))
check("domains are in file order: giniloh, wellroost, aichieve",
      fe.domains() == ["giniloh.com", "wellroost.com", "aichieve.net"], fe.domains())
check("every row carries the five required keys and the three templates",
      all(all(r.get(k) for k in fe.REQUIRED_KEYS) and r["article_path"] == "/{slug}/"
          and r["category_path"] == "/categories/{slug}/" for r in rows))
check("frontend_url is the front's https origin",
      [fe.frontend_url(d) for d in fe.domains()]
      == ["https://giniloh.com", "https://wellroost.com", "https://aichieve.net"])
check("spec() returns the row for a domain", fe.spec("aichieve.net")["tool_path"] == "/tools/{slug}/",
      fe.spec("aichieve.net"))
check("giniloh publishes calculators, not tools",
      fe.spec("giniloh.com")["tool_path"] == "/calculators/{slug}/")
check("the shipped file carries no pinned served_categories (derived by default)",
      all("served_categories" not in r for r in rows))
check("an unknown domain raises", raises(lambda: fe.frontend_url("nope.example")) is True)
check("...spec() too", raises(lambda: fe.spec("nope.example")) is True)

print("\nregistry validation")
check("a duplicate domain raises",
      raises(lambda: fe.load(write_registry([ROW, dict(ROW)]))) is True)
check("a missing required key raises",
      raises(lambda: fe.load(write_registry([{k: v for k, v in ROW.items() if k != "tool_path"}])))
      is True)
check("an empty value for a required key raises",
      raises(lambda: fe.load(write_registry([dict(ROW, frontend_url="")]))) is True)
check("an empty registry raises",
      raises(lambda: fe.load(write_registry([]))) is True)
check("a missing file raises",
      raises(lambda: fe.load(pathlib.Path(tempfile.mkdtemp()) / "absent.json")) is True)
check("invalid JSON raises",
      raises(lambda: fe.load(write_registry("{not json"))) is True)
check("a non-list registry raises",
      raises(lambda: fe.load(write_registry({"domain": "x"}))) is True)
check("a valid registry loads", fe.load(write_registry([ROW]))[0]["domain"] == "example.com")

# --------------------------------------------------------------------------- URL shapes

print("\npath normalisation")
check("a trailing slash is added", fe.path_of("https://giniloh.com/foo") == "/foo/",
      fe.path_of("https://giniloh.com/foo"))
check("an already-normalised path is unchanged", fe.path_of("https://giniloh.com/foo/") == "/foo/")
check("the site root is '/'", fe.path_of("https://giniloh.com") == "/")
check("a query string is dropped",
      fe.path_of("https://aichieve.net/categories/supply-chain-operations/?utm=1")
      == "/categories/supply-chain-operations/")
check("a bare path works like a full URL", fe.path_of("/categories/money-wealth") == "/categories/money-wealth/")
check("slug_of takes the last meaningful segment",
      fe.slug_of("https://giniloh.com/calculators/gpu-compute/") == "gpu-compute")
check("...ignoring the trailing slash and query",
      fe.slug_of("https://aichieve.net/tools/master-asset-tco/?ref=x") == "master-asset-tco")
check("...and is empty at the root", fe.slug_of("https://giniloh.com/") == "")

print("\nrelative_path via the templates")
check("giniloh article -> /<slug>/",
      fe.relative_path("giniloh.com", "article", "wage-floor-sets-robot-payback")
      == "/wage-floor-sets-robot-payback/")
check("giniloh category -> /categories/<slug>/",
      fe.relative_path("giniloh.com", "category", "money-wealth") == "/categories/money-wealth/")
check("giniloh tool -> /calculators/<slug>/",
      fe.relative_path("giniloh.com", "tool", "gpu-compute") == "/calculators/gpu-compute/")
check("aichieve article -> /<slug>/",
      fe.relative_path("aichieve.net", "article", "your-cluster-hidden-clock")
      == "/your-cluster-hidden-clock/")
check("aichieve tool -> /tools/<slug>/ (not /calculators/)",
      fe.relative_path("aichieve.net", "tool", "gpu-compute") == "/tools/gpu-compute/")
check("wellroost tool -> /calculators/<slug>/ (where its tool pages actually resolve: measured "
      "2026-10-15, /tools/<slug>-calculator/ canonicals to the /calculators/ path)",
      fe.relative_path("wellroost.com", "tool", "move-or-improve") == "/calculators/move-or-improve/")
check("...and the /tools/ alias is not a candidate shape there",
      fe.is_candidate_shape("https://wellroost.com/tools/move-or-improve-calculator/", "wellroost.com") is False
      and fe.is_candidate_shape("https://wellroost.com/calculators/move-or-improve/", "wellroost.com") is True)
check("an unknown domain raises",
      raises(lambda: fe.relative_path("nope.example", "article", "x")) is True)
check("an unknown kind raises",
      raises(lambda: fe.relative_path("giniloh.com", "blogpost", "x")) is True)

# --------------------------------------------------------------------------- candidate shapes

print("\nis_candidate_shape (the full table)")
check("a root-level article slug is a candidate",
      fe.is_candidate_shape("https://giniloh.com/wage-floor-sets-robot-payback/", "giniloh.com") is True)
check("a category hub is a candidate",
      fe.is_candidate_shape("https://giniloh.com/categories/supply-chain-operations/", "giniloh.com") is True)
check("giniloh's /calculators/<slug>/ tool is a candidate on giniloh",
      fe.is_candidate_shape("https://giniloh.com/calculators/gpu-compute/", "giniloh.com") is True)
check("aichieve's /tools/<slug>/ tool is a candidate on aichieve",
      fe.is_candidate_shape("https://aichieve.net/tools/gpu-compute/", "aichieve.net") is True)
check("the SAME calculator path is NOT a candidate on aichieve (wrong tool prefix)",
      fe.is_candidate_shape("https://aichieve.net/calculators/gpu-compute/", "aichieve.net") is False)
check("...and /tools/<slug>/ is NOT a candidate on giniloh",
      fe.is_candidate_shape("https://giniloh.com/tools/gpu-compute/", "giniloh.com") is False)
check("a 3-segment nested calculator role page is skipped",
      fe.is_candidate_shape("https://giniloh.com/calculators/career-ai-resilience/chief-executives/",
                            "giniloh.com") is False)
check("any other 3-segment path is skipped",
      fe.is_candidate_shape("https://aichieve.net/a/b/c/", "aichieve.net") is False)
check("a 4-segment path is skipped",
      fe.is_candidate_shape("https://aichieve.net/a/b/c/d/", "aichieve.net") is False)
check("the root is not a candidate",
      fe.is_candidate_shape("https://giniloh.com/", "giniloh.com") is False)
check("every reserved one-segment path is rejected",
      all(fe.is_candidate_shape(f"https://giniloh.com/{word}/", "giniloh.com") is False
          and fe.is_candidate_shape(f"https://aichieve.net/{word}/", "aichieve.net") is False
          for word in RESERVED), RESERVED)
check("any other two-segment prefix is rejected (author)",
      fe.is_candidate_shape("https://aichieve.net/author/gini-loh/", "aichieve.net") is False)
check("...and the real /author/gini-loh/ is the only non-candidate two-segment path on aichieve",
      [u for u in AICHIEVE_URLS if len(fe.path_of(u).strip("/").split("/")) == 2
       and fe.is_candidate_shape(u, "aichieve.net") is False] == ["https://aichieve.net/author/gini-loh/"])

print("\nis_candidate_shape against the real aichieve sitemap")
shape_ok = [u for u in AICHIEVE_URLS if fe.is_candidate_shape(u, "aichieve.net")]
shape_no = [u for u in AICHIEVE_URLS if not fe.is_candidate_shape(u, "aichieve.net")]
check("the registry's tool shape is real: both aichieve /tools/ pages are candidates",
      all(fe.is_candidate_shape(u, "aichieve.net") for u in
          ("https://aichieve.net/tools/gpu-compute/", "https://aichieve.net/tools/master-asset-tco/")))
check("92 of the 97 published URLs are candidate-shaped",
      len(shape_ok) == 92, len(shape_ok))
check("the 5 non-candidates are the root, the reserved furniture and /author/",
      sorted(shape_no) == sorted(["https://aichieve.net/", "https://aichieve.net/about/",
                                  "https://aichieve.net/apps/", "https://aichieve.net/articles/",
                                  "https://aichieve.net/author/gini-loh/"]), sorted(shape_no))

# --------------------------------------------------------------------------- served categories

print("\nserved_categories")
served = fe.served_categories("aichieve.net", AICHIEVE_URLS)
check("aichieve.net's real sitemap serves exactly the two hubs it publishes",
      served == {"artificial-intelligence-future-of-work", "supply-chain-operations"}, served)
check("giniloh.net derives its nine hubs",
      fe.served_categories("giniloh.com", GINILOH_URLS) == {
          "ai-stack-tool-tco", "artificial-intelligence-future-of-work",
          "autonomous-agentic-workflows", "business-automation-operations",
          "career-ai-resilience", "major-purchases-assets", "mental-models-strategy",
          "money-wealth", "supply-chain-operations"},
      fe.served_categories("giniloh.com", GINILOH_URLS))
check("wellroost derives its five hubs",
      fe.served_categories("wellroost.com", WELLROOST_URLS) == {
          "energy-efficiency", "home-cost-decisions", "lifestyle", "smart-home-security",
          "tools-equipment"}, fe.served_categories("wellroost.com", WELLROOST_URLS))
check("a pinned list overrides the derived set",
      fe.served_categories("aichieve.net", AICHIEVE_URLS, pinned=["pinned-hub"]) == {"pinned-hub"})
check("...an empty pin overrides to the empty set, it does not fall through",
      fe.served_categories("aichieve.net", AICHIEVE_URLS, pinned=[]) == set())
check("a front with no category hubs serves nothing",
      fe.served_categories("aichieve.net", [u for u in AICHIEVE_URLS if "/categories/" not in u]) == set())
check("an unknown domain raises",
      raises(lambda: fe.served_categories("nope.example", AICHIEVE_URLS)) is True)

pinned_row = dict(ROW, domain="aichieve.net", frontend_url="https://aichieve.net",
                  served_categories=["registry-pinned"])
with registry([pinned_row]):
    check("a served_categories field in the registry overrides the derived value",
          fe.served_categories("aichieve.net", AICHIEVE_URLS) == {"registry-pinned"})
    check("...and the explicit pinned argument still wins over the registry field",
          fe.served_categories("aichieve.net", AICHIEVE_URLS, pinned=["arg-pinned"])
          == {"arg-pinned"})

# --------------------------------------------------------------------------- renderers

print("\nrenderers")
check("supply-chain-operations is served by giniloh.com and aichieve.net, not wellroost",
      fe.renderers("supply-chain-operations", urls_by_domain=URLS_BY_DOMAIN)
      == ["giniloh.com", "aichieve.net"],
      fe.renderers("supply-chain-operations", urls_by_domain=URLS_BY_DOMAIN))
check("money-wealth is served by giniloh.com only",
      fe.renderers("money-wealth", urls_by_domain=URLS_BY_DOMAIN) == ["giniloh.com"],
      fe.renderers("money-wealth", urls_by_domain=URLS_BY_DOMAIN))
check("a home category is served by wellroost.com only",
      fe.renderers("smart-home-security", urls_by_domain=URLS_BY_DOMAIN) == ["wellroost.com"])
check("an unserved category has no renderers",
      fe.renderers("does-not-exist", urls_by_domain=URLS_BY_DOMAIN) == [])
check("renderers come back in registry order",
      fe.renderers("artificial-intelligence-future-of-work", urls_by_domain=URLS_BY_DOMAIN)
      == ["giniloh.com", "aichieve.net"])
check("a pinned served set changes the renderers",
      fe.renderers("smart-home-security", urls_by_domain=URLS_BY_DOMAIN,
                   pinned_by_domain={"giniloh.com": ["smart-home-security"]})
      == ["giniloh.com", "wellroost.com"])
check("a missing url list is not a crash and not a match",
      fe.renderers("money-wealth", urls_by_domain={}) == [])

# --------------------------------------------------------------------------- eligibility + stamp

print("\neligible")
BOTH = {"sites_live": {"giniloh.com": "/sla-credit-is-not-insurance/",
                       "aichieve.net": "/sla-credit-is-not-insurance/"}}
ONE = {"sites_live": {"giniloh.com": "/giniloh-only/"}}
MISMATCH = {"sites_live": {"giniloh.com": "/calculators/gpu-compute/",
                           "aichieve.net": "/tools/gpu-compute/"}}
check("a target live on every renderer is eligible",
      fe.eligible(BOTH, ["giniloh.com", "aichieve.net"]) is True)
check("a single-renderer subset is eligible",
      fe.eligible(BOTH, ["giniloh.com"]) is True)
check("a renderer the target is not live on makes it ineligible",
      fe.eligible(ONE, ["giniloh.com", "aichieve.net"]) is False)
check("an empty render set is never eligible", fe.eligible(BOTH, []) is False)
check("a candidate with no sites_live is not eligible",
      fe.eligible({}, ["giniloh.com"]) is False)

print("\nstamp")
check("the shared relative path is stamped when every renderer agrees",
      fe.stamp(BOTH, ["giniloh.com", "aichieve.net"]) == "/sla-credit-is-not-insurance/",
      fe.stamp(BOTH, ["giniloh.com", "aichieve.net"]))
check("a single renderer stamps its own path", fe.stamp(ONE, ["giniloh.com"]) == "/giniloh-only/")
check("the calculators/tools mismatch stamps nothing",
      fe.stamp(MISMATCH, ["giniloh.com", "aichieve.net"]) is None,
      fe.stamp(MISMATCH, ["giniloh.com", "aichieve.net"]))
check("...but a single renderer still stamps its own path", fe.stamp(MISMATCH, ["giniloh.com"])
      == "/calculators/gpu-compute/")
check("a renderer with no entry for the target stamps nothing",
      fe.stamp(ONE, ["giniloh.com", "aichieve.net"]) is None)
check("an empty render set stamps nothing", fe.stamp(BOTH, []) is None)
check("a stored absolute URL is normalised to a path",
      fe.stamp({"sites_live": {"giniloh.com": "https://giniloh.com/sla-credit-is-not-insurance"}},
               ["giniloh.com"]) == "/sla-credit-is-not-insurance/")

print(f"\n{len(PASS)} passed, {len(FAIL)} failed")
for name in FAIL:
    print(f"  FAILED: {name}")
raise SystemExit(1 if FAIL else 0)
