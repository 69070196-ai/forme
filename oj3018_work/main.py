"""square overlapping"""
x1,y1,w1,h1 = map(int,(input().split()))
x2,y2,w2,h2 = map(int,(input().split()))
x12 = x1+w1
y12 = y1+h1
x22 = x2+w2
y22 = y2+h2
ow = min(x12,x22) - max(x1,x2)
oh = min(y12,y22) - max(y1,y2)
if ow > 0 and oh > 0:
    print(ow*oh)
else:
    print("no overlapping")
