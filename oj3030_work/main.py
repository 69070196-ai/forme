"""SAITAMA"""
import math
pushup = int(input())
situp = int(input())
squat = int(input())
run = int(input())
r1 = int(input())
r2 = int(input())
r3 = int(input())
r4 = int(input())
d1,d2,d3,d4 =[(pushup/r1),(situp/r2),(squat/r4),(run/r3)]
M = max(d1,d2,d3,d4)
print(math.ceil(M))
