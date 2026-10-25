num = int(input())
for i in range(2,num):
    for j in range(2,int(i**0.5)+1):
        print(i, j)
