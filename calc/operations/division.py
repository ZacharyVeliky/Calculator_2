"""Division class"""


class Division:
    @staticmethod
    def divide(value_a: int, value_b: int):
        try:
            return value_a / value_b
        except Exception as e:
            return e

