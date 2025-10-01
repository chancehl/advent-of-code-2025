def make_matrix(input: str) -> list[list[int]]:
    matrix = []

    for line in input.strip().splitlines():
        values = []

        for value in line.strip().split():
            values.append(int(value))

        matrix.append(values)

    return matrix
