import sys, re
sys.path.insert(0, '/root/editorial-factory/scripts')
import citation_hub_dossier as c

def show(url, kws, w=200):
    r = c.fetch_source(url)
    t = r.get('text') or ''
    print(f"===== {url}\n status={r.get('status')} len={len(t)}")
    for kw in kws:
        for m in list(re.finditer(kw, t, re.I))[:3]:
            s = max(0, m.start()-w); e = min(len(t), m.end()+w)
            print(f"  [{kw}] ...{' '.join(t[s:e].split())}...")
    return t

show("https://arxiv.org/html/2507.09089v1", [r"19%", r"24%", r"forecast", r"246", r"16 ", r"39 percentage", r"two hours"])
show("https://arxiv.org/abs/2302.06590", [r"55\.8", r"95 developers", r"1 hour", r"35%"])
show("https://survey.stackoverflow.co/2025/ai", [r"84%", r"46%", r"47\.1", r"trust", r"68\.7", r"50\.6"], w=160)
show("https://www.gitclear.com/ai_assistant_code_quality_2025_research", [r"63%", r"14%", r"8\.3", r"duplicat", r"refactor", r"copy/paste"], w=220)
