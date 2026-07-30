"""loop minimum"""
N = int(input())
L = []
U = 0
while U < N:
    L.append(int(input()))
    U += 1
L.sort()
print(L[0])
