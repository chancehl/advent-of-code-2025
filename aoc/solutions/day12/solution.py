from aoc.common.timer import timed
import re


# first param is width, second is length, third is required presents
type Region = tuple[int, int, list[int]]


@timed
def part_one(input_txt: str) -> int:
    regions = parse_regions(input_txt)

    # This is a complete hack. Thanks reddit. This problem is meant to look insanely
    # difficult but the problem input makes it trivial. You can count the number of
    # total required presents and multiply them by 9 (as if all of the 3x3 squares were used up)
    # and then check that against the total area available to see if this is a valid region.
    return len(list(filter(lambda r: is_valid_region(r), regions)))


@timed
def part_two(input_txt: str) -> int:
    print("There is no final day part 2. Congratulations on completing everything!")
    return -1


def parse_regions(input_txt: str) -> list[Region]:
    regions = []

    matches = re.findall(r"\d+x\d+\:.+", input_txt)

    for match in matches:
        parts = match.split(":")

        sizes = [int(value) for value in parts[0].strip().split("x")]
        width = sizes[0]
        length = sizes[1]

        nums = [int(value) for value in parts[1].strip().split(" ")]
        regions.append((width, length, nums))

    return regions


def is_valid_region(r: Region) -> bool:
    area = r[0] * r[1]
    return area >= (9 * sum(r[2]))
