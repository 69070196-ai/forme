"""Put in the box"""
W, L, M, N = map(int,input().split())
horizontalLine = M * (W // M)
horizontalArea = horizontalLine * L
verticalLine = M * (L // M)
verticalArea = verticalLine * abs(horizontalLine - W)
left = abs((verticalArea + horizontalArea) - (W * L))
for i in range(M+1,N+1):
    horizontalLine = i *(W // i)
    horizontalArea = horizontalLine * L
    verticalLine = i *(L // i)
    verticalArea = verticalLine * abs(horizontalLine - W)
    left2 = abs((horizontalArea + verticalArea) - (W * L))
    if left2 < left:
        left = left2
print(left)
