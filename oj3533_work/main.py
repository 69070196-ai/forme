""" Horizontal Histogram """
def horizontal():
    """ Maybe a harder histogram """
    histo_string = input()
    horizontal_dict = {}
    for alpha in histo_string:
        if alpha in horizontal_dict:
            if not horizontal_dict[alpha].count("-") % 5:
                horizontal_dict[alpha] += "|"
            horizontal_dict[alpha] += "-"
        else:
            horizontal_dict[alpha] = "-"
    sort_dict = sorted(horizontal_dict ,key=lambda char: (char.isupper(), char.lower()))
    for i in sort_dict:
        print(i, ":", horizontal_dict[i])
horizontal()
