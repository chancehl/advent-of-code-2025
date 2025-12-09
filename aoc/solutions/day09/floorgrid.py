from aoc.common.euclid import Coordinates2D


class FloorGrid:
    def __init__(self, coords: list[Coordinates2D]) -> None:
        self._coords = coords

        # we pad both of these by 2 like in the example so we always
        # have some extra space on the sides. this is for cosmetic purposes
        # only and does not actually affect the calculations
        width = max(coords, key=lambda c: c[0])[0] + 2
        height = max(coords, key=lambda c: c[1])[1] + 2

        self._grid = [["." for _ in range(0, width)] for _ in range(0, height)]

        for x, y in coords:
            self._grid[y][x] = "X"

    def is_red_tile(self, coord: Coordinates2D) -> bool:
        return coord in self._coords

    def is_green_tile(self, coord: Coordinates2D) -> bool:
        # check verticals
        row = self.get_row(coord[1])
        print(row)

        col = self.get_col(coord[0])
        print(col)

        # check horizontals
        return False

    def get_row(self, n: int) -> list[str]:
        return self._grid[n]

    def get_col(self, n: int) -> list[str]:
        col = []
        for i in range(0, len(self._grid)):
            col.append(self._grid[i][n])
        return col

    def print(self):
        s = ""
        for row in self._grid:
            for col in row:
                s += col
            s += "\n"
        print(s)
