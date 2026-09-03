"""dice roll"""
g,r = int(input()),int(input())
if (g > 6 or g < 1 ) or (r > 6  or r < 1):
    print("Invalid")
elif g == r:
    print("Correct!")
else:
    print("Wrong!")
