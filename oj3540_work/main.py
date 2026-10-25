""" Digit V3 """
def digit():
    """ what's that number """
    num_notation = input().split()
    num_list = []
    thousand = 0
    hundred = 0
    ten = 0
    number_dict = {
    "zero": 0, "one": 1, "two": 2,
    "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8,
    "nine": 9, "ten": 10, "eleven": 11,
    "twelve": 12, "thirteen": 13, "fourteen": 14,
    "fifteen": 15, "sixteen": 16, "seventeen": 17,
    "eighteen": 18, "nineteen": 19, "twenty": 20,
    "thirty": 30, "forty": 40, "fifty": 50,
    "sixty": 60, "seventy": 70, "eighty": 80,
    "ninety": 90, "hundred": 100, "thousand": 1000,
}
    for i in num_notation:
        num_list.append(number_dict[i])
    thousand_index = 0
    if 1000 in num_list:
        for l, i in enumerate(num_list):
            if i == 1000:
                thousand *= 1000
                thousand_index = l
                break
            thousand += i
        for _, j in enumerate(num_list[thousand_index+1:]):
            if  j != 100:
                hundred += j
            else:
                hundred *= 100
    else:
        for _, j in enumerate(num_list):
            if  j != 100:
                hundred += j
            else:
                hundred *= 100
    print(thousand + hundred + ten)
digit()
