"""MilCode"""
def main():
    """decoder 1234"""
    num_input = [int(i) for i in input().split()]
    contag = ""
    for i in num_input:
        str_i = str(i)
        thousand = int(str_i[-4:]) if int(str_i[-4:]) >= 1000 else 0
        hundred = int(str_i[-3:]) if int(str_i[-3:]) >=100 else 0
        ten = int(str_i[-2:]) if int(str_i[-2:]) >= 10 else 0
        one = int(str_i[-1:]) if int(str_i[-1:]) >= 1 else 0
        if thousand >= 1000:
            contag += "#"
        if hundred >= 100:
            contag += "/"
        if ten >= 10:
            contag += "+"
        if one >= 1:
            contag += "*"
        if not i:
            contag += "-"
    print(contag)
main()
