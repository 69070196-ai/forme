""" Classify """
def it_kmitl():
    """ what year? """
    id_list = []
    id_dict = {}
    while True:
        id_input = input()

        if id_input == "END":
            break

        id_list.append(id_input[0:4])
    new_list = [int(num) for num in id_list]
    new_list.sort()
    new_list = [str(string) for string in new_list]

    for num in new_list:
        if num in id_dict:
            id_dict[num] += 1
        else:
            id_dict[num] = 1
    old_year = 0
    for i, j in id_dict.items():
        year = int(i[0:2])
        faculty = int(i[2:])
        if year > old_year:
            print(year, faculty, j)
            old_year = year
        else:
            print("--", faculty, j)
it_kmitl()
