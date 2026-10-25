"""CALCULATOR V2"""
def main(place):
    """place"""
    num = int(place)
    click = 0
    multiplier = len(place)
    expo = len(place) - 2
    start = 9 * 10 ** expo
    if num == 1:
        print(1)
    elif len(place) == 1:
        print(num * 2)
    else:
        while start > 1:
            click += (start * multiplier)
            num -= start
            start //= 10
            multiplier -= 1
        click += num * (len(place) + 1)
    if click :
        print(click)
main(input())