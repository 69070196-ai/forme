"""ID TWINS"""
N = int(input())
id_1 = int(input())
id_2 = int(input())
check = "YES"
notimes = 0
for i in range(N):
    if int(str(id_1)[i])+int(str(id_2)[i]) != 9:
        check = "NO"
        notimes += 1
print(check,end="")
if notimes:
    print(f" {notimes}")
