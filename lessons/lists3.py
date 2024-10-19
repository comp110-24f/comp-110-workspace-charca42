"""List looping with for ... in ..."""

# for ... in ... loops
xs: list[str] = ["w", "x", "y", "z"]
# print every element of xs
# can use while or for ... in ...
# while loops index, for ... in ... loops elements
for element in xs:
    # this loops over every element directly, vs the while loop that was looping over
    # index
    print(element)

my_list: list[str] = ["hello", "world"]
new_list: list[str] = []
# can use elem instead of element. it creates a variable that gets assigned a value of
#  each entity in the list
for elem in my_list:
    new_list.append(elem)
    # loops back to check if there are more elements in the list
print(new_list)
# dont want to do new_list = my_list b/c if you modify one it modifies both, doing the
# for ... in ... makes them not linked to the same heap so they won't change if modified

# using a f.i. loop, write code to tell each pet that they're a good boy
pets: list[str] = ["Louie", "Bo", "Bear"]
# can name the element whatever to help describe the element, named it pet here
for pet in pets:
    print(f"Good boy, {pet}!")

# prints 1 first
for x in [1, 2, 3]:
    print(x)

# reasons for using a while loop over a f.i. loop:
# - special condition not related to a sequence
# - modifying the list while looping is weird with f.i. loops
# - want to loop over indexes

# range - a type of sequence you can loop over
# includes start point, doesn't include end point, steps thru everything inbetween
# range(start, end, [step=1]) step is optional, if i dont put it step = 1
# if step = 2, it looks at every other number,
# for idx in range(0,6):

# range in memory is stored on the heap

# prints the index of the range
for idx in range(0, len(my_list)):
    print(idx)

# prints the elements in the range
for elem in range(0, len(my_list)):
    print(elem)

# using range() in a f.i. loop to print every element's index and value
names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for idx in range(0, len(names)):
    # use idx with range mostly, can use idx to assign the names as well
    print(f"{idx}: {names[idx]}")
