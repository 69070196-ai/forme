"""1 digit"""
def main():
    """digit"""
    str_num = ""
    while True:
        num = int(input())
        sumNum = num
        count = 0
        if not num:
            break

        while len(str(sumNum)) > 1:
            for i in str(sumNum):
                count += int(i)
            sumNum = count
            count = 0
        str_num = str_num + str(sumNum)
    for j in str_num:
        print(j)
main()
