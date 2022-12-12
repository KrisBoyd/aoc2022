from scripts.utility import read_data



def puzzles(data):
    # Part 1
    program = []
    for s in data:
        program.append(0)
        if s != 'noop':
            program.append(int(s.split(' ')[1]))

    cycles = [40*s-20 for s in range(1, 7)]
    total = [(1+sum(program[:(s-1)])) * s for i, s in enumerate(cycles)]
    print(sum(total))

    # Part 2
    sprites = [1 + sum(program[:i]) for i, s in enumerate(program)]
    pixels = ['' for c in cycles]
    for i, s in enumerate(sprites):
        row = i // 40
        col = i % 40
        if abs(s - col) <= 1:
            pixels[row] += '#'
        else:
            pixels[row] += '.'

    [print(s) for s in pixels]


if __name__ == '__main__':
    day = __file__.split('/')[-1].split('.')[0]
    data = read_data(f'data/{day}.txt', integer=False)
    puzzles(data)
