from scripts.utility import read_data


def puzzles(data):
    # Part 1
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    scores = {s: i + 1 for i, s in enumerate(alphabet)}

    value = 0
    for r in data:
        first = r[:len(r)//2]
        second = r[len(r)//2:]
        shared = set(first).intersection(set(second))
        for s in shared:
            value += scores[s]

    print(f'Part 1 = {value}')

    # Part 2
    value = 0
    for i in range(len(data)//3):
        g = data[3*i:3*(i+1)]
        shared = set(g[0]).intersection(set(g[1]).intersection(set(g[2])))
        for s in shared:
            value += scores[s]

    print(f'Part 2 = {value}')


if __name__ == '__main__':
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)
    puzzles(data)
