id_card = input("insert number:").strip()

if len(id_card) == 13 and id_card.isdigit():
    print("yes")
else:
    print("no")