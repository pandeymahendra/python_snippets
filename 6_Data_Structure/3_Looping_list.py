letters = ["a", "b", "c"]

# for letter in letters:
for letter in enumerate(letters):
    # print(letter)
    print(letter[0], letter[1])

################################
print("================================")
################################
# Another way for the same result

for index, letter in enumerate(letters):
    print(index, letter)


# items = (0, "a")     --> Tuples
# index, letter = items  # Unpacking the tuples
# for index, letter in enumerate(letters): ---> enumerate will create tuples which will be unpacked in to letters and index same as above
#     print(index, letter)
