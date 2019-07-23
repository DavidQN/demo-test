import unittest
from circles import circle_area
from math import pi

# We can notice here, that with assertAlmostEqual, the left hand is the input
# the right hand is the expected answer
# To run, enter in bash shell

class TestCircleArea(unittest.TestCase):
    
    def test_area(self):
        # Test areas when radius >= 0
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)

    def test_values(self):
        # Make sure value errors are raised when necessary
        self.assertRaises(ValueError, circle_area, -2)