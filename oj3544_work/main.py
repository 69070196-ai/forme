""" Storage Organize system """
def add(storage_dict, product):
    """ Add product """
    name = product[1]
    amount = int(product[2])
    storage_dict[name] = storage_dict.get(name, 0) + amount

def remove(storage_dict, product):
    """ remove product """
    name = product[1]
    amount = int(product[2])

    if name in storage_dict and storage_dict[name] >= amount:
        storage_dict[name] -= amount
    else:
        storage_dict[name] = 0
        print(f"Not enough stock for {name}")

def check(storage_dict, _product):
    """ check the storage """
    insufficients = sorted(
        n for n, amount in storage_dict.items()
        if amount < 5
    )
    if insufficients:
        print(*insufficients, sep="\n")
    else:
        print("All stocks are sufficient")

def report(storage_dict, _product):
    """ report storage """
    for name in sorted(storage_dict):
        print(f"{name}: {storage_dict[name]}")

def org():
    """ Sumphawesee khuen seep """
    storage_org = []
    storage_dict = {}

    while True:
        product = input()

        if product == "END":
            break

        storage_org.append(product)

    handlers = {
        "ADD":add,
        "REMOVE":remove,
        "CHECK":check,
        "REPORT":report
    }

    for product in storage_org:
        product = product.split()
        command = product[0]
        handlers[command](storage_dict, product)
org()
