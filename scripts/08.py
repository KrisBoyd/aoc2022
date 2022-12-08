from scripts.utility import read_data


def puzzles(data):
    # Part 1
    visible = len(data) * 4 - 4
    for i in range(1, len(data)-1):
        for j in range(1, len(data)-1):
            h = int(data[i][j])
            # Up
            if max([int(data[s][j]) for s in range(i)]) < h:
                visible += 1
                continue
            # Down
            if max([int(data[s][j]) for s in range(i+1, len(data))]) < h:
                visible += 1
                continue
            # Right
            if max([int(data[i][s]) for s in range(j+1, len(data))]) < h:
                visible += 1
                continue
            # Left
            if max([int(data[i][s]) for s in range(j)]) < h:
                visible += 1
                continue
    print(visible)

    # Part 2
    max_score = 0
    for i in range(1, len(data)-1):
        for j in range(1, len(data)-1):
            h = int(data[i][j])
            score = 1
            # Up
            up = [int(data[s][j]) >= h for s in range(i)][::-1]
            score *= ((up.index(True) + 1) if any(up) else len(up))
            # Down
            down = [int(data[s][j]) >= h for s in range(i+1, len(data))]
            score *= ((down.index(True) + 1) if any(down) else len(down))
            # Right
            right = [int(data[i][s]) >= h for s in range(j+1, len(data))]
            score *= ((right.index(True) + 1) if any(right) else len(right))
            # Left
            left = [int(data[i][s]) >= h for s in range(j)][::-1]
            score *= ((left.index(True) + 1) if any(left) else len(left))

            max_score = max(max_score, score)
    print(max_score)


if __name__ == '__main__':
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)
    puzzles(data)
