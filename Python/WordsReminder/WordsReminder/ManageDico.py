# - *- coding: utf-8 -*-
import os
import pickle

dicoFileName = "monthly_dictionnary"

def recup_dico():
    if os.path.exists(dicoFileName):
        monthlyDictionnary = open(dicoFileName, "rb")
        myDeplicker = pickle.Unpickler(monthlyDictionnary)
        myDico = myDeplicker.load()
        monthlyDictionnary.close()
    else:
        myDico = {}
    return myDico

def save_dico(dico):
     monthlyDictionnary = open(dicoFileName, "wb")
     myDeplicker = pickle.Pickler(monthlyDictionnary)
     myDeplicker.dump(dico)
     monthlyDictionnary.close()



