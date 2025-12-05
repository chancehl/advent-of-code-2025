from aoc.common.timer import timed

type IngredientRange = tuple[int, int]
type IngredientRanges = list[IngredientRange]


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
    fresh_ids = set()

    for start, end in ranges:
        for i in range(start, end + 1):
            fresh_ids.add(i)

    return len(fresh_ids)


def parse_ranges(input: str) -> IngredientRanges:
    raw = input.split("\n\n")[0]
    processed = []

    for row in raw.splitlines():
        parts = row.split("-")
        processed.append((int(parts[0]), int(parts[1])))

    return processed


def parse_ingredients(input: str) -> list[int]:
    raw = input.split("\n\n")[1]

    return [int(value) for value in raw.splitlines()]


def is_fresh(ingredient: int, ranges: IngredientRanges) -> bool:
    for start, end in ranges:
        if ingredient >= start and ingredient <= end:
            return True

    return False
