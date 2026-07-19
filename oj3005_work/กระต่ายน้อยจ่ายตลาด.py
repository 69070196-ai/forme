"""กระต่ายน้อยจ่ายตลาด"""
shop_list = input().split()
carrot,cabbish,tomato = shop_list
carrot = int(carrot)
cabbish = int(cabbish)
tomato = int(tomato)

CARROT_PRICE = 10
CABBISH_PRICE = 25
TOMATO_PRICE = 3

totalprice = ((carrot * CARROT_PRICE) + (cabbish * CABBISH_PRICE)\
         + (tomato * TOMATO_PRICE))

print(totalprice)
