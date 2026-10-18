""" GongCharm """
def charms():
    """MyGongCharm"""
    N = int(input())
    charm_list = [int(input()) for _ in range(N)]
    charm_list.sort()
    first_charm = charm_list[0]
    gongcharm1 = 1
    gongcharm2 = 1
    for charm in charm_list[1:]:
        if first_charm == charm :
            gongcharm1 += 1
        else:
            first_charm = charm
            gongcharm1 = 1
        if gongcharm2 < gongcharm1:
            gongcharm2 = gongcharm1
    print(gongcharm2)
charms()
