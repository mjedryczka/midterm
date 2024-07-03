"""Calculation Testing"""
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("num1, num2, operation, expected", [
    (Decimal('10'), Decimal('5'), add, Decimal('15')),
    (Decimal('10'), Decimal('5'), subtract, Decimal('5')),
    (Decimal('10'), Decimal('5'), multiply, Decimal('50')),
    (Decimal('10'), Decimal('2'), divide, Decimal('5')),
    (Decimal('10.5'), Decimal('0.5'), add, Decimal('11.0')),
    (Decimal('10.5'), Decimal('0.5'), subtract, Decimal('10.0')),
    (Decimal('10.5'), Decimal('2'), multiply, Decimal('21.0')),
    (Decimal('10'), Decimal('0.5'), divide, Decimal('20')),
])
def test_calculation_operations(num1, num2, operation, expected):
    """Test operations"""
    calc = Calculation(num1, num2, operation)
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {num1} and {num2}"

def test_calculation_repr():
    """Test the return value of __repr__ of a calculation object"""
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "add 10 5 15"
    assert calc.__repr__() == expected_repr, "The __repr__ method output does not match the expected string."

def test_divide_by_zero():
    """Test division by zero"""
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    assert calc.perform() == "ValueError: Cannot divide by zero", "Divide by Zero Failure"
