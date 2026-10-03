"""Lottery Hint"""
def lottery(one, tens, hundreds):
    hint = [one, tens, hundreds]
    place1 = []
    place2 = []
    place3 = []
    for i, x in enumerate(hint):
        op, place = x[0], int(x[1])
        if op == "==":
            hint[i][1] = place
        elif op == ">":
            hint[i][1] = range(place+1 ,10)
        elif op == ">=":
            hint[i][1] = range(place, 10)
        elif op == "<":
            hint[i][1] = range(1, place)
        elif op == "<=":
            hint[i][1] = range(1, place+1)
    places = [hint[0][1], hint[1][1], hint[2][1]]
    for i, j in enumerate(places):
        if isinstance(j, range):
            for k in j :
                if not i:
                    place1.append(k)
                elif i == 1:
                    place2.append(k)
                elif i == 2:
                    place3.append(k)
        else:
            if not i:
                place1 = j
            if i == 1:
                place2 = j
            if i == 2:
                place3 = j
    for num in place3:
        print(num, end="")
        for num1 in place2:
            print(num1, end="")
            for num2 in place1:
                print(num2, end="")
                print()
                
lottery(input().split(), input().split(), input().split())
