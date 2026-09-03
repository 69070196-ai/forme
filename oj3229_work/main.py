""" ONLINE GAME """
base = int(input())
bonus = int(input())
streak = int(input())
score = base + bonus
rank = 0
badge =0
if streak >=3:
    score *= 1.5
if score >= 1500:
    rank =5
elif score >= 1000:
    rank =4
elif score >= 500:
    rank =3
elif score >= 200:
    rank =2
elif score < 200:
    rank = 1
if rank == 5 and streak >=7:
    badge = 99
elif rank == 4 and bonus > 300:
    badge = 88
print(int(score))
print(rank)
print(badge)
