""" Missing Number """
def missed() :
    """ What is missing ?? """
    n = int(input())
    number_list = []
    while True:
        num = int(input())

        if not num:
            break

        number_list.append(num)

    number_list.sort()

    for i in range(1, n+1):
        if i not in number_list:
            print(i)

missed()
