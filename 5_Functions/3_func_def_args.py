# How to define default parameter????
# Define it by specifying value to positional parameter in func definition
# itself like "def increment(number, by=1)"
# This will let the function know that if second parameter is not passed by user
#  then the default value to be taken is 1


def increment(number, by=1):
    return number + by


print(increment(2))  # here second parameter is not passed, so default worked
print(increment(3, 5))  # here we changed and specified
####
# The '*agrs' argument accepts multiple arguments in the functions
# which may not be feasile to define in it.
# def multiply(*numbers):
#     print(numbers)

# multiply(2, 3, 4, 5)


def multiply(*numbers):
    total = 1
    for number in numbers:
        # total = total * number
        total *= number
    return total


print(multiply(2, 2, 3, 4))

# The above example "*agrs" returns (TUPLES) data type
# but with "**agrs" we can have value pair {DICTIONARY} data type


def save_user(**user):
    print(user)


save_user(id=1, name="John", age=20)
# {'id': 1, 'name': 'John', 'age': 20} this is the output
