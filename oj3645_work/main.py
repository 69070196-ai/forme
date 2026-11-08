"""PhoneNumber"""
def phone(number, formats):
    """phone format check"""
    if len(number) == 9:
        if formats == "Domestic":
            print(number[0], number[1:5], number[5:])
        else:
            print("+66", number[1:5], number[5:])
    elif len(number) == 10:
        if formats == "Domestic":
            print(number[:2], number[2:6], number[6:])
        else:
            print("+66" + number[1], number[2:6], number[6:])
def main():
    """PhoneNumber Format"""
    number = input()
    formats = input()
    phone(number, formats)
main()
