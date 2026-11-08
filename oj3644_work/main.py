"""RNG"""
import json
def main():
    """ RNG """
    arr = json.loads(input())
    sum_arr = []
    val = int(input())
    skip = int(input())
    place = 0
    for i in range(255//2):
        combination = 0
        for j in range(i, i+((val*skip)-1), skip):
            position = j % 256
            combination += arr[position]
        sum_arr.append(combination)
    print(max(sum_arr))
main()
