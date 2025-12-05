from aoc.common.timer import timed
from aoc.common.grid import NEIGHBORS

type WrappingPaperGrid = list[list[str]]
type Coordinates = tuple[int, int]


@timed
def part_one(input_txt: str) -> int:
    grid = make_grid(input_txt)
    return sum(
        1
        for row in range(len(grid))
        for col in range(len(grid[0]))
        if grid[row][col] == "@" and is_movable_roll(grid, (row, col))
    )


@timed
def part_two(input_txt: str) -> int:
    grid = make_grid(input_txt)
    count = 0

    while True:
        removable_rolls = [
            (row, col)
            for row in range(len(grid))
            for col in range(len(grid[0]))
            if grid[row][col] == "@" and is_movable_roll(grid, (row, col))
        ]

        if not removable_rolls:
            break

        count += len(removable_rolls)
        for row, col in removable_rolls:
            grid[row][col] = "."

    return count


def make_grid(input: str) -> WrappingPaperGrid:
    return [list(line) for line in input.splitlines()]


def is_movable_roll(grid: WrappingPaperGrid, coords: Coordinates) -> bool:
    row, col = coords
    surrounding_count = sum(
        1 for dr, dc in NEIGHBORS if get_node(grid, (row + dr, col + dc)) == "@"
    )
    return surrounding_count < 4


def get_node(grid: WrappingPaperGrid, coords: Coordinates) -> str | None:
    row, col = coords
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        return grid[row][col]
    return None
