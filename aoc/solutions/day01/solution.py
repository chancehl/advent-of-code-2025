from aoc.common.timer import timed


@timed
def part_one(input_txt: str) -> int:
    (left, right) = make_lists(input_txt)
    sorted_left = sorted(left)
    sorted_right = sorted(right)

    diff = 0

    for i, value in enumerate(sorted_left):
        diff += abs(value - sorted_right[i])

    return diff


@timed
def part_two(input_txt: str) -> int:
    (left, right) = make_lists(input_txt)

    counts = count_numbers(right)

    similarity = 0

    for number in left:
        if number in counts:
            similarity += number * counts[number]

    return similarity


def count_numbers(numbers: list[int]) -> dict[int, int]:
    counts = {}

    for number in numbers:
        if number in counts:
            counts[number] = counts[number] + 1
        else:
            counts[number] = 1

    return counts


def make_lists(raw_input: str) -> tuple[list[int], list[int]]:
    lines = raw_input.splitlines()

    left = []
    right = []

    for line in lines:
        parts = line.split()

        left.append(int(parts[0]))
        right.append(int(parts[1]))

    return (left, right)
