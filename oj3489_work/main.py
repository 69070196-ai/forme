"""Divide3Or5"""
n = int(input())
x = 0
for i in range(1, n+1):
    if not i % 3 or not i % 5:
        x += i
print(x)
