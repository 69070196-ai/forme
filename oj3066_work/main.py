"""ALL THE SAME"""
a = int(input())
b = int(input())
c = int(input())
if a==b==c:
    print("all the same")
elif a != b != c != a:
    print("all different")
elif a == b != c or a == c != b or c == b != a:
    print("neither")
