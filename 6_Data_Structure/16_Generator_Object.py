from sys import getsizeof

# This should return Lists, as per comprehension

values = [x * 2 for x in range(5)]
print(values)

# This should return Tuples as per comprehension
values = (x * 2 for x in range(5))
# print(values)

# If you run the above code, instead of giving Tuples it creates a generator object
# If you have a large collection of elements, it not memory efficient to use Tuples or Lists
# in this situation its recommeneded to use Generator objects
values_1 = (x * 2 for x in range(500))

# for x in values_1:
# print(x)

# Above example gets exact same result/values as below

values_2 = [x * 2 for x in range(500)]
# for x in values_2:
# print(x)

# But a huge difference in the memory usage between the two objects
print("Generator Object Memory Usage(Bytes):", getsizeof(values_1))
print("Lists Object Memory Usage(Bytes):", getsizeof(values_2))
