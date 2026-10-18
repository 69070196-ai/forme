"""Car unsold"""
def car():
    """ 2nd hand smoking """
    n = int(input())
    cars = []

    for _ in range(n):
        _, v = [int(x) for x in input().split()]
        cars.append(v)

    max_v = 0
    unsold = 0

    for v in reversed(cars):
        if v < max_v:
            unsold += 1
        else:
            max_v = v
    print(unsold)
car()
