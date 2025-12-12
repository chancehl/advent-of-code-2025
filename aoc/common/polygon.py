from aoc.common.euclid import Coordinates2D


# I wrote this class originally, but it was insanely inefficient
class Polygon:
    def __init__(self, coords: list[Coordinates2D], filled: bool = False) -> None:
        self._corners = coords
        self._filled = filled

        # row_bounds maps y -> (min_x, max_x) for that row (inclusive)
        self._row_bounds: dict[int, tuple[int, int]] = {}
        # for non-filled shapes, store explicit perimeter points for exact containment checks
        self._perimeter: set[Coordinates2D] = set()

        self.build_polygon(coords, filled)

    def build_polygon(self, coords: list[Coordinates2D], filled: bool = False) -> None:
        if not coords:
            return

        # Build min/max for rows (y) and columns (x) from corner coords
        y_axis: dict[int, list[int]] = {}
        x_axis: dict[int, list[int]] = {}

        for x, y in coords:
            y_axis.setdefault(y, []).append(x)
            x_axis.setdefault(x, []).append(y)

        # For each y present in corners, horizontal span from min_x to max_x
        horizontal_spans: dict[int, set[int]] = {}
        for y, xs in y_axis.items():
            min_x = min(xs)
            max_x = max(xs)
            horizontal_spans[y] = set(range(min_x, max_x + 1))

        # For each x present in corners, vertical span from min_y to max_y
        vertical_spans_by_y: dict[int, set[int]] = {}
        for x, ys in x_axis.items():
            min_y = min(ys)
            max_y = max(ys)
            for y in range(min_y, max_y + 1):
                vertical_spans_by_y.setdefault(y, set()).add(x)

        # Combine spans to form the perimeter points for those rows
        path_xs_by_y: dict[int, set[int]] = {}
        for y, xs in horizontal_spans.items():
            path_xs_by_y.setdefault(y, set()).update(xs)
        for y, xs in vertical_spans_by_y.items():
            path_xs_by_y.setdefault(y, set()).update(xs)

        # If filled, compute continuous interval bounds per row
        if filled:
            for y, xs in path_xs_by_y.items():
                if not xs:
                    continue
                min_x = min(xs)
                max_x = max(xs)
                self._row_bounds[y] = (min_x, max_x)
        else:
            # store explicit perimeter points for exact membership checks
            for y, xs in path_xs_by_y.items():
                for x in xs:
                    self._perimeter.add((x, y))

    def contains(self, a: Coordinates2D, b: Coordinates2D) -> bool:
        smaller_x = min([a, b], key=lambda c: c[0])[0]
        smaller_y = min([a, b], key=lambda c: c[1])[1]

        larger_x = max([a, b], key=lambda c: c[0])[0]
        larger_y = max([a, b], key=lambda c: c[1])[1]

        # iterate rows in the rectangle (note: range is exclusive of larger_x/larger_y
        # to preserve original behavior)
        for inside_y in range(smaller_y, larger_y):
            if self._filled:
                bounds = self._row_bounds.get(inside_y)
                if not bounds:
                    return False
                min_x, max_x = bounds
                if min_x > smaller_x or max_x < (larger_x - 1):
                    return False
            else:
                # exact perimeter membership check
                for inside_x in range(smaller_x, larger_x):
                    if (inside_x, inside_y) not in self._perimeter:
                        return False

        return True
