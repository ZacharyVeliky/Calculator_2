"""Testing addition"""
from calc.operations.addition import Addition
from pathlib import Path
import pandas as pd


# pylint: disable=too-few-public-methods

def test_addition():
    """testing calc result"""
    nums = pd.read_csv("10val1.csv", sep=",")
    addition = Addition(nums)
    assert addition.get_result() == 5.0
