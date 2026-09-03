"""income analysis"""
N = int(input())
num = int(input())
combi = num
highest = num
lowest = num
for _ in range(N-1):
    income = int(input())
    combi += income
    if income > highest:
        highest = income
    if income < lowest:
        lowest = income
print(combi)
print(highest)
print(lowest)
print(f"{combi/N:.1f}")
