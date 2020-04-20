letters = ["a", "b", "c"]

print(letters.count("d"))  # To print occureneces of element "d" in the list

# print(letters.index("d"))
# This gives an error saying that the index does not exist

# A better way to avoid error is to put condition during check

if "d" in letters:
    print(letters.index("d"))
