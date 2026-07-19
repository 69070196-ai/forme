"""safe password check"""
alpha = input()
integer = input()
def main():
    """function"""
    password = ["H", "4567"]
    if [alpha,integer] == password:
        print("safe unlocked")
    elif alpha == password[0]:
        print("safe locked - change digit")
    elif integer == password[1]:
        print("safe locked - change char")
    else:
        print("safe locked")
main() 
