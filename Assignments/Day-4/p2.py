# program to compare the 2 circles are equal or not using operator overloading

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        if self.radius == other.radius:
            return True
        return False


radius1 = int(input("enter the radius for circle 1"))
ob1 = Circle(radius1)
radius2 = int(input("enter the radius for circle 2"))
ob2 = Circle(radius2)
print(ob1 == ob2)
