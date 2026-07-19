"""Trigonometry"""
x = float(input())
y = float(input())

def quadrant():
    """check quadrant"""
    if not x and not y:
        print("O")
    elif x > 0 and y > 0:
        print("Q1")
    elif y > 0 > x:
        print("Q2")
    elif x < 0 and y < 0:
        print("Q3")
    elif y < 0 < x:
        print("Q4")
    elif (x > 0 or x < 0) and not y:
        print("X")
    elif (y > 0 or y < 0) and not x:
        print("Y")
quadrant()
