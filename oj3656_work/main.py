"""Keymidterm"""
def main():
    """key midterm"""
    i = input()
    sum_id = 0
    multiply = int(i[10:]) * 10
    for num in i:
        num = int(num)
        sum_id += num
    key_id = sum_id + multiply
    if len(str(key_id)) > 4:
        key_id = str(key_id)[-4:]
    elif key_id < 1000:
        key_id += 1000
    print(key_id)
main()
