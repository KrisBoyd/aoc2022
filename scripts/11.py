from scripts.utility import read_data


def puzzles(data):
    monkeys = {}
    for s in data:
        if 'Monkey ' in s:
            monkey = int(s.replace('Monkey ', '')[0])
            monkeys[monkey] = {}
        if 'Starting items' in s:
            monkeys[monkey]['items'] = [int(x) for x in s.strip(' ').replace('Starting items: ', '').split(', ')]
        if 'Operation' in s:
            monkeys[monkey]['operation'] = s.split('old ')[1].replace(' ', '')
            if monkeys[monkey]['operation'] == '*old':
                monkeys[monkey]['operation'] = '**2'
        if 'Test' in s:
            monkeys[monkey]['test'] = int(s.split('by ')[1])
        if 'true' in s:
            monkeys[monkey]['true'] = int(s.split('monkey ')[1])
        if 'false' in s:
            monkeys[monkey]['false'] = int(s.split('monkey ')[1])

    for m in monkeys.keys():
        monkeys[m]['inspect'] = 0

    # Part 1 & 2
    common_divisor = 1
    for m in monkeys.keys():
        common_divisor *= monkeys[m]['test']

    rounds = 10_000   # part 1: 20, part 2: 10_000
    divider = 1       # part 1: 3,  part 2: 1
    for r in range(rounds):
        for m in range(len(monkeys)):
            for i in monkeys[m]['items']:
                monkeys[m]['inspect'] += 1
                worry = int(eval(str(i) + monkeys[m]['operation']) / divider)
                worry = worry % common_divisor

                if (worry // monkeys[m]['test']) == (worry / monkeys[m]['test']):
                    monkeys[monkeys[m]['true']]['items'].append(worry)
                else:
                    monkeys[monkeys[m]['false']]['items'].append(worry)
            monkeys[m]['items'] = []

    {print(f"Monkey {m} inspected items {monkeys[m]['inspect']} times") for m in monkeys.keys()}
    res = sorted([monkeys[m]['inspect'] for m in monkeys.keys()])
    print(res[-2] * res[-1])


if __name__ == '__main__':
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)
    puzzles(data)
