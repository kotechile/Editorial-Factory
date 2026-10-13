import sys, re
sys.path.insert(0, '/root/editorial-factory/scripts')
import citation_hub_dossier as c

def show(url, kws, w=170, maxhits=2):
    r = c.fetch_source(url)
    t = r.get('text') or ''
    print(f"===== {url}\n status={r.get('status')} len={len(t)}")
    for kw in kws:
        for m in list(re.finditer(kw, t, re.I))[:maxhits]:
            s = max(0, m.start()-w); e = min(len(t), m.end()+w)
            print(f"  [{kw}] ...{' '.join(t[s:e].split())}...")
    return t

show("https://metr.org/blog/2026-02-24-uplift-update", [r"-18%", r"confidence interval", r"57 developers|could be as high as", r"19% longer", r"selection"])
show("https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study", [r"19% longer", r"246", r"16 (?:experienced )?developers"])
show("https://linearb.io/resources/ai-engineering-productivity-gap", [r"54%", r"45%", r"253 organi", r"4\.7%"])
show("https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here", [r"73%", r"AI coding assistant"])
