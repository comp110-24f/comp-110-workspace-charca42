"""CQ03 - Practice using while loops to iterate over a string"""

__author__ = "730391230"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    # this will keep track of the matches
    track: int = 0
    # this will prevent the while loop from running indefinitely and keep track of
    # repeats
    while track < len(phrase):
        # always want track to increase per repetition, but only increase count if a
        #  match is found
        if phrase[track] == search_char:
            count = count + 1
            track = track + 1
        else:
            track = track + 1
    return count
