"""FAT RABBIT"""
n = int(input())
fat = []
fatty = []
for _ in range(n):
    fat.append(input().split())
mostfat_kg = int(fat[0][1])
mostfat_name = fat[0][0]
for _,y in enumerate(fat):
    if int(y[1]) > 15:
        fatty.append(y)
    if mostfat_kg < int(y[1]):
        mostfat_kg = int(y[1])
        mostfat_name = y[0]
print(len(fatty))
print(mostfat_name)
