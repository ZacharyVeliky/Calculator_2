"""Testing addition"""
import pandas as pd
from calc.operations.addition import Addition


# pylint: disable=too-few-public-methods

def test_addition_10_val():
    """testing calc result"""
    nums = pd.read_csv('tests/csv/10_1.csv')
    addition = Addition(nums)
    assert addition.get_result() == 10


def test_addition_10000_val():
    """testing calc result"""
    nums = pd.read_csv('tests/csv/10000_1.csv')
    addition = Addition(nums)
    assert addition.get_result() == 196141
