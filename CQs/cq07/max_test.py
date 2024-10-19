"""Unit tests that test find_and_remove_max"""

__author__ = "730391230"

from CQs.cq07.find_max import find_and_remove_max


# use case to ensure it returns expected value
def test_find_and_remove_max_use_case() -> None:
    assert find_and_remove_max([5, 4, 7, 2]) == 7


# use case to ensure it mutates the input correctly
def test_find_and_remove_max_mutation() -> None:
    a: list[int] = [5, 4, 6]
    find_and_remove_max(a)
    assert a == [5, 4]


# edge case that ensures correct return value
def test_find_and_remove_max_edge() -> None:
    assert find_and_remove_max([]) == -1
