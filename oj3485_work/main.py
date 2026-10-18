""" intersect """
def intersect():
    """ insect """
    _ = int(input())
    ancients = [int(x) for x in input().split()]
    ancients_dict = {}
    a_list = []
    for x in ancients:
        if x in ancients_dict:
            ancients_dict[x] += 1
        else:
            ancients_dict[x] = 1
    for i, j in ancients_dict.items():
        if j == 1:
            a_list.append(i)
    a_list.sort()
    print(" ".join(map(str,a_list)))
intersect()
