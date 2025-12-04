from utils.dedent import dedent
from .solution import part_one, part_two


def test_part_one_basic_example():
    example_input = """
        L68
        L30
        R48
        L5
        R60
        L55
        L1
        L99
        R14
        L82
    """

    expected = 3
    (result, _) = part_one(dedent(example_input))

    assert expected == result


def test_part_two_basic_example():
    example_input = """
        L68
        L30
        R48
        L5
        R60
        L55
        L1
        L99
        R14
        L82
    """

    expected = 6
    (result, _) = part_two(dedent(example_input))

    assert expected == result


def test_part_two_edge_case():
    example_input = """
        R50
        L50
    """

    expected = 1
    (result, _) = part_two(dedent(example_input))

    assert expected == result
