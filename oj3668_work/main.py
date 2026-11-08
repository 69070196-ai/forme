"""THEOS message"""
def main():
    """what was that"""
    atoz = input()
    atoz_dic = {}
    for i in atoz:
        atoz_dic[i] = atoz_dic.get(i, 0) + 1
    for j, k in atoz_dic.items():
        print(str(k)+j, end="")
main()
