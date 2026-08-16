"""Mad Unicorn"""
departure,destination = input().split()
mass = float(input())
fee = {
    "BKKCNX":10,
    "CNXUBP":15,
    "UBPBKK":20,
    "BKKPKT":25,
    "PKTCNX":30,
    "UBPPKT":40
}
feepermass = {
    "BKKCNX":30,
    "CNXUBP":40,
    "UBPBKK":40,
    "BKKPKT":50,
    "PKTCNX":60,
    "UBPPKT":70
}
way = departure+destination
if way in fee:
    print(f"{(fee[way]+feepermass[way]*mass):.2f}")
else:
    print("Error")
