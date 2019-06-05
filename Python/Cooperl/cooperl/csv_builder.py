"""class for creating a big csv file to analyse as datframe.
    a lot of functions are very specific.
    TODO make it more generic."""
import os
from os.path import normpath, basename
import glob
import math

dir1 = "D:\\My Developments\\PiercutaExperience\\Python\\\Cooperl\\\dataset\\b Deb far\\"
dir2 = "D:\\My Developments\\PiercutaExperience\\Python\\\Cooperl\\\dataset\\b Deb fum\\"
dir3 = "D:\\My Developments\\PiercutaExperience\\Python\\\Cooperl\\\dataset\\b FT11\\"
dir4 = "D:\\My Developments\\PiercutaExperience\\Python\\\Cooperl\\\dataset\\Debit vapeur\\"
dir5 = "D:\\My Developments\\PiercutaExperience\\Python\\\Cooperl\\\dataset\\K01\\"
dir6 = "D:\\My Developments\\PiercutaExperience\\Python\\\Cooperl\\\dataset\\O2\\"
dir7 = "D:\\My Developments\\PiercutaExperience\\Python\\\Cooperl\\\dataset\\TT05\\"

directories = [dir1,dir2,dir3,dir4,dir5,dir6,dir7]

def concat_csv(directory):
    """function concatenating all csv file into dataframe"""
    os.chdir(directory)
    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    df = pd.DataFrame()
    for file in all_filenames:
        path = directory+file
        dftemp = pd.read_csv(path,sep = ';', encoding = "utf-16");
        print(dftemp.dtypes)
        print(dftemp.shape)
        #dftemp["Débit vapeur four ValueY"].astype(float)
        df = pd.concat([df,dftemp],sort=False)
    return df

def create_combined_csv(directories):
    """function concatenating all files in dir and creating a csv file"""
    for dir in directories:
        df = concat_csv(dir)
        prefix = os.path.basename(normpath(dir)) 
        df.to_csv( "D:\\My Developments\\PiercutaExperience\\Python\\Cooperl\\dataset\\combined_csv\\"+prefix+"_combined_csv.csv",sep = ';', index=False, encoding='utf-8-sig')


def concat_combined_csv(directory):
    """function create a big final csv file"""
    os.chdir(directory)
    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    df = pd.DataFrame()
    for file in all_filenames:
        path = directory+file
        dftemp = pd.read_csv(path,sep = ';')
        df = pd.concat([df,dftemp],sort=False, axis=1)
    return df
