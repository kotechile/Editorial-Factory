import json, base64, time, urllib.request

ROOT = '/root/editorial-factory'
POST = 1746
SLUG = 'your-hidden-461-double-counts'

env = {}
for line in open(f'{ROOT}/.env').read().splitlines():
    if '=' in line and not line.strip().startswith('#'):
        k, v = line.split('=', 1)
        env[k.strip()] = v.strip().strip('"').strip("'")

auth = base64.b64encode(f"{env['WP_AICHIEVE_USER']}:{env['WP_AICHIEVE_APP_PASSWORD']}".encode()).decode()
H = {"Authorization": f"Basic {auth}", "Content-Type": "application/json"}


def post(payload):
    req = urllib.request.Request(f"https://cms.giniloh.com/wp-json/wp/v2/posts/{POST}",
                                 data=json.dumps(payload).encode(), headers=H, method="POST")
    return json.load(urllib.request.urlopen(req, timeout=90))


print('-> draft', post({"status": "draft"})['status'])
time.sleep(3)
print('-> publish', post({"status": "publish"})['status'])

for i in range(12):
    time.sleep(20)
    try:
        req = urllib.request.Request(f"https://aichieve.net/{SLUG}/",
                                     headers={"User-Agent": "Mozilla/5.0"})
        r = urllib.request.urlopen(req, timeout=45)
        body = r.read().decode('utf-8', 'replace')
        print(f'probe {i+1}: HTTP {r.status} chars={len(body)} uploads={body.count("wp-content/uploads")}')
        if r.status == 200:
            import re
            m = re.search(r'<h1[^>]*>([^<]*)', body)
            print('h1:', m.group(1).strip() if m else None)
            print('has link:', '/your-exception-log-owes-5-years/' in body)
            break
    except Exception as e:
        print(f'probe {i+1}: {e}')
