"""Pure Rabbit"""
def rabbit_pure(message):
    """RABBIT MASSAGE"""
    message = message.upper()
    R = False
    B = False
    Bcheck = False
    A1 = 0
    A2 = 0
    for i, char in enumerate(message):
        if char == "R":
            R = True
        elif R and char != "A":
            R = False
        if R and char == "A":
            A1 += 1
        else:
            A1 = 0
        if A2 < A1:
            A2 = A1
        if char == "B" and not Bcheck:
            Bcheck = True
            continue
        if Bcheck and char in "IT":
            Bcheck = False
            B = True
        if(char == "A" and not R)or(char not in "RABIT")or(Bcheck and char not in "IT"):
            print("no", i)
            break
    if R or B:
        print("yes", A2)
    elif "IT" in message and "B" not in message:
        print("unknown", len(message))
rabbit_pure(input())
