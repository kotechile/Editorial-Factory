import sys, re
sys.path.insert(0, '/root/editorial-factory/scripts')
import citation_hub_dossier as c

for u in ["https://www.primevideotech.com/video-streaming/scaling-up-the-prime-video-audio-video-monitoring-service-and-reducing-costs-by-90",
          "https://segment.com/blog/goodbye-microservices/",
          "https://dora.dev/research/2025/dora-report/"]:
    r = c.fetch_source(u)
    t = r.get('text') or ''
    print(f"===== {u}\n status={r.get('status')} len={len(t)}")
    print("  HEAD:", ' '.join(t[:600].split()))
    print("  nums:", re.findall(r'\d+(?:\.\d+)?%?', t)[:25])
