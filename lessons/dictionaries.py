"""Examples of dictionary syntax with Ice Cream Shop order tallies"""

ice_cream: dict[str, int] = {
    "chococlate": 12,
    "vanilla": 8,
    "strawberry": 4,
}
# syntax
# name: dict[key,value] = {}

# length of dict = len(name)

# use subscription notation to add elements
# name[key] = value
ice_cream["mint"] = 3

# use subscription notation to access values
# name[key]
# modify:
# name[key] = new_value
ice_cream["chococlate"]
ice_cream["vanilla"] = 10

# cannot have duplicate keys, duplicate values are ok

# check if key is in dict
if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("No orders of mint")

# use pop to remove element
ice_cream.pop("strawberry")

# "for" loops iterate over keys by default
for flavor in ice_cream:
    print(ice_cream[flavor])
