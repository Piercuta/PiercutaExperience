import os
from os.path import normpath, basename
import glob
import pandas as pd
import math
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn import preprocessing
from sklearn import utils
from datetime import datetime
import numpy as np
import seaborn as sns


#df1 = pd.DataFrame([['10:51', 1], ['10:52', 2],['10:53', 2]],
#                   columns=['Time_A', 'number_A'])

df = pd.DataFrame([[1,1, 1], [2,2, 2],[2.5,2.6,2.7],[3,3, 3]],
                  columns=['X', 'Y','Z'])

print(df)

print(df.dtypes)
#plt.plot(df.X,df.Y)
#plt.show()
lab_enc = preprocessing.LabelEncoder()
encoded = lab_enc.fit_transform(df.Z)
print(df.dtypes)
print( df.Z)
#print ( encoded)
lr = linear_model.LinearRegression()
columns=['X','Y']
lr.fit(df[columns],df.Z)
print(lr.coef_)
df = pd.DataFrame([[1.5,1.5], [2.2,2.3]],
                  columns=['X', 'Y'])


prediction = lr.predict(df)

print(prediction)




#create_combined_csv(directories)
#pd.set_option('display.max_columns', 500)
#pd.set_option('display.width', 1000)


#big_file = concat_combined_csv("D:\\My Developments\\PiercutaExperience\\Python\\Cooperl\\dataset\\combined_csv\\")
#print(big_file.describe())
#timenotequal = big_file['Débit vapeur four Time'] != big_file['debit fumées Time']
#print(big_file[timenotequal].describe())
#print(big_file[timenotequal].head(1))


#big_file.to_csv("D:\\My Developments\\PiercutaExperience\\Python\\Cooperl\\dataset\\combined_csv\\big_combine_csv\\big_combine_csv.csv",sep = ';', index=False)


##big_file = pd.read_csv("D:\\My Developments\\PiercutaExperience\\Python\\Cooperl\\dataset\\combined_csv\\big_combine_csv\\big_combine_csv.csv",sep = ';')
#print(big_file.shape)
#big_file = big_file.dropna()
#print(big_file.shape)
#print(big_file.tail(5))
#big_file = big_file.rename(index= str, columns={'Débit Farine four Time' : 'Date et Temps'})
#print(big_file.tail(5))
#columns =  big_file.filter(like='Time').columns
#big_file = big_file.drop(columns,axis=1)
#print(big_file.shape)
#big_file.to_csv("D:\\My Developments\\PiercutaExperience\\Python\\Cooperl\\dataset\\combined_csv\\big_combine_csv\\big_final_combine_csv.csv",sep = ';', index=False)

print(big_file.describe())
print(big_file.shape)
t5_negative = big_file['Température TT05 ValueY'] < 0
t5_positive =  big_file['Température TT05 ValueY'] >= 0

print(big_file[t5_negative].shape)
print(big_file[t5_positive].shape)
print(big_file["Débit vapeur four ValueY"].describe())
print(big_file[t5_negative].describe())
big_file = big_file[t5_positive]
print(big_file.shape)
print(big_file.describe())
print(big_file[big_file['Température TT11 ValueY'] == 0].describe())
print(big_file[big_file['K01 ValueY'] < 0].describe())
#print(big_file[big_file['Delta_Chaudière'] < 0].describe())
#print(big_file[big_file['Delta_Chaudière'] < 0].head(2))

big_file["Date et Temps"] = pd.to_datetime(big_file["Date et Temps"],format='%d.%m.%Y %H:%M:%S')

print(big_file.dtypes)
print(big_file["Date et Temps"].head(5))

print (big_file)

dfdb17 = big_file[big_file["Débit vapeur four ValueY"]==17]
dfdb10 = big_file[big_file["Débit vapeur four ValueY"] == 10]
dfdb5 = big_file[big_file["Débit vapeur four ValueY"] == 5]

print(dfdb17.describe())
print(dfdb10.describe())
print(dfdb5.describe())
print(big_file.head(2))
vapeur_Zero = big_file["Débit vapeur four ValueY"] == 0
dfZero = big_file[vapeur_Zero]
print(dfZero.shape)

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

print(dfZero.tail(5))
print( dfZero.describe())

#plt.figure(1)
#i = 1
#for col in columns:
#    plt.subplot(3,3,i)
#    plt.plot(big_file[col],big_file["Débit vapeur four ValueY"])
#    plt.xlabel(col)
#    plt.ylabel("Débit vapeur four ValueY")
#    i+=1
#plt.show()
#columns = ["Date et Temps",
#           "Débit Farine four ValueY",
#           "debit fumées ValueY",
#           "Poussières ValueY",
#           "Température TT11 ValueY",
#           "Température TT12 ValueY",
#           "Débit vapeur four ValueY",
#           "K01 ValueY",
#           "O2 ValueY",
#           "Température TT05 ValueY"]
#columns = ["debit fumées ValueY",
#           "Débit Farine four ValueY",
#           "Poussières ValueY",        
#           "K01 ValueY",
#           "O2 ValueY",
#           "Température TT05 ValueY"]
#plot_correlation_heatmap(big_file[columns])

print(dfdb17[columns].describe())
print(dfdb10[columns].describe())
print(dfdb5[columns].describe())

#plt.plot(big_file["Débit Farine four ValueY"],big_file["Débit vapeur four ValueY"])
#plt.show()

#best_features = SelectKBest(k=5)
#bf = best_features.fit(big_file[columns],big_file["Débit vapeur four ValueY"])
#bfscores = pd.DataFrame(bf.scores_)
#bfcolumns = pd.DataFrame(big_file[columns].columns)
#featureScores = pd.concat([bfcolumns,bfscores],axis=1)
#featureScores.columns = ['Specs','Score']  #naming the dataframe columns
#print(featureScores.nlargest(10,'Score'))

d1 = datetime(2018,12,2,0,0,0)
d2 = datetime(2018,12,2,23,59,59)

newdf = pd.DataFrame(columns = big_file.columns)
print(newdf.columns)
cpt = 1
for i in range(8,12):
    for j in range(1,31):
        d1 = datetime(2018,i,j,0,0,0)
        d2 = datetime(2018,i,j,23,59,59)
        t_test1 = (big_file['Date et Temps'] >= d1) & (big_file['Date et Temps'] <= d2)
        ter1 = big_file[t_test1].mean()
        print(ter1)
        newdf = newdf.append(big_file[t_test1].mean(),ignore_index = True)
        cpt += 1
        print(newdf)

#plt.figure(1)
#for index,col in enumerate(columns):
#    plt.subplot(3,3,index+1)
#    plt.plot(newdf[col],newdf["Débit vapeur four ValueY"])
#    plt.xlabel(col)
#    plt.ylabel("Débit vapeur four ValueY")
#plt.show()

print(newdf.shape)
print(newdf.describe())
lr1 = linear_model.LinearRegression()
lr1.fit(newdf[columns],newdf["Débit vapeur four ValueY"])
print('r2 : ',lr1.score(newdf[columns],newdf["Débit vapeur four ValueY"]))


#t_test1 = (big_file['Date et Temps'] >= d1) & (big_file['Date et Temps'] <= d2)

#t_test2 = (big_file['Date et Temps'].month == 12) & (big_file['Date et Temps'].month == 2)

print(big_file[columns].head(1))
lr = linear_model.LinearRegression()
lr.fit(big_file[columns],big_file["Débit vapeur four ValueY"])
r2 = lr.score(big_file[columns],big_file["Débit vapeur four ValueY"])
print ('r2 : ',r2)
coefs = lr.coef_
intercept = lr.intercept_
params = big_file[columns].columns
print(len(coefs))
print(len(params))
print('{:25} {:<25}'.format('Variables','Coefs'))
for i in range(0,len(params)):
    print('{:25} {:<25}'.format(params[i],coefs[i]))

print('{:25} {:<25}'.format('Intercept',intercept)) 

#print([lr.coef_,big_file[columns].columns])

joblib.dump(lr, 'First_Linear_regression.pkl')
res = cross_val_score(lr, big_file[columns],big_file["Débit vapeur four ValueY"],cv = 4)
accuracy = res.mean()
print("scores linea regression : " , accuracy)

#sr = linear_model.SGDRegressor(max_iter=1000, tol=1e-3)
#sr.fit(big_file[columns],big_file["Débit vapeur four ValueY"])
#print(cross_val_score(sr, big_file[columns],big_file["Débit vapeur four ValueY"],cv = 4).mean())
#la = linear_model.Lasso()
#la.fit(big_file[columns],big_file["Débit vapeur four ValueY"])
#print("score lasso  : ",cross_val_score(la, big_file[columns],big_file["Débit vapeur four ValueY"],cv = 4).mean())

#le = linear_model.ElasticNet()
#le.fit(big_file[columns],big_file["Débit vapeur four ValueY"])
#print("score elasticNet",cross_val_score(le, big_file[columns],big_file["Débit vapeur four ValueY"],cv = 4).mean())


#plt.plot(big_file["Date et Temps"],big_file["Débit vapeur four ValueY"])
#plt.show()

#concat_combined_csv("D:\\My Developments\\PiercutaExperience\\Python\\Cooperl\\dataset\\combined_csv\\").to_csv("D:\\My Developments\\PiercutaExperience\\Python\\Cooperl\\dataset\\combined_csv\\big_combine_csv\\big_combine_csv.csv",sep = ';', index=False)



#df1 = pd.DataFrame([['10:51', 1], ['10:52', 2],['10:53', 2]],
#                   columns=['Time_A', 'number_A'])
#df2 = pd.DataFrame([['10:50', 1], ['10:52', 2],['10:53', 2]],
#                   columns=['Time_B', 'number_B'])
#df3 = pd.DataFrame([['c', 3, 'cat'], ['d', 4, 'dog']],
#                   columns=['letter', 'number', 'animal'])

#df = pd.concat([df1, df2], sort=False, ignore_index=True)

#print(df)

#print(pd.merge(df,df,left_on ='Time_A',right_on='Time_B', how='left'))

#print(df)
##df = df.dropna()
##print(df)

##df = df.rename(index= str, columns={'Time_A' : 'Time','Time_B' : 'Time'})

##df = df.merge(df.Time_B,how='outer' )

#v = df.filter(like='Time')
#colmuns_name = v.columns
#for col in colmuns_name:
#    if


#print(v)



#print(df.Time)


pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

columns = big_file.columns.difference(["Débit vapeur four ValueY"
                                       ,"Date et Temps"
                                       #,"O2 ValueY"
                                       #,"debit fumées ValueY"
                                       #,"Température TT12 ValueY"
                                       #,"Débit Farine four ValueY"
                                       #,"Poussières ValueY"
                                       #,"Température TT11 ValueY"
                                       #,"K01 ValueY"
                                       #,"Température TT05 ValueY"
                                       ])
print(blr.best_linear_regression.__doc__)

