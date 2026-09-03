"""cartesian"""
def main():
    """dernnaingarn fest"""
    axis = list(input())
    x = 0
    y = 0
    for direct in axis:
        if direct == "N":
            y += 1
        elif direct == "S":
            y -= 1
        elif direct == "E":
            x += 1
        elif direct == "W":
            x -= 1
    print(x,y,(abs(x)+abs(y)))
main()
