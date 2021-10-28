"""Testing multiplication"""
from calc.operations.multiplication import Multiplication


def test_multiply():
    """testing 3 multiplied by 2"""
    assert Multiplication.multiply(3, 2) == 6
