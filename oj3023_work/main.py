"""What a Calculator"""
n = int(input())
def cal():
    """1+...+n"""
    press = n
    digit_length = 1
    start =1
    end = 9
    while n >= start:
        if n > 1:
            if n < end:
                num = (n-start)+1
            else:
                num = (end-start)+1
        else:
            num = 0
        press += (num*digit_length)
        digit_length += 1
        start *= 10
        end = (end*10)+9
    print(press)
cal()
