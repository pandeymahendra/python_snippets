list1 = [1, 2, 3]
list2 = [10, 20, 30]

# what we want to achieve in the output here is given below:
# [(1, 10),(2, 20),(3, 30)] we want to merge the two lists together in this form


# This ZIP() funtion does the same job mentioned above, but returns memory location
x = zip(list1, list2)

# You can list() it to show on the screen
x = list(zip(list1, list2))

# Can also add additional iterables in the construct
x = list(zip("abc", list1, list2))

print(x)
