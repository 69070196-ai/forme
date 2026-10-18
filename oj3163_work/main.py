"""export"""
def main():
    """EXPORT MAN"""
    N = int(input())
    s, o, e = 0, 0, 0
    for _ in range(N):
        x = int(input())
        s += x
        if not x % 2:
            e += 1
        else:
            o += 1
    print(f"SUM {s}")
    print(f"EVEN {e}")
    print(f"ODD {o}")
main()
