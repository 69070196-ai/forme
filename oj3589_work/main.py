"""Fibonacci V1"""
def fibonacci_v1(num):
    """fibonacci func 1"""
    if not num :
        return 0
    if num == 1 :
        return 1
    return fibonacci_v1(num - 1) + fibonacci_v1(num - 2)
print(fibonacci_v1(int(input())))
