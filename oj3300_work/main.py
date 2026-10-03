"""what a work"""
N = int(input())
days = N
work = 0
over = 0
less = 0
for _ in range(N):
    work = int(input())
    if work > 18:
        over += 1
    else:
        less += 1
if less >= over :
    print(days)
else:
    days += over - less - 1
    print(days)
