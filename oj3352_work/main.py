"""LastStand"""
import json
strL = input()
newlist = json.loads(strL)
for x in newlist:
    print(str(x)[-1])
