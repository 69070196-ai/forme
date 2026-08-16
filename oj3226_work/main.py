"""inflation"""
P = float(input())
n = int(input())
pStang = int((P*100)+0.000001)
for _ in range(n):
    pStang += (pStang*381)//10000
baht = pStang//100
stang = pStang%100
print(f"{baht}.{stang:02d}")
