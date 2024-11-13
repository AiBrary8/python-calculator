import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1,-2),-3)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, -2), 6)
        self.assertEqual(self.calc.subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, -2), -8)
        self.assertEqual(self.calc.multiply(4, 2), 8)
        self.assertEqual(self.calc.multiply(-4, -2), 8)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, -2), -5)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-10, 0), "Invalid denominator = 0")

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 8), 2)
        self.assertEqual(self.calc.modulo(10, -8), -6)
        self.assertEqual(self.calc.modulo(-10, 8), 6)
        self.assertEqual(self.calc.modulo(-10, -8), -2)
        self.assertEqual(self.calc.modulo(-10, 0), "Invalid b = 0")
        self.assertEqual(self.calc.modulo(0, -8), 0)

    # Add the following test methods to the TestCalculator class:
#s...
if __name__ == '__main__':
    unittest.main()