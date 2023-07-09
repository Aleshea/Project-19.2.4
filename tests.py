import pytest
from calculator import Calculator

class TestCalculator:

    def setup(self):
        self.calc = Calculator


    # Сложение
    def test_adding_success(self):
        assert self.calc.adding(self, 12, 3) == 15

    # Вычитание
    def test_subtractioning_success(self):
         assert self.calc.subtraction(self, 20, 2) == 18

    # Умножение
    def test_multiplying_success(self):
        assert self.calc.multiply(self, 3, 4) == 12

    # Деление
    def test_divisioning_success(self):
        assert self.calc.division(self, 40, 10) == 4

    def teardown(self):
        print('Выполнено')