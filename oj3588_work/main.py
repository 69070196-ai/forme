"""GCD_N"""
from math import gcd
from functools import reduce
n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))
print(reduce(gcd, l))
