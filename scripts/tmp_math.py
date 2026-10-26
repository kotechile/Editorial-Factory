import math
rows = [1, 5, 10, 20, 40]
for L in rows:
    print(f"0.98^{L} = {0.98**L:.4f}")
print()
for tgt in (0.95, 0.98):
    for L in (5, 10, 20, 40):
        print(f"order fill {tgt:.0%} at L={L}: need line availability {tgt**(1/L):.5f}")
print()
print("0.90^2.25 =", round(0.90**2.25, 4), "gap pts:", round((0.90 - 0.90**2.25)*100, 1))
print("0.90^3.00 =", round(0.90**3.0, 4))
print("0.96 vs 0.82 implied lines:", round(math.log(0.82)/math.log(0.96), 2))
print("0.88.5/2.25 check 0.985^2.25:", round(0.985**2.25, 4))
print("shortage reduction 2%->0.51%:", round((0.98-0.99488)/0.02, 3))
print("0.95^0.1 =", round(0.95**0.1, 5), "0.95^0.05 =", round(0.95**0.05, 5))
print("99% order fill at L=10:", round(0.99**0.1, 5), "L=20:", round(0.99**0.05, 5))
print("0.98^10 as pct:", round(0.98**10*100, 2), "0.98^20:", round(0.98**20*100, 2))
