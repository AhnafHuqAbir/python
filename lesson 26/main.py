import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Compute area of the circle"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Compute perimeter (circumference) of the circle"""
        return 2 * math.pi * self.radius

r = float(input("Enter the radius of the circle: "))

circle1 = Circle(r)

print("Radius:", circle1.radius)
print("Area of Circle:", round(circle1.area(), 2))
print("Perimeter of Circle:", round(circle1.perimeter(), 2))
