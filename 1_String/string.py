
first = "Mahendra"
last = "          Pandey"

# one way to represent string with a space is concatenation
# print(first + " " + last)
msg1 = "{} {}".format(first, last)       # formatted string 1
msg2 = f"{first} {last} { 2 + 2}"
msg3 = f"{len(first)} {last}"
print(msg2)

######################################
first = "Python"
last = "          programming"
print(first.upper())
print(first.lower())
print(first.title())   # Capitalise first letter of every word

# Strips spaces before and after strings {We can use ".lstrip()" and ".rstrip()" for left and right strip'ing}
print(last.strip())
print(first.find("th"))  # tells you index number of string
print(first.replace("P", "J"))      # Replaces string in variable/Object
print("pro" in last)                # Boolean if string is found
print("pro" not in last)
