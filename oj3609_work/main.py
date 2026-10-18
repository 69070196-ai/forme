""" if even/2 else 3n+1 """
def even(n):
    """if it's even do this"""
    return n / 2

def odd(n):
    """if it's odd do this"""
    return (n * 3) + 1

def oddoreven():
    """decide if it's oddoreven and do the above func"""
    num_list =[]
    seq = 1

    while True:
        nums = int(input())
        if not nums :
            break
        num_list.append(nums)

    for num in num_list:
        while num != 1:
            if not num % 2 :
                num = even(num)
                seq += 1
            else :
                num = odd(num)
                seq += 1
        print(seq)
        seq = 1
oddoreven()
