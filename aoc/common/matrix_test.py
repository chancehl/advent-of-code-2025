from aoc.common.matrix import make_matrix


def test_make_matrix_handles_square_matrices():
    input = """
        1 2 3
        4 5 6
        7 8 9
    """

    expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    actual = make_matrix(input)

    assert expected == actual


def test_make_matrix_handles_non_square_matrices():
    input = """
        1 2
        4 5
        7 8
    """

    expected = [[1, 2], [4, 5], [7, 8]]
    actual = make_matrix(input)

    assert expected == actual


def test_make_matrix_handles_empty_input():
    input = ""

    expected = []
    actual = make_matrix(input)

    assert expected == actual
