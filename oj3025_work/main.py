"""SEASON CALCULATOR"""
month = int(input())
date = int(input())
def season():
    """ season condition """
    if month in [1,2]:
        print("winter")
    elif month in [4,5]:
        print("spring")
    elif month in [7,8]:
        print("summer")
    elif month in [10,11]:
        print("fall")
    elif month == 3 and date < 21:
        print("winter")
    elif month == 3 and date >=21:
        print("spring")
    elif month == 6 and date < 21:
        print("spring")
    elif month == 6 and date >=21:
        print("summer")
    elif month == 9 and date < 21:
        print("summer")
    elif month == 9 and date >=21:
        print("fall")
    elif month == 12 and date <21:
        print("fall")
    elif month == 12 and date >=21:
        print("winter")
season()
