"""little rabbit wanna eat boba"""
boba,gram = input().strip().split()
tea,sweetness,V = input().strip().split()
calories = 0
if boba == "H":
    calories += 5*float(gram)
elif boba == "O":
    calories += 3*float(gram)
elif boba == "J":
    calories += 2*float(gram)
if tea == "R":
    if sweetness == "1":
        calories += 12*float(V)
    elif sweetness == "2":
        calories += 18*float(V)
    elif sweetness == "3":
        calories += 25*float(V)
if tea == "T":
    if sweetness == "1":
        calories += 15*float(V)
    elif sweetness == "2":
        calories += 20*float(V)
    elif sweetness == "3":
        calories += 30*float(V)
if tea == "M":
    if sweetness == "1":
        calories += 10*float(V)
    elif sweetness == "2":
        calories += 15*float(V)
    elif sweetness == "3":
        calories += 20*float(V)
print(int(round(calories)))
