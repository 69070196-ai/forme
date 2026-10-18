"""3 Kangaroo Jump to the moon"""
def kangaroo():
    """kangaroo jump between the line"""
    l = sorted([int(input()), int(input()), int(input())])
    k1, k2, k3 = l[0], l[1], l[2]
    print((k2 - 1) - k1 if k2 - k1 > k3 - k2 else print(k3 - (k2 + 1)))
kangaroo()
