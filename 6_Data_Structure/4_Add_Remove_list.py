letters = ["a", "b", "c"]

# ADD
letters.append("d")  # Appends the list
# print(letters)
letters.insert(0, "-")  # This prepends the list starting with index of 0
# print(letters)

# REMOVE

letters.pop()  # Removes the last letter from the list
# print(letters)
letters.pop(1)  # Removes the index 1 letter from the list
# print(letters)
# Removes the index specified as 0:2, bcoz pop() can only remove one index at a time
del letters[0:2]
print(letters)

letters.clear()  # Remove all letters index
