""" OneTwo """
def one_two(num):
    """ one and two!!! """
    if num == 1:
        return "1"
    if num == 2:
        return "2"
    return one_two(num - 1) + one_two(num - 2)
print(one_two(int(input())))
