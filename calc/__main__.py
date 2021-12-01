import glob
import os

import pandas as pd

from calc.operations.addition import Addition

dir_name = os.path.dirname(__file__)
folder = os.path.join(dir_name, 'input')
directories = os.listdir(folder)

# remove after testing
files = glob.glob(folder + "/*.csv")

for file in files:
    nums = pd.read_csv(file)
    print(Addition.get_result(nums))
