"""Triangle"""
tri = int(input())
for i in range(1,tri+1):
    if i < 3 or (i>=3 and i == tri):
        print("0"*i)
    elif i >= 3 and i != tri:
        print(f"0{"1"*(i-2)}0")
