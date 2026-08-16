"""sahakorn"""
YorN = input()
n = int(input())
ruam = 0
for _ in range(n):
    ruam += float(input())
if YorN == "Y":
    ruam *= (1-0.05)
elif YorN == "N" and ruam >= 500:
    ruam *= (1-0.03)
print(f"{ruam+0.000001:.2f}")
