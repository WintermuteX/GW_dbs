import unittest

from CalcCode import *

class TestCalculator(unittest.TestCase):

    def test_calculator_add_method(self):
        result = addition(6,5)
        self.assertEqual(11, result)
        result = addition(6,1)
        self.assertEqual(7, result)
        result = addition(-6,5)
        self.assertEqual(-1, result)
        result = addition(-6,22)
        self.assertEqual(16, result)

    def test_calculator_subtract_method(self):
        result = subtract(6,5)
        self.assertEqual(1, result)
        result = subtract(6,1)
        self.assertEqual(5, result)
        result = subtract(-6,5)
        self.assertEqual(-11, result)
        result = subtract(-6,22)
        self.assertEqual(-28, result)
        
    def test_calculator_multiplication_method(self):
        result = multiplication(6,5)
        self.assertEqual(30, result)
        result = multiplication(20,-2)
        self.assertEqual(-40, result)
        result = multiplication(5,5)
        self.assertEqual(25, result)        
        
    def test_calculator_division_method(self):
        result = division(100, 10.0)
        self.assertEqual(10, result)
        result = division(20,-2.0)
        self.assertEqual(-10, result)
        result = division(20,5)
        self.assertEqual(4, result)        
        
    def test_calculator_sqroot(self):
        result = sqroot(9)
        self.assertEqual(3, result)
        result = sqroot(16)
        self.assertEqual(4, result)
        result = sqroot(1)
        self.assertEqual(1, result)
        
    def test_calculator_factorial(self):
        result = factorial(5)
        self.assertEqual(120, result)
        result = factorial(10)
        self.assertEqual(3628800, result)
        result = factorial(1)
        self.assertEqual(1, result)
        
    def test_calculator_modulo(self):
        result = mod(5,2)
        self.assertEqual(1, result)
        result = mod(9,10)
        self.assertEqual(9, result)
        result = mod(24, 8)
        self.assertEqual(0, result)
        
    def test_calculator_power(self):
        result = power(5,2)
        self.assertEqual(25, result)
        result = power(1,2)
        self.assertEqual(1, result)
        result = power(4, 3)
        self.assertEqual(64, result)
        
    def test_calculator_log(self):
        result = log(10)
        self.assertEqual(1, result)
        result = log(100)
        self.assertEqual(2, result)
        result = log(50)
        self.assertEqual(1.699, round(result,3))
        
    def test_calculator_hypotenuse(self):
        result = hypotenuse(4,3)
        self.assertEqual(5, result)
        result = hypotenuse(1,2)
        self.assertEqual(sqroot(5), result)
        result = hypotenuse(1, 1)
        self.assertEqual(sqroot(2), result)
    
    def test_calculator_cube(self):
        result = cube(4)
        self.assertEqual(64, result)
        result = cube(1)
        self.assertEqual(1, result)
        result = cube(5)
        self.assertEqual(125, result)
        
    def test_calculator_cube_root(self):
        result = cubeRoot(64)
        self.assertEqual(4, round(result,4))
        result = cubeRoot(1)
        self.assertEqual(1, result)
        result = cubeRoot(-1000)
        self.assertEqual(-10, round(result,4))
    
        
        

if __name__ == '__main__':
    unittest.main()   
