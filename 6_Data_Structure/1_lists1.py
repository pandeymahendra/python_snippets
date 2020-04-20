letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
combined = zeros + letters
# If you want to create a list of numbers from 0 - 20
numbers = list(range(20))
chars = list("Hello World")

print("LETTERS : ", letters)
print("MATRIX :", matrix)
print("ZEROS :", zeros)
print("COMBINED :", combined)
print("NUMBERS :", numbers)
print("CHARS : ", chars)
print("First index of LETTERS: ", letters[0])
letters[0] = "A"    # Assign a new value for first index
print("First index of LETTERS after changing 'a' to 'A': ", letters[0])
print("Starting 0 to 3 indexes excluding 3 :", letters[0:3])

################################################################
numbers = list(range(20))  # This will create a list of range numbers
print(numbers[:])   # This will print all in the list
print(numbers[::2])  # This will print the range numbers with 2 steppings
# This will also print the range numbers with 2 steppings starting from last (in reverse order)
print(numbers[::-1])
