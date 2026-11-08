""" SR ??? """
def nor(a : int, b : int):
    if a == 0 and b == 0:
        return 1
    return 0

def sr_ff(s, r, q, p):
    for _ in range(2):
        q = nor(r, p)
        p = nor(s, q)
    return q, p

def main():
    s, r, q, p = 0, 0, 0, 0
    q, p = sr_ff(s, r, q, p)
    print("step1: r , s | q , p")
    print("--------------------")
    print(f"step1: {r} , {s} | {q} , {p}")
    s = 1
    r = 0
    q, p = sr_ff(s, r, q, p)
    print(f"step2: {r} , {s} | {q} , {p}")
    s = 0
    r = 1
    q, p = sr_ff(s, r, q, p)
    print(f"step3: {r} , {s} | {q} , {p}")
    s = 0
    r = 0
    q, p = sr_ff(s, r, q, p)
    print(f"step2: {r} , {s} | {q} , {p}")
main()
