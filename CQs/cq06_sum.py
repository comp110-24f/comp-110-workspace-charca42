"""Summing the elements of a list using different loops"""

__author__ = "730391230"


def w_sum(vals: list[float]) -> float:
    # uses a while loop so this needs idx: int = 0
    idx: int = 0
    sum: float = 0.0
    while idx < len(vals):
        sum = sum + vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    # no while loop, just the sum var
    sum: float = 0.0
    for elem in vals:
        sum = sum + elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    # going to use idx with range, then add the vals[idx]
    sum: float = 0.0
    for idx in range(0, len(vals)):
        sum = sum + vals[idx]
    return sum
