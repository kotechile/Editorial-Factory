import sys, re, json
sys.path.insert(0, '/root/editorial-factory/scripts')
import citation_hub_dossier as c

urls = [
    "https://segment.com/blog/goodbye-microservices/",
    "https://www.primevideotech.com/video-streaming/scaling-up-the-prime-video-audio-video-monitoring-service-and-reducing-costs-by-90",
    "https://www.infoq.com/news/2023/05/amazon-prime-video-microservices/",
    "https://dora.dev/research/2024/dora-report/",
    "https://dora.dev/research/2025/dora-report/",
    "https://survey.stackoverflow.co/2025/ai",
    "https://arxiv.org/html/2507.09089v1",
    "https://arxiv.org/abs/2302.06590",
    "https://www.gitclear.com/ai_assistant_code_quality_2025_research",
    "https://martinfowler.com/articles/microservice-trade-offs.html",
    "https://www.datadoghq.com/container-report/",
    "https://www.cncf.io/reports/cncf-annual-survey-2023/",
]
for u in urls:
    try:
        r = c.fetch_source(u)
        st = r.get('status'); t = r.get('text') or ''
        pcts = re.findall(r'\d+(?:\.\d+)?%', t)[:12]
        print(f"--- {u}\n    status={st} len={len(t)} pct={pcts}")
        if st == 'fetched':
            # show a few context windows around 'microservice' / 'monolith' / 'faster' / 'slower'
            for kw in ('microservice', 'monolith', 'faster', 'slower', 'deploy'):
                m = re.search(r'.{0,120}' + kw + r'.{0,120}', t, re.I)
                if m:
                    print(f"    [{kw}] ...{m.group(0).strip()[:220]}...")
    except Exception as e:
        print(f"--- {u}\n    ERROR {type(e).__name__}: {e}")
