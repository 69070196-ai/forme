""" Heads and legs """
def main():
    """i love leg"""
    animals = int(input())
    legs = int(input())
    rabbit_leg = 4
    bird_leg = 2
    bird = legs // bird_leg
    rabbit = abs(animals-bird)
    bird = abs(animals - rabbit)

    if ((rabbit*rabbit_leg) + (bird*bird_leg)) == legs:
        print(rabbit, bird)
    else:
        print("Impossible")
main()
