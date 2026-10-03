"""BigFrame"""
a, b , c, d, e = input().strip(), input().strip(), input().strip(), input().strip(), input().strip()
mylist = [len(a), len(b), len(c), len(d), len(e)]
Mlist = max(mylist[:])
print("*" * (4 + Mlist))
print(f"* {a}{" "* abs(len(a) - Mlist)} *")
print(f"* {b}{" "* abs(len(b) - Mlist)} *")
print(f"* {c}{" "* abs(len(c) - Mlist)} *")
print(f"* {d}{" "* abs(len(d) - Mlist)} *")
print(f"* {e}{" "* abs(len(e) - Mlist)} *")
print("*" * (4 + Mlist))
