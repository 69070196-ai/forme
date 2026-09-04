"""Store Check"""
num,check = map(int,input().split())
checklist = [0]*check+1
starto = [0]
checking = [0]
for x in range(num):
    starto.append(int(input().split()))
checking.append(input().split())
for i in range(1,check+1):
    watch = int(checking[i])
    for start,stop in starto[i]:
        if int(start) <= watch < int(stop):
            checklist[i] += 1
print(checklist)
