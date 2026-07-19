"""Letter switch"""
letter = input()

if len(letter) == 5 and letter.isalpha():
    print(letter.lower()[::-1])
else:
    print("no")
