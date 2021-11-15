"""Division class"""
from calc.operations.calculation import Calculation


# pylint: disable=too-few-public-methods
# pylint: disable=broad-except


class Division(Calculation):
    """Dividing numbers"""

    def get_result(self):
        """Do the division if not dividing by zero"""
        result = self.values
        for value in self.values:
            try:
                return result / value
            except Exception as error:  # change to raise
                return error

        result = int(self.values(0))
        try:
            result /= int(self.values(1))
            return result
        except Exception as e:
            raise "Divided by zero"
