"""CQ04 - get_coords"""

__author__ = "730391230"


def get_coords(xs: str, ys: str) -> None:
    # prints the formatted pairs of each character
    # need variables to keep track of loops
    xindex: int = 0
    yindex: int = 0
    while len(xs) > xindex:
        while len(ys) > yindex:
            print(f"({xs[xindex]},{ys[yindex]})")
            yindex = yindex + 1
        yindex = 0
        xindex = xindex + 1
