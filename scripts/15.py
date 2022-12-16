from scripts.utility import read_data


def puzzles(data):
    # Parse
    df = []
    for s in data:
        sx = int(s.split('x=')[1].split(',')[0])
        sy = int(s.split(', y=')[1].split(':')[0])
        bx = int(s.split('x=')[2].split(',')[0])
        by = int(s.split(', y=')[2])
        d = (abs(sx - bx) + abs(sy - by))
        df.append([(sx, sy), (bx, by), d])

    # Part 1
    y = 2000000
    coverage = []
    for s in df:
        r = s[2] - abs(s[0][1] - y)  # Steps left on the row
        if r >= 0:
            for i in range(r + 1):
                coverage.extend([s[0][0] + i, s[0][0] - i])

    # Remove beacons on row
    b = set([s[1][0] for s in df if s[1][1] == y])
    print(len(set(coverage) - set(b)))

    # Part 2
    df.sort(key=lambda x: x[0])  # Sort sensors by x
    y_max = 4000000
    for y in range(y_max + 1):
        coverage = None
        for s in df:
            r = s[2] - abs(s[0][1] - y)  # Steps left on the row
            if r >= 0:
                left = s[0][0] - r
                right = s[0][0] + r
                if not coverage:
                    coverage = [left, right]
                else:  # Check with current coverage
                    coverage[0] = min(coverage[0], left)
                    if left <= (coverage[1] + 1):
                        coverage[1] = max(coverage[1], right)
        if coverage[1] <= y_max:
            print(4000000 * (coverage[1] + 1) + y)
            break


if __name__ == '__main__':
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)
    puzzles(data)
