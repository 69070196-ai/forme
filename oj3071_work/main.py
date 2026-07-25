"""division"""
A = int(input())
B = int(input())
d = int(input())
r = int(input())
C = A
mylist = []
while C <= B:
    if C % d == r:
        mylist.append(C%d)
    C += 1
print(len(mylist))
