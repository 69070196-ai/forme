"""vowels count and  max consececutive count"""
def main():
    """main func"""
    n = int(input())
    message_list = [input() for _ in range(n)]
    for line, i in enumerate(message_list, 1):
        vowels = 0
        consecutive1 = 0
        consecutive2 = 0
        for j in i:
            alpha = j.upper()
            if alpha in "AEIOU":
                vowels += 1
                consecutive2 += 1
            else:
                if consecutive2 > consecutive1:
                    consecutive1 = consecutive2
                consecutive2 = 0
        print(f"Line {line}: vowels = {vowels}, max_consecutive = {consecutive1}")
main()
