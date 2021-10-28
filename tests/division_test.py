"""Testing division"""
from calc.operations.division import Division


def test_division():
    """testing 3 divided by 2"""
    assert Division.divide(3, 2) == 1.5
