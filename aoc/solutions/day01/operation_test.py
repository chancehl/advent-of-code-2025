from .operation import Operation

def test_get_next_value():
    # left with no overflow
    assert Operation("L10").get_next_value(50) == 40
    # left with overflow
    assert Operation("L60").get_next_value(50) == 90
    # right with no overflow
    assert Operation("R15").get_next_value(50) == 65
    # right with overflow
    assert Operation("R60").get_next_value(50) == 10

def test_get_passes():
    # left with no overflow
    assert Operation("L10").get_passes(50) == 0
    # left with single overflow past 0
    assert Operation("L10").get_passes(5) == 1
    # left with single overflow on 0
    assert Operation("L10").get_passes(10) == 1
    # left with multi overflow past 0
    assert Operation("L250").get_passes(30) == 3
    # left with multi overflow on 0
    assert Operation("L500").get_passes(0) == 5
    # left starting at 0
    assert Operation("L10").get_passes(0) == 0

    # right with no overflow
    assert Operation("R10").get_passes(50) == 0
    # right with single overflow past 0
    assert Operation("R10").get_passes(95) == 1
    # right with single overflow on 0
    assert Operation("R10").get_passes(90) == 1
    # right with multi overflow past 0
    assert Operation("R250").get_passes(60) == 3
    # right with multi overflow on 0
    assert Operation("R500").get_passes(0) == 5
    # right starting at 0
    assert Operation("R10").get_passes(0) == 0