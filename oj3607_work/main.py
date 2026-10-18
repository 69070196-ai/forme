""" What is worth the most? """

def worth():
    """ W or L """
    n = int(input())
    pw_list = []
    first_index = 0
    worthiest_str = ""
    for _ in range(n):
        price = float(input())
        weight = float(input())
        pw_list.append([price, weight])

    worthiest = pw_list[0][0] / pw_list[0][1]
    first_price = pw_list[0][0]

    for i, pw in enumerate(pw_list):
        price, weight = pw[0], pw[1]
        index = price / weight
        if index < worthiest :
            worthiest = index
            first_price = price
            first_index = i
        elif index == worthiest:
            if price < first_price:
                first_index = i

    worthiest_str = f"{pw_list[first_index][0]:.2f} {pw_list[first_index][1]:.2f}"
    print(worthiest_str)
worth()
