from scripts.utility import read_data
from copy import deepcopy


def puzzles(data):
    # Format
    stack_list = data[:(data.index('')-1)]
    n = (len(stack_list[0])+1)//4

    start = {(i+1): [] for i in range(n)}
    for crates in reversed(stack_list):
        for i in range(n):
            crate = crates[(i*4)+1]
            if crate != ' ':
                start[i+1] += crate

    commands = data[(data.index('')+1):]

    # Part 1
    stacks = deepcopy(start)
    for c in commands:
        c = [s for s in c.split(' ')]
        for i in range(int(c[1])):  # Move i times
            crate = stacks[int(c[3])].pop()  # Remove
            stacks[int(c[5])] += crate       # Add

    message = ''.join([s[-1] for s in stacks.values()])
    print(f'Part 1 = {message}')

    # Part 2
    stacks = deepcopy(start)
    for c in commands:
        c = [s for s in c.split(' ')]
        i = int(c[1])  # Move i times
        crates = stacks[int(c[3])][-i:]  # Select crates
        stacks[int(c[3])] = stacks[int(c[3])][:-i]  # Remove
        stacks[int(c[5])] += crates  # Add

    message = ''.join([s[-1] for s in stacks.values()])
    print(f'Part 2 = {message}')


if __name__ == '__main__':
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)
    puzzles(data)
