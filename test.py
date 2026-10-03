l = []
shorten = []
while True:
    num = int(input())
    if num == -1 :
        break
    l.append(num)
if l:
    start = l[0]
    previous = l[0]
    for num in l[1:]:
        if previous == num-1:
            previous = num
        else:
            if start == previous:
                shorten.append(start)
            else:
                shorten.append(str(start)+"-"+str(previous))
            start = num
            previous = num
    if start == previous:
        shorten.append(start)
    else:
        shorten.append(str(start)+"-"+str(previous))
print(*shorten,sep=", ")
