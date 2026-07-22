"""Price calculate"""
actual_num = int(input())
paid_num = int(input())
price = int(input())
customer = int(input())
remainder = customer % actual_num
groups = customer//actual_num
promo_cal = (groups * paid_num * price)+(remainder* price)
print(promo_cal)
