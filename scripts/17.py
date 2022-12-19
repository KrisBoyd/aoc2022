from scripts.utility import read_data
from copy import deepcopy


def puzzles(data, n):
    gas = data[0]

    # Part 1 & 2
    rocks = [
        [(2, 4), (3, 4), (4, 4), (5, 4)],
        [(3, 4), (3, 5), (3, 6), (2, 5), (4, 5)],
        [(2, 4), (3, 4), (4, 4), (4, 5), (4, 6)],
        [(2, 4), (2, 5), (2, 6), (2, 7)],
        [(2, 4), (2, 5), (3, 5), (3, 4)]
    ]

    g = -1
    fallen = set((s, 0) for s in range(7))
    seen = {}
    for r in range(n):
        # Rock piece
        floor = max(s[1] for s in fallen)
        rock = deepcopy(rocks[r % len(rocks)])
        rock = [(s[0], s[1] + floor) for s in rock]

        while True:
            # Gas
            g += 1
            push = gas[g % len(gas)]
            push = 1 if push == '>' else -1
            new_rock = []
            for p in rock:
                new_rock.append((p[0] + push, p[1]))
            if (min([s[0] for s in new_rock]) < 0) or (max([s[0] for s in new_rock]) > 6) or \
                    (not set(new_rock).isdisjoint(fallen)):
                new_rock = deepcopy(rock)

            # Drop
            drop_rock = []
            for p in new_rock:
                drop_rock.append((p[0], p[1] - 1))

            if not set(drop_rock).isdisjoint(fallen):
                fallen = fallen.union(new_rock)
                break
            else:
                rock = deepcopy(drop_rock)

        # Find repeated situation
        m = max(s[1] for s in fallen)
        top = []
        for x in range(7):
            top.append(max([s[1] for s in fallen if s[0] == x]))
        top = tuple([s - min(top) for s in top])

        pair = (r % len(rocks), g % len(gas), top)
        if pair not in seen.keys():
            seen[pair] = (r, m)
        else:
            rock_heights = {}
            for v in seen.values():
                rock_heights[v[0]] = v[1]

            # Calculate end result
            delta_r = r - seen[pair][0]
            delta_h = m - seen[pair][1]
            print((n // delta_r) * delta_h + rock_heights[n % delta_r - 1])
            break

        if (r + 1) == n:
            print(max(s[1] for s in fallen))


if __name__ == '__main__':
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)
    puzzles(data, n=2022)
    puzzles(data, n=1000000000000)
