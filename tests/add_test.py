"""Testing addition"""
from calc.operations.addition import Addition
# pylint: disable=too-few-public-methods

def test_addition():
    """testing calc result -1"""
    assert Addition.add(3, 2) == 5
