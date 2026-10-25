""" Imposter """
import json
def imposter():
    """ Who's the imposter """
    mate = {}
    dead_mate = {}
    imposter_remains = 0
    while True:
        information = input()

        if information == "Start":
            break

        transfer = json.loads(information)
        mate.update(transfer)

    while True:
        colour = input()

        if colour == "End":
            break

        dead_mate.update({colour:mate[colour]})
        mate.pop(colour)

    for _, j in mate.items():
        if j == "Impostor":
            imposter_remains += 1
    alive_list = sorted(mate)
    dead_list = sorted(dead_mate)
    print(imposter_remains, "Impostor Remains")

    print("***Alive***")
    for i in alive_list:
        print(i, ":", mate[i])

    print("***Dead***")
    for i in dead_list:
        print(i, ":", dead_mate[i])
imposter()
