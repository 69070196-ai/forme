""" Filter """
import json
def main():
    """ filter the pass person """
    input_dict = json.loads(input())
    criterion = float(input())
    pass_id = []
    for i, score in input_dict.items():
        if score >= criterion:
            pass_id.append(i)
    pass_id.sort()
    if pass_id:
        for j in pass_id:
            print(f"{j}\t{input_dict[j]:.2f}")
    else:
        print("Nope")
main()
