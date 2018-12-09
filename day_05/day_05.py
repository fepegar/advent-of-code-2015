import re
from pathlib import Path

this_dir = Path(__file__).parent
verbose = True


def p(*args):
    if verbose:
        print(*args)


def read_input(relative_filepath):
    filepath = this_dir / relative_filepath
    return filepath.read_text().splitlines()


def has_three_vowels(string):
    vowels = 0
    for vowel in 'aeiou':
        vowels += string.count(vowel)
        if vowels >= 3:
            nice = True
            break
    else:
        nice = False
    return nice


def has_two_in_a_row(string):
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            nice = True
            break
    else:
        nice = False
    return nice


def contains_bad(string):
    BAD = (
        'ab',
        'cd',
        'pq',
        'xy',
    )
    for bad in BAD:
        if bad in string:
            is_bad = True
            break
    else:
        is_bad = False
    return is_bad


def contains_sandwich(string):
    for i in range(2, len(string)):
        if string[i] == string[i - 2]:
            nice = True
            break
    else:
        nice = False
    return nice


def contains_pairs(string):
    for i in range(0, len(string) - 1):
        pattern = string[i:i + 2]
        matches = len([m.start() for m in re.finditer(pattern, string)])
        if matches > 1:
            nice = True
            break
    else:
        nice = False
    return nice


def is_nice(string, naive):
    if naive:
        vowels = has_three_vowels(string)
        two = has_two_in_a_row(string)
        bad = contains_bad(string)
        nice = vowels and two and not bad
    else:
        pairs = contains_pairs(string)
        sandwich = contains_sandwich(string)
        nice = pairs and sandwich
    return nice


def count_nice_strings(strings, naive=True):
    nice = (is_nice(string, naive=naive) for string in strings)
    return sum(nice)


def part_1(data):
    answer = count_nice_strings(data)
    return answer


def part_2(data):
    answer = count_nice_strings(data, naive=False)
    return answer


if __name__ == "__main__":
    example = read_input('example.txt')
    data = read_input('input.txt')

    p('Part 1')
    example_1 = part_1(example)
    p('Example 1:', example_1)
    answer_1 = part_1(data)
    p('Answer 1:', answer_1)

    p()

    p('Part 2')
    example_2 = part_2(read_input('example_2.txt'))
    p('Example 2:', example_2)
    answer_2 = part_2(data)
    p('Answer 2:', answer_2)
