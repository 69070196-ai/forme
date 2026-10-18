"""SumOfNumber"""
d = int(input())
s = 0
while s != d:
    num = int(input())
    if num == -1:
        break
    s += num 
print(s)
