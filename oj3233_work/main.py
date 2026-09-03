"""Lottery"""
letter, num = input().split()
letter1, num1 = input().split()
if letter == letter1 and num == num1:
    print(1000000)
elif num == num1:
    print(100000)
elif letter == letter1 and num[2:] == num1[2:]:
    print(2000)
elif letter == letter1 and num[3:] == num1[3:]:
    print(1000)
elif num[2:] == num1[2:]:
    print(200)
elif num[3:] == num1[3:]:
    print(100)
elif letter == letter1:
    print(20)
else:
    print(0)
