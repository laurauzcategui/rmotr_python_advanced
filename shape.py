import functools

class Shape(object):

    def __init__(self):
        self.sides = []

    def add_side(self,side):
        self.sides.append(side)

    def area(self):
        return functools.reduce(lambda x,y : x * y ,self.sides)

class Circle(Shape):
    def __init__(self, radius=0):
        Shape.__init__(self)
        self.radius = radius
        self.add_sides()

    def add_sides(self):
        Shape.add_side(self,self.radius)
        Shape.add_side(self,self.radius)

    def area(self):
        return 3.14 * Shape.area(self)

class Rectangle(Shape):
    def __init__(self, height,width):
        Shape.__init__(self)
        self.height = height
        self.width = width
        self.add_sides()

    def add_sides(self):
        Shape.add_side(self,self.height)
        Shape.add_side(self,self.width)

    def area(self):
        return Shape.area(self)

class Square(Rectangle):
     # Only __init__ method
     def __init__(self,side):
         self.side = side
         Rectangle.__init__(self, self.side, self.side)

c = Circle(radius=10)
assert c.area() == 314.0

s = Square(side=4)
assert s.area() == 16
