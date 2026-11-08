"""RNG"""
import json
from math import gcd

def main():
    """RNG"""
    arr = json.loads(input())
    n = int(input())
    s = int(input())

    size = len(arr)
    s %= size

    g = gcd(s, size)
    length = size // g

    full, remain = divmod(n, length)

    ans = 0

    for start in range(g):
        cycle = [arr[(start + i * s) % size] for i in range(length)]

        cycle_sum = sum(cycle)
        window = sum(cycle[:remain])

        for i in range(length):
            total = full * cycle_sum + window
            ans = max(ans, total)

            window += cycle[(i + remain) % length] - cycle[i]

    print(ans)

main()