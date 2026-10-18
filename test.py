n = int(input())
l = []

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
for _ in range(n):
    l.append(int(input()))
while l[1]:
    
    l[0] = l[1]
    l[1] = 
print(gcd(a, b))
