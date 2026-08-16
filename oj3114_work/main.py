"""Suvarnabhumi Airport Parking"""
from math import ceil
khao = float(input())
aok = float(input())
time = ceil(aok-khao)
park = {
    1:25,
    2:50,
    3:80,
    4:110,
    5:145,
    6:180,
}
if 0.15 <= time >= 0:
    print("FREE")
elif 1 <= time <= 6:
    print(park[time])
elif 24 <= time >= 7:
    print(250)
else:
    print("ERROR")
