"""Name of Cards"""
def name(card):
    """What Card is that ??"""
    face = card[-1].upper()
    value = card[0:-1].upper() if card[0:-1].isalpha() else card[0:-1]
    face_dict = {"D":"Diamonds", "H":"Hearts", "S":"Spades",
                 "C":"Clubs", "A":"Ace", "K":"King","J":"Jack","Q":"Queen"}
    if value.isdigit():
        print(value,"of",face_dict[face])
    else:
        print(face_dict[value],"of",face_dict[face])
name(input())
