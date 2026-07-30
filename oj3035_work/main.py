"""Filter TT"""
r,x,y = map(int,(input().split()))
pigud = x**2+y**2
if pigud < r**2:
    print("IN")
elif pigud == r**2:
    print("ON")
elif pigud > r**2:
    print("OUT")
