#!/usr/bin/env python3
"""Tests for site_corpus — run: python3 scripts/test_site_corpus.py

Hermetic: every page, sitemap and 404 body is a real capture in scripts/fixtures/ and the transport is
a fake, so nothing here touches the network. The captures are the measured facts the module is built
on, and they are the reason these tests can exist at all:

  * wellroost_homepage_shell.html  — `wellroost.com/<unknown>/` answers **200 with the homepage shell**
    (canonical = `https://wellroost.com/`), so "HTTP 200" is not liveness and the canonical link is the
    only identity guard there is;
  * wellroost_battery-payback-five-state-gap.html, aichieve_your-cluster-hidden-clock.html,
    giniloh_wage-floor-sets-robot-payback.html — three real article pages, each with canonical, Article
    JSON-LD (headline/description/dateModified) and a BreadcrumbList pointing at /categories/<slug>/;
  * giniloh_sitemap.xml (1148 locs, reached through robots.txt), wellroost_sitemap-index.xml ->
    wellroost_sitemap-0.xml (40) and aichieve_sitemap-index.xml -> aichieve_sitemap-0.xml (97);
  * aichieve_robots.txt.404.html and aichieve_sitemap.xml.404.html — aichieve.net's `/sitemap.xml` is a
    **404** (its sitemap is the index), so discovery must fall through instead of failing the site.

The rules under test are the ones that decide whether the corpus is trustworthy: a sitemap that is not
reachable must raise rather than read as "no live pages", a page that is not the page we asked for must
be dropped rather than indexed, and the crawl must stay polite (<=3 requests in flight per host) and
cheap (a fresh cache record is served without a request; a stale one is revalidated, not re-downloaded).
"""

from __future__ import annotations

import hashlib
import json
import pathlib
import re
import sys
import tempfile
import threading
import time
import urllib.parse

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import site_corpus as sc  # noqa: E402


# A hub/calculator page: canonically itself, og:title only (no Article JSON-LD), which is exactly the
# branch that used to leave "| Gini Loh" on the end of the name.
OG_ONLY_HTML = """<html><head><title>Some Calculator | Gini Loh</title>
<link rel="canonical" href="https://a.com/calculators/x/">
<meta property="og:title" content="Some Calculator | Gini Loh">
<meta name="description" content="A calculator.">
</head><body><h1>Some Calculator</h1></body></html>
"""

PASS, FAIL = [], []


def check(name, condition, detail=""):  # noqa: ANN001 - house style: the detail is printed, not typed
    (PASS if condition else FAIL).append(name)
    print(f"  [{'ok ' if condition else 'FAIL'}] {name}{'' if condition else f'  <- {detail}'}")


FIXTURES = pathlib.Path(__file__).resolve().parent / "fixtures"

WELLROOST_ARTICLE = "https://wellroost.com/battery-payback-five-state-gap/"
AICHIEVE_ARTICLE = "https://aichieve.net/your-cluster-hidden-clock/"
GINILOH_ARTICLE = "https://giniloh.com/wage-floor-sets-robot-payback/"
SHELL_URL = "https://wellroost.com/no-such-article-xyz/"


def fixture(name) -> bytes:
    return (FIXTURES / name).read_bytes()


def fixture_text(name) -> str:
    return (FIXTURES / name).read_text(encoding="utf-8")


class FakeTransport:
    """A fake `fetch(url, headers) -> (status, headers, body_bytes)`: call log + in-flight census."""

    def __init__(self, routes=None, default=(404, {}, b"")):
        self.routes = dict(routes or {})
        self.default = default
        self.calls = []
        self.inflight = {}
        self.max_inflight = {}
        self.delay = 0.0
        self._lock = threading.Lock()

    def __call__(self, url, headers):
        host = urllib.parse.urlsplit(url).netloc
        with self._lock:
            self.calls.append((url, dict(headers or {})))
            self.inflight[host] = self.inflight.get(host, 0) + 1
            self.max_inflight[host] = max(self.max_inflight.get(host, 0), self.inflight[host])
        try:
            if self.delay:
                time.sleep(self.delay)
            route = self.routes.get(url, self.default)
            if callable(route):
                return route(url, headers)
            status, extra, body = route
            return status, dict(extra), body
        finally:
            with self._lock:
                self.inflight[host] -= 1

    def urls(self):
        return [url for url, _ in self.calls]

    def headers_for(self, url):
        return [headers for called, headers in self.calls if called == url]


def hand_meta(url, **overrides):
    """A metadata dict as the path-shape rules see it (no article markup of its own)."""
    meta = {"url": url, "canonical": url, "title": "Fixture", "excerpt": "", "modified": "",
            "categories": [], "category_slugs": [], "jsonld_types": [], "article": False,
            "canonical_match": True}
    meta.update(overrides)
    return meta


def _without_flag(meta):
    """The same dict with no explicit `article` flag, to exercise classify's type-based fallback."""
    return {key: value for key, value in meta.items() if key != "article"}


URLSET = ("<?xml version=\"1.0\" encoding=\"UTF-8\"?><urlset "
          "xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">{}</urlset>")


def urlset(*locs):
    return URLSET.format("".join(f"<url><loc>{loc}</loc></url>" for loc in locs)).encode("utf-8")


def sitemapindex(*locs):
    return ("<?xml version=\"1.0\" encoding=\"UTF-8\"?><sitemapindex "
            "xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">{}</sitemapindex>").format(
        "".join(f"<sitemap><loc>{loc}</loc></sitemap>" for loc in locs)).encode("utf-8")


def loc_count(name):
    """How many distinct <loc> rows the captured sitemap file itself carries."""
    return len(re.findall(r"<loc>", fixture_text(name)))


# --------------------------------------------------------------------------- the frozen contract

print("the frozen API (other modules import these)")
check("SITEMAP_CANDIDATES is the frozen tuple",
      sc.SITEMAP_CANDIDATES == ("/sitemap.xml", "/sitemap-index.xml", "/sitemap_index.xml"),
      sc.SITEMAP_CANDIDATES)
check("SiteCorpusError is an exception a caller can catch", issubclass(sc.SiteCorpusError, Exception))
check("fetch=None means the real urllib transport, with a 20s timeout",
      callable(sc.default_fetch) and sc.REQUEST_TIMEOUT == 20 and sc.PER_HOST_LIMIT == 3,
      (sc.REQUEST_TIMEOUT, sc.PER_HOST_LIMIT))
check("the fixtures the tests read are present",
      all((FIXTURES / name).exists() for name in (
          "wellroost_homepage_shell.html", "wellroost_battery-payback-five-state-gap.html",
          "aichieve_your-cluster-hidden-clock.html", "giniloh_wage-floor-sets-robot-payback.html",
          "giniloh_sitemap.xml", "giniloh_robots.txt", "wellroost_sitemap-index.xml",
          "wellroost_sitemap-0.xml", "aichieve_sitemap-index.xml", "aichieve_sitemap-0.xml",
          "aichieve_robots.txt.404.html", "aichieve_sitemap.xml.404.html")),
      sorted(p.name for p in FIXTURES.iterdir()))

# --------------------------------------------------------------------------- sitemap discovery

print("\nsitemap discovery — robots, 404s and the sitemap index")

robots_and_real = FakeTransport({
    "https://giniloh.com/robots.txt": (200, {"Content-Type": "text/plain"}, fixture("giniloh_robots.txt")),
    "https://giniloh.com/sitemap.xml": (200, {"Content-Type": "text/xml"}, fixture("giniloh_sitemap.xml")),
    "https://giniloh.com/sitemap-index.xml": (200, {"Content-Type": "text/xml"},
                                              urlset("https://giniloh.com/decoy-never-used/")),
})
giniloh_locs = sc.discover_sitemaps("https://giniloh.com", fetch=robots_and_real)
check("the real robots.txt directive names /sitemap.xml",
      b"Sitemap: https://giniloh.com/sitemap.xml" in fixture("giniloh_robots.txt"))
check("robots.txt's Sitemap: is read and its sitemap is used (every loc surfaced once, no dupes)",
      len(giniloh_locs) == loc_count("giniloh_sitemap.xml"),
      (len(giniloh_locs), loc_count("giniloh_sitemap.xml")))
check("...so the corpus is the real one (1148 locs, incl. a known article)",
      GINILOH_ARTICLE in giniloh_locs and len(giniloh_locs) > 1000, len(giniloh_locs))
check("...and the conventional path is never consulted once a sitemap has answered",
      giniloh_locs and "https://giniloh.com/decoy-never-used/" not in giniloh_locs
      and "https://giniloh.com/sitemap-index.xml" not in robots_and_real.urls(),
      robots_and_real.urls())

unique = FakeTransport({
    "https://x.test/robots.txt": (200, {}, b"User-agent: *\nSitemap: https://x.test/special-feed.xml\n"),
    "https://x.test/special-feed.xml": (200, {}, urlset("https://x.test/only-page/")),
    "https://x.test/sitemap.xml": (200, {}, urlset("https://x.test/conventional-page/")),
})
check("a robots.txt directive wins over the conventional paths, even when it is not /sitemap.xml",
      sc.discover_sitemaps("https://x.test", fetch=unique) == ["https://x.test/only-page/"],
      unique.urls())

aichieve_404 = FakeTransport({
    "https://aichieve.net/robots.txt": (404, {"Content-Type": "text/html"},
                                        fixture("aichieve_robots.txt.404.html")),
    "https://aichieve.net/sitemap.xml": (404, {"Content-Type": "text/html"},
                                         fixture("aichieve_sitemap.xml.404.html")),
    "https://aichieve.net/sitemap-index.xml": (200, {}, fixture("aichieve_sitemap-index.xml")),
    "https://aichieve.net/sitemap-0.xml": (200, {}, fixture("aichieve_sitemap-0.xml")),
})
check("the captured 404 body is real HTML, not a sitemap",
      sc._parse_xml(fixture("aichieve_sitemap.xml.404.html")) is None and
      fixture("aichieve_sitemap.xml.404.html").startswith(b"<!DOCTYPE html>"))
aichieve_locs = sc.discover_sitemaps("https://aichieve.net", fetch=aichieve_404)
check("a robots.txt 404 and a /sitemap.xml 404 fall through to /sitemap-index.xml",
      aichieve_404.urls() == ["https://aichieve.net/robots.txt", "https://aichieve.net/sitemap.xml",
                              "https://aichieve.net/sitemap-index.xml", "https://aichieve.net/sitemap-0.xml"],
      aichieve_404.urls())
check("...and the corpus is the real one (97 locs) rather than an empty failure",
      len(aichieve_locs) == loc_count("aichieve_sitemap-0.xml") == 97, len(aichieve_locs))
check("...with the hubs and tools aichieve.net publishes",
      {"https://aichieve.net/categories/artificial-intelligence-future-of-work/",
       "https://aichieve.net/categories/supply-chain-operations/",
       "https://aichieve.net/tools/gpu-compute/",
       "https://aichieve.net/tools/master-asset-tco/"} <= set(aichieve_locs))

wellroost_index = FakeTransport({
    "https://wellroost.com/robots.txt": (404, {}, b""),
    "https://wellroost.com/sitemap.xml": (404, {}, b""),
    "https://wellroost.com/sitemap-index.xml": (200, {}, fixture("wellroost_sitemap-index.xml")),
    "https://wellroost.com/sitemap-0.xml": (200, {}, fixture("wellroost_sitemap-0.xml")),
})
wellroost_locs = sc.discover_sitemaps("https://wellroost.com", fetch=wellroost_index)
check("a <sitemapindex> is followed one level: the result is the index's CONTENTS, not its own loc",
      len(wellroost_locs) == loc_count("wellroost_sitemap-0.xml") == 40
      and not any(url.endswith(".xml") for url in wellroost_locs), len(wellroost_locs))
check("...and the articles on it are in the corpus",
      WELLROOST_ARTICLE in wellroost_locs and "https://wellroost.com/tools/remodelytics/" in wellroost_locs)

looping = FakeTransport({
    "https://loop.test/robots.txt": (404, {}, b""),
    "https://loop.test/sitemap.xml": (200, {}, sitemapindex("https://loop.test/sitemap.xml")),
})
try:
    sc.discover_sitemaps("https://loop.test", fetch=looping)
    check("a self-referencing sitemap index terminates and then raises", False, "returned a corpus")
except sc.SiteCorpusError:
    check("a self-referencing sitemap index terminates and then raises", True)
check("...the self-referencing document is fetched once and never followed a second level",
      looping.urls().count("https://loop.test/sitemap.xml") == 1, looping.urls())
check("...and after the index comes up empty, the remaining conventional paths are tried once each",
      looping.urls() == ["https://loop.test/robots.txt", "https://loop.test/sitemap.xml",
                         "https://loop.test/sitemap-index.xml", "https://loop.test/sitemap_index.xml"],
      looping.urls())

dedupe = FakeTransport({
    "https://dupes.test/robots.txt": (404, {}, b""),
    "https://dupes.test/sitemap.xml": (200, {}, sitemapindex("https://dupes.test/sitemap-0.xml",
                                                             "https://dupes.test/sitemap-0.xml")),
    "https://dupes.test/sitemap-0.xml": (200, {}, urlset(
        "https://dupes.test/a/", "https://dupes.test/a/#fragment", "https://dupes.test/a/",
        "  https://dupes.test/b/  ")),
})
deduped_locs = sc.discover_sitemaps("https://dupes.test", fetch=dedupe)
check("locs are deduped and defragged (a fragment never names a second page)",
      deduped_locs == ["https://dupes.test/a/", "https://dupes.test/b/"], deduped_locs)
check("...and a child sitemap listed twice is fetched once",
      dedupe.urls().count("https://dupes.test/sitemap-0.xml") == 1, dedupe.urls())

nowhere = FakeTransport({}, default=(404, {}, b""))
try:
    result = sc.discover_sitemaps("https://nowhere.test", fetch=nowhere)
    check("nothing reachable raises instead of returning []", False, result)
except sc.SiteCorpusError as exc:
    check("nothing reachable raises instead of returning []",
          "no reachable sitemap" in str(exc) and "sitemap-index.xml" in str(exc), exc)
check("...having actually tried robots.txt and every conventional path",
      nowhere.urls() == ["https://nowhere.test/robots.txt"] +
      [f"https://nowhere.test{path}" for path in sc.SITEMAP_CANDIDATES], nowhere.urls())

empty = FakeTransport({"https://empty.test/robots.txt": (404, {}, b""),
                       "https://empty.test/sitemap.xml": (200, {}, urlset()),
                       "https://empty.test/sitemap-index.xml": (404, {}, b""),
                       "https://empty.test/sitemap_index.xml": (404, {}, b"")})
try:
    result = sc.discover_sitemaps("https://empty.test", fetch=empty)
    check("a reachable but empty sitemap is not a corpus of zero pages", False, result)
except sc.SiteCorpusError:
    check("a reachable but empty sitemap is not a corpus of zero pages", True)

# --------------------------------------------------------------------------- fetch_page + cache

print("\nfetch_page — the cache, its revalidation, and offline mode")

TAG = '"etag-abc123"'
MODIFIED = "Wed, 14 Oct 2026 19:49:17 GMT"
network = FakeTransport({GINILOH_ARTICLE: (200, {"ETag": TAG, "Last-Modified": MODIFIED},
                                           fixture("giniloh_wage-floor-sets-robot-payback.html"))})
with tempfile.TemporaryDirectory() as tmp:
    cache_dir = pathlib.Path(tmp)
    page = sc.fetch_page(GINILOH_ARTICLE, cache_dir=cache_dir, fetch=network)
    check("the first fetch goes to the network and is not marked cached",
          len(network.calls) == 1 and page["from_cache"] is False, page["from_cache"])
    check("...with the polite User-Agent and the whole document",
          network.calls[0][1]["User-Agent"] == "Mozilla/5.0 (editorial-factory corpus)"
          and page["html"] == fixture("giniloh_wage-floor-sets-robot-payback.html").decode("utf-8")
          and page["etag"] == TAG and page["lastmod"] == MODIFIED, network.calls[0][1])
    expected_path = (cache_dir / "giniloh.com" /
                     f"{hashlib.sha1(GINILOH_ARTICLE.encode('utf-8')).hexdigest()}.json")
    check("the cache file is <cache_dir>/<host>/<sha1(url)>.json",
          expected_path.exists() and len(list(cache_dir.glob('*/*.json'))) == 1, expected_path)

    warm = sc.fetch_page(GINILOH_ARTICLE, cache_dir=cache_dir, fetch=network)
    check("a cache hit does not refetch (0 new transport calls)",
          len(network.calls) == 1 and warm["from_cache"] is True, len(network.calls))
    check("...and answers the same document", warm["html"] == page["html"] and warm["url"] == page["url"])

    # Age the record so the next call must revalidate; the server says 304 Not Modified.
    record = json.loads(expected_path.read_text(encoding="utf-8"))
    record["fetched_at"] = "2020-01-01T00:00:00+00:00"
    expected_path.write_text(json.dumps(record), encoding="utf-8")
    revalidator = FakeTransport({GINILOH_ARTICLE: (304, {}, b"")})
    kept = sc.fetch_page(GINILOH_ARTICLE, cache_dir=cache_dir, fetch=revalidator)
    sent = revalidator.calls[0][1]
    check("a stale record is revalidated conditionally, not downloaded again",
          sent.get("If-None-Match") == TAG and sent.get("If-Modified-Since") == MODIFIED,
          sorted(sent))
    check("a 304 keeps the cached record (html, etag and lastmod all survive)",
          kept["html"] == page["html"] and kept["etag"] == TAG and kept["lastmod"] == MODIFIED
          and kept["from_cache"] is True, {k: kept[k] for k in ("etag", "lastmod", "from_cache")})
    check("...and the record is still on disk afterwards",
          json.loads(expected_path.read_text(encoding="utf-8"))["html"] == page["html"])

    # Only a Last-Modified validator is a valid reason to send a conditional request.
    expected_path.write_text(json.dumps({"url": GINILOH_ARTICLE, "html": "old", "etag": None,
                                         "lastmod": MODIFIED, "fetched_at": "2020-01-01T00:00:00+00:00"}),
                             encoding="utf-8")
    lastmod_only = FakeTransport({GINILOH_ARTICLE: (304, {}, b"")})
    sc.fetch_page(GINILOH_ARTICLE, cache_dir=cache_dir, fetch=lastmod_only)
    check("a record with only Last-Modified revalidates with If-Modified-Since",
          lastmod_only.calls[0][1].get("If-Modified-Since") == MODIFIED
          and "If-None-Match" not in lastmod_only.calls[0][1], sorted(lastmod_only.calls[0][1]))

    offline_miss = FakeTransport({})
    try:
        sc.fetch_page("https://giniloh.com/never-cached/", cache_dir=cache_dir, fetch=offline_miss,
                      offline=True)
        check("offline + cache miss raises instead of reaching for the network", False, "returned")
    except sc.SiteCorpusError:
        check("offline + cache miss raises instead of reaching for the network",
              offline_miss.calls == [], offline_miss.calls)

    expected_path.write_text(json.dumps({"url": GINILOH_ARTICLE, "html": "cached-shell", "etag": TAG,
                                         "lastmod": MODIFIED, "fetched_at": "2020-01-01T00:00:00+00:00"}),
                             encoding="utf-8")
    offline_hit = FakeTransport({})
    stale_but_there = sc.fetch_page(GINILOH_ARTICLE, cache_dir=cache_dir, fetch=offline_hit,
                                   offline=True)
    check("offline + a (stale) cache record serves the record and calls nothing",
          stale_but_there["html"] == "cached-shell" and stale_but_there["from_cache"] is True
          and offline_hit.calls == [], offline_hit.calls)

    no_cache = sc.fetch_page(GINILOH_ARTICLE, fetch=network)
    check("no cache_dir means no cache file and no cache claim",
          no_cache["from_cache"] is False and len(network.calls) == 2, len(network.calls))

flaky_tries = {"n": 0}


def flaky(url, headers):
    flaky_tries["n"] += 1
    if flaky_tries["n"] < 3:
        return 500, {}, b"<html>upstream hiccup</html>"
    return 200, {"ETag": TAG}, fixture("giniloh_wage-floor-sets-robot-payback.html")


saved_backoff = sc.RETRY_BACKOFF
sc.RETRY_BACKOFF = (0, 0)                       # no sleeping in a test run
try:
    retried = FakeTransport({GINILOH_ARTICLE: flaky})
    recovered = sc.fetch_page(GINILOH_ARTICLE, fetch=retried)
    check("a transient answer is retried (2 retries, 3 attempts) and can still succeed",
          flaky_tries["n"] == 3 and recovered["html"].startswith("<!DOCTYPE html"), flaky_tries)
    gone = FakeTransport({GINILOH_ARTICLE: (404, {}, b"nope")})
    try:
        sc.fetch_page(GINILOH_ARTICLE, fetch=gone)
        check("a 404 is not retried and raises", False, "returned")
    except sc.SiteCorpusError as exc:
        check("a 404 is not retried and raises",
              len(gone.calls) == 1 and "HTTP 404" in str(exc), (len(gone.calls), exc))
finally:
    sc.RETRY_BACKOFF = saved_backoff

# --------------------------------------------------------------------------- page_metadata

print("\npage identity — the canonical guard and what a real article page carries")

shell_html = fixture_text("wellroost_homepage_shell.html")
check("the wellroost 200 soft-404 really is the homepage shell",
      sc._canonical_href(shell_html) == "https://wellroost.com/"
      and "<title>WellRoost | The Decision Engine for Your Home</title>" in shell_html[:1200])
check("a 200 page whose canonical is not the URL asked for is REJECTED (None)",
      sc.page_metadata(shell_html, SHELL_URL) is None,
      sc.page_metadata(shell_html, SHELL_URL))
check("...while the same body at the URL it does claim is a page (so it is the identity rule, not "
      "an empty parse)",
      (sc.page_metadata(shell_html, "https://wellroost.com/") or {}).get("title", "").startswith(
          "WellRoost"),
      sc.page_metadata(shell_html, "https://wellroost.com/"))
check("...and the shell is never classified as a link target",
      sc.classify(SHELL_URL, None) is None
      and sc.classify("https://wellroost.com/", sc.page_metadata(shell_html, "https://wellroost.com/"))
      is None)

real_meta = {}
for url, name in ((WELLROOST_ARTICLE, "wellroost_battery-payback-five-state-gap.html"),
                  (AICHIEVE_ARTICLE, "aichieve_your-cluster-hidden-clock.html"),
                  (GINILOH_ARTICLE, "giniloh_wage-floor-sets-robot-payback.html")):
    meta = sc.page_metadata(fixture_text(name), url)
    real_meta[url] = meta
    check(f"{urllib.parse.urlsplit(url).netloc}: every frozen key is present",
          meta is not None and {"url", "title", "excerpt", "modified", "categories", "category_slugs",
                                "canonical"} <= set(meta), None if meta is None else sorted(meta))
    check(f"{urllib.parse.urlsplit(url).netloc}: canonical is the URL we asked for",
          meta and meta["canonical"] == url and meta["url"] == url, meta and meta["canonical"])

check("wellroost: title/excerpt/modified come from the Article JSON-LD",
      real_meta[WELLROOST_ARTICLE]["title"] == "Your Battery Payback: A 5-State Gap"
      and real_meta[WELLROOST_ARTICLE]["excerpt"].startswith("Two-thirds of U.S. homeowners lost power")
      and real_meta[WELLROOST_ARTICLE]["modified"] == "2026-10-12T12:11:38",
      {k: real_meta[WELLROOST_ARTICLE][k] for k in ("title", "excerpt", "modified")})
check("wellroost: the category comes from the BreadcrumbList (Home dropped, &amp; unescaped)",
      real_meta[WELLROOST_ARTICLE]["categories"] == [{"name": "Energy & Efficiency",
                                                      "slug": "energy-efficiency"}]
      and real_meta[WELLROOST_ARTICLE]["category_slugs"] == ["energy-efficiency"],
      real_meta[WELLROOST_ARTICLE]["categories"])
check("aichieve: an article on a frontend the CMS does not know about reads the same way",
      real_meta[AICHIEVE_ARTICLE]["title"] == "Your Cluster's Hidden Clock: 3 Minor Versions, 1 Year"
      and real_meta[AICHIEVE_ARTICLE]["category_slugs"] == ["ai-stack-tool-tco"]
      and real_meta[AICHIEVE_ARTICLE]["modified"] == "2026-10-14T19:10:08",
      {k: real_meta[AICHIEVE_ARTICLE][k] for k in ("title", "category_slugs", "modified")})
check("giniloh: same shape, different site (one category, the position-3 self crumb dropped)",
      real_meta[GINILOH_ARTICLE]["title"] == "Warehouse Payback: $17.00, Not $17.95"
      and real_meta[GINILOH_ARTICLE]["category_slugs"] == ["supply-chain-operations"]
      and real_meta[GINILOH_ARTICLE]["categories"] == [{"name": "Supply Chain & Operations",
                                                        "slug": "supply-chain-operations"}],
      real_meta[GINILOH_ARTICLE]["categories"])

# The <title> fallback is only reached on a page with no JSON-LD and no og:title (a hand-written
# page). Derive that page from the real capture rather than inventing a title string.
no_machine_meta = re.sub(r"<script[^>]*application/ld\+json[^>]*>.*?</script>", "",
                         fixture_text("wellroost_battery-payback-five-state-gap.html"),
                         flags=re.IGNORECASE | re.DOTALL)
for prop in ("og:title", "og:description"):
    no_machine_meta = re.sub(rf"<meta[^>]*property=[\"']{prop}[\"'][^>]*>", "", no_machine_meta,
                             flags=re.IGNORECASE)
fallback = sc.page_metadata(no_machine_meta, WELLROOST_ARTICLE)
check("without JSON-LD/og:*, the title falls back to <title> with the site suffix stripped",
      fallback is not None and fallback["title"] == "Your Battery Payback: A 5-State Gap",
      None if fallback is None else fallback["title"])
check("...and the page is then no longer an article (the markup is what says so)",
      fallback is not None and fallback["article"] is False
      and sc.classify(WELLROOST_ARTICLE, fallback) is None, fallback and fallback["article"])
check("a subtitle is not mistaken for a site stamp (a 5-word tail stays)",
      sc._strip_site_suffix("NY Heat Pump Rebate \u2014 Double Payouts for Sealed Homes")
      == "NY Heat Pump Rebate \u2014 Double Payouts for Sealed Homes"
      and sc._strip_site_suffix("Some Page - Giniloh") == "Some Page"
      and sc._strip_site_suffix("Some Page \u2014 WellRoost") == "Some Page"
      and sc._strip_site_suffix("Warehouse Payback: $17.00, Not $17.95")
      == "Warehouse Payback: $17.00, Not $17.95")

# --------------------------------------------------------------------------- classify

print("\nclassification — markup for articles, path shape for hubs and tools")

classify_table = [
    (GINILOH_ARTICLE, real_meta[GINILOH_ARTICLE], "article"),
    (WELLROOST_ARTICLE, real_meta[WELLROOST_ARTICLE], "article"),
    ("https://giniloh.com/categories/supply-chain-operations/", None, "category"),
    ("https://aichieve.net/categories/artificial-intelligence-future-of-work/", None, "category"),
    ("https://giniloh.com/calculators/move-or-improve/", None, "tool"),
    ("https://aichieve.net/tools/gpu-compute/", None, "tool"),
    ("https://wellroost.com/tools/lease-break-calculator/", None, "tool"),
    # the nested /calculators/<slug>/<role>/ permutations: 1016 of them on giniloh.com
    ("https://giniloh.com/calculators/career-ai-resilience/chief-executives/", None, None),
    ("https://giniloh.com/categories/money-wealth/value/", None, None),
    ("https://giniloh.com/about/", None, None),
    ("https://giniloh.com/author/gini-loh/", None, None),
    ("https://giniloh.com/articles/", None, None),
    ("https://apps.giniloh.com/showcase", None, None),
    ("https://giniloh.com/insights/", None, None),
    ("https://giniloh.com/search/", None, None),
    ("https://giniloh.com/categories/", None, None),
    ("https://giniloh.com/calculators/", None, None),
    ("https://giniloh.com/sitemap.xml", None, None),
    ("https://giniloh.com/robots.txt", None, None),
    ("https://aichieve.net/sitemap-0.xml", None, None),
    (SHELL_URL, None, None),
    ("https://giniloh.com/", None, None),
]
for url, meta, expected in classify_table:
    answer = sc.classify(url, meta if meta is not None else hand_meta(url))
    check(f"classify({urllib.parse.urlsplit(url).path}) -> {expected!r}", answer == expected, answer)

check("no meta at all is always skipped (the page was never fetched)",
      sc.classify(GINILOH_ARTICLE, None) is None)
check("an Article block with a canonical pointing elsewhere is skipped",
      sc.classify(GINILOH_ARTICLE, hand_meta(GINILOH_ARTICLE, article=True,
                                             canonical="https://giniloh.com/other-page/")) is None)
check("an Article block whose canonical is the site root is skipped (the shell again)",
      sc.classify(SHELL_URL, hand_meta(SHELL_URL, article=True,
                                       canonical="https://wellroost.com/")) is None)
check("an article type is read from the JSON-LD types when no explicit flag is carried",
      sc.classify(GINILOH_ARTICLE, _without_flag(hand_meta(GINILOH_ARTICLE,
                                                           jsonld_types=["BlogPosting"]))) == "article"
      and sc.classify(GINILOH_ARTICLE, _without_flag(hand_meta(GINILOH_ARTICLE,
                                                              jsonld_types=["WebSite"]))) is None,
      (_without_flag(hand_meta(GINILOH_ARTICLE, jsonld_types=["BlogPosting"])),
       sc.classify(GINILOH_ARTICLE, _without_flag(hand_meta(GINILOH_ARTICLE, jsonld_types=["WebSite"])))))
check("a trailing slash is not a different page",
      sc.classify("https://giniloh.com/wage-floor-sets-robot-payback",
                  real_meta[GINILOH_ARTICLE]) == "article")

# --------------------------------------------------------------------------- metadata_for

print("\nmetadata_for — the crawl, its bound, and its politeness")

routes = {
    GINILOH_ARTICLE: (200, {"ETag": '"g1"'}, fixture("giniloh_wage-floor-sets-robot-payback.html")),
    WELLROOST_ARTICLE: (200, {"ETag": '"w1"'}, fixture("wellroost_battery-payback-five-state-gap.html")),
    AICHIEVE_ARTICLE: (200, {"ETag": '"a1"'}, fixture("aichieve_your-cluster-hidden-clock.html")),
    SHELL_URL: (200, {"ETag": '"s1"'}, fixture("wellroost_homepage_shell.html")),
    "https://aichieve.net/removed-article/": (404, {}, fixture("aichieve_sitemap.xml.404.html")),
    "https://giniloh.com/categories/supply-chain-operations/": (
        200, {}, urlset("https://giniloh.com/categories/supply-chain-operations/")),
}
corpus_transport = FakeTransport(routes)
asked = [GINILOH_ARTICLE, SHELL_URL, WELLROOST_ARTICLE, "https://aichieve.net/removed-article/",
         "https://giniloh.com/categories/supply-chain-operations/", AICHIEVE_ARTICLE]
with tempfile.TemporaryDirectory() as tmp:
    pages = sc.metadata_for(asked, frontend="https://giniloh.com", cache_dir=tmp,
                            fetch=corpus_transport)
    check("a soft-404 shell and a real 404 are dropped, the resolvable pages are kept in order",
          [p["url"] for p in pages] == [GINILOH_ARTICLE, WELLROOST_ARTICLE,
                                        "https://giniloh.com/categories/supply-chain-operations/",
                                        AICHIEVE_ARTICLE],
          [p["url"] for p in pages])
    check("every kept page carries its kind", [p["kind"] for p in pages] ==
          ["article", "article", "category", "article"], [p["kind"] for p in pages])
    check("...and the metadata the scorer needs travels with it",
          [p["title"] for p in pages if p["kind"] == "article"] ==
          ["Warehouse Payback: $17.00, Not $17.95", "Your Battery Payback: A 5-State Gap",
           "Your Cluster's Hidden Clock: 3 Minor Versions, 1 Year"]
          and pages[1]["category_slugs"] == ["energy-efficiency"]
          and all({"url", "title", "excerpt", "modified", "categories", "category_slugs", "canonical",
                   "kind"} <= set(p) for p in pages),
          [(p["title"], p["category_slugs"]) for p in pages])
    check("the hub is classified by its path even though nothing on the page says so",
          pages[2]["canonical"] == "https://giniloh.com/categories/supply-chain-operations/",
          pages[2]["canonical"])

    before = len(corpus_transport.calls)
    warm_pages = sc.metadata_for(asked, frontend="https://giniloh.com", cache_dir=tmp,
                                 fetch=corpus_transport)
    refetched = corpus_transport.urls()[before:]
    check("a warm run refetches nothing it could cache — only the 404, which has no cacheable page",
          refetched == ["https://aichieve.net/removed-article/"]
          and [p["url"] for p in warm_pages] == [p["url"] for p in pages]
          and all(p["from_cache"] for p in warm_pages),
          (refetched, [p["from_cache"] for p in warm_pages]))

bound_transport = FakeTransport(routes)
try:
    result = sc.metadata_for([GINILOH_ARTICLE] * 5, frontend="https://giniloh.com", fetch=bound_transport,
                             max_pages=3)
    check("more urls than max_pages raises rather than truncating the crawl silently", False, result)
except sc.SiteCorpusError as exc:
    check("more urls than max_pages raises rather than truncating the crawl silently",
          "max_pages" in str(exc) and bound_transport.calls == [], (exc, bound_transport.calls))

unreachable = FakeTransport({}, default=(404, {}, b""))
check("nothing fetchable yields an empty list, never a made-up page",
      sc.metadata_for([GINILOH_ARTICLE], frontend="https://giniloh.com", fetch=unreachable) == [])
calls_before = len(unreachable.calls)
check("an empty input never touches the network",
      sc.metadata_for([], frontend="https://giniloh.com", fetch=unreachable) == []
      and len(unreachable.calls) == calls_before, unreachable.urls())

relative = FakeTransport({WELLROOST_ARTICLE: (200, {}, fixture("wellroost_battery-payback-five-state-gap.html"))})
check("a site-relative url from a sitemap is resolved against the frontend",
      [p["url"] for p in sc.metadata_for(["/battery-payback-five-state-gap/"],
                                         frontend="https://wellroost.com/",
                                         fetch=relative)] == [WELLROOST_ARTICLE],
      relative.urls())

load = FakeTransport({}, default=(404, {}, b""))
load.delay = 0.04
load_urls = [f"https://load-a.test/p{i}/" for i in range(9)] + \
            [f"https://load-b.test/q{i}/" for i in range(4)]
sc.metadata_for(load_urls, frontend="https://load-a.test", fetch=load, max_pages=100)
check("at most 3 requests in flight per host, however many urls a host has",
      load.max_inflight.get("load-a.test") == 3 and load.max_inflight.get("load-b.test", 0) <= 3,
      load.max_inflight)
check("...the cap is reached, so the crawl is parallel, not serialised",
      load.max_inflight.get("load-a.test") == 3, load.max_inflight)
check("...and every url was fetched exactly once", len(load.calls) == 13
      and sorted(load.urls()) == sorted(load_urls), len(load.calls))

again = FakeTransport({}, default=(404, {}, b""))
sc.metadata_for(load_urls[:4], frontend="https://load-a.test", fetch=again, max_pages=100)
check("the per-host gate is released: a later crawl of the same host still proceeds",
      len(again.calls) == 4, len(again.calls))

print("\nsite furniture is stripped from the page's own name")
check("a brand stamp goes",
      sc._strip_site_suffix("Lease Break Penalty & Offset Estimator | Gini Loh")
      == "Lease Break Penalty & Offset Estimator",
      sc._strip_site_suffix("Lease Break Penalty & Offset Estimator | Gini Loh"))
check("...and so does the tagline chunk this Astro build puts in front of it",
      sc._strip_site_suffix("Artificial Intelligence & Future of Work \u2014 dispatches and tools | AIChieve")
      == "Artificial Intelligence & Future of Work",
      sc._strip_site_suffix("Artificial Intelligence & Future of Work \u2014 dispatches and tools | AIChieve"))
check("a short title keeps its own dash subtitle (only a real name survives a second strip)",
      sc._strip_site_suffix("Total Comp \u2014 Real Numbers | Gini Loh") == "Total Comp \u2014 Real Numbers",
      sc._strip_site_suffix("Total Comp \u2014 Real Numbers | Gini Loh"))
check("an unstamped title is left alone",
      sc._strip_site_suffix("Your Battery Payback: A 5-State Gap") == "Your Battery Payback: A 5-State Gap")
check("og:title is stripped too \u2014 the branch a hub or calculator page takes",
      sc.page_metadata(OG_ONLY_HTML, "https://a.com/calculators/x/")["title"] == "Some Calculator",
      sc.page_metadata(OG_ONLY_HTML, "https://a.com/calculators/x/"))

print(f"\n{len(PASS)} passed, {len(FAIL)} failed")
for name in FAIL:
    print(f"  FAILED: {name}")
raise SystemExit(1 if FAIL else 0)
