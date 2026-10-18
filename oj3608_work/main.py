""" Turnstile """
def turn():
    """Turn around"""
    passed = 0
    unlocked = False
    while True :
        push_coin = input()

        if push_coin == "END":
            break

        if push_coin == "C":
            unlocked = True
        elif push_coin == "P" and unlocked:
            passed += 1
            unlocked = False
    print(passed)
turn()
