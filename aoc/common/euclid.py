import math

type Coordinates3D = tuple[int, int, int]


def compute_distance(a: Coordinates3D, b: Coordinates3D) -> float:
    x1, y1, z1 = a
    x2, y2, z2 = b

    xDist = (x2 - x1) ** 2
    yDist = (y2 - y1) ** 2
    zDist = (z2 - z1) ** 2

    return math.sqrt(xDist + yDist + zDist)
