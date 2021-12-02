"""Main"""
import glob
import os
import shutil
import time

# pylint: disable=anomalous-backslash-in-string, invalid-name, unspecified-encoding
# pylint: disable=unnecessary-comprehension,consider-using-with

import pandas as pd

from calc.operations.addition import Addition
from calc.operations.subtraction import Subtraction
from calc.operations.multiplication import Multiplication
from calc.operations.division import Division


print("Reading input folder")
dir_name = os.path.dirname(__file__)
folder = os.path.join(dir_name, 'input')

files = glob.glob(folder + "/*.csv")
record_number = 1

f = open("calc\log " + str(int(time.time())) + ".txt", 'a')

for file in files:
    nums = pd.read_csv(file)
    num_list = []
    for num in nums:
        num_list.append(num)
    nums_tuple = tuple(num_list)
    addition = Addition(nums_tuple)
    f.write(str(int(time.time())) + ": " + os.path.basename(file) + " Record: " + str(
        record_number) + " Addition Result = " + str(int(addition.get_result())) + "\n")
    record_number += 1

for file in files:
    nums = pd.read_csv(file)
    num_list = []
    for num in nums:
        num_list.append(num)
    nums_tuple = tuple(num_list)
    subtract = Subtraction(nums_tuple)
    f.write(str(int(time.time())) + ": " + os.path.basename(file) + " Record: " + str(
        record_number) + " Subtraction Result = " + str(int(subtract.get_result())) + "\n")
    record_number += 1

for file in files:
    nums = pd.read_csv(file)
    num_list = [item for item in nums]
    nums_tuple = tuple(num_list)
    multiply = Multiplication(nums_tuple)
    try:
        f.write(str(int(time.time())) + ": " + os.path.basename(file) + " Record: " + str(
            record_number) + " Multiplication Result = " + str(int(multiply.get_result())) + "\n")
    except OverflowError as error:
        f.write(str(int(time.time())) + ": " + os.path.basename(file) + " Record: " + str(
            record_number) + " Multiplication Result = " + str(error) + "\n")

    record_number += 1

for file in files:
    nums = pd.read_csv(file)
    num_list = []
    for num in nums:
        num_list.append(num)
    nums_tuple = tuple(num_list)
    divide = Division(nums_tuple)
    f.write(str(int(time.time())) + ": " + os.path.basename(file) + " Record: " + str(
        record_number) + " Division Result = " + str(divide.get_result()) + "\n")
    record_number += 1

shutil.move(file, dir_name + '\output')
f.close()
