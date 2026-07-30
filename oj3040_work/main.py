"""coin exchange"""
money = int(input())
M = money
MEDAL = 1
coin = []
while M >= MEDAL:
    if M >= 10:
        coin.append(10)
        M -= 10
    elif M >= 5:
        coin.append(5)
        M -= 5
    elif M >= 2:
        coin.append(2)
        M -=2
    elif M >= 1:
        coin.append(1)
        M -=1
print(f"10 = {coin.count(10)}")
print(f"5 = {coin.count(5)}")
print(f"2 = {coin.count(2)}")
print(f"1 = {coin.count(1)}")
