"""sanyalak"""
N = int(input())
for i in range(1,N+1):
    if i % 5 > 0:
        print("*",end="")
    elif not i%5:
        print("X",end="")
