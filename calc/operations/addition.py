"""Addition class"""
from calc.operations.calculation import Calculation
# pylint: disable=too-few-public-methods


class Addition(Calculation):
    """Adding numbers"""
    @staticmethod
    def add(value_a: int, value_b: int):
        """Do the addition"""
        return value_a + value_b
