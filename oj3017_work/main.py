"""Restaurant Bill"""
rawprice = int(input())

def taxprice():
    """tax"""
    service = rawprice*(10/100)
    if service < 50:
        service = 50
    elif service > 1000:
        service = 1000
    price = rawprice + service
    vat = price*(7/100)
    total = price + vat
    print(f"{total:.2f}")
taxprice()
