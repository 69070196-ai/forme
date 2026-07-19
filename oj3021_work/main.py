"""circle overlapping check"""
x1 = int(input())
y1 = int(input())
r1 = int(input())
x2 = int(input())
y2 = int(input())
r2 = int(input())
def main():
    """this f is cal between two point and sum radius"""
    d = (x2-x1)**2+(y2-y1)**2
    sum_r = (r1+r2)**2
    if d < sum_r:
        print("overlapping")
    else:
        print("no overlapping")
main()
