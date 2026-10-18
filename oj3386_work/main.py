""" Duplicate I """
def who():
    """ who's that pokemon """
    amount1 = int(input())
    amount2 = int(input())
    group1 = {int(input()) for _ in range(amount1)}
    group2 = {int(input()) for _ in range(amount2)}
    group1.intersection_update(group2)
    if group1:
        for k in sorted(group1, reverse=True):
            print(k)
    else:
        print("Nope")
who()
