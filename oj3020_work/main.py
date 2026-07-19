"""coke cap promotion"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
def main():
    """this function calculate how much you have to pay with the cap you have"""
    groups = 0
    remain = 0
    if b > 0 and c <= a and d > 0:
        groups = d//b
        if d % b > 0 :
            remain = d % b
        elif not d % b :
            remain = b
            groups -= 1
        proset = ((b-1)*a)+c
        pro = proset * groups
        remainp = remain * a
        total = pro + remainp
        print(total)
    elif not b :
        print(d*a)
    elif not d :
        print(0)
main()
