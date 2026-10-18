""" Smart Trash Collector """
def detector(trashs):
    """ Premium Trash Detector """
    trash = []
    print_list = []
    for _ in range(trashs):
        trash.append([float(x) for x in input().split()])
    for t in trash:
        plastic, can, glass = t
        print_list.append(f"{sum(t):.1f}")
        if sum(t) > 50:
            print_list.append("Overloaded")
        if plastic > 20:
            print_list.append("Check Type Plastic")
        if can > 20:
            print_list.append("Check Type Can")
        if glass > 20:
            print_list.append("Check Type Glass")
        print(", ".join(print_list))
        print_list = []
detector(int(input()))
