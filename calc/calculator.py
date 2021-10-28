""" This is the increment function"""
from calc.operations.addition import Addition
from calc.operations.subtraction import Subtraction
from calc.operations.multiplication import Multiplication
from calc.operations.division import Division


def inc(value_a):
    """ Increment function adds one to the input value"""
    return value_a + 1


class Calculator:
    """This is the calculator class"""
    calculation = list[0]

    def __init__(self):
        self.result = 0

    def get_result(self):
        """get result of calculation"""
        return self.result

    @staticmethod
    def add_numbers(value_a, value_b):
        """ Adds number to result"""
        return Addition.add(value_a, value_b)

    @staticmethod
    def subtract_numbers(value_a, value_b):
        """ Subtracts value a from value b"""
        return Subtraction.subtract(value_a, value_b)

    @staticmethod
    def multiply_numbers(value_a, value_b):
        """ Multiplies number with result"""
        return Multiplication.multiply(value_a, value_b)

    @staticmethod
    def divide_numbers(value_a, value_b):
        """ Divides result by number"""
        return Division.divide(value_a, value_b)
