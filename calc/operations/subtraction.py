"""Subtraction class"""
from calc.operations.calculation import Calculation
# pylint: disable=too-few-public-methods


class Subtraction(Calculation):
    """Subtracting numbers"""
    @staticmethod
    def subtract(value_a: int, value_b: int):
        """Do the subtraction"""
        return value_a - value_b
