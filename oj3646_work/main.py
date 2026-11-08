"""BTS"""
def main():
    """train fare"""
    day = input()
    age = float(input())
    height = float(input())
    if age < 14:
        if (height < 90) or (height <= 140 and day == "Children Day"):
            print("FREE")
        else:
            print("PAY")
    elif age >= 60:
        if day == "Senior Day":
            print("FREE")
        else:
            print("PAY")
    else:
        print("PAY")
main()
