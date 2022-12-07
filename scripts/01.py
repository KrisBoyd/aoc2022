from scripts.utility import read_data


def puzzles(data):
    calories = []
    count = 0
    for s in data:
        if s:
            count += s
        else:
            calories.append(count)
            count = 0

    print(f'Part 1 = {sorted(calories)[-1]}')
    print(f'Part 2 = {sum(sorted(calories)[-3:])}')


if __name__ == '__main__':
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=True)
    puzzles(data)
