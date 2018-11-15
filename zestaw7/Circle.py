from Point import Point
import math


class Circle:
    def __init__(self, x=0, y=0, radius=1):
        if isinstance(radius, (int, float, complex)):
            if radius < 0:
                raise ValueError("Promień ujemny")
            self.pt = Point(x, y)
            self.radius = radius
        else:
            raise ValueError("Promien niepoprawny!")

    def __repr__(self):  # "Circle(x, y, radius)"
        return str(self.__class__.__name__) + "(" + str(self.pt.x) + "," + str(self.pt.y) + "," + str(
            self.radius) + ")"

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):  # pole powierzchni
        return math.pi * self.radius * self.radius

    def move(self, x, y):  # przesuniecie o (x, y)
        temp = self.pt + Point(x, y)
        return Circle(temp.x, temp.y, self.radius)

    def cover(self, other):  # okrąg pokrywający oba
        jednostkowy = (other.pt - self.pt).norm()
        p1 = self.radius * -1 * jednostkowy + self.pt
        p2 = other.radius * jednostkowy + other.pt
        srodek = (p2 - p1) / 2 + p1
        radius = (p2 - p1).length() / 2
        return Circle(srodek.x, srodek.y, radius)
