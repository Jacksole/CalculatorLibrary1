"""
Unit Test for the calculator library
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)

    def test_division(self):
        asset 5 == calculator.divide(25, 5)

    def mod_div(self):
        asset 1 == calculator.mod_div(5, 2)
