import math

type Coordinates2D = tuple[int, int]
type Coordinates3D = tuple[int, int, int]


def compute_distance(a: Coordinates3D, b: Coordinates3D) -> float:
    x1, y1, z1 = a
    x2, y2, z2 = b

    xDist = (x2 - x1) ** 2
    yDist = (y2 - y1) ** 2
    zDist = (z2 - z1) ** 2

    return math.sqrt(xDist + yDist + zDist)


def compute_area(x: Coordinates2D, y: Coordinates2D) -> int:
    width = abs(x[0] - y[0]) + 1
    height = abs(x[1] - y[1]) + 1

    return width * height
