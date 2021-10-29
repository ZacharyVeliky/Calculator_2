"""Division class"""


class Division:
    """Dividing numbers"""
    @staticmethod
    def divide(value_a: int, value_b: int):
        try:
            return value_a / value_b
        except Exception as e:
            return e

