import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
       assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_failed(self):
       assert self.calc.multiply(self, 2, 2) == 5

    def test_division_correctly(self):
       assert self.calc.division(self, 10, 2) == 5

    def test_division_failed(self):
       assert self.calc.division(self, 10, 1) == 5

    def test_adding_correctly(self):
       assert self.calc.adding(self, 110, 200) == 310

    def test_adding_failed(self):
       assert self.calc.adding(self, 110, 200) == 18

    def test_subtraction_correctly(self):
        assert self.calc.subtraction(self, 30, 5) == 25

    def test_subtraction_failed(self):
        assert self.calc.subtraction(self, 40, 30) == 100