"""prime num"""
def cal():
    start,stop = map(int,(input().split()))
    numlist = []
    if start <= 1:
        start = 2
    for i in range(start,stop+1):
        numlist.append(i)
    for x in range(start,stop+1):
        for i in range(2,100000):
            if not x%i and i < x:
                numlist.remove(x)
                break
    print(*numlist,sep=" ")
    print(f"Total primes: {len(numlist)}")
cal()
