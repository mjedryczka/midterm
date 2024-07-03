"""Testing Calculator side of math operations"""
from calculator import Calculator

def test_addition():
    """Test addition"""
    assert Calculator.add(2,2) == 4

def test_subtraction():
    """Test subtraction"""
    assert Calculator.subtract(2,2) == 0

def test_divide():
    """Test division"""
    assert Calculator.divide(2,2) == 1

def test_multiply():
    """Test multiplication"""
    assert Calculator.multiply(2,2) == 4
