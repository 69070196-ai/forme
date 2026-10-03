"""isPrime ? Large"""
def is_prime(x):
    """is that a prime number ?"""
    check = True
    if x == 1:
        print("NO")
        return
    for num in range(2, int(x ** 0.5) + 1):
        if not x % num:
            check = False
            break
    print("YES" if check else "NO")
is_prime(int(input()))
