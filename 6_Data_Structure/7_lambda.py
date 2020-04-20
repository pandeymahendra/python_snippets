items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

# def sort_item(item):
# return item[1]

# Lambda is an anonymous function, you dont need to define a function like the one before, instead
# We can use lambda. To use labmda "items.sort(key=lambda parameters:expression)", where parameters is
# item and expression is item[1]

items.sort(key=lambda item: item[1])
# print(items)

# What if you want to print only prices of the items in the list

prices = []

for item in items:
    prices.append(item[1])

print(prices)

# The same can be cleaner and achieved with map() function

prices = list(map(lambda item: item[1], items))
print(prices)

# There is also filter function where we can use expression

# x = filter(lambda item: item[1] >= 10, items)  #This returns just the filter object at memory location
# print(x)


# The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)


# COMPREHENSION method is the cleanest method of all
prices = [item[1] for item in items]
# same as above filtered, but using comprehension
filtered = [item for item in items if item[1] >= 10]
print(filtered)
