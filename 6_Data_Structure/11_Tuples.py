# Tuple is a read only list denoted by () rather than []
# They are immutable (cannot be modified/mutated), so .append .insert will not work
# point = ()
# point = (1, 2, 3)
# point = 1,
# All 3 examples above are valid Tuple's. Please note that last example
# point = 1, {last 1, ... the comma is important otherwise it will be taken as 1 interger}

point = (1, 2, 3)
print(type(point))

point = (1, 2) + (3, 4)  # Thats how you can concatenate tuples
print(point)

point = (1, 2) * 3  # This will repeat the Tuples * 3 times
print(point)

point = [1, 2, 3]           # This is a list
point = tuple([1, 2, 3])    # This is how you can convert a list to a tuple
print(point)

print(point[0:2])  # Thats how to refer indexes of tuple and print

x, y, z = point  # unpacking tuple
print(x)
print(y)
print(z)

if 10 in point:
    print("10 Exists")
else:
    print("10 Does not exist")
