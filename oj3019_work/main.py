"""safe password check"""
alpha = input()
integer = input()
check = alpha+integer
def main():
    """function"""
    password = "H4567"
    if check == password:
        print("safe unlocked")
    elif check[0] == password[0]:
        print("safe locked - change digit")
    elif check[1:] == password[1:]:
        print("safe locked - change char")
    else:
        print("safe locked")
main() 
