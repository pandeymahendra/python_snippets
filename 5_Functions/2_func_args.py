
def greet(first, last):   # first and last are known as positional parameters
    print(f"Hi {first} {last}")
    print("Welcome to Python")
# greet("Mahendra", "Pandey")   # whereas, name here will be called argument
# greet("John", "Smith")

#######
# In python there are 2 types of functions
# 1 - functions that perform a task
# 2 - function that returns a value
# greet() was an example of performing a task because it was print'ing


def get_hello(name):
    return f"Hi {name}"


# get_hello("Mahendra")  # executing this nothing prints on screen coz this is just "return"ing
message = get_hello("Mahendra")
print(message)
###


def increment(number, by):
    return number + by


# result = increment(2, 1)
# print(result)
print(increment(2, 1))
