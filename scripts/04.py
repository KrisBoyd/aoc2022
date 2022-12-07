from scripts.utility import read_data


def puzzles(data):
    # Part 1 & 2
    values = [0, len(data)]
    for s in data:
        first, second = s.split(',')
        first = [int(i) for i in first.split('-')]
        second = [int(i) for i in second.split('-')]
        # Part 1
        if first[0] <= second[0] and first[1] >= second[1]:
            values[0] += 1
        elif second[0] <= first[0] and second[1] >= first[1]:
            values[0] += 1
        # Part 2
        if first[1] < second[0] or first[0] > second[1]:
            values[1] -= 1

    print(f'Part 1 = {values[0]}')
    print(f'Part 2 = {values[1]}')


if __name__ == '__main__':
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)
    puzzles(data)
