from scripts.utility import read_data
from collections import defaultdict

def puzzles(data):
    print(data)


if __name__ == '__main__':
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)
    puzzles(data)
