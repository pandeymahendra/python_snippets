# If you want to work with external resources like file, database, network etc.
# You should release them once the code execution/job is completed. Like, if you open a file
# once needs to make sure to close it as well.


try:
    file = open("3_Cleaning_Up.py")
    age = int(input("Age: "))
    xfactor = 10 / age
    # If we try closing here and code encounters error before this, it wont execute close()
    # file.close()
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age")
    # If we try puttin it here, it will only work if there is an exception,
    # if you dont have exception it will execute else: block
    # file.close()
else:
    print("No exception were thrown")

# This is the solution to close() the file, bcoz its always executed wether you have an exception or not
finally:
    file.close()
