"""movie ticket"""
def ticket():
    """recieve inputs"""
    seats = int(input())
    solds = []
    i = 0
    while True:
        try:
            solds.append(input().split())
            i += 1
        except EOFError :
            return solds, seats
def main():
    """MAIN"""
    sold, seat = ticket()
    for age, tic in sold:
        age, tic = int(age),int(tic)
        if not seat:
            break
        if age < 15:
            print(-1)
        elif 15 <= age <= 22 and seat - tic >= 0:
            print(f"{(150 * tic) * (1 - 0.2):.0f}",seat - tic)
            seat -= tic
        elif age >= 60 and seat - tic >= 0:
            print(f"{(150 * tic) * (1 - 0.5):.0f}",seat - tic)
            seat -= tic
        elif 22 < age < 60 and seat - tic >= 0:
            print(f"{(150 * tic):.0f}",seat - tic)
            seat -= tic
        else:
            print(-2)
main()
