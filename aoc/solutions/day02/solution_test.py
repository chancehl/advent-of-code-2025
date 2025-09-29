import pytest
from itertools import combinations

from aoc.solutions.day02.solution import (
    is_safe,
    is_safe_with_dampener,
    get_direction,
    ASCENDING,
    DESCENDING,
)


class TestGetDirection:
    def test_returns_ascending(self):
        assert get_direction([1, 2, 3]) == ASCENDING

    def test_returns_descending(self):
        assert get_direction([5, 3, 1]) == DESCENDING

    def test_equal_first_two_returns_descending(self):
        # current code treats equal as DESCENDING
        assert get_direction([2, 2, 3]) == DESCENDING

    def test_raises_if_too_short(self):
        with pytest.raises(ValueError):
            get_direction([1])


class TestIsSafe:
    def test_simple_ascending_valid(self):
        assert is_safe([1, 2, 3]) is True

    def test_simple_descending_valid(self):
        assert is_safe([9, 7, 6]) is True

    def test_invalid_due_to_large_jump(self):
        assert is_safe([1, 5, 6]) is False

    def test_invalid_due_to_zero_difference(self):
        assert is_safe([2, 2, 3]) is False

    def test_invalid_due_to_wrong_direction(self):
        assert is_safe([1, 2, 1]) is False


class TestIsSafeWithDampener:
    def test_safe_without_dampener(self):
        assert is_safe_with_dampener([1, 2, 3]) is True

    def test_becomes_safe_after_removing_one(self):
        # [1, 2, 6] is unsafe, but removing 6 → [1,2] is safe
        assert is_safe_with_dampener([1, 2, 6]) is True

    def test_not_safe_even_with_dampener(self):
        # No removal can make this safe
        assert is_safe_with_dampener([1, 10, 20]) is False

    def test_descending_with_one_bad(self):
        # [9, 7, 5, 20] is unsafe, but removing 20 works
        assert is_safe_with_dampener([9, 7, 5, 20]) is True
