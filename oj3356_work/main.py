"""Bus seat"""
seats = int(input())
row = int(input())
sit = int(input())
for i in range(seats):
    line = []
    startseat = seats - i
    for _ in range(row):
        if startseat == sit:
            line.append("XX")
            startseat += seats
            continue
        if len(str(startseat)) == 1:
            line.append("0"+str(startseat))
            startseat += seats
        else:
            line.append(startseat)
            startseat += seats
    print(*line)
    if not (i + 1) % 2 and i != (seats - 1):
        print()
