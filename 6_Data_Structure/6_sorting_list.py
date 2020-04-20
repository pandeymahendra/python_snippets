numbers = [3, 13, 56, 34, 2, 4, 5]

numbers.sort()              # Sort in ascending order
numbers.sort(reverse=True)  # Sort in reverse order
# print(sorted(numbers))      # Same as sort but can be used with print directly
# print(sorted(numbers, reverse=True))

# print(numbers)

########################################################################
# What if we have list with tuples inside, how do you sort this???
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

items.sort()  # Even after passing sort, it doesn't work'
print(items)


# Solution to the above problem is defining your own function


def sort_item(item):
    return item[1]


# items.sort(sort_item) # This should give an error that "sort()" takes no positional arguments
items.sort(key=sort_item)
print(items)
