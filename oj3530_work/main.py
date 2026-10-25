""" if a is int and a do not a any int b that a % b**2 = 0 thus a is squarefree """
def square():
    """ Square Free or not ? """
    nums = int(input())
    sqfree = 1
    sqfree_check = True

    for i in range(2, nums+1):
        for j in range(2, int(i ** 0.5) + 1):
            j_square = j ** 2

            if not i % j_square:
                sqfree_check = False
                break
        if sqfree_check:
            sqfree += 1

        sqfree_check = True
    print(sqfree)
square()
