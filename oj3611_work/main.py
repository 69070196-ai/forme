""" What promotion ? """
def promotion():
    """f ts"""
    coffee_price = float(input())
    b_discount = float(input())
    c_discount = float(input())
    least_price = float(input())
    coffee_amount = int(input())
    total_price = coffee_price * coffee_amount
    first_price = coffee_price + (coffee_price * (1 - b_discount / 100) * (coffee_amount - 1))
    second_price = (total_price) * (1 - c_discount / 100) if \
        total_price >= least_price else total_price

    print(1 if first_price < second_price else 2)
    print(f"{min(first_price,second_price):.2f}")
promotion()
