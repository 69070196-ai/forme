"""TEN DIVISION"""
N = int(input())
a = N
L = []
while a >= 0:
    if not a%10:
        L.append(a)
    a -= 1
print(*L,sep=" ")
