# DICTIONARY is a collections of key/value pairs Ex. PhoneBook
# Name -> Contact

# One can define dict in both ways, but 2nd method is a cleaner approach
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)

# We can get a value associated with a key, by specifying key string and not index number like
# point[0] because in dict, the key itself is an index and value is the element
print(point["x"])
print(point["y"])

# Similarly, we can assign a new value to a key
point["x"] = 10
point["z"] = 20
print(point["x"])
print(point)  # To list all key/value pairs

# What if you try to access a non existing key
# 2 ways to resolve: use "if" or ".get()" method
if "a" in point:
    print(point["a"])

print(point.get("a"))  # --> This will return "None" if it cannot find.

# We can change what it shows instead of "None" by:
print(point.get("a", 0))  # --> This returns 0 instead of "None"

# To delete a key/value pair:

del point["x"]
# print(point)

# How to loop through the keys
point = dict(x=1, y=2, z=20)
print(point)

for k in point.keys():   # .keys() method lists the keys only and not values, so this iterates through keys
    print(k)

for k in point.values():   # .values() method lists the values only and not keys, so this iterates through values
    print(k)

for k in point.items():  # .items() method lists the keys and values, so this iterates through both
    print(k)

# DICTIONARY Comprehension Examples
values = []

for x in range(5):
    values.append(x * 2)
print(values)

# same can be achived in dict comprehension
# [expression for item in items]


[x * 2 for x in range(5)]  # This returns list
#  |       |        |
#  |      item      items
#  expression

{x * 2 for x in range(5)}  # This returns Set

new = {x * 2 for x in range(5)}
print(new)

# The sytactical difference between the Set and Dictionary is:
{1, 2, 3}  # --> Sets
{1: "a", 2: "b", 3: "c"}  # --> Dictionary

# --> x: x * 2 will give {0: 0, 1: 2, 2: 4} as a dictionary
new = {x: x * 2 for x in range(5)}
print(new)
