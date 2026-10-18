""" Ai mar 4 khon """
def howmany_person():
    """How many Person are there ?"""
    male = 0
    female = 0
    participants = 0
    while True:
        identity = input()
        check_id = int(identity)

        if check_id < 0:
            break

        participants += 1

        if identity[-1] in "13579":
            male += 1
        elif identity[-1] in "02468":
            female += 1
    print(male, female, participants)
howmany_person()
