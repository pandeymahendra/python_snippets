# Sets are another data structure, that finds and eliminates duplicates from the
# list. To define a set we use {}. Sets are unordered, and hence cannot be accessed using indexes.

numbers = [1, 1, 1, 2, 3, 4, 5, 5, 6]
first = set(numbers)  # We can convert list to set using the set function
print(first)

second = {5, 6, 7, 8}
print("UNION:", (first | second))  # This is called Union of sets

# Intersection will give you the result of elements that exists in both the Sets
print("INTERSECTION:", (first & second))

# Difference will give you the result of elements that DO NOT match from first to second
print("DIFFERENCE:", (first - second))

# Symmetric difference will return elements that exists in either first OR second but not both
print("SYMMETRIC DIFFERENCE:", (first ^ second))

# DOEN NOT WORK:
# print(first[0])  # Sets are unordered, hence un-indexed

if 1 in first:
    print("1 in SET: YES")
