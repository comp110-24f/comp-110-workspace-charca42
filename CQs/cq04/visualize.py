"""CQ04 - visualizing imported functions"""

__author__ = "730391230"

from CQs.cq04.concatenation import concat

from CQs.cq04.coordinates import get_coords

x: str = "123"
y: str = "abc"

print(concat(x, y))

get_coords(x, y)
