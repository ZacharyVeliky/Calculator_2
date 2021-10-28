"""Testing subtraction"""
from calc.operations.subtraction import Subtraction


def test_subtraction():
    """testing calc result -1"""

    assert Subtraction.subtract(1, 2) == -1
