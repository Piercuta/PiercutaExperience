# - *- coding: utf-8 -*-
import os
import pickle
import datetime
import re

my_monthly_dico_filename = "monthly_dictionnary"
my_full_dico_filename = "full_dictionnary"

def recup_dico(dico_filename):
    """function to get the dictionnary (accordinghis name) from binary file"""
    if os.path.exists(dico_filename):
        binary_dictionnary = open(dico_filename, "rb")
        my_deplicker = pickle.Unpickler(binary_dictionnary)
        my_dico = my_deplicker.load()
        binary_dictionnary.close()
    else:
        my_dico = Dictionnary()
    return my_dico

def save_dico(dico_filename,my_new_dico):
    """function to save the dictionnary as a binary file"""
    binary_dictionnary = open(dico_filename, "wb")
    my_deplicker = pickle.Pickler(binary_dictionnary)
    my_deplicker.dump(my_new_dico)
    binary_dictionnary.close()

def def_and_confirmation()->(str,bool):
    """function to interact with the user asking a definition and a confirmation
       it returns a tuple"""
    definition = input_checking("Tapez un mot puis sa définition (format -> 'Mot : def') \n", r"[a-zA-ZÀ-ÿ]+\s:{1}\s[a-zA-ZÀ-ÿ]+")
    confirmation = input_checking("Confirmez vous ce mot et sa définition ? y or n \n",r"^(y|n)$")
    if confirmation == 'y':
        confirmation = True
    else:
        confirmation = False
    return (definition , confirmation)

def input_checking(question : str, regular_expression)->str:
    chaine = input(question)
    while re.search(regular_expression, chaine) is None:
        print("Format non respectée ! ")
        chaine = input(question)
    return chaine

class Dictionnary:
    def __init__(self):
        # date of dictionnary creation
        self.datetime = datetime.datetime.now()
        self.dictionnary = {}

    def display_all_definition(self):
        if len(self.dictionnary) != 0:
            for key,value in self.dictionnary.items():
                print (key + " : " + value + "\n\n")
        else:
            print("pas de définition dans le dictionnaire")

    def add_dictionnary(self, monthlyDico):
        self.dictionnary.update(monthlyDico)
    
