"""line sorting"""
def main():
    """line sorting"""
    lineAmount = int(input())
    message_length = [input() for _ in range(lineAmount)]
    sorted_message = sorted(message_length,key=len )
    for i in sorted_message:
        print(i)
main()
