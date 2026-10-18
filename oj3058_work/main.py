"""BrickBridge"""
a = int(input())
b = int(input())
goal = int(input())
a1 = goal-min(goal//5,b)*5
if a<a1:
    print(-1)
elif a>=a1 :
    print(a1)
