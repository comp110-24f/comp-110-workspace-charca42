"""test file for unit_tests firsts fn"""

from lessons.unit_tests import get_first, remove_first, remove_and_get_first


def test_get_first_use_case() -> None:
    """testing basic function for get_first fn"""
    # dont need to define parameters or return type, this is just testing function
    assert get_first([4, 5, 6, 7]) == 4
    # the boolean assertion tests how i want fn to behave


# use the "testing" tab to test the test fn, will get check on bottom if worked


def test_get_first_edge_case() -> None:
    """testing g_f on an edge case (empty imput)"""
    assert get_first([]) == -1
    # testing edge cases follows a similar structure


def test_remove_first_edge_case() -> None:
    """testing r_f on empty list. should not do anything"""
    a: list[int] = []
    remove_first(a)
    assert a == []
    # does not pass this b/c if there is empty list, pop gives error.
    # need to modify original fn to change this


def test_remove_and_get_first_use_case() -> None:
    """testing returning the first element"""
    assert remove_and_get_first([4, 5, 6, 7]) == 4
    # since this assert statement is false, it gives error and feedback on  the error
    # fixed it in unit_tests and now it is true


# fn remove_first takes more work to test that it returns nothing
def test_remove_first_use_case() -> None:
    """testing remove+first returns nothing"""
    a: list[int] = [4, 5, 6, 7]
    remove_first(a)
    assert a == [5, 6, 7]
    # can add other lines of code to help with assertion


def test_remove_and_first_mutation() -> None:
    """testing r_a_g_f removes first element"""
    # checking if the fn properly mutates the parameter
    a: list[int] = [1, 2, 3]
    remove_and_get_first(a)
    assert a == [2, 3]
