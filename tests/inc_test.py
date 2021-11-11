""" content of calculator.py#"""
import calc.calculator as calc
# pylint: disable=too-few-public-methods


def test_answer():
    """This Tests the function"""
    assert calc.inc(4) == 5
