"""Shorten"""
l = []
result = []
while True:
    num = int(input())
    if num == -1:
        break
    l.append(num)
start = l[0]
previous = l[0]
for num1 in l[1:]:
    if previous == num1-1:
        previous = num1
    elif previous != num1-1:
        if start == previous:
            result.append(str(start))
        elif start < previous:
            result.append(str(start)+"-"+str(previous))
        start = num1
        previous = num1
if start == previous:
            result.append(str(start))
elif start < previous:
    result.append(str(start)+"-"+str(previous))
print(*result, sep=", ")