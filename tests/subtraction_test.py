"""Testing subtraction"""
from calc.operations.subtraction import Subtraction
# pylint: disable=too-few-public-methods


def test_subtraction():
    """testing calc result -1"""

    assert Subtraction.subtract(1, 2) == -1
