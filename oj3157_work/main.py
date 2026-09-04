"""point collect"""
N = int(input())
point = 0
plusorminus = 0
for i in range(N):
    plusorminus = input()
    if plusorminus == "+":
        point += 10
    elif plusorminus == "-":
        point -= 5
print(point)
