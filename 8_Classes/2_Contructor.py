# Contructors are used to declare intance variables


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print("Draw")


# Suppose we want to supply X and Y coordinates to the class
# point = Point(1, 2)
# So, for this we need to use contructors

p = Point(7, 13)

print(p.x, " | ", p.y)
