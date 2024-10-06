"""Basic syntax of lists"""

# create an empty list
my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor
# either work

print(my_numbers)

# string analogy
# my_name: str = "" literal
# my_name: str = str() constructor

# adding item to list
# <list name>.append(<item>)
my_numbers.append(1.5)
my_numbers.append(2.5)
print(my_numbers)
foo: list[int] = [2, 5, 8, 1]
print(foo[len(foo) - 1])

# can modify lists with subscription index
# b/c lists are mutable, but strings are not
# can do this with lists of strings but not strings alone
foo[1] = 95
print(foo)

# length of list
print(len(foo))

# removing item from list
foo.pop(2)
print(foo)

# adding duplicates to list
foo.append(95)


def display(int_list: list[int]) -> None:
    """Displays all elements of int_list"""
    index: int = 0
    while index < len(int_list):
        print(int_list[index])
        index += 1


display(int_list=foo)
