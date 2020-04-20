command = ""

# while command != "quit":
# the problem with this is what if someone types QUIT instead of "quit"

# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)

# INFINITE Loop Example (same as above example)

while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
