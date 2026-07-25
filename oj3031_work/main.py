"""INK FLOOD"""
import math
S,N =map(int,(input().split()))
PI = 3.1416
limit = 0
pigud = []
while limit < N:
    pigud.append(map(int,(input()).split()))
    limit +=1
for i in pigud:
    x,y = i
    time = (PI*((x**2+y**2)))/S
    print(math.ceil(time))
