"""Largest Number"""
def main():
    """main func"""
    num1, num2, num3 = input(), input(), input()
    n1 = int(num1+num2+num3)
    n2 = int(num1+num3+num2)
    n3 = int(num2+num3+num1)
    n4 = int(num2+num1+num3)
    n5 = int(num3+num1+num2)
    n6 = int(num3+num2+num1)
    if n3<=n1>=n2 and n5<=n1>=n4 and n1>=n6:
        print(n1)
    elif n3<=n2>=n1 and n5<=n2>=n4 and n2>=n6:
        print(n2)
    elif n1<=n3>=n2 and n5<=n3>=n4 and n3>=n6:
        print(n3)
    elif n1<=n4>=n2 and n5<=n4>=n3 and n4>=n6:
        print(n4)
    elif n1<=n5>=n2 and n4<=n5>=n3 and n5>=n6:
        print(n5)
    elif n1<=n6>=n2 and n3<=n6>=n4 and n6>=n5:
        print(n6)
main()
