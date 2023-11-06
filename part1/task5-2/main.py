import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            print("Radius cannot be negative.")
        self._radius = value

    @property
    def diameter(self):
        return 2 * self.radius

    @property
    def circumference(self):
        return 2 * math.pi * self.radius
    
    @property
    def area(self):
        return math.pi * self.radius**2
    
    def __str__(self) -> str:
        return "Circle [\nradius = {0}, \ndiameter = {1}, \ncircumference = {2}, \narea = {3}\n]".format(self.radius, self.diameter, self.circumference, self.area)

# instanciation
circle1 = Circle(12)
print(circle1)

circle2 = Circle(-1)