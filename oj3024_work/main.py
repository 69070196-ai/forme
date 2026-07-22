"""Surprising Vote"""
t = float(input())
m = float(input())
x = t -(2*m)
if x < 0:
    x = 0
d = m -x
if d > 2:
    print("Surprising")
else:
    print("Not surprising")
