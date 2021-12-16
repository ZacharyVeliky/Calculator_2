import os
import pandas as pd


class Read:
    @staticmethod
    def ReadCSV(filename):
        data = pd.read_csv(os.path.abspath(filename))
        return data

    @staticmethod
    def CSVLength(filename):
        length = pd.read_csv(os.path.abspath(filename))
        return len(length.index)
