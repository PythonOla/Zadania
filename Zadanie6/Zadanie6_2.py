import unittest 

class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        if y == 0:
            raise ZeroDivisionError
        self.x = x
        self.y = y

    def __str__(self):
        if self.y == 1:
            return str(self.x)
        else:
            return str(self.x) + '/' + str(self.y) # zwraca "x/y" lub "x" dla y=1

    def __repr__(self):
        return "Frac(" + str(self.x) + ', ' + str(self.y) + ")"       # zwraca "Frac(x, y)"

    def toCommonDenominator(self, other): 
        return (
            Frac(self.x * other.y, self.y * other.y),
            Frac(other.x * self.y, other.y * self.y)
        )

    # Python 2.7 i Python 3
    def __eq__(self, other):
        if self.y == other.y:
            return self.x == other.x
        else:
            (commonSelf, commonOther) = self.toCommonDenominator(other)
            return commonSelf.x == commonOther.x

    def __ne__(self, other): 
        return not self == other

    def __lt__(self, other): 
        if self.y == other.y:
            return self.x < other.x
        else:
            (commonSelf, commonOther) = self.toCommonDenominator(other)
            return commonSelf.x < commonOther.x

    def __le__(self, other): 
        return self < other or self == other

    def __gt__(self, other): 
        return not self <= other

    def __ge__(self, other): 
        return not self < other

    def __add__(self, other): 
        if self.y == other.y:  # frac1 + frac2
            return Frac(
                self.x + other.x,
                self.y
            )
        else:
            (commonSelf, commonOther) = self.toCommonDenominator(other)
            return commonSelf + commonOther

    def __sub__(self, other): 
        return self + (-other)
          # frac1 - frac2

    def __mul__(self, other):
        return Frac(
            self.x * other.x,
            self.y * other.y
        )   # frac1 * frac2

    def __div__(self, other): 
        return Frac(
              self.x * other.y,
              self.y * other.x
        )          # frac1 / frac2, Python 2

    def __truediv__(self, other): 
        return self.__div__(other)  # frac1 / frac2, Python 3

    def __floordiv__(self, other):
        exactResult = self / other
        return exactResult.x // exactResult.y  # frac1 // frac2, opcjonalnie

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self): 
        return float(self.x) / float(self.y) # float(frac)

    def __hash__(self):
        return hash(float(self))   # immutable fracs
        # assert set([2]) == set([2.0])

# Kod testujący moduł.

class TestFrac(unittest.TestCase): 
    
    def setUp(self):
        self.fracA = Frac(2,5)
        self.fracB = Frac(-1, 3)

    def testToStr(self):
        self.assertEqual(str(self.fracA), '2/5')
        self.assertEqual(str(Frac(4,1)), '4')

    def testToRepr(self):
        self.assertEqual(repr(self.fracA), 'Frac(2, 5)')

    def testToCommonDenominator(self):
        self.assertEqual(
            self.fracA.toCommonDenominator(self.fracB),
            (Frac(6,15), Frac(-5,15))
        )

    def testEquals(self):
        self.assertFalse(self.fracA == self.fracB)

    def testNotEquals(self):
        self.assertTrue(self.fracA != self.fracB)
    
    def testLT(self):
        self.assertTrue(self.fracB < self.fracA)
        self.assertFalse(self.fracA < Frac(4,10))

    def testLE(self):
        self.assertTrue(self.fracB <= self.fracA)
        self.assertTrue(self.fracA <= Frac(4,10))

    def testGT(self):
        self.assertTrue(self.fracA > self.fracB)
        self.assertFalse(self.fracA > Frac(4,10))
    
    def testGE(self):
        self.assertTrue(self.fracA >= self.fracA)
        self.assertTrue(self.fracA >= Frac(4,10))
    
    def testAddition(self):
        self.assertEqual(
            self.fracA + self.fracB,
            Frac(1,15)
        )

    def testSubstraction(self):
        self.assertEqual(
            self.fracA - self.fracB,
            Frac(11,15)
        )

    def testMultiplication(self):
        self.assertEqual(
            self.fracA * self.fracB,
            Frac(-2, 15)
        )

    def testDivision(self):
        self.assertEqual(
            self.fracA / self.fracB,
            Frac(-6, 5)
        )

    def testIntegerDivision(self):
        self.assertEqual(
            self.fracA // self.fracB,
            -6 // 5
        )

    def testPlus(self):
        self.assertEqual(self.fracA, +self.fracA)

    def testMinus(self):
        self.assertEqual(-self.fracA, Frac(-2,5))

    def testInverse(self):
        self.assertEqual(~self.fracA, Frac(5,2))
        self.assertEqual(~self.fracB, Frac(-3, 1))

    def testFloatConversion(self):
        self.assertEqual(float(self.fracA), 0.4)

    def testHash(self):
        self.assertEqual(self.fracA.__hash__(), hash(0.4))

if __name__ == '__main__':
    unittest.main()
    