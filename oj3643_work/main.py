"""GAME"""
def main():
    """ game """
    A = int(input())
    B = int(input())
    A = A - (A // 3) * 3
    B = B - (B // 3) * 3
    print(A if A == B else "Error")
main()
