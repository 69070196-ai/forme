"""SCORE"""
lines = int(input())
mylist = []
x = 0
while x < lines:
    mylist.append(int(input()))
    x += 1
highest = max(mylist)
h = []
for i in mylist:
    if i == highest:
        h.append(i)
print(highest)
print(len(h))
