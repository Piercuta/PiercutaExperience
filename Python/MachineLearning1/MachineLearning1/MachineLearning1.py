# - *- coding: utf-8 -*-
"""Machinelaerning1.py : machine learning experience tree cover type"""
import pandas as pd
import math
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDRegressor

"""Machinelaerning1.py : test with population of barcelona"""
df = pd.read_csv("D:\\My Developments\\PiercutaExperience\\Python\\MachineLearning1\\barcelona_datasets\\population.csv");

columnpopulation = []
for year in df.Year.unique():
    booltemp = df.Year == year
    boolmale = df.Gender == 'Male'
    boolfemale = df.Gender == 'Female'
    print("the population in " + str(year) + " is ",df[booltemp].Number.sum())
    print("male : ",df[booltemp & boolmale].Number.sum())
    print("female : ",df[booltemp & boolfemale].Number.sum())
    columnpopulation.append(df[booltemp].Number.sum())

years = df.Year.unique()
submission = {"Year" : years,
              "Population" : columnpopulation
    }
newdf = pd.DataFrame(submission)
#liste district.name en constante évolution
print(newdf.shape)
print (newdf)
district_names = df['District.Name'].unique()

plt.figure(1)
plt.subplot(4,4,1)

plt.scatter(newdf.Year,newdf.Population)
plt.plot(newdf.Year,newdf.Population)
plt.xlabel("year")
plt.ylabel("population")
plt.title("barcelona ")
#plt.show()

def pouplationYears_districtName(df, crtieria):
    res = []
    for year in years:
           booltemp = df.Year == year
           res.append(df[crtieria & booltemp].Number.sum())
    mydict = {"Year" : years,
              "Population" : res
    }
    return pd.DataFrame(mydict)

nbsubplot = 2
for namedistrict in district_names:
    district_name_value = pouplationYears_districtName(df, df['District.Name'] == namedistrict)
    plt.subplot(4,4,nbsubplot)
    plt.scatter(district_name_value.Year,district_name_value.Population)
    plt.plot(district_name_value.Year,district_name_value.Population)
    plt.xlabel("year")
    plt.ylabel("population")
    plt.title(namedistrict)
    nbsubplot+=1
    
plt.show()   


#print(df.Number.sum())
#print(df['Neighborhood.Name'].describe())

#col_types = df.dtypes;
#dims = df.shape;
#print (col_types);
#print (dims);
#print (df.head(5));
#print(df.describe())

#print(df.Immigrants.max())
#print (df.groupby('Age').size())
#df = df.sort_values(by = 'Immigrants', ascending = False)

#print(df.Immigrants.sum())

#print(df.head(5))
#print (df.loc[df.Number == df.Number.max()])



#plt.plot(df.Longitude, df.Latitude)
#plt.show()

#print(df.Transport.unique())

#val = df.Transport.unique()


#print(val[1])
#nightbusbool = df.Transport == val[1]

#print(df.Longitude[nightbusbool].head(5))

#print(df.Longitude.shape)
#print(df.Longitude[nightbusbool].shape)
#print(df['District.Name'].describe())
#plt.plot(df.Longitude[nightbusbool], df.Latitude[nightbusbool])
#plt.show()

#plt.barh(df.Age, 2)
#plt.show()

