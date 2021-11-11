"""Division class"""
# pylint: disable=too-few-public-methods
# pylint: disable=broad-except
# pylint: disable=invalid-name


class Division:
    """Dividing numbers"""
    @staticmethod
    def divide(value_a: int, value_b: int):
        """Do the division if not dividing by zero"""
        try:
            return value_a / value_b
        except Exception as e:
            return e
