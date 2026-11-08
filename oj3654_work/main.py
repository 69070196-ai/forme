"""BBE"""
def main():
    """BBE ddmmyy or mmddyy"""
    n = int(input())
    if not n:
        print("no clue")
        return
    num_list = []
    for _ in range(n):
        date = input()
        num_list.append(date)
    for i in num_list:
        date = i
        date1 = int(date[:2])
        date2 = int(date[2:4])
        check = True
        if date1 > 12:
            print("ddmmyy")
            check = False
            break
        if date2 > 12:
            print("mmddyy")
            check = False
            break
    if check:
        print("no clue")
main()
