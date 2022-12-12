from scripts.utility import read_data


def get_value(data, x, y):
    if data[x][y] == 'E':
        return ord('z')
    if data[x][y] == 'S':
        return ord('a')
    return ord(data[x][y])


def puzzles(data):
    end_row = ''.join(data).index('E') // len(data[0])
    end_col = ''.join(data).index('E') % len(data[0])

    steps = [[10_000] * len(s) for s in data]
    steps[end_row][end_col] = 0

    sum_values = 1e12
    while sum_values > sum([sum(s) for s in steps]):
        sum_values = sum([sum(s) for s in steps])
        print(sum_values)
        for i in range(len(data)):
            for j in range(len(data[i])):
                current = get_value(data, i, j)
                # Check left
                if j > 0:
                    value = get_value(data, i, j-1)
                    if value - current <= 1:  # at most one step down
                        steps[i][j] = min(steps[i][j], steps[i][j-1] + 1)
                # Check right
                if j < (len(data[i]) - 1):
                    value =get_value(data, i, j+1)
                    if value - current <= 1:  # at most one step down
                        steps[i][j] = min(steps[i][j], steps[i][j+1] + 1)
                # Check up
                if i > 0:
                    value = get_value(data, i-1, j)
                    if value - current <= 1:  # at most one step down
                        steps[i][j] = min(steps[i][j], steps[i-1][j] + 1)
                # Check down
                if i < (len(data) - 1):
                    value = get_value(data, i+1, j)
                    if value - current <= 1:  # at most one step down
                        steps[i][j] = min(steps[i][j], steps[i+1][j] + 1)

    row = ''.join(data).index('S') // len(data[0])
    col = ''.join(data).index('S') % len(data[0])
    print(f'Minimum steps for {data[row][col]} = {steps[row][col]}')

    # Part 2
    shortest = 1000
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'a':
                shortest = min(shortest, steps[i][j])
    print(shortest)


if __name__ == '__main__':
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)
    puzzles(data)
