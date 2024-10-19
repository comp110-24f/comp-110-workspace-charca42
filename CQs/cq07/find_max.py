"""Hosts the find_and_remove_max function"""

__author__ = "730391230"


def find_and_remove_max(input: list[int]) -> int:
    # if input is empty, return -1 and don't modify input
    if len(input) == 0:
        return -1
    # finds and returns the largest number in input
    largest: int = 0
    idx: int = 0
    while idx < (len(input) - 1):
        if input[idx] > input[idx + 1]:
            if largest < input[idx]:
                largest = input[idx]
        elif largest < input[idx + 1]:
            largest = input[idx + 1]
        idx += 1
    # removes all instances of the largest number
    idx = 0
    while idx < len(input):
        while input[idx] == largest:
            input.pop(idx)
            idx = 0
        idx += 1
    return largest
