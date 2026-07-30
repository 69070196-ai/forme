"""BrickBridge"""
a = int(input())
b = int(input())
goal = int(input())
a1 = goal-(b*5)
if a1 > a:
    print(-1)
elif a1<0:
    if b <= 2:
        print(a1+5)
    else:
        print(a1+(5*(b-2)))
else:
    print(a1)
