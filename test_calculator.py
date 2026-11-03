import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # Add the following test methods to the TestCalculator class:

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, 2), 1)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(1, 2), -1)
        self.assertEqual(self.calc.subtract(21, 2), 19)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3,0),0)
        self.assertEqual(self.calc.multiply(-3,3),-9)

    def test_divide(self):
        self.assertEqual(self.calc.divide(3,1),3)
        self.assertEqual(self.calc.divide(3,3),1)    

    def test_module(self):
        self.assertEqual(self.calc.modulo(3,1),0)
        self.assertEqual(self.calc.modulo(17,6),5)    
    
   

if __name__ == '__main__':
    unittest.main()