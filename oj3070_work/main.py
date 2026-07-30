"""odd or even"""
a = int(input())%2
b = int(input())%2
c = int(input())%2
mylist = [a,b,c]
even = 0
odd = 0
for i in mylist:
    if not i:
        even +=1
    else:
        odd +=1
print(even)
print(odd)
