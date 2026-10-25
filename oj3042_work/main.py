"""TEN DIVISION"""
N = int(input())
divideten_list = []
for num in range(N, -1, -1):
    if not num % 10:
        divideten_list.append(num)
print(*divideten_list,sep=" ")
