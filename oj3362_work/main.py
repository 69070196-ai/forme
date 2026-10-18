
"""Rabbit Love"""

def extend_name(name, targets):
    """extend name"""
    original = name
    i = 0

    while len(name) < targets:
        name += original[i]
        i = (i + 1) % len(original)

    return name


name1 = input().strip()
name2 = input().strip()

target = max(len(name1), len(name2))

name1 = extend_name(name1, target)
name2 = extend_name(name2, target)

result = ""

for a, b in zip(name1, name2):
    if a.lower() in "love" or b.lower() in "love":
        result += "w"
    else:
        result += "$"

COUNT_W = result.count("w")
max_streak = 0
current_streak = 0

for char in result:
    if char == "w":
        current_streak += 1
        max_streak = max(max_streak, current_streak)
    else:
        current_streak = 0

if COUNT_W % 2 == 1:
    result += str(max_streak)
elif max_streak < 2:
    result += "#"

print(result)
