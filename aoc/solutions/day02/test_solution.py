from .solution import is_invalid_id, get_size_range


def test_is_invalid_id():
    assert is_invalid_id(11)
    assert is_invalid_id(99)
    assert is_invalid_id(1010)
    assert is_invalid_id(1158511585)

    assert not is_invalid_id(1)
    assert not is_invalid_id(95)
    assert not is_invalid_id(17)
    assert not is_invalid_id(20202021)


def test_is_invalid_with_chunk_size():
    assert is_invalid_id(11, size=1)
    assert is_invalid_id(111, size=1)
    assert is_invalid_id(123123, size=3)

    assert not is_invalid_id(123123, size=2)


def test_get_size_range():
    assert get_size_range(11) == (1, 1)
    assert get_size_range(1111) == (1, 2)
    assert get_size_range(123123) == (1, 3)
