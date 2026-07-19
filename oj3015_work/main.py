"""Price calculate"""
actual_num = int(input())
paid_num = int(input())
price = int(input())
customer = int(input())
n = customer // actual_num
countable = int(f"{actual_num}"f"{paid_num}")
poss_int = int(f"{price}"f"{customer}")
remainder = customer % actual_num
groups = customer//actual_num
promo_cal = (groups * paid_num * price)+(remainder* price)
if countable > 0 and poss_int >=0 :
    if customer >=actual_num:
        print(promo_cal)
    else:
        print(customer*price)
else:
    print("Not what we expected")
