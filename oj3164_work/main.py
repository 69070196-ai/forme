"""ordered pair"""
def main():
    """list eiei"""
    n = int(input())
    xlist = []
    mylist= []
    sumlist = []
    for i in range(n):
        mylist.append(int(input()))
        mylist.append(int(input()))
        xlist.append(mylist)
        mylist = []
    for _,i in enumerate(xlist):
        sumlist.append(max(i))
    if n > 1 :
        print(*sumlist,sep= " + ",end= "")
    if n == 1:
        print(f"{sum(sumlist)}")
    else:
        print(f" = {sum(sumlist)}")
main()
