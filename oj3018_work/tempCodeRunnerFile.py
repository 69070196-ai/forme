"""square overlapping"""
x1,y1,w1,h1 = map(int,(input().split()))
x2,y2,w2,h2 = map(int,(input().split()))
d = (x2-x1)**2+(y2-y1)**2
x12 = x1+w1
y12 = y1+h1
x22 = x2+w2
y22 = y2+h2
ow = max(x1,x2)-min(x12,x22)
oh = max(y1,y2)-min(y12,y22)
if d < (w1+w2)**2 or d < (h1+h2)**2:
    print(ow*oh)
else:
    print("no overlapping")
