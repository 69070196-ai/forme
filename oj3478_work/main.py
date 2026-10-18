""" Easy Histogram """
def easy(strings):
    """Histogram Dict"""
    str_dict = {}
    for a in strings:
        if a.isalpha():
            if a in str_dict:
                str_dict[a] += 1
            else:
                str_dict[a] = 1
    new = sorted(str_dict, key=lambda char: (char.lower(), char.isupper()))
    for x in new:
        print(f"{x} = {str_dict[x]}")
easy(input())
