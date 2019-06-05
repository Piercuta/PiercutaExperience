"""projetc for cooperl - arc atlantique"""
import os
from os.path import normpath, basename
import pandas as pd
import math
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn import preprocessing
from sklearn import utils
from datetime import datetime
import numpy as np
import seaborn as sns
from sklearn.externals import joblib
from sklearn.model_selection import cross_val_score
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import tool_linear_regression as tlr
import tool_features_selection as tfs




pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
#tfs.plot_correlation_heatmap(df_selected)


############################################################# for testing small csv file ###########################################################################


df_selected = pd.read_csv("D:/My Developments/PiercutaExperience/Python/Cooperl/dataset/Analyse tonnage vapeur four - Données compilées .csv",sep = ';')
print (df_selected.dtypes)
df_selected["Date"] = pd.to_datetime(df_selected["Date"],format='%m/%d/%Y')
df_selected = df_selected.dropna()

# should correspond to the excel gaetan document score 0.99 TODO try on excel.
#lr = linear_model.LinearRegression()
#lr.fit(df_selected[['O2', 'Debit farine', 'Debit fumée', 'delta T']], df_selected['2FT01 (débit vapeur)'])
#print(lr.score(df_selected[['O2', 'Debit farine', 'Debit fumée', 'delta T']], df_selected['2FT01 (débit vapeur)']))

best_lr, r2_max, best_subset = tlr.best_linear_regression(df_selected.select_dtypes(include = ['float64','int64']), '2FT01 (débit vapeur)')
print(df_selected.shape)
print(best_lr)
print(r2_max)
print(best_subset)

tlr.target_approx(best_lr, df_selected, best_subset, 'target_approx')
print (df_selected.shape)
print (df_selected.head(5))

tlr.graph_compare(df_selected['Date'], df_selected['2FT01 (débit vapeur)'], df_selected['target_approx'])


############################################################# for testing big file combine ###########################################################################


#df_selected = pd.read_csv("D:/My Developments/PiercutaExperience/Python/Cooperl/dataset/combined_csv/big_combine_csv/big_final_combine_csv.csv",sep = ';')
#print(df_selected.dtypes)
#df_selected["Date et Temps"] = pd.to_datetime(df_selected["Date et Temps"],format='%d.%m.%Y %H:%M:%S')
#df_selected = df_selected.dropna()


#best_lr, r2_max, best_subset = tlr.best_linear_regression(df_selected.select_dtypes(include = ['float64','int64']), 'Débit vapeur four ValueY')
#print(df_selected.shape)
#print(best_lr)
#print(r2_max)
#print(best_subset)

#tlr.target_approx(best_lr, df_selected, best_subset, 'target_approx')

#tlr.graph_compare(df_selected['Date et Temps'], df_selected['Débit vapeur four ValueY'],df_selected['target_approx'])






