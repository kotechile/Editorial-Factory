import sys, re
sys.path.insert(0, 'scripts')
import citation_hub_dossier as c

t = c.fetch_source("https://www.ecfr.gov/current/title-26/section-1.422-4")['text']
i = t.find("( d ) Examples")
if i < 0:
    i = t.find("Examples. The following examples")
print(t[i:i + 9000].replace("\n", " "))
