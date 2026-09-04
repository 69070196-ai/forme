"""HOTEL IN THE MIDDLE OF BANGKOK THAT DOESNT HAVE 13th floor"""
from math import prod
code = list(input())
one,two,three,four,five = int(code[0]),int(code[1]),int(code[2]),int(code[3]),int(code[4])
digitList = [one,two,three,four,five]
stDigit = 0
ndDigit = 0
rdDigit = 0

if one > 5:
    stDigit = 9
elif two > 5:
    stDigit = 10
elif three > 5:
    stDigit = 11
elif four > 5:
    stDigit = 12
elif five > 5:
    stDigit = 14
else:
    stDigit = 13

if code == code[::-1]:
    if one + five > 5 :
        ndDigit = 1
    elif two * four > 5:
        ndDigit = 2
else:
    if 1//5 > 5:
        ndDigit = 1
    elif two-five > 5:
        ndDigit = 2

if sum(digitList) > 25:
    rdDigit = 1
elif prod(digitList) > 55:
    rdDigit = 2
print(str(stDigit)+str(ndDigit)+str(rdDigit))
