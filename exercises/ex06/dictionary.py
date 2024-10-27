"""EX06 - defines invert, """

__author__ = "730391230"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Returns a dict that inverts the keys and the values"""
    output: dict[str, str] = {}
    # use this test idx loop to move the values to a list and check if any of them are
    #  equal
    test: list[str] = []
    i1: int = 0
    i2: int = 1
    # keys become values, but there cant be duplicate keys, so raise error when
    # duplicate values
    for key in input:
        test.append(input[key])
    # check if any value is equal, raise error if it is
    while i1 < len(test):
        while i2 < len(test):
            if test[i1] != test[i2]:
                i2 += 1
            else:
                raise KeyError("Keys cannot have duplicates!")
        i1 += 1
        i2 = i1 + 1

    # keys become values, but there cant be duplicate keys, so raise error when
    # duplicate values
    for key in input:
        output[input[key]] = key
    return output


def favorite_color(input: dict[str, str]) -> str:
    """Takes an input dict of names and favorite colors, and return the color that
    appears the most"""
    # if there is a tie, return the color that appeared first
    fav: str = ""
    # need a way to keep track of repeats
    color: str = ""
    c1: int = 0
    c2: int = 0
    # assigns the color to "color", then checks each value to see if it is equal to
    # "color" and adds a count if so. then, it compares to the highest count (c2) and
    # if it is higher, it saves that color as "fav", resets the count, and moves to
    #  next key
    for key in input:
        color = input[key]
        for key2 in input:
            if input[key2] == color:
                c1 += 1
        if c1 > c2:
            c2 = c1
            fav = input[key]
        c1 = 0
    return fav


def count(input: list[str]) -> dict[str, int]:
    """Makes the values of the list into the keys of a dict, and the value of the dict
    is the count of each item"""
    new: dict[str, int] = {}
    # loop thru input. if elem is in dict, +1 to count. if not, add elem = 1
    for elem in input:
        if elem in new:
            new[elem] += 1
        else:
            new[elem] = 1
    return new


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Produces a dict where each key is a unique letter and each value is a list of
    the words that begin with the letter"""
    output: dict[str, list[str]] = {}
    # need to put keys as the first index of input
    # add the input to the list in the dict if the letter is there or make a new list
    for elem in input:
        letter = (elem[0]).lower()
        # keeps track of the first character in the element and makes it lowercase
        if letter in output:
            output[letter].append(elem)
            # adds the element to the list for the letter
        else:
            output[letter] = [elem]
            # makes a new list for the new letter
    return output


def update_attendance(input: dict[str, list[str]], day: str, student: str) -> None:
    """Mutates the input dict by adding the given student to the day in the dict list"""
    # checks if day is in dict as a key
    if day in input:
        if (student in input[day]) is False:
            input[day].append(student)
    else:
        input[day] = [student]
