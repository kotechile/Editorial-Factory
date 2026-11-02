from statistics import NormalDist
nd = NormalDist()

def cr(M, H):
    return M / (M + H)

def z(p):
    return round(nd.inv_cdf(p), 2)

def H(cost, rate, days):
    return cost * rate * days / 365.0

rows = [
    ("A precision pump, 30% margin", 200, 0.30, 45, 0.25, 0),
    ("A + 5% invoice fine on a $200 unit", 200, 0.30, 45, 0.25, 10),
    ("B commodity bracket, 12% margin", 200, 0.12, 45, 0.25, 0),
    ("B + 5% invoice fine ($10)", 200, 0.12, 45, 0.25, 10),
    ("C bulk fastener $20, 50% margin", 20, 0.50, 45, 0.25, 0),
    ("D $0.60 bracket feeding a line, 7-day cover, $30 miss", 0.60, 0.50, 7, 0.25, 0),
    ("E $5 clip, 50% margin, 14-day cover", 5, 0.50, 14, 0.25, 0),
]
print(f"{'sku':52} {'H':>8} {'M':>8} {'CR':>7} {'z_cr':>5} {'z98':>5} {'ratio98':>7}")
for name, cost, m, days, rate, fine in rows:
    h = H(cost, rate, days)
    M = cost * m + fine
    if name.startswith("D"):
        M = 30.0
    p = cr(M, h)
    zc = z(p)
    r = round(z(0.98) / zc, 2) if zc else None
    print(f"{name:52} {h:8.4f} {M:8.2f} {p*100:6.2f}% {zc:5.2f} {z(0.98):5.2f} {r:7.2f}")

print()
print("z values: 0.90", z(0.90), "| 0.95", z(0.95), "| 0.98", z(0.98), "| 0.99", z(0.99), "| 0.999", z(0.999))
print("99 vs 95 factor:", round(nd.inv_cdf(0.99)/nd.inv_cdf(0.95), 3))
print("98 vs 95 factor:", round(nd.inv_cdf(0.98)/nd.inv_cdf(0.95), 3))
print("B ratio 2.05/0.83:", round(nd.inv_cdf(0.98)/nd.inv_cdf(cr(24, H(200,0.25,45))), 3), "CR", round(cr(24, H(200,0.25,45))*100,2))
print("A CR", round(cr(60, H(200,0.25,45))*100,2), "z", z(cr(60, H(200,0.25,45))))
print("C CR", round(cr(10, H(20,0.25,45))*100,2), "z", z(cr(10, H(20,0.25,45))))
print("E CR", round(cr(2.5, H(5,0.25,14))*100,2), "z", z(cr(2.5, H(5,0.25,14))))
print("D CR", round(cr(30, H(0.6,0.25,7))*100,4), "z", z(cr(30, H(0.6,0.25,7))))
print("milk check: H=4/365*1.5 =", round(4/365*1.5, 6), "M=0.45 CR=", round(cr(0.45, 4/365*1.5)*100,2))
