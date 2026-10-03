"""Giraffe"""
N = int(input())
l = []
full = 0
for _ in range(N):
    l.append(int(input()))
for i, height in enumerate(l) :
    left = l[i - 1] if i - 1 >= 0 else 0
    right = l[i + 1] if i + 1 < N else 0
    if left < height > right:
        full += 1
print(full)
