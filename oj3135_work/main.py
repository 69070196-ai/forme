"""gift and thief"""
N,K,T = map(int,(input().split()))
position = 0
check = 1
while position not in (1,T):
    if T == 1:
        break
    if check == 1:
        position = 1
    position = (position - 1 + K ) % N + 1
    if position > 1:
        check += 1
print(check)
