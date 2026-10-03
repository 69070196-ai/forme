"""left arrow"""
from math import ceil
k = int(input())
n = int(input())
middle = ceil(n/2)
for i in range(n):
    if i+1 == middle:
        print("*"*k)
    else:
        print(" "*(abs((n - middle) - (i))-1),"*"*k)
