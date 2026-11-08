"""it's magic"""
def main():
    """where's the ball"""
    codes = input()
    start = 1
    for code in codes:
        if (start == 1 and code == "A") or (start == 3 and code == "B"):
            start = 2
        elif (start == 1 and code == "C") or (start == 2 and code == "B"):
            start = 3
        elif (start == 2 and code == "A") or (start == 3 and code == "C"):
            start = 1
    print(start)
main()
