"""Unit testing - writing fn to test other fn"""

# uses pytest as a framework
# catches unexpected inputs

# test file names end with "_test.py"
# test fn names begin with "test_"
# def test_name() -> None:
# other code goes here
# assert <boolean expression>

# unit tests are helpful since REPL is tedious

# use case: testing properties for how we expect the program to be used
# edge case: testing instances outside typical usage (ex: empty/incorrect input)


# if running pytest from repl: end with .py


def get_first(input: list[int]) -> int:
    """Returns index = 0 of input list"""
    if len(input) == 0:
        return -1
    return input[0]


def remove_first(input: list[int]) -> None:
    """Removes index = 0 of list"""
    input.pop(0)


def remove_and_get_first(input: list[int]) -> int:
    """Remove and return index = 0 of input list"""
    first: int = input[0]
    input.pop(0)
    # since it removes it first, it returns the second element of the list
    return first
