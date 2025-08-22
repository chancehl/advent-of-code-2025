from solutions.day_one.day_one import make_lists


def test_make_lists():
    assert make_lists(["1   2", "3   4", "5   6"]) == [[1, 3, 5], [2, 4, 6]]
    assert make_lists([]) == [[], []]
    assert make_lists(["1   2"]) == [[1], [2]]
