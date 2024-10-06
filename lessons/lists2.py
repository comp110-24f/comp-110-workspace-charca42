a: str = "24"
b: str = a
# relative reassignment operator - simplified way of doing x = x + y
a += "6"
# a = "246" b/c str adding
print(b)

c: list[int] = [2, 4]
# memory diagram: list itself in H, name and location in S
# S-H-O for lists: table in H; id:0,1,etc in left; list[int]: 2,4,etc in right
# S - value for c is "id:0" so it is a reference to the location to find the def
d: list[int] = c
# since d is the same ID as c, in S b|id:0 as well
c.append(6)
print(d)


# fn can take lists as arg, return/create lists, and modify lists
def display(vals: list[int]) -> None:
    # prints each item in the list
    idx: int = 0
    while idx < len(vals):
        print(vals[idx])
        idx += 1


# for S-H-O, the values in the list would be mentioned in the H when display is called
# the ID is in the S

display([1, 2, 3])


def odds_list(min: int, max: int) -> list[int]:
    """returns list of odds between min and max"""
    odds: list[int] = list()
    # stored on the H
    x: int = min
    while x <= max:
        if x % 2 == 1:
            odds.append(x)
        x += 1
    # odds is not written as RV, "odds" is a reference to a list, so the RV = list ID
    return odds


global_odds: list[int] = odds_list(2, 6)
print(global_odds)
