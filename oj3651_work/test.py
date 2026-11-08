"""Diginity_Midterm2014"""

def main():
    """Main Function"""
    while True:
        num = input()
        if not int(num):
            break

        while len(num) >= 2:
            total = 0
            for n in num:
                total += int(n)
            num = str(total)

        print(num)

main()