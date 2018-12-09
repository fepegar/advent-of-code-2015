import hashlib
from pathlib import Path

this_dir = Path(__file__).parent
verbose = True


def p(*args):
    if verbose:
        print(*args)


def read_input(relative_filepath):
    filepath = this_dir / relative_filepath
    lines = filepath.read_text().splitlines()
    if len(lines) == 1:
        lines = lines[0]
    return lines


def get_min_hash_number(key, zeros=5):
    n = 0
    while True:
        string = f'{key}{n}'
        result = hashlib.md5(bytes(string.encode())).hexdigest()
        if result[:zeros] == zeros * '0':
            return n
        n += 1


def part_1(data):
    answer = get_min_hash_number(data)
    return answer


def part_2(data):
    answer = get_min_hash_number(data, 6)
    return answer


if __name__ == "__main__":
    examples = read_input('example.txt')
    data = read_input('input.txt')

    p('Part 1')
    for example in examples:
        example_1 = part_1(example)
        p('Example 1:', example_1)
    answer_1 = part_1(data)
    p('Answer 1:', answer_1)

    p()

    p('Part 2')
    answer_2 = part_2(data)
    p('Answer 2:', answer_2)
