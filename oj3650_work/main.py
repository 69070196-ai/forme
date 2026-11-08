"""BookWorm"""
def main():
    """best efficients book reader"""
    amount = int(input())
    time = []
    book_list = []
    book_amount = []
    for _ in range(amount):
        times = float(input())
        book = int(input())
        for _ in range(book):
            book_list.append(float(input()))
        book_amount.append(book)
        time.append(times)
    first = 0
    for i in range(amount):
        first_list = book_list[first:first+book_amount[i]]
        first_list.sort()
        combination = 0
        book_read = 0
        for j in first_list:
            num = j

            if (num + combination) > time[i]:
                break
            combination += num
            book_read += 1
        first += book_amount[i]
        print(book_read)
main()
