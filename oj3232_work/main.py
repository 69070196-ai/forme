"""little frog"""
X, Y = map(int,(input()).split())
sumary = X
if X > Y:
    times = 1
else:
    times = 0
while sumary <= Y:
    if X - 2 > 0:
        X -= 2
        sumary += X
    else:
        times = -1
        break
    times += 1
print(times)

