import math

def circle_area(radius):
    area = math.pi * (radius ** 2)
    return area

r = float(input("Enter the radius of the circle: "))
print("Area of the circle:", round(circle_area(r), 2))
