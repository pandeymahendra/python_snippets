# Arrays are a good choice compared to list when you have large list of numbers
# Lets say 10,000 or more numbers

from array import array
# array() - "Google array typecode" thats the first argument that it takes,
# its a string of 1 character that determines the type of elements in the arrays

numbers = array("i", [1, 2, 3])

# Arrays can be edited the same way as list with methods like .append()
# .insert() etc.

print(numbers[0])
