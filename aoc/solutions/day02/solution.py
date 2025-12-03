from aoc.common.timer import timed
from itertools import batched


@timed
def part_one(input_txt: str) -> int:
    id_ranges = [create_range(value) for value in input_txt.split(",")]

    invalid_sum = 0

    for start, end in id_ranges:
        current = start

        while current <= end:
            if is_invalid_id(current):
                invalid_sum += current

            current += 1

    return invalid_sum


@timed
def part_two(input_txt: str) -> int:
    id_ranges = [create_range(value) for value in input_txt.split(",")]

    invalid_sum = 0

    for start, end in id_ranges:
        current = start

        while current <= end:
            if check_all_sizes(current):
                invalid_sum += current

            current += 1

    return invalid_sum


def create_range(s: str) -> tuple[int, int]:
    parts = s.split("-")

    start = int(parts[0])
    end = int(parts[1])

    return (start, end)


def is_invalid_id(n: int, **kwargs) -> bool:
    chars = str(n)

    chunk_size = kwargs.get("size", len(chars) // 2)
    if chunk_size < 1:
        return False

    batches = batched(chars, chunk_size)
    batches = list(batches)

    return all(batch == batches[0] for batch in batches)


def get_size_range(n: int) -> tuple[int, int]:
    return (1, len(str(n)) // 2)


def check_all_sizes(n: int) -> bool:
    (start, end) = get_size_range(n)

    for i in range(start, end + 1):
        if is_invalid_id(n, size=i):
            return True

    return False
