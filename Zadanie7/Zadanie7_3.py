from points import Point
import unittest as ut

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
    # Chcemy, aby x1 < x2, y1 < y2.
        if not x1 < x2:
             raise ValueError("x1 powinno być mniejsze od x2")
        if not y1 < y2:
             raise ValueError("y1 powinno być mniejsze od y2")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):          # "[(pt1.x, pt1.y), (pt2.x, pt2.y)]"
        return "[("+str(self.pt1.x)+", "+str(self.pt1.y)+"), ("+str(self.pt2.x)+", "+str(self.pt2.y)+")]"

    def __repr__(self):        # "Rectangle(pt1.x, pt1.y, pt2.x, pt2.y)"
        return "Rectangle("+str(self.pt1.x)+", "+str(self.pt1.y)+", "+str(self.pt2.x)+", "+str(self.pt2.y)+")"

    def __eq__(self, other):   # obsługa rect1 == rect2
        if not isinstance(other, Rectangle):
             return False
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):           # zwraca środek prostokąta
        x_mid = self.pt1.x + 0.5 * (self.pt2.x - self.pt1.x)
        y_mid = self.pt1.y + 0.5 * (self.pt2.y - self.pt1.y)
        return Point(x_mid, y_mid)

    def area(self):             # pole powierzchni
        width = self.pt2.x - self.pt1.x
        height = self.pt2.y - self.pt1.y
        return width * height

    def move(self, x, y):       # przesunięcie o (x, y)
        self.pt1.x += x
        self.pt2.x += x
        self.pt1.y += y
        self.pt2.y += y

    def intersection(self, other):  # część wspólna prostokątów
        if not isinstance(other, Rectangle):
             raise ValueError("Podaj prostokąt")
        x1 = max(self.pt1.x, other.pt1.x)
        x2 = min(self.pt2.x, other.pt2.x)
        y1 = max(self.pt1.y, other.pt1.y)
        y2 = min(self.pt2.y, other.pt2.y)
        return Rectangle(x1, y1, x2, y2)

    def cover(self, other):     # prostąkąt nakrywający oba
        if not isinstance(other, Rectangle):
             raise ValueError("Podaj prostokąt")
        x1 = min(self.pt1.x, other.pt1.x)
        x2 = max(self.pt2.x, other.pt2.x)
        y1 = min(self.pt1.y, other.pt1.y)
        y2 = max(self.pt2.y, other.pt2.y)
        return Rectangle(x1, y1, x2, y2)

    def make4(self):           # zwraca krotkę czterech mniejszych
        center = self.center()
        first = Rectangle(center.x, self.pt1.y, self.pt2.x, center.y)
        second = Rectangle(center.x, center.y, self.pt2.x, self.pt2.y)
        third = Rectangle(self.pt1.x, center.y, center.x, self.pt2.y)
        fourth = Rectangle(self.pt1.x, self.pt1.y, center.x, center.y)
        return (first, second, third, fourth)

# Kod testujący moduł.

class TestRectangle(ut.TestCase):
    def setUp(self):
        self.r1 = Rectangle(-2,-2,2,2)
        self.r2 = Rectangle(-4,-4,4,4)
        self.r3 = Rectangle(0,0,6,6)
    def testStr(self):
        self.assertEqual(str(self.r1), "[(-2, -2), (2, 2)]")
    def testRepr(self):
        self.assertEqual(repr(self.r1), "Rectangle(-2, -2, 2, 2)")
    def testEq(self):
        self.assertEqual(self.r1, Rectangle(
            self.r1.pt1.x,
            self.r1.pt1.y,
            self.r1.pt2.x,
            self.r1.pt2.y
            ))
    def testNeq(self):
        self.assertNotEqual(self.r1, self.r2)
        self.assertNotEqual(self.r2, self.r3)
    def testCenter(self):
        self.assertEqual(self.r1.center(), Point(0,0))
        self.assertEqual(self.r3.center(), Point(3,3))
    def testArea(self):
        self.assertEqual(self.r1.area(), 16)
    def testMove(self):
        testRect = Rectangle(1,2,3,4)
        testRect.move(5,-5)
        self.assertEqual(testRect, Rectangle(6, -3, 8, -1))
    def testIntersection(self):
        self.assertEqual(self.r1.intersection(self.r3), Rectangle(0, 0, 2, 2))
        self.assertEqual(self.r1.intersection(self.r2), self.r1)
    def testCover(self):
        self.assertEqual(self.r1.cover(self.r3), Rectangle(-2, -2, 6, 6))
        self.assertEqual(self.r1.cover(self.r2), self.r2)
    def testMake4(self):
        self.assertEqual(self.r3.make4(), (
            Rectangle(3, 0, 6, 3),
            Rectangle(3, 3, 6, 6),
            Rectangle(0, 3, 3, 6),
            Rectangle(0, 0, 3, 3)
        ))


if __name__ == '__main__':
    ut.main()
    