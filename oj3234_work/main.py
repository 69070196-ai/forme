"""christmas light"""
color, num = input().split()
num = int(num)
colorlist = ["Red","Green","Blue"]
start = 0
if color == "G":
    start = 1
elif color == "B":
    start = 2
for _ in range(num):
    print(colorlist[start],end=" ")
    if start == 2:
        start = 0
    else:
        start += 1
