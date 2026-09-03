"""Conan"""
name = list(input())
num = int(input())
numkey = []
decode = []
alphadict = {
    1 : "a",
    2 : "b",
    3 : "c",
    4 : "d",
    5 : "e",
    6 : "f",
    7 : "g",
    8 : "h",
    9 : "i",
    10 : "j",
    11 : "k",
    12 : "l",
    13 : "m",
    14 : "n",
    15 : "o",
    16 : "p",
    17 : "q",
    18 : "r",
    19 : "s",
    20 : "t",
    21 : "u",
    22 : "v",
    23 : "w",
    24 : "x",
    25 : "y",
    26 : "z"
}
for i in name:
    for k,v in alphadict.items():
        if i == v:
            numkey.append(k)
            break
for i,_ in enumerate(numkey):
    for _ in range(num):
        if numkey[i]+1 > 26:
            numkey[i] = 0
        numkey[i] += 1
for i in numkey:
    decode.append(alphadict[i])
print(*decode,sep="")
