from scripts.utility import read_data
from copy import deepcopy


def puzzles(data):
    data = [[int(x) for x in s.split(',')] for s in data]
    data = [tuple(s) for s in data]

    # Part 1
    surface = len(data) * 6
    for c in data:
        adjacent = [(c[0] + 1, c[1], c[2]),
                    (c[0] - 1, c[1], c[2]),
                    (c[0], c[1] + 1, c[2]),
                    (c[0], c[1] - 1, c[2]),
                    (c[0], c[1], c[2] + 1),
                    (c[0], c[1], c[2] - 1)]
        for a in adjacent:
            if a in data:
                surface -= 1
    print(surface)

    # Part 2
    size_max = max([max(s) for s in data]) + 1
    size_min = min([min(s) for s in data]) - 1

    water_grid = set()
    for x in range(size_min, size_max + 1):
        for y in range(size_min, size_max + 1):
            for z in range(size_min, size_max + 1):
                if (x in [size_min, size_max]) or (x in [size_min, size_max]) or (z in [size_min, size_max]):
                    water_grid.add((x, y, z))

    # Flow water inwards
    surface = 0
    check_grid = deepcopy(water_grid)
    while len(check_grid):
        p = list(check_grid)[0]
        check_grid = check_grid - {p}
        # Flow in all directions
        adjacent = [(p[0] + 1, p[1], p[2]),
                    (p[0] - 1, p[1], p[2]),
                    (p[0], p[1] + 1, p[2]),
                    (p[0], p[1] - 1, p[2]),
                    (p[0], p[1], p[2] + 1),
                    (p[0], p[1], p[2] - 1)]

        for a in adjacent:
            if (a not in water_grid) and (a not in data) and (max(a) <= size_max) and (min(a) >= size_min):
                check_grid.add(a)
                water_grid.add(a)
            if a in data:
                surface += 1
    print(surface)


if __name__ == '__main__':
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)
    puzzles(data)
