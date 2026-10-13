import json, sys
base = '/root/editorial-factory/'
d = json.load(open(base+'context/verticals.json'))['verticals']
v = d['enterprise_tech_leadership'] if isinstance(d, dict) else next(x for x in d if x['id'] == 'enterprise_tech_leadership')
print(json.dumps(v, indent=2))
print('====PERSONA====')
p = json.load(open(base+'context/personas.json'))['personas']
pi = p['eng_leader'] if isinstance(p, dict) else next(x for x in p if x['id'] == 'eng_leader')
print(json.dumps(pi, indent=2))
