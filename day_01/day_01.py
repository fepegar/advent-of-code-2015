"""
Solutions for day 1.
"""

from os.path import dirname, join

UP = '('
DOWN = ')'


def get_floor(steps):
    return steps.count(UP) - steps.count(DOWN)


def get_first_basement(steps):
    floor = 0
    index = 1
    for char in steps:
        if char == UP:
            floor += 1
        elif char == DOWN:
            floor -= 1
        if floor < 0:
            return index
        else:
            index += 1


def main():
    with open(join(dirname(__file__), 'examples1.txt')) as f:
        examples = f.read().splitlines()
    with open(join(dirname(__file__), 'input.txt')) as f:
        steps = f.read()

    print('Part 1')
    for example in examples:
        floor = get_floor(example)
        print('Solution to {}: {}'.format(example, floor))
    solution1 = get_floor(steps)
    print('Solution to part 1: {}'.format(solution1))

    print()

    print('Part 2')
    for example in examples:
        index = get_first_basement(example)
        print('Solution to {}: {}'.format(example, index))
    solution2 = get_first_basement(steps)
    print('Solution to part 2: {}'.format(solution2))


if __name__ == '__main__':
    main()
