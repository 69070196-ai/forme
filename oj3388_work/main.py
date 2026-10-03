"""113 HATERS"""
string = input()
numbers = list(string)
while "113" in string:
    for i, _ in enumerate(numbers):
        num = numbers[i]
        right = numbers[i+1] if i+1 < len(numbers) else ""
        rightright = numbers[i+2] if i+2 < len(numbers) else ""
        if num != "1":
            continue
        if num+right+rightright == "113":
            numbers.pop(i)
            numbers.pop(i)
            numbers.pop(i)
    string = "".join(str(num) for num in numbers)
print(*numbers,sep="")
