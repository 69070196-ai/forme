"""E_A Chess possiblilty"""
R_A = int(input())
R_B = int(input())
AORB = input()

E_A = 1 /(1 + (10)**((R_B - R_A)/400))
E_B = 1 /(1 + (10)**((R_A - R_B)/400))
if AORB in ("A","a") and R_A >= 0:
    print(f"{E_A:.2f}")
elif AORB in ("B","b") and R_B >= 0:
    print(f"{E_B:.2f}")
