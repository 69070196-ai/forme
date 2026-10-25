""" how much is it?? """
def iphone():
    """ iphone 13 promax """
    phone_storage = input() + input()
    price_dict = {"iPhone 13 mini128 GB":25900, "iPhone 13 mini256 GB":29900,
                  "iPhone 13 mini512 GB":37900, "iPhone 13128 GB":29900,
                   "iPhone 13256 GB":33900, "iPhone 13512 GB":41900,
                    "iPhone 13 Pro128 GB":38900,"iPhone 13 Pro256 GB":42900,
                    "iPhone 13 Pro512 GB":50900, "iPhone 13 Pro1 TB":58900,
                    "iPhone 13 Pro Max128 GB":42900, "iPhone 13 Pro Max256 GB":
                    46900, "iPhone 13 Pro Max512 GB":54900,
                    "iPhone 13 Pro Max1 TB":62900}
    print(price_dict[phone_storage] if phone_storage in price_dict else "Not Available")
iphone()
