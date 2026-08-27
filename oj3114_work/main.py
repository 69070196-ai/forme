"""Suvarnabhumi Airport Parking"""
from math import ceil
khao = float(input())
aok = float(input())
time = aok-khao
if time > 0.15:
    time = ceil(time)
park = {
    1:25,
    2:50,
    3:80,
    4:110,
    5:145,
    6:180,
}
if time <=  0.15:
    print("FREE")
elif 1 <= time <= 6:
    print(park[time])
elif 6 < time <= 24:
    print(250)
else:
    print("ERROR")
