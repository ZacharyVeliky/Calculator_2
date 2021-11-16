"""Calculation Class"""


class Calculation:
    """ Abstraction"""

    def __init__(self, values: tuple):
        """ constructor method"""
        self.values = Calculation.convert_args_to_tuple_of_float(values)

    @classmethod
    def create(cls, values: tuple):
        """ instantiate objects"""
        return cls(values)

    @staticmethod
    def convert_args_to_tuple_of_float(values):
        """ Turn values to a list of floats"""
        list_values_float = []
        for item in values:
            list_values_float.append(float(item))
        return tuple(list_values_float)
