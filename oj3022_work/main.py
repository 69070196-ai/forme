"""Temperature Converter"""
def main():
    """TEMP CONDITION"""
    TEMP = 0
    C = 0
    T = float(input())
    B = input()
    A = input()
    if B == "C":
        C = T
    elif B == "F":
        C = (T-32)/1.8
    elif B == "R":
        C = (T-491.67)/1.8
    elif B == "K":
        C = T-273.15
    if A == "C":
        TEMP = C
    elif A == "F":
        TEMP = (C*1.8)+32
    elif A == "R":
        TEMP = (C*1.8)+491.67
    elif A == "K":
        TEMP = C+273.15
    print(f"{TEMP:.2f}")
main()
