"""POD"""
N,K = map(int,(input().split()))
L = []
limit = 0
pod = []
K1 = []
n = 0
for i in range(K):
    K1.append(n+1)
    n += 1
while limit < N:
    L.append(int(input()))
    limit += 1
for i in L:
    pod.append(i)
    if pod in K1:
        L.(K1)

