# Exception handling is a way to prevent premature termination of the program and also give out
# descriptive messgaes to non-technical users.

# age = int(input("Age: "))
# The above statement expects an int, but if you type any other value.. its bound to give you an error

# Handling exception code:
try:
    age = int(input("Age: "))
except ValueError:
    # except ValueError as err:
    print("You didn't enter a valid age")
    # print(err)                  # To see the error as is

else:  # We have else: block for try: as well
    print("No exception were thrown")


# Without exception handling the below code would not work as the program terminates prematurely
print("Further execution continues")
