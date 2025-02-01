# super() = Function used in a child class to call methods from a parents class (superclass).
# Allows you to extend the functionality of the inherited menthods

class Circle:
    def __init__(self, color, filled, radius):
        self.color = color
        self.filled = filled
        self.radius = radius


class Square:
    def __init__(self, color, filled, width):
        self.color = color
        self.filled = filled
        self.width = width


class Triangle:
    pass
