"""xport"""
def main():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    n4 = int(input())
    n5 = int(input())
    n6 = int(input())
    mylist = [n1,n2,n3,n4,n5,n6]
    s = n1+n2+n3+n4+n5+n6
    even = 0
    odd = 0
    for i in mylist:
        if not i%2 and i >= 0:
            even += 1
        elif i%2 and i >= 0:
            odd += 1
    print(f"SUM {s}")
    print(f"EVEN {even}")
    print(f"ODD {odd}")
main()
