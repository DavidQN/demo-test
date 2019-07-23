import unittest
from calc import Calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        # Test Add with simple integers
        self.assertAlmostEqual(Calculator.add(2,2), 4)
        self.assertAlmostEqual(Calculator.add(10,11), 21)
        self.assertAlmostEqual(Calculator.add(4,2), 6)
        
    def test_add_values(self):
        # Make sure value errors are raised when necessary. 
        # This function should only accept integers
        self.assertRaises(ValueError, Calculator.add, "asda", "asdasd")
        self.assertRaises(ValueError, Calculator.add, {}, [])

    def test_divide(self):
        # Test division
        self.assertAlmostEqual(Calculator.divide(8,2), 4)
        self.assertAlmostEqual(Calculator.divide(9,2), 4.5)
        self.assertAlmostEqual(Calculator.divide(5,4), 1.25)

    def test_multiply(self):
        # Test multiply
        self.assertAlmostEqual(Calculator.multiply(2, 4), 8)
        self.assertAlmostEqual(Calculator.multiply(5, 5), 25)
        self.assertAlmostEqual(Calculator.multiply(3.3, 6.5), 21.45)
        