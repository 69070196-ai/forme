"""3d distance"""
import math
p1 = input().split()
x1,y1,z1 = p1
x1 = int(x1)
y1 = int(y1)
z1 = int(z1)
p2 = input().split()
x2,y2,z2 = p2
x2 = int(x2)
y2 = int(y2)
z2 = int(z2)

d = math.sqrt(((x1 - x2)**2) +((y1-y2)**2)+((z1-z2)**2))
print(f"{d:.2f}")
