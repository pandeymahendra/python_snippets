# A class is a blueprint for creating new objects
# An Object is an instance of a class

# Class: Human
# Object: John, Jane, Ron etc.


class Point:
    def draw(self):
        print("Draw")


point = Point()

print(type(point))

point.draw()

# To check if point object "isinstance" of Point class

print(isinstance(point, Point))
