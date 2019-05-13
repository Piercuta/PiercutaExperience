# - *- coding: utf-8 -*-
"""Machinelaerning1.py : machine learning experience tree cover type"""

import pandas as pd

df = pd.read_csv("D:\\My Developments\\PiercutaExperience\\Python\\MachineLearning1\\train.csv");
col_types = df.dtypes;
dims = df.shape;
print (col_types);
print (dims);
print (df.head(5));
print(df.ftypes);
print(df.Aspect.nunique())
print(df.Id.nunique())

print(df.head(5))

df_first_five = df.head(5)
boolex = df_first_five.Aspect == 51
print (df_first_five[boolex])
var = df.count(axis='columns')
print (var.nunique())
print(df.describe())