""" Slice The bread I'm an idiot sandwich """
def bread():
    """What are you ?"""
    W, H, _, _ = [int(num) for num in input().split()]
    vertical = sorted([int(v) for v in input().split()] + [W,0])
    horizontal = sorted([int(h) for h in input().split()] + [H,0])
    v_list = [vertical[i+1]-vertical[i] for i in range(len(vertical)-1)]
    h_list = [horizontal[j+1]-horizontal[j] for j in range(len(horizontal)-1)]
    area_list = []
    for i in v_list:
        for j in h_list:
            area_list.append(i*j)
    area_list.sort(reverse=True)
    print(area_list[0], area_list[1])
bread()
