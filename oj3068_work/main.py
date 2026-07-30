"""athikasuthin?"""
year = int(input())
if (year >= 1582 and not year%4 and year%100) or (not year%400) :
    print("yes")
elif (year < 1582 and not year%4):
    print("yes")
else:
    print("no")
