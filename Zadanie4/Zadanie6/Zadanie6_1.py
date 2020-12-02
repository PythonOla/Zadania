import unittest as ut

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self): 
        return '(' + str(self.x) + ', ' + str(self.y) + ')'          # zwraca string "(x, y)"

    def __repr__(self): 
        return 'Point' + str(self)       # zwraca string "Point(x, y)"

    def __eq__(self, other): 
        return  self.x == other.x and self.y == other.y   # obsługa point1 == point2

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other): 
        return Point(self.x + other.x, self.y + other.y)  # v1 + v2

    def __sub__(self, other): 
        return Point(self.x - other.x, self.y - other.y)  # v1 - v2

    def __mul__(self, other): 
        return self.x * other.x + self.y * other.y  # v1 * v2, iloczyn skalarny (liczba)

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D (liczba)
        return self.x * other.y - self.y * other.x

    def length(self): 
        return (self.x**2 + self.y**2)**0.5         # długość wektora

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points


# Kod testujący moduł.

class TestPoint(ut.TestCase): 
    def setUp(self):
        self.pointA = Point(1, 2)
        self.pointB = Point(1, -3)

    def testToString(self):
        self.assertEqual(str(self.pointA), "(1, 2)")
        self.assertEqual(str(self.pointB), "(1, -3)")

    def testToRepr(self):
        self.assertEqual(repr(self.pointA), "Point(1, 2)")
        self.assertEqual(repr(self.pointB), 'Point(1, -3)')
    
    def testEqual(self):
        self.assertFalse(self.pointA == self.pointB)
        self.assertTrue(self.pointA == Point(1, 2))

    def testNotEqual(self):
        self.assertTrue(self.pointA != self.pointB)
        self.assertFalse(self.pointA != Point(1, 2))

    def testAdd2D(self):
        self.assertEqual(self.pointA + self.pointB, Point(2, -1))

    def testSub2D(self):
        self.assertEqual(self.pointA - self.pointB, Point(0, 5))
        self.assertEqual(self.pointB - self.pointA, Point(0, -5))

    def testDotProduct2D(self):
        self.assertEqual(self.pointA * self.pointB, -5)

    def testCrossProduct2D(self):
        self.assertEqual(self.pointA.cross(self.pointB), -5)
        self.assertEqual(self.pointB.cross(self.pointA), 5)

    def testLength(self):
        self.assertEqual(self.pointA.length(), 5**0.5)
        self.assertEqual(self.pointB.length(), 10**0.5)

    def testHash(self):
        self.assertEqual(self.pointA.__hash__(), hash((1,2)))
        self.assertEqual(self.pointB.__hash__(), hash((1, -3)))

if __name__ == '__main__':
    ut.main()
    
