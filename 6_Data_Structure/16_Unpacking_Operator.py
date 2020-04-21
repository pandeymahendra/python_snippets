numbers = [1, 2, 3]
print(numbers)


# What if you want to get a result like 1 2 3 instead of [ 1, 2, 3]
# thats where you can use unpacking
print(*numbers)  # Prefix the variable with '*' to unpack

# Same way we can unpack strings

print(list("Hello"))
print(*list("Hello"))

first = [1, 2]
second = [3, 4, 5]
unpack = [*first, *second]  # --> We can unpack like this
unpack = [*first, 'a', *second]
print(unpack)

# Dictionaries can also be unpacked but we need to use two '**'
first = {"x": 1, "y": 2}
second = {"z": 3}
unpack = {**first, **second}
print(unpack)
