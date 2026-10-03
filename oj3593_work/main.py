"""fibonacci v2"""
known = {0:0, 1:1, 2:1, 3:2, 4:3, 5:5, 6:8, 7:13, 8:21, 9:34, 10:55}
def fibonacii_v2(num):
    if num in known:
        return known[num]
    result = fibonacii_v2(num - 1) + fibonacii_v2(num - 2)
    known[num] = result
    return result
print(fibonacii_v2(int(input())))
