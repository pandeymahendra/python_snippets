# A better way then finally: is using with statement
# Whenever we open the with statement python will automatically close the resources opened.

try:
    # file = open("3_Cleaning_Up.py")
    with open("3_Cleaning_Up.py") as file:
        print("Any code related to file goes here")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age")
else:
    print("No exception were thrown")

    # file.__enter__
    # file.__exit__
# The above two magic methods will be automatically called by "with" and we dont need finally:
# IF an object supports these two magic methods it works with "with" statement
