"""Testing division"""
from calc.operations.division import Division
# pylint: disable=too-few-public-methods


def test_division():
    """testing 3 divided by 2"""
    assert Division.divide(3, 2) == 1.5
