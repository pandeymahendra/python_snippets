numbers = [1, 2, 3]
# you can unpack the list like this:
first = numbers[0]
second = numbers[1]
third = numbers[2]

# but thats not a clean method
# the clean method is given below

# Unfortunately this way requires exact number of variables as many indexes
first, second, third = numbers


# What if we have so many indexes in this list and want to refer only starting two:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# *others indicates a list of all possible indexes between second & last
first, second, *others, last = numbers

print(first)
print(second)
print(others)
print(last)
