""" List Prime """
def prime():
    """ prime? """
    num = int(input())
    if num == 1:
        print("No")
        return
    prime_list = []
    prime_checked = True
    for i in range(2, int(num ** 0.5)+1):
        if not num % i:
            prime_checked = False
            break
    if prime_checked:
        print("Yes")
        prime_list.append(num)
        for j in range(2, num):
            prime_checked = True
            for k in range(2, int(j ** 0.5)+1):
                if not j % k:
                    prime_checked = False
                    break
            if prime_checked:
                prime_list.append(j)
        prime_list.sort()
        print(*prime_list, sep=" ")
    else:
        print("No")
prime()
