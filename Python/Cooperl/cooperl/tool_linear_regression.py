"""list of fucntions used to find the best linear regression form a dataframe"""
import pandas as pd
import itertools
from sklearn import linear_model
import matplotlib.pyplot as plt

def best_linear_regression(dataframe, target):
    """Function searching the best linear regression from all features combination"""
    columns = dataframe.columns.difference([target])
    best_lr = linear_model.LinearRegression()
    r2_max = 0
    cpt = 0
    for k in range(1,len(columns)):
        for subset in combination_n_k(columns,k):
            lr = linear_model.LinearRegression()
            lr.fit(dataframe[list(subset)],dataframe[target])
            cpt += 1
            print (cpt)
            r2 = lr.score(dataframe[list(subset)],dataframe[target])
            if r2 > r2_max :
                best_lr, r2_max, best_subset = lr,r2, subset
    return (best_lr , r2_max, best_subset)
    

def combination_n_k(list_elem, k):
        return itertools.combinations(list_elem,k)

def target_approx(lr,dataframe, subset, target_approx_name):
    """build a new column of linear regression model prediction"""
    dataframe[target_approx_name] = lr.predict(dataframe[list(subset)]) 

def  graph_compare(X, real_Y, approx_Y):
    """scatter two curves (the approx and the real values)"""
    plt.figure(1)
    plt.plot(X,real_Y,color = 'blue' , label = 'real')
    plt.xlabel('time')
    plt.ylabel("target")
    plt.plot(X,approx_Y, color = 'red', label = 'approx')
    plt.legend()
    plt.show()