import os

import pandas as pd


class Read:
    @staticmethod
    def ReadCSV(filename):
        data = pd.read_csv(os.path.abspath(filename))
        #data.set_index(['input_1'], inplace=True)
        return data

