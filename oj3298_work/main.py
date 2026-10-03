"""Little Rabbit love BUU"""
BUU = input()
BUUlist = list(BUU)
check = False
streak = 0
streak1 = 0
if "buu" in BUU.lower():
    for a in BUU :
        if a.lower() == "b":
            check = True
        elif a.lower() != "u":
            check = False
        if check:
            if a.lower() == "u":
                streak += 1
            else:
                streak = 0
        if streak1 < streak:
            streak1 = streak
check = False
if streak1:
    print(f"Yes {streak1}")
elif "b" in BUU.lower():
    for x, y in enumerate(BUU):
        if not check:
            if y.lower() == "b":
                check = True
                continue
        if check:
            BUUlist[x] = "U"
    print(*BUUlist,sep="")
else:
    for i, _ in enumerate(BUU):
        if (i % 3) + 1 == 1:
            print("B",end="")
        elif (i % 3) + 1 in (2,3):
            print("U",end="")
