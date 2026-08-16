"""coke cap promotion"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
def main():
    """this function calculate how much you have to pay with the cap you have"""
    nodiscountprice = d*a
    discountuget = 0
    if b > 0 :
        discountuget = ((d-(d>0))//b)*(a-c)
    price = nodiscountprice-discountuget
    print(price)
main()
