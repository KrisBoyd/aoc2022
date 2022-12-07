from scripts.utility import read_data


def puzzles(data, length):
    for i in range(length - 1, len(data)):
        if len(set(data[(i-length+1):(i+1)])) == length:
            print(i+1)
            break


if __name__ == '__main__':
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)[0]
    puzzles(data, 4)
    puzzles(data, 14)
