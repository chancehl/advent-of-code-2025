import os


def read_input():
    path = os.path.join(os.path.dirname(__file__), "example.txt")

    with open(path, "r") as f:
        return [line.strip() for line in f.readlines()]


def part_one(input: list[str]) -> int:
    (left, right) = make_lists(input)

    sorted_left = sorted(left)
    sorted_right = sorted(right)

    diff = 0

    for i in range(len(sorted_left)):
        diff += abs(sorted_left[i] - sorted_right[i])

    return diff


def part_two(input: list[str]) -> int:
    (left, right) = make_lists(input)

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


def make_lists(lines: list[str]) -> tuple[list[int], list[int]]:
    left = []
    right = []

    for line in lines:
        parts = line.split("   ")

        left.append(int(parts[0]))
        right.append(int(parts[1]))

    return [left, right]


if __name__ == "__main__":
    result_one = part_one(input=read_input())
    result_two = part_two(input=read_input())

    print(result_one, result_two)
