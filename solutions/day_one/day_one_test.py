from solutions.day_one.day_one import make_lists


def test_make_lists():
    input = ["1   2", "3   4", "5   6"]
    result = make_lists(input)

    assert result == [[1, 3, 5], [2, 4, 6]]
