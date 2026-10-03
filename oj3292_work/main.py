"""Arrow"""
RorL = input()
size = int(input())
b = size
tall = b + (b - 1)
middle = (tall - 1) // 2
def right():
    """RIGHT ARROW"""
    a = size
    for i in range(tall):
        if i <= middle:
            print(f"{" " * (2 * i)}{"*" * a}")
        elif i  > middle:
            print(f"{" " * (2 * (tall - 1 - i))}{"*" * a}")
        if i < middle:
            a -= 1
        else:
            a += 1
    a = size
def left():
    """LEFT ARROW"""
    a = size
    for i in range(tall):
        print(f"{" " * (abs((tall - middle - 1) - i))}{"*" * a}")
        if i < middle:
            a -= 1
        else:
            a += 1
for RL in RorL:
    if RL == "R":
        right()
    else:
        left()
    if len(RorL) > 1:
        print()
