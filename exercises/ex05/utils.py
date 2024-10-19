"""EX05 - utility functions"""

__author__ = "730391230"


def only_evens(input: list[int]) -> list:
    """Returns a new list containing only the elements of the input that were even"""
    # should not mutate input. use len and append
    idx: int = 0
    evens: list[int] = []
    while idx < len(input):
        if input[idx] % 2 == 0:
            evens.append(input[idx])
        idx += 1
    return evens


def sub(input: list[int], start: int, end: int) -> list:
    """Generates a list which is a subset of input, between start and end -1"""
    # cant mudate input.
    idx: int = 0
    subset: list[int] = []
    # if start is negative, starts at the beginning of the list
    if start < 0:
        start = 0
    # if end is longer than input, ends at end of input
    if end > (len(input)):
        end = len(input)
    # checks if list is empty, start is longer than list, or end is shorter than 0
    if (len(input) == 0) or (start >= len(input)) or (end <= 0):
        return subset
    # check to return the value at start position but not end
    while (idx + start) <= (end - 1):
        subset.append(input[idx + start])
        idx += 1
    return subset


def add_at_index(input: list[int], add: int, idx: int) -> None:
    """Modified input to put add at the given index"""
    # this mutates input
    # need a way to raise an index error if index is wrong
    if (idx < 0) or (idx > len(input)):
        raise IndexError("Index is out of bounds for the input list")
    # first have to add the item to the end
    input.append(add)
    # now have to get the item to the right place
    replace: int = len(input) - 1
    # going to shift values one position to the right in list order until i get to idx
    while replace > idx:
        input[replace] = input[replace - 1]
        replace -= 1
    input[idx] = add
