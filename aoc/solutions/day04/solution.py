from aoc.common.timer import timed

type WrappingPaperGrid = list[list[str]]
type Coordinates = tuple[int, int]


@timed
def part_one(input_txt: str) -> int:
    grid = make_grid(input_txt)

    movable_rolls = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[col][row] == "@" and is_movable_roll(grid, (row, col)):
                movable_rolls += 1

    return movable_rolls


@timed
def part_two(input_txt: str) -> int:
    grid = make_grid(input_txt)

    count = 0

    while True:
        removable_rolls = get_removable_rolls(grid)

        if len(removable_rolls) == 0:
            break

        count += len(removable_rolls)

        for row, col in removable_rolls:
            grid[col][row] = "."

    return count


def make_grid(input: str) -> WrappingPaperGrid:
    grid = []

    lines = input.splitlines()

    for line in lines:
        grid.append(list(line))

    return grid


def is_movable_roll(grid: WrappingPaperGrid, coords: Coordinates) -> bool:
    surrounding_rolls = 0

    row, col = coords

    left = (row - 1, col)
    right = (row + 1, col)

    up = (row, col - 1)
    down = (row, col + 1)

    up_left = (row - 1, col - 1)
    up_right = (row + 1, col - 1)

    down_right = (row + 1, col + 1)
    down_left = (row - 1, col + 1)

    to_check = [left, right, up, down, up_left, up_right, down_right, down_left]

    for node in to_check:
        if get_node(grid, node) == "@":
            surrounding_rolls += 1

            if surrounding_rolls >= 4:
                return False

    return True


def get_node(grid: WrappingPaperGrid, coords: Coordinates) -> str | None:
    row, col = coords

    if row < 0 or row > len(grid[0]) - 1 or col < 0 or col > len(grid) - 1:
        return None

    return grid[col][row]


def get_removable_rolls(grid: WrappingPaperGrid) -> list[Coordinates]:
    coords = []

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[col][row] == "@" and is_movable_roll(grid, (row, col)):
                coords.append((row, col))

    return coords
