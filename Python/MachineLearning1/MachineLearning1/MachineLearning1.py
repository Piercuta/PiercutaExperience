# - *- coding: utf-8 -*-
"""Machinelaerning1.py : machine learning experience tree cover type"""

import pandas as pd

df = pd.read_csv("D:\\My Developments\\PiercutaExperience\\Python\\MachineLearning1\\train.csv");
col_types = df.dtypes;
dims = df.shape;
print (col_types);
print (dims);