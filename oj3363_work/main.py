"""rabbit disease"""
r, c = map(int,(input().split()))
i, j = map(int,(input().split()))
infection = int(input())
xy = []
possibility = 0
each = []
point = 0

for _ in range(infection):
    xy.append(input().split())

for x,y in xy:
    if not abs(i-int(x)) and not abs(j-int(y)):
        possibility = 100
    elif abs(i-int(x)) <= 1 and abs(j-int(y)) <= 1:
        possibility = 60
    elif abs(i-int(x)) <= 2 and abs(j-int(y)) <= 2:
        possibility = 20
    else:
        possibility = 0
    if possibility:
        break
check = False
if c > r:
    for k in range(c):
        for j in range(r):
            each.append([j,k])
elif r > c:
    for k in range(r):
        for j in range(c):
            each.append([k,j])
else:
    for k in range(r):
        for j in range(c):
            each.append([k,j])
for x,y in each:
    for i,j in xy :
        if abs(x-int(i)) > 2 or abs(y-int(j)) > 2:
            check = True
        else:
            check = False
            break
    if check:
        point += 1

print(point)
print(f"{possibility}%")
