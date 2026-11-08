""" Data Spike """
def main():
    """ data spike """
    data = []
    for _ in range(8):
        data_input = int(input())
        data.append(data_input)
    print(max(data))
main()
