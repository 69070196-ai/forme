"""pile of card"""
def card():
    """playing card"""
    face = input()
    cardict = {
        "c":"clubs","s":"spades",
        "h":"hearts","d":"diamonds",
        "a":"ace","j":"jack",
        "q":"queen","k":"king"
    }
    if face.isalpha():
        face = face.lower()
        print(f"{cardict[face[0:-1]]} of {cardict[face[-1]]}")
    else:
        face = face[0:-1]+face[-1].lower()
        print(f"{face[0:-1]} of {cardict[face[-1]]}")
card()
