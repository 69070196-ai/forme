"""Flower"""
size, amount = map(int,input().split())
total = size * (size + 1) // 2
count = 1
while total <= amount:
    total = total * (total + 1) // 2
    count += 1
print(count)
