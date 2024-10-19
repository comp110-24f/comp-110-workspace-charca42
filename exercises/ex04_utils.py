"""Reverse engineering list algorithims"""

__author__ = "730391230"


def all(int_list: list[int], num: int) -> bool:
    """Returns a bool indicating whether all the ints in the list are the same as num"""
    # need a way to count the repeats thru the while loop
    idx: int = 0
    if len(int_list) == 0:
        return False
    # returns false if empty
    # returns true/false based on if all ints in int_list = num, so two diff return cond
    while idx < len(int_list):
        if num == int_list[idx]:
            idx += 1
        else:
            return False
    return True


def max(int_list: list[int]) -> int:
    """Returns the largest int in the given list"""
    # raising valueerror if the list is empty
    if len(int_list) == 0:
        raise ValueError("max() arg is an empty List")
    # need a way to run through all the values and compare each individually
    idx: int = 0
    largest: int = int_list[0]
    while idx < (len(int_list) - 1):
        # system to make sure there isn't an error from idx+1 > len of int_list
        # has to compare two ints and keep the largest one
        # also has to keep the largest int from previous comparisons
        if int_list[idx] > int_list[idx + 1]:
            if largest < int_list[idx]:
                largest = int_list[idx]
        # assign largest as the first int, then check it vs the other ints
        # the larger int is then compared to largest
        elif largest < int_list[idx + 1]:
            largest = int_list[idx + 1]
        idx += 1
    return largest


def is_equal(int_list1: list[int], int_list2: list[int]) -> bool:
    """Checks if each element at every idex is equal in 2 lists"""
    # doesn't assume lists are equal length
    idx1: int = 0
    idx2: int = 0
    # two indexing trackers
    # doesnt assume equal length and runs through each int list
    if len(int_list1) == len(int_list2):
        # checks for same length
        while idx1 < len(int_list1):
            if int_list1[idx1] == int_list2[idx2]:
                idx1 += 1
                idx2 += 1
            else:
                return False
        return True
    return False


def extend(int_list1: list[int], int_list2: list[int]) -> None:
    """Appends the values from the second list into the first list"""
    idx: int = 0
    # way of counting through int_list2
    # need to count thru int_list 2 and append each item
    while idx < len(int_list2):
        int_list1.append(int_list2[idx])
        # appends for each index increase
        idx += 1
