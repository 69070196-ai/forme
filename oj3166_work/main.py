"""GPAX"""
N = int(input())
combination = []
check = True
for _ in range(N):
    combination.append(int(input()))
for i in combination:
    if i < 50:
        check = False
avg = sum(combination)/N
print(f"{avg:.1f}")
if check and avg >=60:
    print("PASS")
else:
    print("FAIL")
