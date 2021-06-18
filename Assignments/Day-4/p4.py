# program to construct a 2 circle by radius and compute their area, circumference and compare them
import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def areaOfCircle(self):
        return math.pi * self.radius * self.radius

    def circumferenceOfCircle(self):
        return 2 * math.pi * self.radius

    def __ge__(self, other):
        if self.radius == other.radius:
            return "Both the circles are equal"
        elif self.radius > other.radius:
            return "Circle 1 is bigger than Circle 2"
        return "Circle 2 is bigger than Circle 1"


radius1 = int(input("enter the radius for circle 1 "))
radius2 = int(input("enter the radius for circle 2 "))
ob1 = Circle(radius1)
ob2 = Circle(radius2)
print("Circumference of circle 1 {:.2f}".format(ob1.circumferenceOfCircle()))
print("Circumference of circle 2 {:.2f} ".format(ob2.circumferenceOfCircle()))
print("Area of Circle 1 {:.2f} ".format(ob1.areaOfCircle()))
print("Area of Circle 2 {:.2f}".format(ob2.areaOfCircle()))
print(ob1 >= ob2)
