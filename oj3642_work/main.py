""" TicTacToe """
def who_woncheck(xo, line1, line2, line3):
    """XO check"""
    check = False
    for i in range(3):
        if line1[i] == xo and line2[i] == xo and line3[i] == xo:
            check = True
    if line1 == xo*3 or line2 == xo*3 or line3 == xo*3:
        check = True
    elif line1[0] == xo and line2[1] == xo and line3[2] == xo:
        check = True
    elif line1[2] == xo and line2[1] == xo and line3[0] == xo:
        check = True
    return check

def main():
    """Who won"""
    line1 = input()
    line2 = input()
    line3 = input()
    if who_woncheck("O", line1, line2, line3):
        print("O WIN")
    elif who_woncheck("X", line1, line2, line3):
        print("X WIN")
    else:
        print("DRAW")
main()
