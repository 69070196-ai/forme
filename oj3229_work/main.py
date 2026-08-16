"""inflation"""
P = float(input())
n = int(input())
A = P*((1+0.0381)**n)
print(int(A*100)/100)
