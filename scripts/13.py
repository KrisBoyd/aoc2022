from scripts.utility import read_data
from collections import defaultdict


def compare(left, right):
    if type(left) != type(right):
        left = left if type(left) is list else [left]
        right = right if type(right) is list else [right]

    if type(left) is list and type(right) is list:
        for i in range(min(len(left), len(right))):
            result = compare(left[i], right[i])
            if result is not None:
                return result
        if len(left) < len(right):
            return True
        elif len(left) > len(right):
            return False

    if type(left) is int and type(right) is int:
        if left < right:
            return True
        elif left > right:
            return False


def puzzles(data):
    # Part 1
    pairs = {}
    for i in range((len(data)+1)//2):
        left = data[i * 2]
        right = data[i * 2 + 1]
        pairs[i+1] = compare(left, right)

    print(sum([k for k, v in pairs.items() if v]))

    # Part 2 - Count numbers below dividers
    order = defaultdict(int)
    for left in [[[2]], [[6]]]:
        for i, right in enumerate(data):
            if not compare(left, right):
                order[str(left)] += 1

    print((order['[[2]]'] + 1) * (order['[[6]]'] + 1 + 1))


if __name__ == '__main__':
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)
    data = [eval(s) for s in data if s != '']
    puzzles(data)
