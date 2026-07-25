"""birthday"""
from datetime import date,timedelta
y1 = int(input())
m1 = int(input())
d1 = int(input())
y2 = int(input())
m2 = int(input())
d2 = int(input())
date1 = (y1,m1,d1)
date2 = (y2,m2,d2)
diff = date1 - date2
zero = timedelta(days=0)
weeks = timedelta(days=7)
if diff < zero and abs(diff) > weeks:
    print("1")
elif diff > zero and diff > weeks:
    print("2")
elif diff <= weeks:
    print("0")
