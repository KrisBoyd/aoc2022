from scripts.utility import read_data


def calculate_score(data, scores):
    total_score = 0
    for r in data:
        total_score += scores[r]
    print(f'Total score = {total_score}')


def puzzles(data):
    # Part 1
    scores = {'AX': 3 + 1,
              'BX': 0 + 1,
              'CX': 6 + 1,
              'AY': 6 + 2,
              'BY': 3 + 2,
              'CY': 0 + 2,
              'AZ': 0 + 3,
              'BZ': 6 + 3,
              'CZ': 3 + 3
              }
    calculate_score(data, scores)

    # Part 2
    scores = {'AX': 0 + 3,
              'BX': 0 + 1,
              'CX': 0 + 2,
              'AY': 3 + 1,
              'BY': 3 + 2,
              'CY': 3 + 3,
              'AZ': 6 + 2,
              'BZ': 6 + 3,
              'CZ': 6 + 1
              }
    calculate_score(data, scores)


if __name__ == '__main__':
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)
    data = [s.replace(' ', '') for s in data]
    puzzles(data)
