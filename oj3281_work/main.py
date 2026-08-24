"""ijudge-kmitl"""
def main():
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
    else:
        print("invalid")
main()
