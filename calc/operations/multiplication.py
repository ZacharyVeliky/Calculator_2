"""Subtraction class"""
from calc.operations.calculation import Calculation
# pylint: disable=too-few-public-methods


class Multiplication(Calculation):
    """Multiplying numbers"""
    @staticmethod
    def multiply(value_a: int, value_b: int):
        """Do the multiplication"""
        return value_a * value_b
