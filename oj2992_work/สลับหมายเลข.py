"""สลับหมายเลข"""
number = input()
operation = input()

swapnum = number[-1:-3:-1]

number = int(number)
swapnum = int(swapnum)

if operation == "+":
    plus = number + swapnum
    print(f'{number} {operation} {swapnum} = {plus}')
elif operation == "-":
    minous = number - swapnum
    print(f'{number} {operation} {swapnum} = {minous}')
elif operation == "*":
    multiply = number * swapnum
    print(f'{number} {operation} {swapnum} = {multiply}')
elif operation == "/":
    divine = number / swapnum
    print(f'{number} {operation} {swapnum} = {divine}')
