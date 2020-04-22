# How do you handle difference exceptions

try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age")
# If you give 0 as the input, 0 is non divisible, hence the type of exception will be different
# except ZeroDivisionError:               # A better way is given above
    # print("You didn't enter a valid age")

else:  # We have else: block for try: as well
    print("No exception were thrown")
