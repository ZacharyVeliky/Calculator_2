"""Subtraction class"""
from calc.operations.calculation import Calculation
# pylint: disable=too-few-public-methods


class Subtraction(Calculation):
    """Subtracting numbers"""

    def get_result(self):
        """get the subtraction results"""
        result = 0.0
        for value in self.values:
            result = result - value
        return result
