"""stats"""
def main():
    """statistics"""
    n = int(input())
    x = 0
    y = -99999999999999999999999999
    z = 9999999999999999999999999
    A = 0
    for _ in range(n):
        x = int(input())
        if x > y:
            y = x
        if x < z:
            z = x
        A += x
    print(f"MIN: {z:.3f}")
    print(f"MAX: {y:.3f}")
    print(f"AVG: {A/n:.3f}")
main()
