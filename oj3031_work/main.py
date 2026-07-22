"""INK FLOOD"""
import math
S,N =map(int,(input().split()))
pi = 3.1416
r =math.sqrt(S/pi)
limit = 0
pigud = []
while limit < N:
    pigud.append(map(int,(input()).split()))
    limit +=1
for i in pigud:
    x,y = i
    print(x)
    print(y)
