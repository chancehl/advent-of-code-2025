from .solution import is_invalid_id


def test_is_invalid_id():
    assert is_invalid_id(11)
    assert is_invalid_id(99)
    assert is_invalid_id(1010)
    assert is_invalid_id(1158511585)

    assert not is_invalid_id(95)
    assert not is_invalid_id(17)
    assert not is_invalid_id(20202021)
