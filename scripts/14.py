from scripts.utility import read_data

def puzzles(data):
    # Parse data
    rocks = set()
    for s in data:
        s = [eval(f'[{x}]') for x in s.split(' -> ')]
        for i in range(1, len(s)):
            x = sorted([s[i-1][0], s[i][0]])
            y = sorted([s[i-1][1], s[i][1]])
            for a in range(x[0], x[1] + 1):
                for b in range(y[0], y[1] + 1):
                    rocks.add((a, b))

    # Part 1
    abyss = max([r[1] for r in rocks])
    sand_rocks = rocks.copy()
    start = (500, 0)
    end = False
    while not end:
        p = start
        while True:
            if p[1] >= abyss:
                end = True
                break
            if (p[0], p[1] + 1) not in sand_rocks:
                p = (p[0], p[1] + 1)
            elif (p[0] - 1, p[1] + 1) not in sand_rocks:
                p = (p[0] - 1, p[1] + 1)
            elif (p[0] + 1, p[1] + 1) not in sand_rocks:
                p = (p[0] + 1, p[1] + 1)
            else:
                sand_rocks.add(p)
                break
    print(len(sand_rocks) - len(rocks))

    # Part 2
    floor = max([r[1] for r in rocks]) + 2
    sand_rocks = rocks.copy()
    start = (500, 0)
    end = False
    while not end:
        p = start
        while True:
            if p[1] >= floor:
                rocks.add(p)  # Sand on the floor is actually rock
                sand_rocks.add(p)
                break
            if (p[0], p[1] + 1) not in sand_rocks:
                p = (p[0], p[1] + 1)
            elif (p[0] - 1, p[1] + 1) not in sand_rocks:
                p = (p[0] - 1, p[1] + 1)
            elif (p[0] + 1, p[1] + 1) not in sand_rocks:
                p = (p[0] + 1, p[1] + 1)
            elif p not in sand_rocks:
                sand_rocks.add(p)
                break
            else:
                end = True
                break
    print(len(sand_rocks) - len(rocks))







if __name__ == '__main__':
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)
    puzzles(data)
