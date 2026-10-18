"""Lottery Hint"""
def lottery(o, t, h):
    """LOTTERY STYLE"""
    hint = [o, t, h]
    op = [i for i,_ in hint]
    place = [int(i) for _,i in hint]
    for i, j in enumerate(op):
        if j == ">":
            place[i] = range(place[i] + 1, 10)
        elif j == "<":
            place[i] = range(0, place[i])
        elif j == ">=":
            place[i] = range(place[i], 10)
        elif j == "<=":
            place[i] = range(0, place[i] + 1)
        elif j == "==":
            place[i] = [place[i]]
        elif j == "!=":
            x = place[i]
            place[i] = [0,1,2,3,4,5,6,7,8,9]
            place[i].remove(x)
    for i in place[2]:
        for j in place[1]:
            for k in place[0]:
                print(str(i) + str(j) + str(k))
lottery(input().split(), input().split(), input().split())
