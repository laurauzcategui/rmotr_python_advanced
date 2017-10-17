#!/usr/bin/python


class Shape(object):
    def area(self):
        raise NotImplementedError()


class Circle(Shape):
    def __init__(self, radius=0):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width


class Square(Rectangle):
    # Only __init__ method
    def __init__(self, side):
        self.side = side
        Rectangle.__init__(self, self.side, self.side)

c = Circle(radius=10)
assert c.area() == 314.0

s = Square(side=4)
assert s.area() == 16
