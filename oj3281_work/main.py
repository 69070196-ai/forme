"""ijudge-kmitl"""
def main():
    """URL CHECK"""
    url = input()
    valid = "https://ijudge.it.kmitl.ac.th/problems/"
    if url[:len(valid)] == valid:
        num = url
        if url[-1] == "/":
            num_id = num[-5:-1]
        else:
            num_id = num[-4:]
        num_id_ok = num_id.isdigit()
        if num_id_ok:
            if num_id[0] == "0":
                print("0 STAR")
            elif num_id[0] == "1":
                print("1 STAR")
            elif num_id[0] == "2":
                print("2 STAR")
            elif num_id[0] == "3":
                print("3 STAR")
            else:
                print("INVALID")
        else:
            print("INVALID")
    else:
        print("INVALID")
main()
