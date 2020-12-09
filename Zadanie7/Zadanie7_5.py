from points import Point
from math import pi
import unittest as ut

class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.center = Point(x, y)
        self.radius = radius

    def __repr__(self):       # "Circle(x, y, radius)"
        return "Circle(" + str(self.center.x) + ", " +str(self.center.y) + ", " + str(self.radius) + ")"

    def __eq__(self, other):
        return self.center == other.center and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):            # pole powierzchni
        return pi * self.radius ** 2

    def move(self, x, y):     # przesuniecie o (x, y)
        self.center += Point(x, y)

    def cover(self, other):   # najmniejszy okrąg pokrywający oba
        centersDistance = (self.center - other.center).length()
        if self.radius + centersDistance < other.radius: # self zawiera się w other
            return Circle(other.center.x, other.center.y, other.radius)
        elif other.radius + centersDistance < self.radius: # other zawiera się w self
            return Circle(self.center.x, self.center.y, self.radius)
        else:
            enclosingRadius = (self.radius + other.radius + centersDistance) / 2
            theta = 0.5 + abs(self.radius - other.radius) / (2 * centersDistance)
            center = Point((1-theta)*self.center.x, (1-theta)*self.center.y) + Point(theta * other.center.x, theta * other.center.y)
            return Circle(center.x, center.y, enclosingRadius)



# Kod testujący moduł.

class TestCircle(ut.TestCase):
    def setUp(self):
        self.c1 = Circle(0, 0, 5)
        self.c2 = Circle(0, 0, 8)
        self.c3 = Circle(2, 2, 4)
    def testRepr(self):
        self.assertEqual(repr(self.c3), "Circle(2, 2, 4)")
    def testEqual(self):
        self.assertEqual(self.c2, Circle(0, 0, 8))
    def testNotEqual(self):
        self.assertNotEqual(self.c1, self.c2)
    def testArea(self):
        self.assertEqual(self.c3.area(), 16 * pi)
    def testMove(self):
        testCircle = Circle(1, 1, 3)
        testCircle.move(-2, 2)
        self.assertEqual(testCircle, Circle(-1, 3, 3))
    def testCover(self):
        self.assertEqual(self.c1.cover(self.c2), Circle(0, 0, 8))
        self.assertEqual(self.c2.cover(self.c3), Circle(0, 0, 8))
        self.assertEqual(self.c3.cover(self.c1), Circle(0.6464466094067263, 0.6464466094067263, (5 + 4 + 8 ** 0.5) / 2))


if __name__ == '__main__':
    ut.main()
    