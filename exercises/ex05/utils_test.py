"""Testing utility functions from EX05"""

__author__ = "730391230"

# need 3x unit test functions for each function
# 1 edge case and 2 use cases (one tests what the fn returns, and one tests mutation)

from exercises.ex05.utils import only_evens, sub, add_at_index

import pytest


def test_only_evens_use_case() -> None:
    """Testing basic function of only_evens"""
    # assert what is returned is what should be returned
    assert only_evens([15, 6, 3]) == [6]


def test_only_evens_mutation() -> None:
    """Testing that only_evens doesn't mutate input"""
    # to do this, assess the list rather than the return
    a: list[int] = [4, 6, 8, 9]
    only_evens(a)
    assert a == [4, 6, 8, 9]


def test_only_evens_edge() -> None:
    """Testing an edge case where the input is not as expected"""
    assert only_evens([]) == ([])


def test_sub_use_case() -> None:
    """Testing basic function of sub"""
    # asserting that the fn returns the correct value
    assert sub([14, 6, 8, 3, 2], 1, 4) == [6, 8, 3]


def test_sub_mutation() -> None:
    """Testing to ensure sub does not mutate input list"""
    b: list[int] = [5, 7, 2, 5, 3]
    sub(b, 1, 2)
    assert b == [5, 7, 2, 5, 3]


def test_sub_edge() -> None:
    """testing sub with an edge case to ensure correct function"""
    assert sub([], 5, 8) == []


def test_add_at_index_use_case() -> None:
    """Testing add_at_index to ensure that it mutates"""
    # no return value, so will check to ensure no return value is given
    assert add_at_index([4, 7, 5, 8, 9], 1, 5) == None


def test_add_at_index_mutation() -> None:
    """Testing add_at_index to ensure it mutates input"""
    # since no return value, will have to check the input list
    c: list[int] = [5, 10, 15]
    add_at_index(c, 8, 1)
    assert c == [5, 8, 10, 15]


def test_add_at_index_edge_raise_indexerror() -> None:
    """Testing add_at_index with an edge case"""
    # going to prompt an IndexError with invalid index to test edge case
    with pytest.raises(IndexError):
        add_at_index([5, 10, 13], 4, 4)
