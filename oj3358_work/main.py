"""Fat Pig"""
pig_amount = int(input())
weight = input().split()
more = []
for i in range(1, pig_amount + 1):
    if int(weight[2 * (i - 1)]) > int(weight[(2 * (i - 1)) + 1]):
        more.append(int(weight[2 * (i - 1)]))
    else:
        more.append(int(weight[(2 * (i - 1)) + 1]))
if len(more) > 1:
    print(*more,sep=" + ",end=" = ")
print(sum(more))
