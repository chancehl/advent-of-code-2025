from aoc.common.euclid import Coordinates2D


# This is the one I wrote. It works, but it holds the shape in memory and is super inefficient.
# See the file with a similar name in this directory for an optimized version.
class Polygon:
    def __init__(self, coords: list[Coordinates2D], filled: bool = False) -> None:
        self._path = self.build_polygon(coords, filled)
        self._corners = coords

    def build_polygon(
        self, coords: list[Coordinates2D], filled: bool = False
    ) -> list[Coordinates2D]:
        path = []

        y_axis = {}

        sorted_coords = sorted(coords, key=lambda c: c[1])
        for _, y in sorted_coords:
            if y not in y_axis:
                y_axis[y] = list(filter(lambda c: c[1] == y, sorted_coords))

        x_axis = {}

        sorted_coords = sorted(coords, key=lambda c: c[0])
        for x, _ in sorted_coords:
            if x not in x_axis:
                x_axis[x] = list(filter(lambda c: c[0] == x, sorted_coords))

        for y in y_axis:
            largest_x_coord = max(y_axis[y], key=lambda c: c[0])[0]
            smallest_x_coord = min(y_axis[y], key=lambda c: c[0])[0]

            for value in range(smallest_x_coord, largest_x_coord + 1):
                path.append((value, y))

        for x in x_axis:
            largest_y_coord = max(x_axis[x], key=lambda c: c[1])[1]
            smallest_y_coord = min(x_axis[x], key=lambda c: c[1])[1]

            for value in range(smallest_y_coord, largest_y_coord + 1):
                path.append((x, value))

        if filled:
            grouped_y = {}
            for _, y in path:
                if y not in grouped_y:
                    shared_y = list(filter(lambda c: c[1] == y, path))
                    grouped_y[y] = set([coord[0] for coord in shared_y])

            for x in grouped_y:
                max_x = max(grouped_y[x])
                min_x = min(grouped_y[x])

                for value in range(min_x, max_x + 1):
                    if (value, x) not in path:
                        path.append((value, x))

        return path

    def contains(self, x: Coordinates2D, y: Coordinates2D) -> bool:
        smaller_x = min([x, y], key=lambda c: c[0])[0]
        smaller_y = min([x, y], key=lambda c: c[1])[1]

        larger_x = max([x, y], key=lambda c: c[0])[0]
        larger_y = max([x, y], key=lambda c: c[1])[1]

        for inside_x in range(smaller_x, larger_x):
            for inside_y in range(smaller_y, larger_y):
                if (inside_x, inside_y) not in self._path:
                    return False

        return True

    def render(self):
        rows = max(self._path, key=lambda c: c[1])[1] + 1
        cols = max(self._path, key=lambda c: c[0])[0] + 1

        grid = [["." for _ in range(0, cols)] for _ in range(0, rows)]
        for x, y in self._path:
            if (x, y) in self._corners:
                grid[y][x] = "#"
            else:
                grid[y][x] = "X"

        s = ""
        for row in grid:
            for col in row:
                s += col
            s += "\n"
        print(s)
