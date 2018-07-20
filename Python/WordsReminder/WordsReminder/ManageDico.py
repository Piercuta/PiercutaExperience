import os
import pickle
import datetime

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

def def_and_confirmation():
    """function to interact with the user asking a definition and a confirmation
    it returns a tuple"""
    definition = input("Tapez un mot puis sa définition en les séparant de deux points : \n")
    confirmation = input("confirmez vous ce mot et sa définition ? y or n \n")
    return (definition , confirmation)


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
    
