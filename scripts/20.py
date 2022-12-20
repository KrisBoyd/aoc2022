from scripts.utility import read_data
from copy import deepcopy


def mix_file(df):
    res = deepcopy(df)
    for j in range(len(df)):
        s = [x for x in res if x[0] == j][0]
        i = res.index(s)
        t = (i + s[1]) % (len(df) - 1)
        t = t if t > 0 else len(df)
        res.pop(i)
        res.insert(t, s)
    return res


def puzzles(data, decryption, times):
    # Part 1 & 2
    res = list(enumerate([s * decryption for s in data]))
    for j in range(times):
        res = mix_file(res)

    res = [x[1] for x in res]
    value = 0
    for j in [1000, 2000, 3000]:
        value += res[(res.index(0) + j) % len(res)]
    print(value)


if __name__ == '__main__':
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=True)
    puzzles(data, decryption=1, times=1)
    puzzles(data, decryption=811589153, times=10)
