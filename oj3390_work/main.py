"""Array 2D"""
notright_row = 0
notright_column = 0
check1 = False
check2 = False
row_array = [[int(i) for i in input().split()], [int(i) for i in input().split()],
             [int(i) for i in input().split()], [int(i) for i in input().split()],
             [int(i) for i in input().split()]]
column_array = list(zip(row_array[0],row_array[1],
                    row_array[2],row_array[3],row_array[4]))
for i, j in enumerate(row_array):
    if sum(j) % 2:
        notright_row = i
        check1 = True
        break
for k, l in enumerate(column_array):
    if sum(l) % 2:
        notright_column = k
        check2 = True
        break
if check1 and check2:
    print(notright_row, notright_column)
else:
    print(-1, -1)
