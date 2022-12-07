from scripts.utility import read_data
from collections import defaultdict


def puzzles(data):
    print(data)

    files = defaultdict(int)
    current = []
    for c in data:
        if c == '$ ls':
            continue
        if c[:4] == '$ cd':
            if c[5:] == '..':
                current.pop()
            else:
                current.append(c[5:])
        elif c[0:3] != 'dir':
            n = int(c.split(' ')[0])
            for i, s in enumerate(current):
                path = '/'.join(current[0:(i+1)])
                files[path] += n

    # Part 1
    values = 0
    for k, v in files.items():
        if v <= 100_000:
            values += v
    print(values)

    # Part 2
    to_delete = files['/'] - 40_000_000
    best = ('', 1e32)
    for k, v in files.items():
        if (v >= to_delete) and (v <= best[1]):
            best = (k, v)
    print(best)


if __name__ == '__main__':
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)
    puzzles(data)
