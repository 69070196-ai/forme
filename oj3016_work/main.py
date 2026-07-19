"""power of seven"""
x = int(input())
def main():
    """pattern founds"""
    if not x % 4:
        print("1")
    elif x % 4 == 1:
        print("7")
    elif x % 4 == 2:
        print("9")
    elif x % 4 == 3:
        print("3")
main()
