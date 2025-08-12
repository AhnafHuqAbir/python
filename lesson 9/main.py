import math

def circumference_of_circle(radius):
    return 2 * math.pi * radius

r = float(input("Enter the radius of the circle: "))
circumference = circumference_of_circle(r)
print(f"The circumference of the circle is: {circumference:.2f}")
