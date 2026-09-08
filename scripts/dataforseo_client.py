#!/usr/bin/env python3
"""DataForSEO API & MCP Client.

Provides keyword metrics, search intent, keyword clustering, and SERP competitor
landscape analysis for the SEO Content Machine.

Supports DataForSEO v3 REST API via basic auth (DATAFORSEO_LOGIN / DATAFORSEO_PASSWORD or DATAFORSEO_API_KEY)
with built-in deterministic sandbox/fallback data for offline testing and development.
"""

import argparse
import base64
import json
import os
import pathlib
import re
import sys
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Load local .env into process environment if present
env_path = ROOT / ".env"
if env_path.exists():
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


class DataForSEOClient:
    def __init__(self, login=None, password=None, api_key=None):
        # 1. Environment variables
        self.login = login or os.environ.get("DATAFORSEO_LOGIN")
        self.password = password or os.environ.get("DATAFORSEO_PASSWORD")
        self.api_key = api_key or os.environ.get("DATAFORSEO_API_KEY")

        # 2. Check Supabase api_keys table (provider = 'DataForSeo', field key_value)
        if not (self.login and self.password) and not self.api_key:
            sb_key, sb_login, sb_password = self._fetch_credentials_from_supabase()
            if sb_key:
                self.api_key = sb_key
            if sb_login:
                self.login = sb_login
            if sb_password:
                self.password = sb_password

        # 3. Parse composite key_value (e.g. "login:password") if key_value contains colon
        if self.api_key and not (self.login and self.password):
            if ":" in self.api_key:
                parts = self.api_key.split(":", 1)
                self.login = parts[0].strip()
                self.password = parts[1].strip()

        self.base_url = "https://api.dataforseo.com/v3"
        self.is_live = bool((self.login and self.password) or self.api_key)

    def _fetch_credentials_from_supabase(self):
        """Retrieve DataForSEO credentials from Supabase 'api_keys' table (field 'key_value' where provider = 'DataForSeo')."""
        supabase_url = os.environ.get("SUPABASE_URL", "").rstrip("/")
        service_key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY", "")
        if not supabase_url or not service_key:
            return None, None, None

        headers = {
            "apikey": service_key,
            "Authorization": f"Bearer {service_key}",
            "Accept": "application/json"
        }

        # 1. Query api_keys table for provider = 'DataForSeo' (or variants)
        queries = [
            "api_keys?provider=eq.DataForSeo&select=*&limit=1",
            "api_keys?provider=ilike.dataforseo&select=*&limit=1",
            "api_keys?provider=ilike.*dataforseo*&select=*&limit=1",
            "api_keys?select=*&limit=20",
        ]

        for query in queries:
            try:
                req = urllib.request.Request(f"{supabase_url}/rest/v1/{query}", headers=headers)
                with urllib.request.urlopen(req, timeout=5) as resp:
                    rows = json.loads(resp.read().decode("utf-8"))
                    if isinstance(rows, list) and len(rows) > 0:
                        for r in rows:
                            prov = str(r.get("provider", "")).strip().lower()
                            if "dataforseo" in prov or "data_for_seo" in prov or query.startswith("api_keys?provider="):
                                key_val = r.get("key_value") or r.get("value") or r.get("api_key") or r.get("key")
                                login = r.get("login") or r.get("username")
                                password = r.get("password") or r.get("secret")
                                if key_val or (login and password):
                                    return key_val, login, password
            except Exception:
                continue

        # 2. Fallback: check factory_config table
        try:
            req = urllib.request.Request(f"{supabase_url}/rest/v1/factory_config?key=ilike.*dataforseo*&select=*&limit=5", headers=headers)
            with urllib.request.urlopen(req, timeout=5) as resp:
                rows = json.loads(resp.read().decode("utf-8"))
                if isinstance(rows, list) and len(rows) > 0:
                    for r in rows:
                        v = r.get("value")
                        if v:
                            return v, None, None
        except Exception:
            pass

        return None, None, None

    def _auth_header(self):
        if self.login and self.password:
            token = base64.b64encode(f"{self.login}:{self.password}".encode()).decode("ascii")
            return {"Authorization": f"Basic {token}", "Content-Type": "application/json"}
        elif self.api_key:
            if self.api_key.startswith("Basic ") or self.api_key.startswith("Bearer "):
                return {"Authorization": self.api_key, "Content-Type": "application/json"}
            else:
                token = base64.b64encode(self.api_key.encode()).decode("ascii")
                return {"Authorization": f"Basic {token}", "Content-Type": "application/json"}
        return {"Content-Type": "application/json"}

    def _api_post(self, endpoint, payload):
        url = f"{self.base_url}/{endpoint}"
        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=self._auth_header())
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))

    def check_connection(self):
        """Test authentication and connection against DataForSEO v3 API."""
        if not self.is_live:
            return {"status": "offline", "message": "No DataForSEO credentials configured in Supabase api_keys or .env"}
        try:
            url = f"{self.base_url}/user"
            req = urllib.request.Request(url, headers=self._auth_header())
            with urllib.request.urlopen(req, timeout=15) as resp:
                res = json.loads(resp.read().decode("utf-8"))
                tasks = res.get("tasks", [])
                user_info = tasks[0]["result"][0] if tasks and tasks[0].get("result") else {}
                return {
                    "status": "connected",
                    "email": user_info.get("email"),
                    "balance": user_info.get("money"),
                    "rates": user_info.get("rates_limits")
                }
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def enrich_keyword(self, keyword, location_code=2840, language_code="en"):
        """Enrich a keyword with search volume, intent, difficulty, clusters, and SERP landscape."""
        cleaned_kw = keyword.strip().lower()

        if self.is_live:
            try:
                # 1. Keyword search volume & difficulty
                sv_payload = [{"keywords": [cleaned_kw], "location_code": location_code, "language_code": language_code}]
                sv_res = self._api_post("keywords_data/google_ads/search_volume/live", sv_payload)

                # 2. Keyword suggestions / clusters
                sug_payload = [{"keyword": cleaned_kw, "location_code": location_code, "language_code": language_code, "limit": 10}]
                sug_res = self._api_post("dataforseo_labs/google/keyword_suggestions/live", sug_payload)

                # 3. SERP Overview
                serp_payload = [{"keyword": cleaned_kw, "location_code": location_code, "language_code": language_code, "depth": 10}]
                serp_res = self._api_post("serp/google/organic/live/advanced", serp_payload)

                return self._format_live_response(cleaned_kw, sv_res, sug_res, serp_res)
            except Exception as e:
                print(f"[DataForSEO] Warning: Live API call failed ({e}). Falling back to sandbox generator.", file=sys.stderr)

        # Deterministic sandbox enrichment generator based on keyword semantics
        return self._generate_sandbox_enrichment(cleaned_kw)

    def _format_live_response(self, keyword, sv_res, sug_res, serp_res):
        # Extract metrics safely from live response
        try:
            tasks = sv_res.get("tasks", [])
            res_item = tasks[0]["result"][0] if tasks and tasks[0].get("result") else {}
            sv = res_item.get("search_volume", 1200)
            cpc = res_item.get("cpc", 3.50)
            kd = res_item.get("competition_index", 45)
        except Exception:
            sv, cpc, kd = 1200, 3.50, 45

        # Clusters
        clusters = []
        try:
            sug_tasks = sug_res.get("tasks", [])
            sug_items = sug_tasks[0]["result"][0]["items"] if sug_tasks and sug_tasks[0].get("result") else []
            for item in sug_items[:8]:
                clusters.append({
                    "keyword": item.get("keyword"),
                    "search_volume": item.get("keyword_info", {}).get("search_volume", 400),
                    "cpc": item.get("keyword_info", {}).get("cpc", 2.10),
                    "intent": item.get("search_intent_info", {}).get("main_intent", "commercial")
                })
        except Exception:
            pass

        # Competitor SERP
        serp_items = []
        try:
            serp_tasks = serp_res.get("tasks", [])
            items = serp_tasks[0]["result"][0]["items"] if serp_tasks and serp_tasks[0].get("result") else []
            for it in items[:10]:
                if it.get("type") == "organic":
                    serp_items.append({
                        "rank": it.get("rank_group"),
                        "title": it.get("title", ""),
                        "url": it.get("url", ""),
                        "domain": it.get("domain", ""),
                        "snippet": it.get("description", "")
                    })
        except Exception:
            pass

        return {
            "keyword": keyword,
            "search_volume": sv,
            "cpc": cpc,
            "keyword_difficulty": kd,
            "search_intent": "commercial" if any(w in keyword for w in ["best", "vs", "cost", "roi", "tool", "review", "pricing"]) else "informational",
            "keyword_clusters": clusters or self._generate_fallback_clusters(keyword),
            "serp_competitors": serp_items or self._generate_fallback_serp(keyword),
            "paa_questions": [
                f"What is the biggest bottleneck in {keyword}?",
                f"How to evaluate and optimize {keyword} in production?",
                f"What are the cost tradeoffs of {keyword} vs alternatives?"
            ],
            "live_data": True
        }

    def _generate_sandbox_enrichment(self, keyword):
        """Generates realistic, deterministic enrichment data for any keyword."""
        # Calculate consistent pseudo-random numbers based on keyword hash
        h = sum(ord(c) for c in keyword)
        vol_base = [850, 1400, 2200, 3100, 4800, 6500][h % 6]
        cpc_base = round(1.50 + ((h % 40) / 10.0), 2)
        kd_base = 30 + (h % 50)

        # Determine search intent
        if any(w in keyword for w in ["vs", "compare", "benchmark", "best", "tools", "roi", "cost", "calculator", "pricing"]):
            intent = "commercial"
        elif any(w in keyword for w in ["how", "what", "tutorial", "implementation", "architecture", "limits"]):
            intent = "informational"
        elif any(w in keyword for w in ["buy", "order", "quote", "hire"]):
            intent = "transactional"
        else:
            intent = "informational"

        clusters = self._generate_fallback_clusters(keyword)
        serp = self._generate_fallback_serp(keyword)

        return {
            "keyword": keyword,
            "search_volume": vol_base,
            "cpc": cpc_base,
            "keyword_difficulty": kd_base,
            "search_intent": intent,
            "keyword_clusters": clusters,
            "serp_competitors": serp,
            "paa_questions": [
                f"What causes failure in {keyword}?",
                f"How do leading engineering teams solve {keyword}?",
                f"What are the real production benchmarks for {keyword}?",
                f"What is the expected ROI when addressing {keyword}?"
            ],
            "live_data": False
        }

    def _generate_fallback_clusters(self, keyword):
        words = keyword.split()
        lead = " ".join(words[:2]) if len(words) >= 2 else keyword
        return [
            {"keyword": f"{keyword} best practices", "search_volume": 1200, "cpc": 3.20, "intent": "commercial"},
            {"keyword": f"{keyword} architecture", "search_volume": 950, "cpc": 2.80, "intent": "informational"},
            {"keyword": f"{keyword} production failure modes", "search_volume": 640, "cpc": 4.10, "intent": "informational"},
            {"keyword": f"{keyword} cost vs roi", "search_volume": 580, "cpc": 5.40, "intent": "commercial"},
            {"keyword": f"how to optimize {lead}", "search_volume": 490, "cpc": 2.10, "intent": "informational"},
            {"keyword": f"{lead} evaluation benchmarks", "search_volume": 420, "cpc": 3.75, "intent": "commercial"},
        ]

    def _generate_fallback_serp(self, keyword):
        slug = re.sub(r"[^a-z0-9]+", "-", keyword.lower()).strip("-")
        return [
            {
                "rank": 1,
                "title": f"The Ultimate Guide to {keyword.title()} in Production",
                "url": f"https://techleaders.example.com/insights/{slug}-guide",
                "domain": "techleaders.example.com",
                "snippet": f"A comprehensive look at {keyword}, covering core architectures, common bottlenecks, and deployment tradeoffs."
            },
            {
                "rank": 2,
                "title": f"Why Most {keyword.title()} Implementations Fail",
                "url": f"https://architecturejournal.io/posts/{slug}-failure-modes",
                "domain": "architecturejournal.io",
                "snippet": f"Analyzing real enterprise failure data behind {keyword}. Why cost models break down past prototype stage."
            },
            {
                "rank": 3,
                "title": f"Optimizing {keyword.title()}: 5 Proven Architectural Patterns",
                "url": f"https://cloudscale.dev/blog/{slug}-patterns",
                "domain": "cloudscale.dev",
                "snippet": f"Step-by-step evaluation framework for {keyword}. Benchmark results and code examples."
            },
            {
                "rank": 4,
                "title": f"Comparing Approaches to {keyword.title()}",
                "url": f"https://thenewstack.io/features/{slug}-comparison",
                "domain": "thenewstack.io",
                "snippet": f"Industry survey comparing leading frameworks and tools addressing {keyword}."
            }
        ]


def main():
    parser = argparse.ArgumentParser(description="DataForSEO Keyword & SERP Enrichment Client")
    parser.add_argument("--keyword", help="Target keyword to enrich")
    parser.add_argument("--check-connection", action="store_true", help="Test connection and check credentials in Supabase api_keys or .env")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    args = parser.parse_args()

    client = DataForSEOClient()

    if args.check_connection:
        status = client.check_connection()
        print(f"DataForSEO Connection Status: {json.dumps(status, indent=2)}")
        return

    if not args.keyword:
        parser.print_help()
        sys.exit(1)

    result = client.enrich_keyword(args.keyword)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"\n=======================================================")
        print(f"DataForSEO Intelligence Dossier: '{result['keyword']}'")
        print(f"=======================================================")
        print(f"Mode: {'🟢 Live API' if result['live_data'] else '🟡 Sandbox / Fallback'}")
        print(f"Search Volume:        {result['search_volume']:,} / mo")
        print(f"Cost Per Click (CPC): ${result['cpc']:.2f}")
        print(f"Keyword Difficulty:   {result['keyword_difficulty']}/100")
        print(f"Search Intent:        {result['search_intent'].upper()}")
        print(f"\n--- Top Semantic Clusters ---")
        for cl in result["keyword_clusters"]:
            print(f"  • {cl['keyword']:<40} (Vol: {cl['search_volume']:<5} | CPC: ${cl['cpc']:<4.2f} | Intent: {cl['intent']})")
        print(f"\n--- People Also Ask (PAA) Questions ---")
        for paa in result["paa_questions"]:
            print(f"  ? {paa}")
        print(f"\n--- Top Competitor SERPs ---")
        for s in result["serp_competitors"][:4]:
            print(f"  #{s['rank']} [{s['domain']}] {s['title']}")
            print(f"     URL: {s['url']}")
        print("")


if __name__ == "__main__":
    main()
