"""BrickBridge"""
a = int(input())
b = int(input())
goal = int(input())
a1 = goal-b*5
if a<a1:
    print(-1)
if a1 < 0:
    if b*5 > goal:
        a1 = goal -((b-1)*5)
        print(a1)
if a>=a1:
    print(a1)
