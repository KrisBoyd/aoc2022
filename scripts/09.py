from scripts.utility import read_data


def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1


def puzzles(data):
    # Part 1
    positions = []
    head = [0, 0]
    tail = [0, 0]
    for s in data:
        for i in range(int(s.split(' ')[1])):
            head_old = head.copy()
            if s[0] == 'R':
                head[0] += 1
            if s[0] == 'L':
                head[0] -= 1
            if s[0] == 'U':
                head[1] += 1
            if s[0] == 'D':
                head[1] -= 1

            if (abs(head[0] - tail[0]) > 1) or (abs(head[1] - tail[1]) > 1):
                tail = head_old.copy()

            positions.append(tuple(tail))

    print(len(set(positions)))

    # Part 2
    positions = []
    knots = [[0, 0] for s in range(10)]
    for s in data:
        for i in range(int(s.split(' ')[1])):
            if s[0] == 'R':
                knots[0][0] += 1
            if s[0] == 'L':
                knots[0][0] -= 1
            if s[0] == 'U':
                knots[0][1] += 1
            if s[0] == 'D':
                knots[0][1] -= 1

            # Update tails
            for j, tail in enumerate(knots[1:]):
                head = knots[j].copy()
                if (abs(head[0] - tail[0]) > 1) or (abs(head[1] - tail[1]) > 1):
                    if head[0] == tail[0]:  # Vertical
                        tail[1] = (head[1] + tail[1]) // 2
                    elif head[1] == tail[1]:  # Horizontal
                        tail[0] = (head[0] + tail[0]) // 2
                    elif (abs(head[0] - tail[0]) == 2) and (abs(head[1] - tail[1]) == 2):  # Diagonal
                        tail[0] = (head[0] + tail[0]) // 2
                        tail[1] = (head[1] + tail[1]) // 2
                    else:  # Horsey
                        tail[0] += sign((head[0] - tail[0]))
                        tail[1] += sign((head[1] - tail[1]))
                    knots[j+1] = tail.copy()
                if j == 8:  # j = 0 gives solution for Part 1
                    positions.append(tuple(tail))

    print(len(set(positions)))


if __name__ == '__main__':
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)
    puzzles(data)
