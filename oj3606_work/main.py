""" Bro know ball """
def centi(num):
    """transfer to centimetre"""
    return num * 10**2

def bounce() :
    """how many bouncing"""
    height = float(input()) * 3 / 5
    bounce_times = 0
    while centi(height) > 1:
        height = height * 3 / 5
        bounce_times += 1
    print(bounce_times)
bounce()
