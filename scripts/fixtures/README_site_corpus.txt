Captured fixtures for scripts/site_corpus.py and scripts/test_site_corpus.py
===========================================================================

Every file here is a byte-for-byte capture of what the live site answered on 2026-10-15 (UTC), taken
with curl from the repo host, read-only:

    curl -sS -L -A "Mozilla/5.0 (editorial-factory corpus)" -o <file> <url>

Nothing is hand-written and nothing was trimmed: the largest file (giniloh_sitemap.xml, 162 KB) is well
under the 200 KB budget, so it is kept whole — all 1148 <loc> rows the live sitemap carries.

| File | Source | Status | Bytes |
|---|---|---|---|
| wellroost_homepage_shell.html | https://wellroost.com/no-such-article-xyz/ | 200 | 63664 |
| wellroost_battery-payback-five-state-gap.html | https://wellroost.com/battery-payback-five-state-gap/ | 200 | 25828 |
| aichieve_your-cluster-hidden-clock.html | https://aichieve.net/your-cluster-hidden-clock/ | 200 | 27164 |
| giniloh_wage-floor-sets-robot-payback.html | https://giniloh.com/wage-floor-sets-robot-payback/ | 200 | 41317 |
| giniloh_sitemap.xml | https://giniloh.com/sitemap.xml | 200 | 165864 (1148 locs) |
| giniloh_robots.txt | https://giniloh.com/robots.txt | 200 | 64 (one Sitemap: directive) |
| wellroost_sitemap-index.xml | https://wellroost.com/sitemap-index.xml | 200 | 184 (index -> sitemap-0.xml) |
| wellroost_sitemap-0.xml | https://wellroost.com/sitemap-0.xml | 200 | 3465 (40 locs) |
| aichieve_sitemap-index.xml | https://aichieve.net/sitemap-index.xml | 200 | 183 (index -> sitemap-0.xml) |
| aichieve_sitemap-0.xml | https://aichieve.net/sitemap-0.xml | 200 | 7918 (97 locs) |
| aichieve_robots.txt.404.html | https://aichieve.net/robots.txt | 404 | 14212 |
| aichieve_sitemap.xml.404.html | https://aichieve.net/sitemap.xml | 404 | 14212 |

The two aichieve 404 bodies are byte-identical on purpose: aichieve.net is one Astro deploy whose
not-found page is the same document for both paths. That is the measured fact the discovery test relies
on — `aichieve.net/sitemap.xml` is a 404, so its corpus can only be reached through the sitemap index.

The wellroost shell is the measured soft 404: a URL that does not exist answers **200** with the
homepage and `canonical = https://wellroost.com/`. It is the reason page identity is decided by the
canonical link and never by an HTTP status.

These files are read only by scripts/test_site_corpus.py (and, for its own fixture cases,
scripts/test_frontends.py). They are never fetched at test time: the test suite is hermetic, and passes
with every socket call blocked.
