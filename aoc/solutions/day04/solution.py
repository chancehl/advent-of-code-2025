from aoc.common.timer import timed

type WrappingPaperGrid = list[list[str]]
type Coordinates = tuple[int, int]


@timed
def part_one(input_txt: str) -> int:
    grid = make_grid(input_txt)

    movable_rolls = 0

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[y][x] == "@" and is_movable_roll(grid, (x, y)):
                movable_rolls += 1

    return movable_rolls


@timed
def part_two(input_txt: str) -> int:
    return -1


def make_grid(input: str) -> WrappingPaperGrid:
    grid = []

    lines = input.splitlines()

    for line in lines:
        row = list(line)
        grid.append(row)

    return grid


def is_movable_roll(grid: WrappingPaperGrid, coords: Coordinates) -> bool:
    surrounding_rolls = 0

    x, y = coords

    left = (x - 1, y)
    right = (x + 1, y)

    up = (x, y - 1)
    down = (x, y + 1)

    up_left = (x - 1, y - 1)
    up_right = (x + 1, y - 1)

    down_right = (x + 1, y + 1)
    down_left = (x - 1, y + 1)

    to_check = [left, right, up, down, up_left, up_right, down_right, down_left]

    for node in to_check:
        if get_node(grid, node) == "@":
            surrounding_rolls += 1

            if surrounding_rolls >= 4:
                return False

    return True


def get_node(grid: WrappingPaperGrid, coords: Coordinates) -> str | None:
    x, y = coords

    if x < 0 or x > len(grid[0]) - 1 or y < 0 or y > len(grid) - 1:
        return None

    return grid[y][x]
