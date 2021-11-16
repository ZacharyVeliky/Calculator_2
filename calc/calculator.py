""" This is the increment function"""
from calc.history.calculations import Calculations


def inc(value_a):
    """ Increment function adds one to the input value"""
    return value_a + 1


class Calculator:
    """This is the calculator class"""

    @staticmethod
    def get_last_result_value():
        """ This is the gets the result of the calculation"""
        # I made this method so that I don't have more than one action per function
        return Calculations.get_last_calculation_result_value()

    @staticmethod
    def add_numbers(tuple_num: tuple):
        """ Adds number to result"""
        return Calculations.add_addition(tuple_num)

    @staticmethod
    def subtract_numbers(tuple_num: tuple):
        """ Subtracts value a from value b"""
        return Calculations.add_subtraction(tuple_num)

    @staticmethod
    def multiply_numbers(tuple_num: tuple):
        """ Multiplies number with result"""
        return Calculations.add_multiplication(tuple_num)

    @staticmethod
    def divide_numbers(tuple_num: tuple):
        """ Divides result by number"""
        return Calculations.add_division(tuple_num)
