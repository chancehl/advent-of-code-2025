from aoc.common.timer import timed

type IngredientRange = tuple[int, int]


@timed
def part_one(input_txt: str) -> int:
    ranges = parse_ranges(input_txt)
    ingredients = parse_ingredients(input_txt)

    sum = 0

    for ingredient in ingredients:
        if is_fresh(ingredient, ranges):
            sum += 1

    return sum


@timed
def part_two(input_txt: str) -> int:
    ranges = parse_ranges(input_txt)

    # sort the elements first
    ranges.sort(key=lambda r: r[0])

    # use a modified sweep line algorithm for merging the ranges
    merged_ranges = [ranges[0]]
    for start, end in ranges[1:]:
        previous_start, previous_end = merged_ranges[-1]
        if start <= previous_end:
            merged_ranges[-1] = (previous_start, max(end, previous_end))
        else:
            merged_ranges.append((start, end))

    # sum the ranges (start, =end)
    # ex: range 3, 5 -> we want to count 3, 4, and 5.
    fresh_ingredients = 0
    for start, end in merged_ranges:
        total_ingredients = (end + 1) - start
        fresh_ingredients += total_ingredients

    return fresh_ingredients


def parse_ranges(input: str) -> list[IngredientRange]:
    raw = input.split("\n\n")[0]
    processed = []

    for row in raw.splitlines():
        parts = row.split("-")
        processed.append((int(parts[0]), int(parts[1])))

    return processed


def parse_ingredients(input: str) -> list[int]:
    raw = input.split("\n\n")[1]

    return [int(value) for value in raw.splitlines()]


def is_fresh(ingredient: int, ranges: list[IngredientRange]) -> bool:
    for start, end in ranges:
        if ingredient >= start and ingredient <= end:
            return True

    return False


def merge_ranges(ranges: list[IngredientRange]) -> list[IngredientRange]:
    """
    A modified version of a sweep line algorithm for efficiently merging ranges of numbers

    example: [(3,5), (10,14), (16,20), (12,18)] becomes [(3,5), (10,20)]
    """
    ranges.sort(key=lambda r: r[0])
    merged_ranges = [ranges[0]]

    for start, end in ranges[1:]:
        previous_start, previous_end = merged_ranges[-1]
        if start <= previous_end:
            merged_ranges[-1] = (previous_start, max(end, previous_end))
        else:
            merged_ranges.append((start, end))

    return merged_ranges
